# Learning to Soar Together

## Performance-Aware Cooperative Search with Autonomous Gliders

**Documented:** 2026-09-21  
**Planning target:** CWSF 2027, Senior category  
**Origin:** The user proposed combining Flato et al.'s 2024 thermal-soaring study with Mohamadi and Kara's SKYSURF framework. This note records the resulting strategy discussion.  
**Status:** Candidate for serious investigation; not a selected final project, demonstrated performance gain, verified novelty claim, or prediction of a medal.

[Idea library](README.md) · [Broader cooperative-soaring idea](cooperative-thermal-soaring-search.md) · [Fixed-wing search concept](fixed-wing-autonomous-search.md)

> **Central question:** When does better individual flight control improve cooperative aerial search?

> **Proposed contribution:** A team planner that accounts for how well its aircraft can actually exploit rising air, rather than simply inserting a learned soaring controller into a cooperative search system.

## 1. Purpose: science that leads to a practical system

Chris is interested in aerospace, swarms of flying machines, and possibly the search component of search and rescue. The intended project combines scientific investigation with a practical system that uses the resulting knowledge.

The proposed platform is a small team of powered gliders. The aircraft would exploit rising air to conserve battery power while continuing a shared search mission. The aircraft, controller, fleet size, test site, and hardware budget have not been selected.

The contribution is **not merely connecting two existing algorithms**. It is investigating the interaction between local flight skill and team decisions, then testing whether a new connection between those layers improves the mission.

```text
Learn or characterize individual soaring capability
        ↓
Measure how uncertainty changes achievable performance
        ↓
Decide when soaring is useful for the mission
        ↓
Coordinate search and soaring across the team
        ↓
Evaluate target finding, time, energy, and failures
        ↓
Validate selected claims on physical aircraft
```

Throughout this document, paper descriptions are **source-derived background**. Questions, hypotheses, the A–E comparison, development stages, and suggested outcomes are **proposed research from the discussion**, not findings from the papers. Documentation-level clarifications do not freeze an implementation or experimental protocol.

## 2. The two-paper foundation

| Source | Relevant established contribution | Proposed role in Chris's project |
|---|---|---|
| **Flato et al., 2024, Nature Communications** [R1] | Simulation-based deep reinforcement learning for thermal soaring in horizontal wind; investigates learning bottlenecks, curriculum training, observation requirements, robustness, and behaviour compared with vulture flight data. | Foundation for investigating individual soaring skill and its reliability. |
| **Mohamadi and Kara, SKYSURF, 2026** [R2, R3] | Cooperative soaring-capable UAV framework with local/global behaviour management, task allocation, navigation, and control; evaluates persistent monitoring, target detection, and energy. | Foundation for the shared mission and coordinated decisions. |

These are overlapping contributions, not two disjoint modules. In particular, SKYSURF already includes local control as well as team management. Neither paper establishes that this proposed combination will improve Chris's search task.

### Publication and version note

SKYSURF has an arXiv version submitted on **13 February 2026** [R2] and a journal version published on **20 August 2026** in the *International Journal of Intelligent Robotics and Applications* [R3]. Earlier idea notes described the arXiv version only. The detailed assumptions used here refer to **arXiv v1**, not an assumed identical journal full text.

The publisher's public bibliography already cites Flato et al. and earlier multi-agent thermalling work. Therefore, “reinforcement learning plus cooperative gliders” is not itself a novelty claim. [R3]

## 3. The scientific issue between individual skill and mission success

### Broad question

> Does an aircraft that gains altitude more effectively automatically become a better member of a search team?

Do not assume the answer is yes.

**Hypothetical illustration, not an observed result:** two aircraft search different areas. One discovers rising air and circles efficiently, improving its local soaring outcome while delaying its assigned search. Another aircraft may have to compensate. In a different situation, a short diversion could save enough energy to finish a mission that otherwise would end early.

The proposed study asks when those outcomes differ and whether team decisions need to change to make use of improved individual flight control.

### Recommended first research question

> **Under uncertain wind estimates, does a cooperative planner that accounts for each aircraft's achievable soaring performance improve target-finding success compared with simply inserting a learned soaring controller into an existing coordination strategy?**

Start with wind-estimation error as the principal uncertainty. Do not initially combine communication failures, moving targets, multiple camera types, unfamiliar airframes, and complex terrain into the same experiment.

### Hypotheses to test

- **H1 — Local and mission performance can diverge.** Better individual soaring does not necessarily improve target-finding success before a deadline.
- **H2 — Performance-aware decisions may add value.** A planner using measured achievable soaring benefit and its uncertainty may improve mission performance beyond the straightforward controller/planner combination.
- **H3 — The benefit is conditional.** The added planning complexity may offer little advantage when estimates are accurate, useful thermals are absent, or the reference strategy already makes adequate decisions.

These hypotheses can be rejected. “The learned controller is better” must itself be measured, not assumed from the fact that it uses reinforcement learning.

## 4. Proposed original contribution: connect achievable flight performance to decisions

Instead of treating a reported thermal as automatically worth visiting, the proposed planner asks:

> Given this aircraft's state, the controller's measured capability, and uncertainty in the conditions, how much useful altitude is it likely to gain, and how much mission time will that cost?

It would use that estimate to decide whether an aircraft should:

1. continue searching;
2. divert to rising air; or
3. leave a thermal and resume its search responsibility.

A possible implementation would characterize a controller's expected altitude gain, exploitation success, and time cost across development conditions, then give the mission planner those estimates with an uncertainty description. This is a **proposed interface**, not a selected model or completed algorithm. The final estimator must use information available to the aircraft; its exact inputs and update rule remain open.

The scientific contribution would be a measured interaction between flight capability, uncertain information, and team outcomes. The practical contribution would be a planner that uses that relationship to make better search decisions.

### Training information is not deployment information

Flato et al. use a thermal-centre-dependent training reward but do not include the centre in the policy's observations. Their simulated actions change bank angle and angle of attack; wind information affects performance. [R1]

Preserve those distinctions when reproducing or adapting the method. Simulator truth may be used for training rewards and evaluation where explicitly declared, but hidden thermal or target truth must not become undeclared planner inputs during final testing.

The same rule applies to the proposed performance estimator: calibrate it using development data, not the answers to the final test missions.

## 5. Proposed A–E experiment

Keep the same fleet size, airframe model, environment, observation access, and mission resources unless a difference is the explicit factor being tested.

| System | Individual soaring | Team decisions | Purpose |
|---|---|---|---|
| **A — Reference system** | Conventional controller | Independent or fixed search assignments | Establish the reference. |
| **B — Improved individual skill** | Learned controller | Same assignments as A | Isolate the effect of learned local control. |
| **C — Improved cooperation** | Same conventional controller as A | Cooperative mission planner | Isolate cooperation under conventional control. |
| **D — Straightforward combination** | Same learned controller as B | Same cooperative planner as C | Test the basic combination of the two research directions. |
| **E — Proposed contribution** | Same learned controller as D | Cooperative planner informed by measured capability and uncertainty | Test whether the proposed connection between control and planning adds value. |

The cooperative planner may be based on a documented, reproducible subset of SKYSURF. Call it **SKYSURF-inspired** unless the relevant published method has actually been reproduced. Document changes in assumptions, modules, tuning, and evaluation.

### What the comparisons answer

- **A versus B:** Does learned control help without changing assignments?
- **A versus C:** Does cooperation help without changing the controller?
- **C versus D:** Does learned control improve the cooperative system?
- **D versus E:** Does Chris's proposed performance-aware planning add value beyond the straightforward combination?

**D versus E is the central test of the proposed additional contribution.** A comparison only against A would not distinguish original improvement from the benefits of stronger existing components.

Use credible, competently tuned alternatives. Give C and D a realistic integration and tuning effort; E should not win merely because D was left improperly configured. Keep the learned controller fixed between D and E during the comparison so the planner's contribution can be interpreted.

## 6. Outcomes, resource accounting, and independent evidence

### Proposed primary outcome

> **Probability of finding a target before a fixed deadline, using the same aircraft count and initial energy budget, while preserving a defined recovery reserve.**

Operational definitions of a valid detection, allowable false alarms, mission failure, and the reserve must be specified before final testing. They are not numerical requirements established by this note.

### Supporting outcomes

Record time to valid detection, total electrical energy, altitude gained, unsuccessful thermal diversions, and missed search opportunities. Retain unsuccessful searches in the analysis rather than reporting detection time only for successful missions.

Longer endurance and greater altitude gain are explanatory measurements, not automatic evidence of better search performance.

### Initial sensing model and later realism check

SKYSURF arXiv v1 models targets as points detectable on overflight and omits takeoff/landing and avionics energy in its problem formulation. [R2, Section 3, items 7 and 9]

For the first controlled comparison, use a common, clearly labeled simplified detection model across A–E. This isolates the flight-and-planning interaction. Later, test whether the result survives a measured camera/detection model and more complete electrical accounting.

Do not change the sensing model only for E. Do not treat a monitoring result as proof of real search-and-rescue effectiveness.

### Proposed validation discipline

Use the same held-out mission scenarios across methods. Separate development, tuning, and final evaluation conditions. Run multiple independently trained policies where learning variability matters, rather than selecting only the best seed.

Report uncertainty across independent policies and missions; simulation timesteps or consecutive camera frames are not independent mission trials. Pilot results should inform the practical number of repeats. No statistical power or effect size is asserted in this concept note.

Include accurate-estimate conditions as well as controlled wind-estimation errors. Keep true weather separate from the estimate supplied to each method, so the experiment can distinguish environmental difficulty from information quality. Define only the initial uncertainty model needed for that test; added complexities are later extensions.

These are proposed evaluation choices, informed by the repository's emphasis on fair comparisons, independent evidence, and honest claim boundaries. [I1, I2]

## 7. Simulation-led development with physical validation

### Stage 1 — Reproduce essential components

Establish a credible conventional soaring reference, a learning-based local controller, and a manageable cooperative mission model. Check compatible units, airframe dynamics, action interfaces, energy definitions, and observations before combining them.

The two papers are not plug-and-play implementations of one aircraft. An abstract control action in simulation is not already an actuator command that can safely be flown. Use established stabilizing flight-control software for initial physical work; do not assume unrestricted learned control is required.

**Output:** documented reproductions or adaptations with known discrepancies and baseline results.

### Stage 2 — Run the controlled mission comparison

Implement A–E in a shared evaluation environment. First establish whether individual soaring performance changes as expected, then test whether mission results change with it.

**Output:** results showing where the combination helps, where it does not, and which component accounts for the difference. A functioning simulation alone is not the intended scientific conclusion.

### Stage 3 — Test controller interfaces on hardware

Hardware-in-the-loop testing can run intended controller hardware against a simulator to examine timing and interfaces. It cannot validate the simulator's aerodynamic or atmospheric assumptions.

**Output:** interface and timing evidence, explicitly separate from physical soaring evidence.

### Stage 4 — Validate selected claims on one powered glider

Begin with an instrumented aircraft and supervised testing with pilot takeover. Measure flight behaviour and electrical consumption, and check which aspects of the simulation match those measurements.

**Output:** a bounded physical flight and energy dataset. Do not claim that validating one subsystem validates the full autonomous search mission.

### Stage 5 — Demonstrate cooperation when feasible

A second aircraft can support a genuine cooperative demonstration once the base system, supervision, test access, and permissions are established. A larger fleet can remain a simulation study.

Repeated flights by one aircraft are useful for characterization and replay tests, but are not evidence of simultaneous real-world swarm coordination.

**Output:** a small-team result if achieved, with simulation, replay, and physical evidence labeled separately.

## 8. What the project could establish

These are **examples of possible conclusions**, not promised findings:

- A locally stronger controller improves search only when the team planner accounts for its actual performance under uncertain estimates.
- A simpler planner already captures most of the available benefit, making the added uncertainty model unnecessary in the tested regime.
- Gains appear in simulation but do not transfer to the measured aircraft, revealing a specific modeling limitation.
- Soaring improves endurance but harms time-critical target finding under some conditions.

A negative result is valuable when it answers the research question and identifies a supported limitation. Failure to complete an integration is not, by itself, an equivalent scientific result.

## 9. Novelty boundaries and feasibility risks

The project must not claim to invent autonomous thermalling, learned soaring, cooperative gliders, or the use of rising air for mission endurance. It must identify a precise difference from the closest existing methods and show why that difference affects a meaningful conclusion. [R1–R3]

The focused novelty review must cover **performance-aware and uncertainty-aware mission planning**, not only the two motivating papers. Existing work may already answer the proposed question under equivalent assumptions. Reproduction, rigorous comparison, or a revised question may then be the appropriate next step.

Open feasibility issues include controller/code availability and licensing, compute needs, the chosen airframe, instruments, flight experience, mentor support, budget, test-site access, and repeatable suitable conditions. No equipment or permission is assumed to exist merely because it would be useful.

Before physical trials, establish the applicable operating requirements and safe supervised test plan. This note is not a flight procedure or an authorization for autonomous operations. Use controlled test targets, not active rescue incidents.

Keep uncertain wind estimates as the first research condition. Thermal-map sharing, communication delays, real camera errors, and larger fleets can be added only when they answer a necessary follow-up question.

## 10. Why retain this idea for CWSF 2027?

This is an application of the historical analysis, not a conclusion about award probabilities.

| Proposed project element | Corresponding research structure in the analysis |
|---|---|
| Measure controller behaviour across conditions | Engineering experiment |
| Investigate a mismatch between local success and mission success | Benchmark and failure analysis |
| Redesign planning around the measured limitation | Mechanism-informed redesign |
| Demonstrate the integrated search system | Integrated functional system |

The analysis recognizes these structures across medal levels and does not establish a winning formula. [I1, I2]

The combination strengthens the technical foundation of the fixed-wing idea and fits Chris's interests in aerospace and swarm learning. It does not remove the prior-art and physical-validation risks noted in the earlier [recommendation](recommendation-2026-09-18.md).

**Recommendation recorded from the discussion:** investigate this direction seriously, with the original contribution located in the interaction between measured individual capability and team decisions. This documentation does not silently replace the earlier ranking or select the final project.

## 11. Next decision gates and expected deliverables

1. **Closest-work gate:** write a comparison of the two papers and the nearest performance-aware planning approaches. State the exact proposed difference and its consequence.
2. **Reproduction gate:** obtain compatible, credible reference components. Record adaptations rather than claiming exact reproduction without evidence.
3. **Scientific gate:** demonstrate a measurable local-versus-mission interaction before building extra fleet complexity.
4. **Contribution gate:** compare D and E under equal resources, observation access, and fair tuning.
5. **Physical gate:** determine which claims can be tested on the available aircraft and document anything that remains simulation-only.

Potential deliverables are the prior-art matrix, controller-capability characterization, A–E evaluation code and results, a measured flight/energy dataset, a hardware demonstration, and a report explaining successful and unsuccessful regimes.

The project objective remains:

> **Use the two papers to investigate a new, testable problem—not merely demonstrate that their components can be connected.**

## 12. References and source-verification notes

These sources were checked for this documentation on **2026-09-21**. This was a targeted verification of the discussion, not a new exhaustive literature review or an independent reproduction of either paper.

### R1 — Individual thermal-soaring learning

**Flato, Y., Harel, R., Tamar, A., Nathan, R., & Beatus, T. (2024).** *Revealing principles of autonomous thermal soaring in windy conditions using vulture-inspired deep reinforcement-learning.* **Nature Communications, 15**, 4942.

- DOI: https://doi.org/10.1038/s41467-024-48670-x
- Publisher: https://www.nature.com/articles/s41467-024-48670-x
- Author-hosted published PDF: https://huji.move-ecol.com/sites/default/files/s41467-024-48670-x.pdf

**Inspection:** the publisher URL encountered a redirect error; the author-hosted published PDF supplied the abstract and printed page 2, including training observations/actions and reward boundaries. Page 2 was also inspected visually. No numerical performance claim was independently reproduced.

### R2 — SKYSURF, versioned open manuscript

**Mohamadi, H. E., & Kara, N. (2026).** *SKYSURF: A Self-learning Framework for Persistent Surveillance using Cooperative Aerial Gliders.* **arXiv:2602.12838v1**, submitted 13 February 2026.

- Abstract: https://arxiv.org/abs/2602.12838
- Versioned HTML: https://arxiv.org/html/2602.12838v1
- arXiv DOI: https://doi.org/10.48550/arXiv.2602.12838

**Inspection:** abstract, Section 3 assumptions, framework outline, and bibliography. The detection and power-accounting qualifications above are specifically attributed to this version. This is not a numerical reproduction.

### R3 — SKYSURF, journal record

**Mohamadi, H., & Kara, N. (2026).** *SKYSURF: a self-learning framework for persistent surveillance using cooperative aerial gliders.* **International Journal of Intelligent Robotics and Applications**. Published 20 August 2026.

- DOI: https://doi.org/10.1007/s41315-026-00553-8
- Publisher record: https://link.springer.com/article/10.1007/s41315-026-00553-8

**Inspection:** public metadata, abstract, and bibliography. Full subscription text was not reviewed or compared line by line with arXiv v1. The record corrects the earlier preprint-only description; the two records are versions of the same work, not independent evidence.

### Internal analysis and related concepts

- **I1:** [Evidence-grounded Senior project archetypes](../../reports/analysis/project-archetypes.md).
- **I2:** [Senior engineering and robotics patterns](../../reports/analysis/engineering-robotics-patterns.md).
- [Senior analysis overview and evidence boundaries](../../reports/analysis/README.md).
- [CWSF 2027 design implications](../../reports/analysis/cwsf2027-design-implications.md).
- [Fixed-wing autonomous search](fixed-wing-autonomous-search.md).
- [Broader cooperative thermal-soaring concept](cooperative-thermal-soaring-search.md), including its ArduSoar and ArduPilot background references.
- [Recommendation dated 2026-09-18](recommendation-2026-09-18.md), preserved as the prior selection rationale.

[R1]: https://doi.org/10.1038/s41467-024-48670-x
[R2]: https://arxiv.org/html/2602.12838v1
[R3]: https://doi.org/10.1007/s41315-026-00553-8
[R1–R3]: #12-references-and-source-verification-notes
[I1]: ../../reports/analysis/project-archetypes.md
[I2]: ../../reports/analysis/engineering-robotics-patterns.md
