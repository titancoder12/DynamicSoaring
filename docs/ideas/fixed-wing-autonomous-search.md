# Fixed-wing autonomous search: energy, detection and cooperative flight

**Working title:** *Flying Farther Is Not Enough — Energy- and Detection-Aware Search with Autonomous Fixed-Wing Aircraft*  
**Documented:** 2026-09-18  
**Planning target:** CWSF 2027, Senior category  
**Status:** Candidate concept for investigation; not a selected final project, verified novelty claim, flight authorization or prediction of an award.

[Back to repository guide](../../README.md#how-to-use-this-analysis)

## 1. Purpose and discussion context

Chris is interested in aerospace, swarms of flying machines and possibly the search component of search and rescue. The desired project is not simply an impressive aircraft: it should combine rigorous scientific investigation with a practical solution whose usefulness is demonstrated.

This note preserves the autonomous-aeroplane discussion and its references. The proposed platform is a small electric fixed-wing aircraft, potentially a powered glider. The intended contribution is to investigate how flight decisions affect both energy consumption and useful search observations, then use that knowledge in an autonomous search strategy.

> Investigate how aircraft flight decisions affect energy use and search effectiveness, then build an autonomous fixed-wing system that uses those findings to search better.

This is an additional candidate alongside the earlier [seven research architectures](../../reports/analysis/cwsf2027-candidate-architectures.md), not a replacement for them or evidence that a final topic has been chosen.

### Evidence labels used in this note

- **Established background / prior art:** supported by the linked external references.
- **Historical-analysis interpretation:** a proposed design lesson from the repository's Senior CWSF analysis, not proof of what causes medals.
- **Proposed research:** questions, hypotheses, experiments and design choices suggested in our discussion. No results are claimed.
- **Open issue:** something that must be measured, checked or decided before committing to the project.

The experimental details below organize and modestly elaborate the discussion for planning. They are not a frozen protocol, confirmed hardware specification or comprehensive literature review.

## 2. Why a fixed-wing aeroplane?

A fixed-wing platform puts the research directly in contact with aerodynamics, flight dynamics, energy management, atmospheric sensing and control. NASA describes lift-to-drag ratio as an aerodynamic-efficiency measure and relates it to glide distance for a given height loss. That provides a physical foundation, but it does not by itself determine the best electric-aircraft search strategy. [R1]

**Proposed application framing:** begin with wide-area reconnaissance over a controlled search area, rather than hovering next to obstacles or navigating beneath a forest canopy. Flight planning would account for continuous motion, turns, wind and opportunities to observe a target during a pass.

Two different achievements must remain distinct:

| Platform achievement | Research achievement |
|---|---|
| An aircraft follows an autonomous mission. | A tested decision rule improves a meaningful search outcome or reveals an important operating limit. |
| Several aircraft share data. | Sharing is shown to help relative to the same fleet without the proposed coordination. |
| A powered glider stays airborne longer. | The extra endurance translates into useful search performance after accounting for time, sensing quality and electrical load. |

ArduPilot Plane already supports waypoint missions in AUTO mode, and its soaring functionality can respond to thermals to extend endurance with reduced motor use. These are enabling capabilities and possible baselines, not novel contributions by Chris. [R2][R3]

**Design preference from the discussion:** use established flight-control software where appropriate. Concentrate original work on one unresolved flight/sensing/mission question rather than simultaneously inventing an airframe, autopilot and detector.

## 3. Main candidate: useful search rather than longer flight

### Practical objective

Help one small aircraft, and eventually a cooperating team, find more search targets within a limited initial energy budget and a mission deadline while preserving a recovery reserve.

### Broad research question

> How do flight speed, altitude and energy-saving flight behaviour affect actual target-detection performance, and can a planner use measured relationships to make better search decisions?

This is deliberately a research direction, not yet a final hypothesis. The first study should isolate one principal tradeoff.

### Recommended first narrowing

> Under a fixed camera and detection system, when do flight-speed and altitude choices that conserve energy reduce useful target observations, and can a measured energy–detection model improve search success under matched resources?

**Proposed first experimental variables:** airspeed and altitude within an independently established safe operating envelope. Wind would initially be a measured condition or robustness test. Thermal soaring and communication limitations would be later extensions.

### Hypotheses to test, not assume

**H1 — Endurance and search success can diverge.** Some energy-saving flight choices may produce fewer useful observations or slower detection, so maximum endurance need not maximize target-finding success before a deadline.

**H2 — Joint planning can earn its complexity.** A planner using measured energy and detection relationships may outperform energy-only and ordinary survey strategies under some conditions. An equally credible outcome is that a simple, well-tuned baseline performs just as well.

**H3 — Cooperation has conditional value.** Sharing search observations or reallocating responsibilities may improve the same fleet's performance, but coordination costs or redundant information may eliminate that benefit.

A hypothetical example illustrates H1: one aircraft stays airborne longer but obtains poor search imagery; another spends more energy on a useful revisit and finds the target earlier. This example is motivation for an experiment, not an observed result.

## 4. Scientific finding → practical solution

The intended research chain is:

```text
A real search limitation: time and energy are constrained
        ↓
Measure how flight choices change energy use and detection
        ↓
Establish a relationship or operating boundary
        ↓
Develop a decision rule that uses the measured relationship
        ↓
Implement the rule on a fixed-wing aircraft
        ↓
Compare with credible alternatives under matched conditions
        ↓
Test whether a cooperating team adds further value
```

The scientific output should be more than a higher internal reward or longer flight. It might be a measured regime in which conserving energy helps or harms search, a validated model linking flight decisions to observations, or a decision method that improves the tradeoff.

The practical output should be a functioning aircraft executing the resulting search choices, with logs and controlled target-finding tests. A dummy-target demonstration establishes a bounded prototype capability, not operational search-and-rescue readiness.

## 5. Connection to the Senior CWSF analysis

The [engineering and robotics report][I1] recommends explicit claims, fair comparisons, independent evaluation and preservation of failure cases. Those practices appear across medal levels; the report does not establish a winning formula.

| Historical-analysis lesson | Application to the fixed-wing candidate |
|---|---|
| Optimize the real objective, not a convenient proxy. | Evaluate target finding and time, not only endurance, coverage or planner reward. |
| Cooperation needs a counterfactual. | Compare the same fleet with and without the proposed sharing or allocation rule. |
| Integration and validation are different achievements. | Separate component tests, simulation, one-aircraft flights and simultaneous multi-aircraft evidence. |
| Retain unfavorable conditions. | Include situations where conserving energy, revisiting or cooperating provides little benefit. |
| Count independent experiments properly. | Use independent scenarios or flight runs rather than treating every video frame as a replicate. |

These are prospective design choices informed by the reports. Neither the fixed-wing platform nor the presence of statistics, AI or real flight is evidence of a likely medal. See also the [2027 design implications][I2] and [analysis evidence boundaries][I3].

## 6. Proposed experimental programme

### Stage A — Characterize one aircraft and its sensing system

Begin with one reliable, instrumented aircraft. Measure flight performance, electrical energy and observation quality under selected conditions. Use controlled dummy targets and retain independent target-location records.

Keep the camera, detection model and detection threshold fixed for the initial flight-policy comparisons. Record flight choices, target detections, false alarms, time and energy with compatible timestamps.

Characterization should establish what the aircraft and camera actually do. It should not assume that a flight-simulation model, camera footprint or detector-confidence score is a validated measurement of search success.

**Deliverable:** a measured flight/sensing dataset and a model checked against those measurements.

### Stage B — Establish the tradeoff

Test the restricted speed/altitude question using repeated conditions and new target layouts. Separate data used to construct or tune the model from final evaluation data.

A flight strategy should be allowed to lose. For example, a lower-energy option could fail to improve detection, or an apparently useful revisit could consume more time than it saves.

**Deliverable:** a documented relationship between selected flight decisions, energy cost and useful search outcomes, including uncertainty and failure conditions.

### Stage C — Develop and validate the autonomous decision rule

Use the measured relationship in a planner that chooses among a limited set of prevalidated flight options. Start with an interpretable rule or model; reinforcement learning is optional, not a requirement for sophistication.

A simulator can support paired comparisons across many scenarios, but it must use a sensing/energy model with documented limits. The planner must not access hidden target truth or information unavailable to a deployed aircraft.

**Deliverable:** an autonomous search strategy and comparisons with credible alternatives, followed by a physical one-aircraft demonstration.

### Stage D — Add genuine cooperation

Once the base experiment works, aim for a second aircraft if resources, permissions and supervision allow. Larger teams can be explored in simulation.

Compare an independently searching fleet with the same fleet using the proposed coordination. Possible shared information includes search observations, unresolved target candidates and, in a later soaring extension, reports of rising air.

Repeated flights by one aircraft can characterize sensing or support replay-based evaluation. They cannot establish simultaneous real-world swarm coordination. Label simulated, replayed and physical evidence separately.

**Deliverable:** a small-team result that isolates the contribution of cooperation rather than merely increasing aircraft count.

## 7. Evaluation contract

The following is a proposed contract to refine after the pilot, not a claim that a final study has already been preregistered.

### Primary outcome

> Probability of finding the target before a specified deadline, using the same fleet and initial energy budget, while maintaining a defined recovery reserve.

Choose the operational definition of a valid detection and the false-alarm tolerance before final testing. Include target-absent trials so a method cannot appear successful by reporting everything as a target.

### Secondary outcomes

- Time to first valid detection, with unsuccessful searches retained rather than discarded.
- Electrical energy consumed and recovery-reserve compliance.
- Detection and false-alarm outcomes under each tested condition.
- Flight duration, search coverage and revisits as explanatory measures rather than automatic substitutes for success.
- Communication and computation costs when the cooperative extension is evaluated.

Measure total electrical load where practical, including propulsion and onboard equipment. Specify whether takeoff, climb, search and recovery are included in each comparison. Do not silently count only motor energy while describing a whole-mission battery result.

### Comparators and component-removal tests

| Comparator | Purpose |
|---|---|
| Ordinary fixed survey pattern | Practical simple reference. |
| Energy-oriented planner | Tests whether conserving energy alone is sufficient. |
| Credible existing search-oriented planner | Avoids comparing only with a deliberately weak baseline. The exact method is still to be selected through literature review. |
| Proposed planner without the learned/measured detection relationship | Isolates whether the sensing model actually changes outcomes. |
| Same fleet without the proposed coordination | Isolates cooperation from fleet size. |

Keep aircraft, camera, detector, initial resources and recovery rules comparable. Where simultaneous equality is impossible, report the tradeoff rather than hiding the difference in one score.

Use paired simulator scenarios and independent held-out layouts. For real flights, record weather and battery state, and balance or randomize test order where feasible. Report uncertainty at the scenario/flight level. The pilot should determine variability and a practical number of independent trials; no unsupported sample-size claim is made here. [I1][I2]

## 8. Optional aerospace-focused extension: autonomous soaring

A powered glider could gain altitude in rising air and then spend that altitude on useful search flight. Existing ArduPilot soaring support makes this a potential platform capability, not a new invention. [R3]

A 2024 Nature Communications paper by Flato and colleagues studies simulated reinforcement-learning-based thermal soaring in windy conditions, compares learned behaviour with vulture flight data, and investigates learning bottlenecks. It is a precedent for using flight as a scientific model problem, not evidence that Chris's search strategy is validated. [R4]

### Candidate soaring question

> When should a search aircraft divert to rising air, and when should it ignore that opportunity because its search task is more urgent?

### Candidate cooperative extension

> Does another aircraft's report of rising air improve that decision, and under what conditions does a stale or uncertain report cause a costly detour?

These are proposed questions. Sharing thermal information and cooperative soaring already have prior art; they must not be presented as new merely because Chris implements them.

### Direct overlap: SKYSURF

Mohamadi and Kara's February 2026 SKYSURF preprint studies cooperative powered gliders, thermal exploitation and persistent target monitoring in simulation. Section 3 models targets as mass points detectable on overflight and excludes takeoff/landing and avionic power consumption. [R5]

**Proposed follow-up, not a verified research gap:** test whether endurance-oriented benefits persist with measured detection errors, a mission deadline and complete electrical accounting. Changing assumptions is not automatically novelty; it must reveal a meaningful result beyond relevant prior work.

Keep soaring outside the minimum project's critical path. Its inclusion depends on the literature, the aircraft, suitable weather and safe access. Failure to obtain repeatable thermal flights must not erase the core energy–detection study.

## 9. Novelty and scope boundaries

| Established or already investigated | What this candidate would still need to establish |
|---|---|
| Autonomous waypoint missions. [R2] | A distinct, tested mission decision method. |
| Autonomous thermalling, including prior real-aircraft tests. [R3][R7] | A narrower contribution tied to useful search rather than thermalling itself. |
| Learning-based thermal soaring. [R4] | A question and evaluation beyond reproducing established soaring behaviour. |
| Cooperative glider monitoring and thermal exploitation. [R5] | A defensible difference from the closest cooperative-search/soaring approaches. |

The initial literature set is a starting point, not an exhaustive novelty review. In particular, energy-aware aerial search and sensor-aware flight planning require a focused search before claiming that the narrowed speed/altitude question is unresolved.

Do not assume that adding AI, using several aircraft, or combining existing components creates a scientific contribution. Reproduction of a strong existing method may be an essential first milestone.

## 10. Feasibility, safety and open decisions

The initial design should not combine a custom airframe, custom autopilot, new image detector, unrestricted learned flight control, thermal soaring and a large fleet. Select one principal research contribution and use the other components to support it.

**Proposed platform approach:** one small electric fixed-wing aircraft first, potentially a powered glider; an established autopilot; a fixed camera/detector; appropriate instrumentation; supervised testing with pilot takeover. Hardware selection has not been made.

**Unknowns:** budget, available aircraft, flying experience, mentor support, test-site access, flight permissions, camera capability, localization/airspeed instrumentation and seasonal conditions. Do not turn those unknowns into assumed resources or a procurement commitment.

Transport Canada's official guidance distinguishes operation categories, pilot requirements, locations and special permissions. Confirm the requirements for the actual aircraft and planned single- or multi-aircraft activity before outdoor tests. This note is not legal clearance or a flight manual. [R6]

Use controlled dummy-target trials, not active rescue incidents or unattended wilderness operations. A consultation with an appropriate SAR practitioner could later establish which output would be useful to a search team, but no such validation is claimed here.

### Decision gates

1. **Novelty:** identify the closest energy-aware search and cooperative-soaring methods and state the exact unresolved question. Change direction if they already answer it under equivalent assumptions.
2. **Measurement:** demonstrate repeatable energy and detection measurements with adequate independent reference data.
3. **Base result:** establish whether the selected flight tradeoff exists before adding fleet complexity.
4. **Practical implementation:** demonstrate the decision rule on one aircraft under controlled conditions.
5. **Cooperation:** add a second aircraft only when it enables a testable additional contribution.
6. **Soaring:** retain as an extension only if novelty, repeatability and flight access justify it.

## 11. Intended deliverables and current status

Potential deliverables are a focused prior-art matrix, measured flight/sensing dataset, reproducible simulator, validated decision method, physical prototype, same-fleet cooperation comparison and report of both favorable and unfavorable regimes.

**Nothing in this note reports completed fixed-wing experiments.** There is no selected airframe, committed fleet size, verified novel algorithm, measured performance gain or final CWSF 2027 topic decision.

The provisional recommendation remains:

> Build the project around what it teaches us about flying for a useful purpose—not simply around the fact that the aeroplane flies autonomously.

## 12. References and source checks

The references cited or directly implicated in the fixed-wing discussion are retained below, including both SKYSURF abstract and full-text links. R7 is an additional foundational source reached from ArduPilot's soaring documentation. External sources were checked on **2026-09-18**. Links are provided rather than republishing entire papers or manuals.

### R1 — Aerodynamic foundation

**NASA Glenn Research Center.** *Lift to Drag Ratio.* Official educational reference.  
URL: https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/lift-to-drag-ratio/

Supports the role of lift-to-drag ratio and its relationship to glide angle/range. It does not establish a battery endurance model or target-detection performance for the proposed aircraft. Page text inspected.

### R2 — Existing autonomous mission capability

**ArduPilot.** *AUTO Mode — Plane documentation.* Official living documentation.  
URL: https://ardupilot.org/plane/docs/auto-mode.html

Supports waypoint-mission execution and documents pilot-input behaviour. This is platform background, not novelty or proof that a specific installation is safe. Page text inspected; no firmware version or aircraft configuration is selected here.

### R3 — Existing autonomous soaring capability

**ArduPilot.** *Soaring — Plane documentation.* Official living documentation.  
URL: https://ardupilot.org/plane/docs/soaring.html

Supports thermal-responsive soaring as an existing capability and identifies airframe/instrumentation considerations. The page links to ArduSoar (R7). Page text inspected; detailed setup is intentionally left to a later supervised engineering plan.

### R4 — Learning and scientific investigation of thermal soaring

**Flato, Y., Harel, R., Tamar, A., Nathan, R., & Beatus, T. (2024).** *Revealing principles of autonomous thermal soaring in windy conditions using vulture-inspired deep reinforcement-learning.* **Nature Communications, 15**, 4942.  
DOI: https://doi.org/10.1038/s41467-024-48670-x  
Publisher: https://www.nature.com/articles/s41467-024-48670-x  
Author-lab PDF: https://huji.move-ecol.com/sites/default/files/s41467-024-48670-x.pdf

The author-hosted published paper's abstract and introductory text were inspected after the publisher page encountered a redirect/access problem. The study develops a simulation-based learning system and compares behaviour with bird-flight data; it is not a completed SAR fleet demonstration. No numerical results were independently reproduced for this note.

### R5 — Closely overlapping cooperative-glider research

**Mohamadi, H. E., & Kara, N. (2026).** *SKYSURF: A Self-learning Framework for Persistent Surveillance using Cooperative Aerial Gliders.* **arXiv:2602.12838v1**, submitted 13 February 2026.  
Abstract: https://arxiv.org/abs/2602.12838  
Versioned text: https://arxiv.org/html/2602.12838v1  
DOI: https://doi.org/10.48550/arXiv.2602.12838

Abstract and relevant problem-formulation/mission text inspected. The assumptions discussed above are explicitly listed in Section 3, items 7 and 9. Treat this as a preprint and simulation study, not independently reproduced performance or operational SAR validation. Its omission of some effects motivates checking robustness, not dismissing the study.

### R6 — Canadian flight-planning reference

**Transport Canada.** *Learn the rules before you fly your drone.* Official guidance hub.  
URL: https://tc.canada.ca/en/aviation/drone-safety/learn-rules-you-fly-your-drone

Page inspected; it links to operation categories, pilot certificates, legal/safety guidance, where to fly and special-operation permissions. Requirements must be checked again for the actual test plan. No particular operation is authorized by this concept note.

### R7 — Supplementary foundational soaring paper

**Tabor, S., Guilliard, I., & Kolobov, A. (2018).** *ArduSoar: an Open-Source Thermalling Controller for Resource-Constrained Autopilots.* Referenced by ArduPilot as an IROS 2018 paper; **arXiv:1802.08215v2**.  
Abstract: https://arxiv.org/abs/1802.08215  
Versioned record: https://arxiv.org/abs/1802.08215v2

Added during documentation through R3. Abstract and version history inspected. The authors report real small-UAV flight tests. This strengthens the requirement not to claim autonomous thermalling itself as new; the method has not been reproduced here.

### Internal analysis and methodology

- **I1:** [Senior engineering and robotics patterns][I1] — source of the design lessons about counterfactuals, proxies, integration and independent evaluation.
- **I2:** [Implications for CWSF 2027][I2] — evaluation discipline and limits on interpreting the historical sample.
- **I3:** [Senior historical analysis overview][I3] — scope, uneven evidence depth and absence of a proven medal formula.
- [Research design](../02-research-design.md), [data schema](../03-data-schema.md), [collection protocol](../04-collection-protocol.md) and [decision log](../07-decision-log.md) govern the historical study. This concept note does not modify its records or coding definitions.

[R1]: https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/lift-to-drag-ratio/
[R2]: https://ardupilot.org/plane/docs/auto-mode.html
[R3]: https://ardupilot.org/plane/docs/soaring.html
[R4]: https://doi.org/10.1038/s41467-024-48670-x
[R5]: https://arxiv.org/html/2602.12838v1
[R6]: https://tc.canada.ca/en/aviation/drone-safety/learn-rules-you-fly-your-drone
[R7]: https://arxiv.org/abs/1802.08215v2
[I1]: ../../reports/analysis/engineering-robotics-patterns.md
[I2]: ../../reports/analysis/cwsf2027-design-implications.md
[I3]: ../../reports/analysis/README.md
