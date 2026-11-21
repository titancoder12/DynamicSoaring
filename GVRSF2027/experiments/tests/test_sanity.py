"""Sanity checks: physics the simulator MUST get right before any real experiment.

Run from the experiments/ folder:
    python -m pytest tests          (or:  python tests/test_sanity.py)

If one of these fails after you change something, STOP and find out why
before trusting any other result.
"""

import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))                         # so 'soaring_sim' can be imported

from soaring_sim.simulation import run_case, COLUMNS  # noqa: E402
from soaring_sim.energy import mean_rate              # noqa: E402

CONFIG = json.loads((ROOT / "EXP-001-sanity-checks" / "config.json").read_text())
SIM = CONFIG["simulation"]
CASES = {c["name"]: c for c in CONFIG["cases"]}
COL = {c: i for i, c in enumerate(COLUMNS)}

# Air-relative energy rate in uniform wind must match still air within this.
# Physics (Galilean invariance) says they are EXACTLY equal on a flat Earth.
# JSBSim models a round, rotating Earth, which adds tiny extra forces, and
# floating-point rounding adds noise. Both are far below 0.05 W/kg, which is
# ~0.5 % of the still-air rate (~ -9.5 W/kg) - small compared with the
# ~1-2 W/kg effects the wind-shear cases produce.
TOLERANCE_W_PER_KG = 0.05

_cache = {}


def _run(name):
    if name not in _cache:
        rows, info = run_case(SIM, CASES[name])
        _cache[name] = (rows, info)
    return _cache[name]


def _rate(rows, column):
    return mean_rate([r[COL["t"]] for r in rows], [r[COL[column]] for r in rows])


def test_still_air_loses_energy():
    rows, info = _run("still_air")
    assert not info["stopped_early"], info
    assert rows[-1][COL["e_air"]] < rows[0][COL["e_air"]]
    assert _rate(rows, "e_air") < 0
    # In still air both frames are the same thing.
    assert abs(_rate(rows, "e_air") - _rate(rows, "e_ground")) < 1e-9


def test_uniform_wind_gives_no_free_air_relative_energy():
    # (wind case, the still-air case flown the same way)
    pairs = [("uniform_headwind", "still_air"),
             ("uniform_tailwind", "still_air"),
             ("uniform_wind_circling", "still_air_circling")]
    for windy, calm in pairs:
        rate = _rate(_run(windy)[0], "e_air")
        calm_rate = _rate(_run(calm)[0], "e_air")
        assert abs(rate - calm_rate) < TOLERANCE_W_PER_KG, (windy, rate, calm_rate)


def test_starting_airspeed_is_the_same_in_every_wind():
    for name in CASES:
        rows, _ = _run(name)
        assert abs(rows[0][COL["airspeed"]] - SIM["start"]["airspeed_mps"]) < 0.01, name


def test_wind_sign_convention():
    """Tailwind: ground speed = airspeed + wind. Headwind: airspeed - wind.
    Also JSBSim's airspeed must equal |v_ground - w| at every logged step."""
    for name, sign in (("uniform_tailwind", +1), ("uniform_headwind", -1)):
        rows, _ = _run(name)
        for r in rows:
            va = math.sqrt((r[COL["vg_north"]] - r[COL["w_north"]]) ** 2
                           + (r[COL["vg_east"]] - r[COL["w_east"]]) ** 2
                           + r[COL["vg_down"]] ** 2)
            assert abs(va - r[COL["airspeed"]]) < 0.01, (name, r[COL["t"]])
        r = rows[len(rows) // 2]
        expected = r[COL["airspeed"]] + sign * 8.0
        assert abs(r[COL["ground_speed"]] - expected) < 0.1, (name, r[COL["ground_speed"]], expected)


def test_runs_are_deterministic():
    a, _ = run_case(SIM, CASES["shear_headwind"])
    b, _ = run_case(SIM, CASES["shear_headwind"])
    assert a == b


if __name__ == "__main__":
    # Plain-Python fallback if pytest is not installed.
    failed = 0
    for fn_name, fn in list(globals().items()):
        if fn_name.startswith("test_"):
            try:
                fn()
                print(f"PASS  {fn_name}")
            except AssertionError as e:
                failed += 1
                print(f"FAIL  {fn_name}: {e}")
    sys.exit(1 if failed else 0)
