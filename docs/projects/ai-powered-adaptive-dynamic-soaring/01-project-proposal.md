# 01 — Engineering Project Proposal and Scientific Questions

[Project home](README.md) · [Experiments](04-experiments-and-evaluation.md) · [References](06-annotated-references.md)

## 1. Motivation and application

Small fixed-wing UAVs are attractive for environmental monitoring, ocean/coastline observation, mapping and scientific measurement, but battery capacity limits endurance. Nature provides a compelling alternative energy source: the **wind's velocity difference between altitude layers**. Albatrosses employ dynamic soaring to exploit that wind shear.

The engineering goal is to **build an instrument that actually flies and measures its own performance**, rather than merely propose a novel algorithm. Professional literature on neural control, reinforcement learning and powertrain optimization provides usable reference methods.

Possible real-world applications (motivation, not measured claims):
- Longer-endurance environmental and marine observations.
- Reduced propulsion-energy requirement on appropriate windy missions.
- Autonomous aircraft that can adapt to variable atmospheric conditions.
- Understanding the practical limits of small UAVs versus soaring-specialized gliders.

This investigation may find that a small fixed wing cannot physically benefit at feasible wind shear; that is not a reason to hide the result.

## 2. Core engineering question

**Can a student-designed fixed-wing UAV, supported by a physics-validated simulator, use an adaptive AI controller to exploit wind gradients and reduce energy consumption compared with conventional flight-control strategies while maintaining safe flight?**

Research subquestions:
1. What wind-gradient strength and aerodynamic efficiency are needed for a complete dynamic-soaring cycle to provide a net mechanical-energy benefit?
2. Can a controller trained under known wind fields execute safe cycles when the wind is only partially observed or changing?
3. How does a learned controller compare with a conventional glide, a fixed soaring trajectory, a model-based optimizer and robust/adaptive classical control?
4. Can a supervisory controller recognize when soaring **is not energetically worthwhile** and choose a safer, more efficient alternative?
5. How closely does the FW-01's real glide behavior match its model, and what limits prevent physical dynamic soaring?

Subquestion 4 is a possible optional investigation, not a required novelty claim. It was discussed as a promising way to connect AI, wind estimation and practical energy management.

## 3. Working hypotheses — falsifiable, not conclusions

- **H1 / threshold physics:** For a fixed aircraft there is a region of wind shear, drag and maneuverability within which dynamic-soaring cycles yield positive net mechanical energy; outside it, they lose energy.
- **H2 / adaptation:** Under uncertain or unseen winds, an adaptive policy *may* perform better than a fixed preplanned cycle, but may not outperform a fully optimized or robust conventional controller.
- **H3 / imperfect estimation:** Wind-estimation errors, observation lag and turbulence change both energy gain and safety; performance improvement should be assessed as a function of uncertainty, not asserted universally.
- **H4 / supervisory decision (optional):** A policy that decides whether to soar at all may reduce energy expenditure or risky maneuvers compared with an always-soar policy under mixed wind conditions.
- **H5 / model validation:** A low-cost small aircraft's measured glide polar or glide ratio may differ enough from idealized aerodynamic coefficients to alter simulated feasibility.

The student may refine and preregister a narrower primary hypothesis before the final experiment; record all revisions and reasons.

## 4. What the student will independently engineer

Possible student contributions:
- Physical airframe assembly / modifications, wiring, flight testing, and logging.
- Airframe parameter identification (mass, wing area, glide ratio, stall speed, control authority).
- Wind-gradient simulator and physically correct energy accounting.
- Wind estimator and robust/AI controller.
- Integration of simulator, flight control firmware, telemetry and repeatable test procedures.
- Controlled comparison, graphs, statistical analysis and documentation.
- Interpretation of constraints, failures and comparison to published work.

Distinguish original student design/code/measurements from copied, adapted or reproduced ideas, simulators and autopilot functions. Keep acknowledgments, licenses and paper references.

## 5. Explicit scope

**In scope:** a single fixed-wing UAV; shear-driven dynamic soaring; simulation + real airframe engineering; supervised flight control; energy/safety comparison; reproducibility.

**Not in the initial scope:** multi-aircraft swarms, thermal-updraft searching, ocean deployment, extreme-weather testing, autonomous outdoor soaring as a mandatory milestone, high-altitude flights, or a claim to world's-first AI dynamic soaring.

**2027 deliverables, conditional on feasibility:**
1. Flight-worthy prototype and bill of materials.
2. Verified physical/aerodynamic measurements and flight logs.
3. Published-reference-inspired simulator with unit and physics tests.
4. At least one credible conventional soaring baseline and one adaptive-control candidate.
5. Comparison plots with uncertainty and failure analysis.
6. A reproducible lab notebook, a concise CWSF research report and a demonstration.

## 6. Research standard

At CWSF, the depth comes from *what the aircraft and simulator allow us to measure and learn*. A polished build is important; so are a fair baseline, testable hypotheses, unexpected results and evidence-to-claim discipline. Reproducing established research is a legitimate learning and validation foundation, but a report should make clear which findings are replications and which are the student's own experiments or improvements.

## 7. Critical decisions still open

- Which airframe best supports accurate measurements: FW-01 or a more efficient dedicated glider?
- Which published model can be faithfully reproduced without unrealistic computing demands?
- What is the simplest wind-estimation algorithm with useful accuracy?
- What should the first learning task be: trajectory optimization, online tracking adaptation, or safe soar/no-soar switching?
- Is the project chiefly about **net mechanical energy**, **battery energy per distance**, or **endurance**? These are not interchangeable and require distinct tests.
- Which safe, legal outdoor tests can be performed in British Columbia?

See [decision log and risks](07-cwsf-story-risks-and-decisions.md).
