# EXP-001 sanity checks: still air, uniform wind, wind shear

rate = (energy at end - energy at start) / duration, in W/kg (= J/kg per s).
`air` = air-relative energy, `ground` = ground-relative energy.
`frame_gap_swing_Jkg` = how far (ground - air) energy moved during the run.

| case | duration_s | height_start_m | height_end_m | airspeed_end_mps | rate_air_Wkg | rate_ground_Wkg | frame_gap_swing_Jkg | note |
|---|---|---|---|---|---|---|---|---|
| still_air | 60.0 | 200.0 | 139.5 | 27.86 | -9.497 | -9.497 | 0.0 | finished |
| uniform_headwind | 60.0 | 200.0 | 139.5 | 27.86 | -9.497 | -9.612 | 7.0 | finished |
| uniform_tailwind | 60.0 | 200.0 | 139.5 | 27.86 | -9.497 | -9.382 | 7.0 | finished |
| still_air_circling | 60.0 | 200.0 | 131.3 | 29.52 | -10.038 | -10.038 | 0.0 | finished |
| uniform_wind_circling | 60.0 | 200.0 | 131.4 | 29.5 | -10.038 | -10.364 | 472.1 | finished |
| shear_headwind | 60.0 | 200.0 | 130.2 | 27.53 | -11.168 | -10.002 | 70.0 | finished |
| shear_tailwind | 60.0 | 200.0 | 146.7 | 28.11 | -8.195 | -9.589 | 83.7 | finished |
