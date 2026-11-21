"""Run ONE wind case in JSBSim and return its time series.

How a run works:
  1. Load the glider model.
  2. Set the starting state (height, airspeed, heading, flight-path angle).
  3. Every time step (default 1/120 s):
       a. work out the wind at the glider's CURRENT height and give it to JSBSim
          (wind shear means the wind changes as the glider climbs or sinks, so
          it must be updated every step - JSBSim does not do this for us)
       b. ask the controller for control commands
       c. advance JSBSim by one step
       d. record everything, including both energies
  4. Stop at the end time, or early if the glider gets too close to the surface.

JSBSim quirks handled here (found while testing - see EXP-001 README):
  * Starting speed: JSBSim's own "initial wind" settings (ic/vw-*) gave
    inconsistent starting airspeeds in our tests, so we DON'T use them.
    Instead we set the starting GROUND velocity ourselves:
        v_ground = v_air (what we want) + wind at the start height
    and set the atmosphere wind directly. The glider then starts at exactly
    the airspeed in the config, in every wind case.
  * run_ic() resets the atmosphere wind to zero, so the wind is set AFTER it.
  * Gliders have no engine, so JSBSim's trim routine cannot find a steady
    state ("udot doesn't appear to be trimmable"). We start in a gentle glide
    and let the controller settle it.
"""

import math
import os

# Hide JSBSim's start-up banner (must be set before jsbsim is imported).
os.environ.setdefault("JSBSIM_DEBUG", "0")

import jsbsim  # noqa: E402

from .units import FT_TO_M, M_TO_FT
from .wind import make_wind_model
from .energy import ground_relative_energy, air_relative_energy
from .controllers import make_controller

# Columns recorded each logged step (all SI units).
COLUMNS = [
    "t", "h", "airspeed",
    "vg_north", "vg_east", "vg_down", "ground_speed",
    "w_north", "w_east",
    "theta_deg", "phi_deg", "psi_deg",
    "elevator", "aileron",
    "e_ground", "e_air",
]


def _read_state(fdm, t0):
    """Read JSBSim properties and convert them to SI units."""
    return {
        "t": fdm.get_sim_time() - t0,
        "h": fdm["position/h-agl-ft"] * FT_TO_M,
        "airspeed": fdm["velocities/vtrue-fps"] * FT_TO_M,
        # Ground velocity in North-East-Down axes, relative to the Earth's surface
        "vg_north": fdm["velocities/v-north-fps"] * FT_TO_M,
        "vg_east": fdm["velocities/v-east-fps"] * FT_TO_M,
        "vg_down": fdm["velocities/v-down-fps"] * FT_TO_M,
        "w_north": fdm["atmosphere/wind-north-fps"] * FT_TO_M,
        "w_east": fdm["atmosphere/wind-east-fps"] * FT_TO_M,
        "theta_deg": fdm["attitude/theta-deg"],
        "phi_deg": fdm["attitude/phi-deg"],
        "psi_deg": fdm["attitude/psi-deg"],
        "p": fdm["velocities/p-rad_sec"],
        "q": fdm["velocities/q-rad_sec"],
        "r": fdm["velocities/r-rad_sec"],
    }


def _set_wind(fdm, w_north, w_east):
    fdm["atmosphere/wind-north-fps"] = w_north * M_TO_FT
    fdm["atmosphere/wind-east-fps"] = w_east * M_TO_FT
    fdm["atmosphere/wind-down-fps"] = 0.0


def run_case(sim_cfg, case_cfg, aircraft_dir=None):
    """Run one case. Returns (rows, info).

    sim_cfg : the "simulation" section of config.json
    case_cfg: one entry of the "cases" list
    aircraft_dir: folder holding custom aircraft (None = JSBSim built-ins)
    """
    dt = 1.0 / float(sim_cfg.get("rate_hz", 120))
    duration = float(sim_cfg["duration_s"])
    log_every = int(sim_cfg.get("log_every_steps", 12))     # 12 x 1/120 s = 0.1 s
    min_height = float(sim_cfg.get("min_height_m", 5.0))

    start = dict(sim_cfg["start"])
    start.update(case_cfg.get("start", {}))                 # a case may override
    h0 = float(start["height_m"])
    v_air0 = float(start["airspeed_mps"])
    heading0 = float(start["heading_deg"])
    gamma0 = float(start.get("flight_path_deg", -2.0))     # negative = descending

    wind = make_wind_model(case_cfg.get("wind", {"type": "still"}))
    # A case's "controller" settings are added on top of the default ones -
    # unless the case picks a different controller type, then it replaces them.
    controller_cfg = dict(sim_cfg.get("controller", {"type": "glide"}))
    case_ctrl = case_cfg.get("controller", {})
    if case_ctrl.get("type", controller_cfg.get("type")) != controller_cfg.get("type"):
        controller_cfg = {}
    controller_cfg.update(case_ctrl)
    controller = make_controller(controller_cfg)

    # --- 1. Load the model -------------------------------------------------
    fdm = jsbsim.FGFDMExec(None)            # None = use JSBSim's built-in data folder
    fdm.set_debug_level(0)                  # keep the console quiet
    if aircraft_dir:
        fdm.set_aircraft_path(str(aircraft_dir))
    if not fdm.load_model(sim_cfg["aircraft"]):
        raise RuntimeError(f"JSBSim could not load aircraft '{sim_cfg['aircraft']}'")
    fdm.set_dt(dt)

    # --- 2. Starting state -------------------------------------------------
    w_n0, w_e0 = wind(h0)
    hdg, gam = math.radians(heading0), math.radians(gamma0)
    va_n = v_air0 * math.cos(gam) * math.cos(hdg)       # air-relative velocity
    va_e = v_air0 * math.cos(gam) * math.sin(hdg)
    va_d = -v_air0 * math.sin(gam)                      # down is positive
    fdm["ic/terrain-elevation-ft"] = 0.0
    fdm["ic/h-agl-ft"] = h0 * M_TO_FT
    fdm["ic/psi-true-deg"] = heading0
    fdm["ic/theta-deg"] = gamma0                        # start with nose along the path
    fdm["ic/phi-deg"] = 0.0
    fdm["ic/vn-fps"] = (va_n + w_n0) * M_TO_FT          # ground = air + wind
    fdm["ic/ve-fps"] = (va_e + w_e0) * M_TO_FT
    fdm["ic/vd-fps"] = va_d * M_TO_FT
    if not fdm.run_ic():
        raise RuntimeError("JSBSim run_ic() failed")
    _set_wind(fdm, w_n0, w_e0)                          # AFTER run_ic (it resets wind)

    t0 = fdm.get_sim_time()
    state = _read_state(fdm, t0)
    # The airspeed property is only refreshed by a time step; use the value we set.
    state["airspeed"] = v_air0
    controller.reset(state)

    rows = []
    info = {"stopped_early": False, "reason": "finished"}
    n_steps = int(round(duration / dt))
    cmd = {"elevator": 0.0, "aileron": 0.0, "rudder": 0.0}

    for step in range(n_steps + 1):
        # --- 3a. wind at the current height
        w_n, w_e = wind(state["h"])
        _set_wind(fdm, w_n, w_e)

        # --- 3d. record (before stepping, so row 0 is the starting state)
        if step % log_every == 0 or step == n_steps:
            rows.append(_make_row(state, cmd))
        if step == n_steps:
            break
        if state["h"] < min_height:
            info = {"stopped_early": True, "reason": f"below {min_height} m at t={state['t']:.1f} s"}
            break

        # --- 3b. controller
        if step > 0:
            cmd.update(controller.update(state))
        fdm["fcs/elevator-cmd-norm"] = cmd.get("elevator", 0.0)
        fdm["fcs/aileron-cmd-norm"] = cmd.get("aileron", 0.0)
        fdm["fcs/rudder-cmd-norm"] = cmd.get("rudder", 0.0)

        # --- 3c. advance the simulation
        fdm.run()
        state = _read_state(fdm, t0)

    return rows, info


def _make_row(s, cmd):
    gs = math.hypot(s["vg_north"], s["vg_east"])
    e_g = ground_relative_energy(s["h"], s["vg_north"], s["vg_east"], s["vg_down"])
    e_a = air_relative_energy(s["h"], s["vg_north"], s["vg_east"], s["vg_down"],
                              s["w_north"], s["w_east"])
    return [s["t"], s["h"], s["airspeed"], s["vg_north"], s["vg_east"], s["vg_down"], gs,
            s["w_north"], s["w_east"], s["theta_deg"], s["phi_deg"], s["psi_deg"],
            cmd.get("elevator", 0.0), cmd.get("aileron", 0.0), e_g, e_a]
