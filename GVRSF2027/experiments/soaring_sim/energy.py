"""Specific energy: energy per kilogram of glider (units: J/kg = m^2/s^2).

Dividing by mass lets us compare gliders of different sizes.

    e = g*h + |v|^2 / 2
        g*h      potential energy per kg   (g in m/s^2, h in m)
        |v|^2/2  kinetic energy per kg     (v in m/s)

The big question is: v relative to WHAT?

GROUND-RELATIVE  (used by Sachs 2005):   v = v_ground
    The glider's velocity measured from the ground/sea surface.

AIR-RELATIVE     (used by Richardson 2015): v = v_ground - w   (= the airspeed vector)
    The glider's velocity measured from the moving air around it.

Why they differ: a glider flying at 27 m/s airspeed with an 8 m/s tailwind
moves at 35 m/s over the ground, but at 19 m/s into a headwind. Its
ground-relative kinetic energy jumps up and down just by TURNING, even though
nothing about its flight through the air changed. Air-relative energy does not
care about that, which is why in a UNIFORM, STEADY wind it should behave
exactly like still air (no free energy). Only a wind that CHANGES (with height,
or in time) can give a glider real air-relative energy - that is the
dynamic-soaring effect.

Deciding which frame your project's main measurement uses is YOUR decision.
This starter logs both so you can compare them on real runs.

The "energy rate" (W/kg = J/kg per second) used in the summary is:
    rate = (e_end - e_start) / (t_end - t_start)
"""

from .units import G


def ground_relative_energy(h, vg_north, vg_east, vg_down):
    """Specific energy using the ground velocity (J/kg)."""
    v2 = vg_north**2 + vg_east**2 + vg_down**2
    return G * h + 0.5 * v2


def air_relative_energy(h, vg_north, vg_east, vg_down, w_north, w_east, w_down=0.0):
    """Specific energy using the velocity relative to the air (J/kg).

    v_air = v_ground - w   (component by component)
    """
    va_n = vg_north - w_north
    va_e = vg_east - w_east
    va_d = vg_down - w_down
    return G * h + 0.5 * (va_n**2 + va_e**2 + va_d**2)


def mean_rate(t, e):
    """Average energy rate (W/kg) over a run: (last - first) / duration."""
    duration = t[-1] - t[0]
    if duration <= 0:
        return float("nan")
    return (e[-1] - e[0]) / duration
