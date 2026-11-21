# 04 — Testing, Variables, Controls, Comparison and Evaluation

[Project home](README.md) · [Physics](02-physics-and-modeling.md) · [Research proposal](01-project-proposal.md)

## 1. Primary question to test

**Under uncertain wind-shear profiles, does an adaptive AI dynamic-soaring controller outperform a conventional controller on safely harvested energy and propulsion-energy use for the same aircraft and comparable mission conditions?**

The study must also be willing to answer **no**. A controlled result identifying failure thresholds is a useful conclusion.

## 2. Five comparison methods discussed

| Code | Flight/control method | Why include it |
| --- | --- | --- |
| A | Steady unpowered glide and/or ordinary powered level/cruise flight | Baseline energy expenditure without intentional dynamic soaring |
| B | Fixed, precomputed dynamic-soaring maneuver | Tests whether simply knowing a periodic path is enough |
| C | Model-based optimized dynamic-soaring trajectory + conventional tracking controller | Strong classical baseline; run estimated-wind version fairly |
| D | Robust/adaptive classical soaring controller | Tests whether AI is actually needed to handle uncertainty |
| E | Learned AI-powered adaptive dynamic-soaring controller | Proposed integration of Ideas 1 + 5 |

For studies of the optional *soar or not* decision add:
- **F:** always-attempt-soaring supervisor with safe fallback.
- **G:** wind-aware or confidence-aware soar/glide/powered-flight supervisor.
- **H:** oracle using true wind field and/or optimal hindsight decision — **upper bound, not a deployable fair baseline**.

**Critical:** A/B/C/D/E comparisons require task-matched initial conditions, physical constraints and sensing. Ordinary cruise/steady glide is not a direct same-end-state comparator for every full dynamic-soaring cycle; use a carefully defined common mission/end state and power objective.

## 3. Independent variables (initial suggested matrix)

Start with *one primary independent variable* to keep the CWSF question clear, then sensitivity studies:

1. **Wind shear strength**: include zero shear, below predicted threshold, near threshold, and above threshold.
2. **Wind estimate error / partial observability**: exact/oracle, mildly noisy, severely noisy, delayed estimates.
3. **Wind variability**: steady idealized shear, time-varying shear, turbulence/gusts.
4. **Aircraft aerodynamic efficiency**: measured FW-01 drag polar; optional more efficient glider in simulation.
5. **Controller family**: A through E; if studying switching add F/G.
6. **Model mismatch**: perturbed mass, lift/drag coefficients, control latency and response.

Explore wind direction, minimum turn radius, initial energy and sensor noise only if time allows.

## 4. Dependent variables and how to measure

| Metric | Meaning | Caveat |
| --- | --- | --- |
| **Net mechanical energy per complete comparable soaring cycle** | Difference between initial and final modeled mechanical energy in a specified frame | Match endpoints, wind states and account for work/losses; no partial-cycle cherry-picking |
| **Electrical energy used (J or Wh)** | Integral of measured/simulated battery power over a defined mission | Requires calibrated V/I measurement; negative motor commands not proof of energy gain |
| **Energy per distance (J/m)** | Flight energy needed per ground distance traveled | Use comparable routes/mission constraints and consider wind-assisted travel bias |
| **Endurance / distance** | Time or range achieved under comparable battery/mission assumptions | Cannot infer physical endurance solely from mechanical-energy reward |
| **Recovery and tracking error** | Trajectory or attitude deviation under gust disturbances | Smaller tracking error does not necessarily mean better net energy extraction |
| **Cycle completion rate** | Proportion completing a safe, full maneuver | Specify completion and safety rules in advance |
| **Safety failures** | Stalls, bank/load excursions, ground/altitude violations, geofence breaches | Report even if an RL reward obscures them |
| **Minimum usable wind shear** | Lowest tested shear for successful net-positive unpowered cycles | Depends on airframe/model; estimate uncertainty and uncertainty bands |
| **Controller compute latency** | Ability to execute safely at intended frequency | Include inference/optimizer wall-clock and onboard constraints |

Choose one **primary endpoint** before final trials; treat others as secondary to avoid selecting whatever produces the most impressive plot.

## 5. Controlled variables

Keep the same:
- Aircraft mass/geometry/drag model and actuator limits.
- Starting airspeed, altitude, heading/relative state, initial battery charge and mission constraints.
- Wind-field random seed in paired comparisons.
- Simulation timestep/integrator, sensing noise model and available observations.
- Training data budgets and tuning opportunity for learned controllers, as defensible; document computational differences.
- Safety envelope, failsafe policy and abort conditions.
- Measurement procedures for physical glides (site/time/weather permitting); randomize flight order when safe and practical.

## 6. Minimum experimental sequence

**Experiment 0 — physics audit**
- Still air, uniform steady wind, known shear, timestep convergence.
- Confirm energy accounting and no free-energy loophole.

**Experiment 1 — reproduction**
- Reproduce one published non-learning or neural-feedback dynamic-soaring result using clearly stated parameter differences.
- Compare trajectory shape, energy and constraints. Do not claim exact replication when the model/input set differs.

**Experiment 2 — shear/airframe threshold**
- Sweep wind gradient and aerodynamic polar for the same conventional optimized maneuver.
- Plot positive/negative energy regions and safety feasibility. Measure the FW-01 candidate against this map.

**Experiment 3 — adaptive control**
- Train E on designated wind conditions, freeze final checkpoint and test on held-out fields.
- Compare B/C/D/E with identical test cases and fair observation access.

**Experiment 4 — uncertainty robustness**
- Vary wind-estimation error, turbulence and sensor noise one axis at a time.
- Add model mismatch and report failure surfaces.

**Experiment 5 — optional supervisory switching**
- Compare E-always-soar versus G-soar-only-when-beneficial during a mission with alternating viable/nonviable wind regimes.
- Control for transition cost, route completion and battery use.

**Experiment 6 — physical validation**
- Measure glide efficiency and power use on the actual FW-01 (or revised airframe) and adjust simulator parameters.
- Optional autopilot SITL/HIL demonstrations. Do not require dangerous real wind-shear cycling outdoors.

## 7. Statistics and repeatability

- Use many **independent wind-field test seeds**; a practical feasibility starting target could be >= 20 paired conditions, increased if variability is high.
- For learned controllers, evaluate >= 3 independent training seeds when feasible and report variance; these are *planning targets*, not claims of work completed or substitutes for power analysis.
- Report mean or median, spread/confidence intervals and the distribution of failures.
- Preselect trial termination rules and keep failed episodes; do not quietly rerun unfavorable seeds.
- Separate training, validation/tuning and frozen final-test sets.
- Archive simulator code version, config, aircraft polar, seed, policy checkpoint, telemetry file, run date and any exclusions.

## 8. Ablation tests

To see *why* an improvement occurs, compare E with/without:
- Wind history or online wind estimation.
- Recurrent memory/belief state.
- Domain-randomized wind during training.
- Supervisor safety gating.
- Ability to choose soaring versus ordinary flight.
- Accurate versus perturbed airframe model.

Do not run every ablation if it prevents completion of the main A–E study.

## 9. Success, failure and inconclusive criteria

**Success:** verified physics; nontrivial test performance with no hidden constraint violations; transparent comparison showing an effect with uncertainty, OR a strong bounded negative finding about shear, aircraft efficiency, or AI limitations.

**Engineering success:** safe, characterized flight-worthy UAV, logged tests, versioned design decisions, and realistic explanation of what was physically demonstrated.

**Failure / redesign gate:** simulation can generate energy in steady uniform wind; learned controller violates safety constraints; unrepeatable gains; simulation and physical measurements disagree without explanation.

**Inconclusive:** insufficient independent test conditions, excessive sensor noise, uncalibrated power measurement, infeasible experimental control, missing baseline, or conflicting confidence intervals that do not resolve a useful effect.

## 10. Example data-record schema (proposed)

Fields: run_id, timestamp, repository_commit, dynamics_version, aircraft_id, wind_profile_id, wind_seed, controller, controller_training_seed, observation_model, shear_strength, timestep, initial_state, final_state, energy_frame, net_energy_j, battery_energy_j, distance_m, safety_events, complete_cycle, abort_reason, inference_ms, notes.

All data rows are future artifacts; this document does not represent collected data.
