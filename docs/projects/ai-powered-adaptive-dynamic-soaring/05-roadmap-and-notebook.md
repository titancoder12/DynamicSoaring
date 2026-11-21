# 05 — Build Roadmap, Parallel Workstreams and Engineering Notebook

[Project home](README.md) · [System](03-aircraft-and-control-architecture.md) · [Experiments](04-experiments-and-evaluation.md)

## 1. Guiding strategy

**Build → Understand → Reproduce → Experiment → Improve.**

This is intentionally an *engineering-first* Grade 11 effort: use published papers as references, work toward a physical flying aircraft, but also establish a scientifically credible simulator and controlled experiment. Follow two parallel tracks instead of waiting for one to finish before starting the other.

## 2. Milestone schedule (planning targets, not completed work)

| Time (approx.) | Physical aircraft track | Physics/AI track | Review gate |
| --- | --- | --- | --- |
| **Oct–Nov 2026** | Inventory FW-01; weigh and measure; choose flight controller/sensors; bench electronics; plan safe test site | Read foundational papers; implement 3-D aircraft/wind model; physics regression tests | Simulator does not manufacture energy; physical platform powers on safely |
| **Nov–Dec 2026** | Complete airframe assembly, safe RC and assisted flight; collect basic glide and power logs when feasible | Implement steady glide, fixed cycle and classical trajectory optimizer; reproduce one published result | Conventional baselines work and physics and airframe assumptions are justified |
| **Dec 2026–Jan 2027** | Quantify lift/drag and wind-estimation limitations; refine airframe or adopt better glider if needed | Train adaptive controller; start holdout evaluation; optional supervisor for soar/no-soar decisions | Measurable robustness or documented negative result, no concealed safety failures |
| **Feb 2027** | Calibrate model against physical logs; evaluate realistic sensor/control delays | Complete ablations and independent test trials; SITL/HIL integration if feasible | Locked experiments with uncertainty and audit trail |
| **Mar–Apr 2027** | Demonstration readiness and safe physical validation only | Final plots, methods, results, limitations and science-fair report | Credible, reproducible evidence and clear distinction between simulation and physical tests |

The actual regional-fair / CWSF deadlines must be checked separately and can move these dates earlier. Protect time for schoolwork and test repeatability; narrow scope rather than stretching every feature.

## 3. Physical platform checklist

- [ ] Record current FW-01 design revision, material, intended dimensions, mass budget and CG.
- [ ] Inventory motor, ESC, battery, propeller, RC Tx/Rx, servos, flight controller, wiring and software versions.
- [ ] Confirm regulator/BEC or separate regulated power supply meets sensor/FC current and voltage needs.
- [ ] Bench verify failsafes and manual override without mounted propeller.
- [ ] Choose airspeed sensor and current/voltage measurement instrumentation; log rates and accuracy.
- [ ] Record hardware photos and wiring schematic.
- [ ] Perform safe conventional control/trim and glide measurements.
- [ ] Identify stall/turning limits and glide-polar uncertainty.
- [ ] Decide from evidence whether a more efficient glider is needed.

## 4. Simulation / AI checklist

- [ ] Select a published reference dynamic-soaring model and note its parameters.
- [ ] Write aircraft/atmosphere units, coordinate frames, equations, and integrator.
- [ ] Test still air, uniform wind, simple shear and timestep convergence.
- [ ] Document the measured or justified drag polar and safety constraints.
- [ ] Implement fixed trajectory and optimized classical baseline.
- [ ] Reproduce and compare a published result.
- [ ] Train an adaptive policy with realistic partial observations.
- [ ] Add held-out wind shear / changing-wind scenarios.
- [ ] Compare with matched baselines, count failures and uncertainty intervals.
- [ ] Run SI units and metric auditing; distinguish energy proxies from actual watt-hours.
- [ ] Integrate with flight-controller SITL and then HIL only if necessary.

## 5. Go / no-go decisions

**Gate A — physics model trustworthy:** no AI training until zero-shear and energy tests pass.

**Gate B — achievable soaring:** if airframe model needs unrealistically strong shear, stop claiming real dynamic-soaring capability of FW-01; pursue safer physical validation and/or redesign an efficient glider.

**Gate C — adaptation adds value:** if learning does not beat well-tuned conventional control, preserve this result and investigate *why*, rather than changing metrics afterward.

**Gate D — physical testing ready:** pilot competence, approved operating environment, failsafe, manual takeover and legal compliance required before outdoor experiments.

**Gate E — CWSF completeness:** stop adding features early enough for valid repeated results, notebook, graphs and explanation.

## 6. Logbook template — repeat after each iteration

### Entry metadata
- Date/time:
- Version / commit:
- Experiment/build ID:
- Author and collaborators:
- Objective or problem:
- Previous observation prompting this step:

### Hypothesis / engineering prediction
- What should happen?
- Physical/control reasoning:
- What result could disprove it?

### Build or method
- Parts, tools, CAD/software versions:
- Reused published code/model references and modifications:
- Independent variable(s):
- Dependent variable(s):
- Controlled variable(s):
- Procedure, units and calibration:
- Trial count / seeds:

### Evidence
- Raw file paths, photos, log IDs:
- Measurements with uncertainty:
- Graphs and statistical summary:
- Safety anomalies / crashes / aborted trials:
- Comparison to baseline:
- Differences from previous revision:

### Conclusion and next action
- What the data *actually* supports:
- Remaining uncertainty:
- Change to design or hypothesis:
- Next experiment:
- Authorization / safety requirements:

## 7. Artifact directory proposal (not yet created)

Within this folder, later add subdirectories as needed for `design/`, `notebook/`, `experiments/`, `figures/`, `simulation/`, `hardware/`, but only when real artifacts exist. Avoid committing bulky raw sensor logs or copied restricted papers without checking repository size, privacy, licensing and provenance.

## 8. Possible minimum CWSF demonstration

1. Display the physical aircraft, electronics diagram and flight/control data.
2. Show a side-by-side physics simulation of two algorithms under the **same** wind conditions.
3. Plot true versus estimated wind and energy versus time, not just a 3-D animation.
4. Show a sensitivity plot identifying when the learned approach helps, loses, or becomes unsafe.
5. State clearly what was simulated, what was physically tested, what was taken from literature, and what the student developed.

A reliable demonstration of a bounded effect is more valuable than an unsupported claim of perpetual or autonomous real-life soaring.
