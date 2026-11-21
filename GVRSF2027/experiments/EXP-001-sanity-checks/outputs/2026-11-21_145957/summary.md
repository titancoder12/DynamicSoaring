# EXP-001 sanity checks: still air, uniform wind, wind shear

rate = (energy at end - energy at start) / duration, in W/kg (= J/kg per s).
`air` = air-relative energy, `ground` = ground-relative energy.
`frame_gap_swing_Jkg` = how far (ground - air) energy moved during the run.

| case | duration_s | height_start_m | height_end_m | airspeed_end_mps | rate_air_Wkg | rate_ground_Wkg | frame_gap_swing_Jkg | note |
|---|---|---|---|---|---|---|---|---|
| still_air | 60.0 | 200.0 | 139.5 | 27.86 | -9.497 | -9.497 | 0.0 | finished |
