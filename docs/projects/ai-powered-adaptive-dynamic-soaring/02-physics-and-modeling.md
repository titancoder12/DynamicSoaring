# 02 — Albatross Dynamic Soaring: Physics and Simulation Requirements

[Project home](README.md) · [Experiments](04-experiments-and-evaluation.md) · [Papers](06-annotated-references.md)

## 1. Two different kinds of soaring

**Dynamic soaring (this project):** an aircraft extracts energy from *wind shear*, i.e. winds with different speed/direction at different altitudes, using coordinated climbs, turns and descents. The key resource is the wind-velocity gradient, not just a strong uniform breeze.

**Thermal soaring (different mechanism):** an aircraft circles in *rising air* generated, for example, by solar heating. Its air mass carries it upward. The 2024 Flato et al. vulture-inspired RL paper and ArduPilot's built-in SOARING/THERMAL functionality concern **thermal soaring**, not this exact albatross mechanism.

Also distinguish **ridge lift** (upward airflow over terrain) from horizontal wind shear; windy coastal settings may contain several effects simultaneously, which a good experiment isolates.

## 2. Intuitive physical picture

Albatross-inspired cycle (simplified, not a universal optimal trajectory):
1. Climb through a layer where wind speed changes with altitude.
2. Turn at a higher level relative to the local wind.
3. Descend through the shear while adjusting heading.
4. Turn near the lower layer and repeat if wind energy gained exceeds drag and maneuver losses.

The correct sequence, heading and timing depend on wind direction, aircraft dynamics, and constraints. In a uniform steady wind field with no vertical air movement, a purely cyclic unpowered flight **cannot sustainably harvest energy just because the air is moving**.

The atmosphere supplies energy. Dynamic soaring is not free energy or an assurance of perpetual flight.

## 3. Baseline quantities and coordinates

For aircraft mass m, altitude h, gravitational acceleration g, ground-relative velocity v_g, and local wind velocity W(x,t):

- Air-relative velocity: **v_a = v_g − W**.
- Airspeed: **V_a = |v_a|**.
- Ground-frame mechanical energy: **E_g = m g h + 0.5 m |v_g|²**.
- A useful air-relative diagnostic: **E_a = m g h + 0.5 m V_a²**.

**Do not treat these two energies as interchangeable in shear or compare isolated partial maneuvers with different end states.** Define the reference frame and control volume before inferring wind-energy extraction. In the air-relative energy balance, wind acceleration/gradient effects must appear explicitly; avoid silently introducing or removing energy through a coordinate transformation.

For aerodynamic force models:
- Dynamic pressure: q = 0.5 ρ V_a².
- Lift magnitude: L = q S C_L.
- Drag magnitude: D = q S C_D.
- Simple polar as a starting approximation: C_D = C_D0 + k C_L².

S is reference wing area; coefficients and their ranges must come from measurement or justified reference models. A fitted glide polar is preferable to an arbitrary optimistic one.

**Cycle comparisons:** normalize to the same initial energy and require sufficiently matched altitude, airspeed, heading/track, location where relevant, and elapsed/mission constraints. For powered vs unpowered comparisons account explicitly for propulsion work and transitions. Track total battery energy rather than using an uncalibrated control-effort reward as actual energy consumed.

## 4. Minimum physics model for a useful first simulator

- A three-dimensional point-mass aircraft with heading, flight-path angle, speed, position and altitude; enforce feasible pitch/bank rates and load factor.
- Aerodynamic lift/drag dependent on airspeed and angle of attack or commanded load factor.
- Stall-speed, bank-angle, turning-rate, structural-load and minimum-altitude constraints.
- Wind vector W(z) with a controllable vertical gradient; later add time variation and spatially varying shear.
- Zero-wind, uniform-wind and simple shear cases with analytic/known properties.
- Ground contact, geofence, numerical integration stability and reproducible initial conditions.
- Throttle/propulsion dynamics and battery energy accounting if using a powered aircraft.

A 3-DOF point-mass model may be enough for the first physics experiment; a 6-DOF model can be introduced when actuator, aerodynamic and flight-control behavior matter. Do not claim the simpler model captures real turbulence or actual FW-01 handling.

Candidate wind profiles:
- Constant uniform horizontal wind as a no-extraction control.
- Smooth monotonic shear, e.g. exponential or logarithmic with physically justified near-surface conditions.
- A sharp-layer model used carefully for literature reproduction, clearly labeled idealized.
- Wind varying across trials in amplitude/direction and later with stochastic gusts.

## 5. Physics-verification checks before training AI

1. **Gravity/glide test:** in still air an unpowered vehicle loses mechanical energy through drag; energy cannot grow by numerical artifact.
2. **Uniform wind test:** identical-relative-state full loops in steady uniform horizontal wind must not provide recurring net energy harvest.
3. **Shear-only test:** positive gains arise only from physically consistent exchange with the imposed wind gradient; double-check sign conventions in opposing headings.
4. **Step-size convergence:** halving the integrator timestep should not substantially change the main metric.
5. **Constraint test:** unrealistic minimum speed, bank/turn rate, stall or load factor cannot be silently exceeded.
6. **Baseline reproduction:** reproduce the qualitative shape and, where comparable, numerical trend of at least one published optimal-soaring trajectory.
7. **Model-mismatch test:** perturb aerodynamic coefficients, air density, sensor lag and wind gradients.
8. **Energy accounting:** separate ground/air-relative mechanical energy, wind work, drag dissipation and motor/battery energy with a declared frame.

## 6. Critical feasibility gate for FW-01

The approximately 85 cm 3D-printed FW-01 concept is an **unverified candidate** for dynamic soaring. It may suffer too much drag, insufficient glide ratio, limited speed range or excessive turn losses. Before claiming a flight implementation:
- Weigh the full airframe with battery, autopilot and sensors.
- Measure wing area, CG, geometry, usable airspeed and safe bank limit.
- Estimate glide ratio and sink polar from simulation and controlled flight measurements.
- Model shear threshold with *measured* parameters.
- If unrealistic shear is needed, switch real-hardware testing to stable glide/flight-control validation, or consider a high-efficiency glider while keeping the existing FW-01 useful.

**Avoid aggressive low-altitude wind-shear experiments, coastal cliffs, strong winds and over-water flights** simply to imitate wild albatrosses. These environments are high-risk and not necessary to demonstrate rigorous high-school research.

## 7. Role of AI

Control is a sequential decision process: estimate the atmosphere; decide whether energy extraction is possible; select feasible flight references; execute them using a stable low-level controller; reevaluate from measurements.

Possible AI approaches:
- RL chooses target bank/flight-path/airspeed references.
- RL optimizes a compact trajectory parameterization (as in published work).
- A supervised neural feedback controller imitates trajectories from a classical optimizer.
- An uncertainty-aware supervisor chooses among glide, dynamic soar or powered cruise.

Start with a reproducible conventional optimization baseline; **AI is a hypothesis being evaluated, not an assumed improvement**.

## 8. Open model questions

Precisely specify wind-frame sign conventions, aircraft dynamics, observation availability, control frequency, throttle bounds and objective before comparing algorithms. The flight computer cannot observe true simulator wind gradients in real life; train/evaluate with realistic sensed quantities and report any oracle experiments separately.
