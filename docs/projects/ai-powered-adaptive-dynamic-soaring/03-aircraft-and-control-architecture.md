# 03 — Airframe, Autopilot, Adaptive Controller and Integration

[Project home](README.md) · [Physics](02-physics-and-modeling.md) · [Roadmap](05-roadmap-and-notebook.md)

## 1. Two-track development

The **real aircraft** and **flight simulator** proceed in parallel, sharing a documented aircraft-parameter file and test logs. A demonstration of learning in software must not be passed off as physical evidence; likewise, a manually stable physical flight does not prove dynamic-soaring control.

### Physical airframe: FW-01 as first candidate

Existing discussion already includes a small 3D-printed flying-wing UAV, roughly 85 cm span. These dimensions are *contextual estimates from planning*, not confirmed measurements of the final constructed airframe.

Record, rather than assume:
- Mass with and without propulsion battery and sensing payload.
- Wing span/area, mean aerodynamic chord, aspect ratio, CG range.
- Airfoil and drag-polar assumptions, stall speed, best-glide airspeed, sink rate.
- Elevon travel, actuator speed, available bank/turn performance.
- Propulsion configuration (motor, propeller, ESC and battery), thrust/current data.
- Actual flight-controller model, firmware, sensor suite and failsafes.

A light, efficient sailplane-type airframe may later be preferable to a flying wing for realistic soaring; changing airframes is a research decision to document, not proof that the original idea failed.

### Sensors and logging (candidate functions, no purchase assumption)

- IMU and barometer for attitude, acceleration and altitude trends.
- GNSS for ground velocity/position where conditions permit.
- Pitot airspeed sensor strongly preferred for meaningful gliding and wind estimation.
- Battery voltage/current sensor for real electrical-energy accounting.
- Optional magnetometer and powertrain RPM logging.
- Telemetry logging of timestamps, controls, mode, wind estimate, airspeed, altitude, battery power and safety events.

Groundspeed alone is **not airspeed**. Air-relative estimates require validated sensors/models; differentiating noisy GNSS/barometer measurements can be problematic.

## 2. Controller separation — safer and clearer

**Low-level autopilot:** conventional validated ArduPilot or equivalent fixed-wing stabilization, mixing, actuator constraints, geofence, RC takeover and failsafes.

**High-level adaptive controller:** receives estimated state and wind-related observations, chooses bounded references (trajectory/airspeed/bank/altitude or maneuver modes), and never bypasses safety constraints.

**Supervisory gate:** determines if a requested maneuver is within a safe envelope; rejects the maneuver or returns to a conservative mode when wind estimate confidence, altitude, airspeed or telemetry is inadequate.

**Pilot:** retains manual override and authority for all outdoor testing.

Initially, high-level AI should operate in a simulator, with low-level control stable independently. Keep an explicit fallback to conventional control.

## 3. What ArduPilot already provides — and does not

ArduPilot Plane includes standard fixed-wing flight control, MAVLink-based telemetry/integration and SITL (software-in-the-loop). SITL supports simulated wind and failures, with external flight dynamics engines such as JSBSim.

ArduPilot's **SOARING / THERMAL mode** is documented for circling in *rising thermals*. It is **not an existing ready-made dynamic-soaring controller** for altitude wind shear. It can inform glider instrumentation and mode-switching patterns but does not satisfy this project's key algorithm.

Reference documentation:
- https://ardupilot.org/plane/docs/soaring-4_1.html
- https://ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html
- https://ardupilot.org/dev/docs/sitl-with-jsbsim.html
- https://en.ardupilot.org/dev/docs/SITL_simulation_parameters.html

## 4. Suggested software stack (choices not yet committed)

- **Physics prototype:** Python scientific environment with fixed-step numerical integration and unit tests; simple trajectory plots.
- **Baseline optimizer:** robust classical control and/or numerical trajectory optimizer under common aircraft constraints.
- **Learning:** PPO or another continuous-control RL method; train with wind-profile domain randomization.
- **Higher-fidelity validation:** ArduPilot Plane SITL + an aircraft model such as JSBSim when model compatibility and shear modeling have been verified.
- **Hardware-in-the-loop:** only if the chosen autopilot board supports it and the physical/simulation I/O path can be validated.
- **Data analysis:** reproducible scripts that export configuration, code version, seeds, trial tables, energy figures and confidence intervals.

SITL wind controls do not by themselves guarantee the **altitude-dependent shear profile** needed here. Verify what the selected physics backend actually simulates; implement custom wind fields or an external dynamics layer if necessary.

## 5. Interfaces and communications

Separate radio roles:
- **RC transmitter/receiver:** independent manual pilot control and failsafe/override link, potentially CRSF/ELRS depending on actual hardware selection.
- **Autopilot telemetry / mission:** MAVLink can carry state, logs and bounded high-level commands to a ground computer or companion computer.
- **Video/FPV:** optional for situational awareness, not necessary for basic dynamic soaring and not a replacement for RC control.
- **ESC/BEC:** check actual voltage/current ratings and wiring; never assume every ESC provides suitable regulated power for the full avionics load.

Do not purchase hardware solely based on this concept document; audit what FW-01 already uses and test pinouts, power budgets, firmware support and emergency handling.

## 6. Development phases / validation gates

1. Bench-test motor, elevons, radio receiver, failsafe, flight controller orientation and current draw **without mounted propeller during configuration**.
2. Perform approved safe manual/assisted test flights; tune conventional flight modes first.
3. Log stabilized glide sections and quantify model error.
4. Run proposed AI exclusively in simulation until constraint behavior is repeatable and tested.
5. Integrate AI with autopilot using software-in-the-loop, then hardware-in-the-loop if worthwhile.
6. Undertake restricted supervised physical validation of **selected safe behaviors** only when stable and legal; no real-world energy-positive dynamic-soaring promise.

## 7. Safety and Canadian operational rules

Check current Transport Canada rules for aircraft operating weight, airspace, pilot certification, registration, flight location and visual line-of-sight before a flight. Custom-built aircraft are not exempt. A sub-250 g aircraft has different rules but still cannot be flown recklessly. Do not use shoreline, cliffs or turbulent high-wind sites just because wind shear appears convenient.

Sources:
- https://tc.canada.ca/en/aviation/drone-safety/flying-your-drone-safely-legally
- https://tc.canada.ca/en/aviation/drone-safety/registering-your-drone

## 8. Engineering risks and fallback

**Real dynamic soaring too demanding:** measure the flight envelope and use the physical aircraft for glide-model validation plus SITL dynamic soaring.

**AI too hard to tune:** reproduce a neural-feedback controller from published optimizer trajectories and compare to the optimizer.

**Unreliable wind estimation:** report the sensitivity curve, retain an oracle-wind upper bound, and compare only methods with equal sensor access.

**Physical energy measurement noisy:** use repeated calibrated power measurements; explicitly distinguish modeled energy from measured electrical energy.

**Not enough time:** prioritize one complete physical platform, one reproducible physics model and one fair A/B experiment over numerous incomplete features.
