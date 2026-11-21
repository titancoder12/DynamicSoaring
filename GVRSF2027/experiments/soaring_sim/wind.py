"""Wind models.

A wind model is just a function of height:  wind(h) -> (w_north, w_east)
in m/s, where (w_north, w_east) is the velocity OF THE AIR relative to the
ground ("which way the air is moving"), as an arrow pointing north/east.

Config files describe wind the way weather reports do:
    "speed": wind speed in m/s
    "from_deg": the compass direction the wind blows FROM
                (0 = from the north, 90 = from the east, 180 = from the south)
So a wind "from 0 deg" pushes the air SOUTH: w_north is negative.

JSBSim sign convention (checked by experiment, see EXP-001 README):
    'atmosphere/wind-north-fps' > 0 means the air moves toward the north.
    A glider heading north at 27 m/s ground speed with wind-north = +8 m/s
    has an airspeed of 19 m/s (tailwind) - so JSBSim uses exactly the
    "velocity of the air" arrow described above. No hidden sign flips.

Wind is NOT turbulent here and has no vertical component.
"""

import math


def _direction_vector(from_deg):
    """Unit arrow (north, east) pointing the way the air MOVES."""
    to_rad = math.radians(from_deg + 180.0)   # blows TO the opposite direction
    return math.cos(to_rad), math.sin(to_rad)


def make_wind_model(cfg):
    """Build a wind function from one case's "wind" section of config.json.

    Supported types:
      {"type": "still"}
          No wind at all. The control case.
      {"type": "uniform", "speed": 8, "from_deg": 0}
          Same wind at every height. Physics says this should NOT give
          the glider any real (air-relative) energy.
      {"type": "linear_shear", "speed_ref": 8, "height_ref_m": 150,
       "gradient_per_s": 0.05, "from_deg": 0}
          Wind speed changes with height:
              speed(h) = speed_ref + gradient * (h - height_ref)
          (never below 0). gradient is in (m/s) per metre = 1/s.
      {"type": "log_shear", "speed_ref": 8, "height_ref_m": 10,
       "roughness_m": 0.0002, "from_deg": 0}
          The classic wind profile over the sea:
              speed(h) = speed_ref * ln(h / z0) / ln(h_ref / z0)
          Most of the change happens in the lowest ~20 m, which is where
          albatrosses do their dynamic soaring.
    """
    kind = cfg.get("type", "still")

    if kind == "still":
        return lambda h: (0.0, 0.0)

    dn, de = _direction_vector(cfg.get("from_deg", 0.0))

    if kind == "uniform":
        s = float(cfg["speed"])
        return lambda h: (s * dn, s * de)

    if kind == "linear_shear":
        s_ref = float(cfg["speed_ref"])
        h_ref = float(cfg["height_ref_m"])
        grad = float(cfg["gradient_per_s"])

        def wind(h):
            s = max(0.0, s_ref + grad * (h - h_ref))
            return s * dn, s * de
        return wind

    if kind == "log_shear":
        s_ref = float(cfg["speed_ref"])
        h_ref = float(cfg["height_ref_m"])
        z0 = float(cfg.get("roughness_m", 0.0002))

        def wind(h):
            if h <= z0:
                return 0.0, 0.0
            s = s_ref * math.log(h / z0) / math.log(h_ref / z0)
            return s * dn, s * de
        return wind

    raise ValueError(f"Unknown wind type '{kind}'. Use still, uniform, linear_shear or log_shear.")
