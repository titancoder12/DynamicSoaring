# 07 — CWSF 2027 Project Positioning, Risks, Decisions and Scope

[Project home](README.md) · [Papers](06-annotated-references.md) · [Roadmap](05-roadmap-and-notebook.md)

**Status update — October 23, 2026:** The broad albatross-inspired dynamic-soaring subject is now selected. The historical October 18 discussion below retains its original proposal status; current scope, the nature–engineering–applications structure, and open implementation decisions are consolidated in the [science fair entry folder](../../../GVRSF2027/docs/README.md).

## 1. The key conversation decision (2026-10-18)

The student clarified: **It is acceptable that professional scientists have already worked on AI dynamic soaring.** The student is in Grade 11, values learning from credible research, and wants **real engineering and building**, not an exhausting search for world's-first algorithmic novelty.

This changes the proposed project strategy:
- Use academic papers as design references and benchmarks.
- Make a real flying machine and reliable simulator.
- Learn and reproduce known physics/algorithms accurately.
- Engineer an implementation, conduct original controlled tests, and improve or characterize performance.
- Preserve substantial time for evidence, reporting and careful physical validation.
- Distinguish a meaningful student contribution from claiming to have invented all the pieces.

At the time of this October 18 discussion, the project remained a **candidate**. The October 23 topic selection is recorded above and does not establish experimental performance or an award outcome.

## 2. Project narrative

**Motivation:** Longer-endurance fixed-wing UAVs are useful for scientific/environmental observation; albatrosses exploit wind shear efficiently.

**Problem:** Conventional small aircraft require propulsion energy; natural wind gradients are variable and may be difficult to exploit safely.

**Engineering response:** Student-designed and constructed UAV, measured aerodynamic characteristics, a validated flight simulator and adaptive AI flight-control logic.

**Scientific question:** Under which conditions does learning/online adaptation improve wind-energy harvesting over classical control, and where does it fail?

**Evidence:** Physics checks, optimized baseline, frozen holdout tests, variance and failure plots, physical logs, hardware/SITL demonstrations.

**Limitations:** Small-airframe glide efficiency, controlled wind availability, estimator imperfections and physical validation constraints.

## 3. Avoid two unhelpful extremes

1. **Only novelty hunting:** Rejecting a good engineering project solely because a university group published something related. Avoid this. Existing research is a valuable technical foundation.
2. **Only flashy hardware:** Building a drone and playing an AI demo without measurement or fair experimental comparison. Avoid this too; a real science-fair investigation needs falsifiable questions and credible evidence.

The balance is engineering novelty at a sensible scale, physical understanding and honest performance evidence.

## 4. What was discussed and preserved

- Initial six flight-based candidates: adaptive control, environmental sensing, bio-inspired cooperative flight, morphing wings, albatross soaring and marine monitoring.
- Clarification: the intended combination is **Idea 1 + Idea 5**, **not** Idea 1 + Idea 3 (swarm formation).
- Original combined question: can adaptive control exploit wind gradients better under uncertain winds?
- Reviewed prior art: neural feedback (2019), deep RL trajectory optimization (2025), integrated planning/control RL (2025), powertrain-aware energy optimization (2026).
- High-school objective: the professional papers are **references**, not disqualifying competition.
- Proposed build-first phases: actual FW-01 UAV; reproduce physics; engineer adaptive control; perform original tests.
- Controlled baselines: steady glide/powered flight, fixed cycle, optimized classical cycle, robust classical controller and AI controller.
- Optional narrower study: controller decides **when not to soar**, switching to glide/cruise under inadequate shear.
- Feasibility caveat: the current small flying wing may not be efficient enough for real energy-positive dynamic soaring.
- Parallel-track recommendation: build FW-01 and simulation together; safe physical validation does not depend on successful actual dynamic soaring.
- CWSF goal: a compelling artifact **plus** measured aerodynamic and control findings, rather than claims of unprecedented fundamental theory.

## 5. Main scientific risks

- Literature already contains AI-controlled dynamic soaring: position contributions honestly as implementation/reproduction/measurement/extension.
- Numerical artifacts can masquerade as harvested energy: still-air/uniform-wind and integration tests are mandatory.
- Learned control may exploit simulator flaws/reward functions: freeze evaluation, enforce safety independently.
- An idealized wind gradient may not occur at a safe field site: keep all demanding soaring tests in simulation.
- A small flying wing may have an inadequate glide ratio: measure and adapt the hardware plan.
- True wind, airspeed and energy measurements may be noisy: calibrate sensors and use uncertainty bounds.
- Energy in the air-relative frame is not the same as measured motor/battery electrical energy: state the metric clearly.
- ArduPilot automatic SOARING is thermalling: do not mistake it for a solved dynamic-soaring autopilot.
- Over-scoping RL, CFD, new airframe, camera sensing and autonomous outdoor flight together can jeopardize completion.

## 6. Risk-controlled fallback ladder

**Level 1 (must achieve if feasible):** stable custom plane, documented design, credible glide logs + physically verified shear simulation with classical results.

**Level 2:** learned dynamic-soaring controller outperforms or meaningfully contrasts with a conventional benchmark under controlled test conditions; publish both wins and losses.

**Level 3:** SITL/HIL aircraft-controller integration and calibrated model of real airframe.

**Level 4 (optional):** supervised safe physical adaptive control experiment.

**Level 5 (not a dependency):** real outdoor positive-net-energy dynamic soaring / persistent autonomous soaring.

If the higher levels fail, the project need not collapse.

## 7. How to defend the project at CWSF

Possible judge questions and substantive answers:
- **"Is the idea new?"** Prior work demonstrates the broader mechanism; the student implemented/reproduced specific algorithms and tested defined questions with their own aircraft/model. Cite each inherited method.
- **"What did you personally build?"** Show hardware, CAD/electronics, code versions, measurements, flight logs and a chronological notebook.
- **"Why AI?"** Present controlled baseline and show where the adaptive policy improves, ties, or worsens; AI is tested, not assumed superior.
- **"Does your plane actually soar?"** Separate real gliding/flight-control measurements from simulated dynamic soaring. Do not imply field demonstration where none occurred.
- **"Where does the energy come from?"** Wind gradient; compare mechanical and electrical energy with correct frames and drag/propulsion losses.
- **"How did you test reliability?"** Matched conditions, held-out scenarios, independent trials, confidence intervals, ablations and negative cases.
- **"Why does this matter?"** Potential lower-energy environmental observations, but actual mission savings depend on viable wind and vehicle performance.

## 8. Decision register

| Date | Status | Decision |
| --- | --- | --- |
| 2026-10-18 | Recorded | Candidate formed from Idea 1 + Idea 5; Idea 1 + 3 remains a separate historical alternative. |
| 2026-10-18 | Recorded | Prior university research is accepted as a foundation/reference, not automatic rejection. |
| 2026-10-18 | Proposed approach | Build and simulate in parallel; four progressive build/physics/AI/experiments stages. |
| 2026-10-18 | Risk constraint | Real dynamic soaring is a stretch goal; never substitute idealized simulation for physical evidence. |
| 2026-10-18 | Open | Select aircraft/flight controller/RC and sensor set after inventory, budget, power and physical feasibility. |
| 2026-10-18 | Open | Choose primary scientific metric and freeze experimental protocol once baseline model is validated. |
| 2026-10-18 | Open | Determine whether explicit soar/no-soar AI supervision is worth additional implementation time. |

## 9. What not to claim yet

- No AI controller, physics simulation, FW-01 flight performance or battery savings has been verified in this dossier.
- No medal probability or outcome can be deduced.
- No confirmation that the FW-01 can safely perform dynamic soaring.
- No assertion that one paper's percentage result will transfer to a different aircraft.
- No guarantee of outdoors/autonomy permissions, final hardware selection or completed CWSF project.

## 10. Recommended immediate next three actions

1. **Physical track:** inventory FW-01 parts and determine actual mass, wing geometry, electronics, sensor capability, and safe conventional flight-test readiness.
2. **Physics track:** read [R5]/[R6] and [R1]/[R2] and implement a minimal 3-D dynamic-soaring model with energy conservation checks and classical baseline.
3. **Research track:** choose and write down a primary endpoint and the smallest A/B comparison that would be scientifically meaningful before training RL.
