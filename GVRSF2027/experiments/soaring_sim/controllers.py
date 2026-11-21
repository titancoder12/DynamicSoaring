"""Controllers: the "pilot" that moves the control surfaces every time step.

Every controller follows the same tiny interface:

    controller.reset(state)          called once, at the start of a run
    controller.update(state) -> dict called every time step

`state` is a dict with these keys (all SI units / degrees):
    t            time since start (s)
    h            height above the surface (m)
    airspeed     true airspeed (m/s)
    vg_north, vg_east, vg_down   ground velocity (m/s)
    w_north, w_east              wind at the glider (m/s)
    theta_deg    pitch angle (deg, + = nose up)
    phi_deg      bank angle (deg, + = right wing down)
    psi_deg      heading (deg, 0 = north, 90 = east)
    p, q, r      roll / pitch / yaw rates (rad/s)

`update` must return a dict with any of:
    "elevator", "aileron", "rudder"   each between -1 and +1

JSBSim control sign conventions (checked by experiment on the SGS glider):
    elevator +  -> nose goes DOWN      (elevator -  -> nose up)
    aileron  +  -> rolls RIGHT (phi increases)

Because all controllers share this interface, the experiment code never needs
to change when you swap controllers - you only change "controller" in
config.json. That is how you keep conditions IDENTICAL between controllers.
"""


def _clip(x, lo=-1.0, hi=1.0):
    return max(lo, min(hi, x))


class GlideController:
    """Default controller: a plain, steady glide. NOT a soaring controller.

    It does just enough so the glider flies calmly instead of wobbling:
      * Pitch: chooses a pitch angle that holds the target airspeed
        (too fast -> raise the nose a bit, too slow -> lower it), then moves
        the elevator to reach that pitch, with damping on pitch rate q.
      * Roll: holds a fixed bank angle (0 = wings level, straight flight;
        e.g. 20 = a steady right-hand circle).
      * Rudder: centred.

    It does nothing clever with the wind. Any energy change you see with this
    controller comes from the glider and the wind, not from smart flying.
    """

    def __init__(self, target_airspeed=27.0, bank_deg=0.0,
                 k_speed=0.5, k_theta=0.08, k_q=0.6, k_phi=0.04, k_p=0.3):
        self.target_airspeed = target_airspeed   # m/s
        self.bank_deg = bank_deg                 # deg
        self.k_speed = k_speed   # deg of pitch per m/s of speed error
        self.k_theta = k_theta   # elevator per deg of pitch error
        self.k_q = k_q           # elevator per rad/s of pitch rate (damping)
        self.k_phi = k_phi       # aileron per deg of bank error
        self.k_p = k_p           # aileron per rad/s of roll rate (damping)
        self.theta_ref = 0.0

    def reset(self, state):
        # Use the starting pitch as the "normal" glide pitch.
        self.theta_ref = state["theta_deg"]

    def update(self, state):
        speed_error = state["airspeed"] - self.target_airspeed
        theta_cmd = self.theta_ref + self.k_speed * speed_error
        theta_error = theta_cmd - state["theta_deg"]
        # elevator + is nose DOWN, so a positive pitch error needs NEGATIVE elevator
        elevator = -self.k_theta * theta_error + self.k_q * state["q"]

        bank_error = self.bank_deg - state["phi_deg"]
        aileron = self.k_phi * bank_error - self.k_p * state["p"]

        return {"elevator": _clip(elevator), "aileron": _clip(aileron), "rudder": 0.0}


class HandsOffController:
    """Holds every control centred. Useful to see the glider's natural
    motion (it slowly oscillates up and down - the 'phugoid')."""

    def reset(self, state):
        pass

    def update(self, state):
        return {"elevator": 0.0, "aileron": 0.0, "rudder": 0.0}


class MyController:
    """TEMPLATE for your own controller (fixed-trajectory, conventional, ...).

    Steps:
      1. Rename this class (e.g. FixedTrajectoryController).
      2. Put its settings in __init__ (they come from config.json "controller").
      3. Write reset() and update() - read `state`, return control commands.
      4. Add it to CONTROLLERS at the bottom of this file.
      5. In an experiment's config.json set  "controller": {"type": "<your name>"}.

    Write down in your Digital Logbook what the controller is meant to do
    BEFORE you test it, and how you tuned it.
    """

    def __init__(self, **settings):
        self.settings = settings

    def reset(self, state):
        raise NotImplementedError("Write your own reset() here.")

    def update(self, state):
        raise NotImplementedError("Write your own update() here.")


# Name used in config.json  ->  class
CONTROLLERS = {
    "glide": GlideController,
    "hands_off": HandsOffController,
    "mine": MyController,
}


def make_controller(cfg):
    """Build a controller from a config section like
    {"type": "glide", "target_airspeed": 27, "bank_deg": 0}."""
    cfg = dict(cfg)
    kind = cfg.pop("type", "glide")
    if kind not in CONTROLLERS:
        raise ValueError(f"Unknown controller '{kind}'. Options: {list(CONTROLLERS)}")
    return CONTROLLERS[kind](**cfg)
