"""Unit conversions.

JSBSim uses US/imperial units internally (feet, feet per second, pounds).
This project uses SI units everywhere (metres, m/s, J/kg) so ALWAYS convert
at the boundary: right after reading a JSBSim property, or right before
writing one. Never mix the two inside your own code.
"""

FT_TO_M = 0.3048          # exact, by definition of the international foot
M_TO_FT = 1.0 / FT_TO_M

# Standard gravity (m/s^2). JSBSim's own gravity varies slightly with
# altitude and latitude (about 9.80 m/s^2 here); using one constant keeps the
# energy formula simple. The difference is ~0.1-0.3 %, far smaller than the
# effects we compare. If you want, read 'accelerations/gravity-ft_sec2' instead.
G = 9.80665
