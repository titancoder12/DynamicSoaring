# Search for Safety: uncertainty-aware aerial sensing for humanitarian route assessment

**Documented:** 2026-10-18  
**Target:** Possible CWSF 2027 Senior research direction.  
**Status:** Integrated *candidate* concept only. No final topic, novelty validation, simulated performance, physical experiment, operational evacuation system, or medal prediction.  
**Origin:** User watched [a documentary](https://www.youtube.com/watch?v=CyA9s4MEwnw) and proposed (1) fixed-wing observation of FPV-sized drones, (2) safer-route planning for civilians in war/disaster zones, and (3) identifying and protecting people from FPV threats, with the overarching objective **"rather than attack, protect people in war zones."** The linked video's full transcript was not independently reviewed, so no specific scenes are attributed.

[Idea library](README.md) · [Airborne detection](humanitarian-fixed-wing-drone-detection.md) · [Route assessment](uncertainty-aware-civilian-route-assessment.md) · [Passive warning](passive-drone-early-warning.md) · [Search Without False Confidence](cooperative-aerial-search-under-occlusion.md)

## 1. The integrated concept in plain language

A fixed-wing survey aircraft, or simulated group of aerial sensors, collects imperfect observations about road access and hazards. A decision-support system estimates the uncertainty of each observation, accounts for shared blind spots and older data, and decides **what to inspect again** before assessing potential routes. It can also say "insufficient evidence" rather than give false reassurance.

```text
Unarmed aerial/ground sensors or simulated agents
      -> imperfect timestamped observations
      -> evidence quality, overlap and freshness estimation
      -> candidate route risk assessments
      -> select a valuable new inspection / withhold recommendation
      -> updated assessment, explanation and human review
```

This is **relative risk assessment in controlled simulations**, not identification of a real-world "safe corridor." Detection of benign small drones and passive early warning are independently testable modules, not mandatory components of the routing study.

## 2. Scientific and humanitarian motivation (established background)

UN HRMMU reported at least **395 civilians killed and 2,635 injured** by short-range drone attacks from February 2022 to April 2025, including civilian travel and humanitarian activity [R2]. These dated observations establish the importance of protecting civilians; they do **not** demonstrate the effectiveness of this proposal or describe the current casualty total.

The ICRC explains that humanitarian safe passages are agreements between conflict parties and can remain hazardous even when agreed [R3]. Therefore an algorithm cannot guarantee safety in active hostilities, and a school project should not provide live conflict-zone route decisions. **Natural-disaster-type blocked roads, controlled optical observations and synthetic hazards** provide a bounded experimental analogue.

## 3. Proposed core research question

> Under a fixed inspection budget, correlated missed observations and uncertain road conditions, can a decision-aware verification/abstention method reduce **confidently incorrect low-risk route assessments**, compared with established sensing and routing policies?

A particularly tractable first test is **false confidence from correlated inspections**: five nearby views may repeat one blind spot, not provide five independent confirmations. Stale reports are a valuable later extension rather than a simultaneous first variable.

### Falsifiable hypotheses (not findings)

- **H1 — False independence:** Naively multiplying confidence from shared-error observations leads to unreliable low-risk route classifications.
- **H2 — Decision-aware sensing:** Selective inspections of route-critical unknown segments can outperform uniform inspection or uncertainty-only sensing under certain budgets.
- **H3 — Honest uncertainty:** Withholding unsupported route assessments can reduce false reassurance but increases unresolved cases and time; quantify both.
- **H4 — Conditional benefit:** Under fully visible or stable easy conditions, extra verification may have little benefit or lose to simpler methods.

The most valuable result may be a **boundary map** explaining when the advanced method does and does not help, not merely a higher overall score.

## 4. Four separately documented candidate components

| Direction | Proposed contribution | Independent note |
|---|---|---|
| Fixed-wing camera sensing of small drones | Reliability, visual domain shift, uncertainty, bird confounders | [Aerial detection](humanitarian-fixed-wing-drone-detection.md) |
| Route-aware uncertain sensing | Correlated/stale evidence, route-risk confidence, decision-aware inspection | [Route assessment](uncertainty-aware-civilian-route-assessment.md) |
| Passive early warning | Audio/visual fusion, false alarms, warning calibration | [Passive warning](passive-drone-early-warning.md) |
| Combined humanitarian system | Allocate sensing to avoid unjustified route confidence and explain uncertainty | This note |

**Critical scope discipline:** Proving one scientific relationship with one camera and a simulator is stronger than integrating all four modules without robust comparison. No drone disabling, RF jamming, hacking, interception or offensive targeting is part of any proposed experiment.

## 5. Proposed experiment: minimum defensible design

### Stage 0 — Prior art and precise contribution gate

Compare the latest related 2026 UAV route-inspection papers [R4, R5] and the repo's occlusion/perception references. Document assumptions, accessible sensors, budgets, staleness/correlation model, abstention policy, success criteria and code availability. UAV-based road inspection is **already known**; novelty of the suggested false-confidence mitigation has not been verified. A new application label is not a scientific contribution.

### Stage 1 — Reproduce a failure mechanism

Construct a synthetic road network with hidden true blocked/passable segments. Simulated inspection produces imperfect observations with independently controlled shared blind spots. Give the model *only* the noisy observations, while an independent scorer retains truth. Establish whether repeated observations create measurable overconfidence under realistic assumptions.

**Deliverable:** Ground-truth checked simulator, calibrated baseline, and a plotted relationship between error correlation and unsupported confidence (including failures to reproduce the predicted effect).

### Stage 2 — Fairly compare route and sensing policies

| Policy | What it isolates |
|---|---|
| Optimistic shortest-route | Basic routing without new evidence |
| Conservative route without inspection | Caution versus sensing |
| Fixed/uniform road inspection | Coverage without adaptive decisions |
| Uncertainty-first active inspection | Information gain alone |
| Credible published joint inspection/routing baseline | Strong relevant prior work |
| Proposed decision-aware verification with abstention | Additional original mechanism, if one survives the novelty gate |

Match inspection and computation budgets, initial knowledge, sensor noise, risk threshold and allowed planning horizon. Avoid privileging the proposed method with hidden truth or unequal tuning.

### Stage 3 — Prespecified outcomes and independent evaluation

**Primary endpoint:** False-low-risk route assessments at a **predeclared minimum recommendation coverage and fixed observation budget**. Any method that abstains on everything fails the practical comparison.

**Secondary:** Route failures, path cost, sensing time/energy, risk-calibration error, decision delays, abstention/human-review rates, false alerts, and regret against an omniscient *diagnostic only* oracle.

Use paired independent held-out road maps, hazard seeds and observation conditions. Summarize uncertainty across independent scenarios, **not** across adjacent frames or timesteps. Include scenario classes where the proposed method has no advantage. Freeze evaluation rules before final testing.

### Stage 4 — Controlled real-sensor test

Use a tabletop road network with benign obstacles and independently recorded passability truth, inspecting with a camera from different viewpoints. A single permitted supervised hobby aircraft can later test the sensing distribution outdoors, but a real aircraft swarm is *not required* to answer the first question. Physical demo results should not be described as proof of real evacuation safety.

### Stage 5 — Optional multi-agent/fixed-wing extensions

Only if core results stand up: communication delay, multiple sensing agents, fixed-wing energy/detection constraints, or viewpoint-dependent occlusion. Keep thermal soaring, rocket-assisted launch and counter-drone hardware separate until they have independent research value.

## 6. Variables and evaluation contract

| Category | Candidate variables |
|---|---|
| Independent | Observation error correlation; observation age (later); partial visibility; inspection budget; policy |
| Dependent | False reassurance; assessment coverage; latency; route regret; calibration; resource cost |
| Controlled | Road graph distribution; true hazard sampling; sensor quality; initial data; resource accounting |
| Independent trial | New graph/incident scenario with distinct noise and hazard realization |

**Success:** Repeatable relation between evidence quality and route-assessment reliability, tested on new conditions and with a controlled physical analogue. **Valid negative result:** Simple method equals or beats complex method, or extra verification costs more than it helps. **Inconclusive:** Dataset leakage, inadequate ground truth, no credible baseline, unrepeatable scenario generation, conflated variables or unmatched costs.

## 7. Safety, deployment and ethics boundaries

- No live war-zone route recommendations, real-time tactical situational awareness, locations of civilians, humanitarian movements, checkpoints, or active drone threat locations. Do not publish sensitive movement information.
- Never designate a route "safe" based on software; use uncertainty-aware, relative assessments in research settings.
- No automatic hostile-intent inference, drone attack/disablement, jamming, spoofing, hacking, kinetic countermeasures or weaponization.
- Use lawful benign footage, anonymization and permission; follow current Canadian RPAS safety/airspace rules.
- RF scanning and interception have separate ISED obligations; Canada generally prohibits jammers [R7, R8].
- Real humanitarian corridors are negotiated and remain hazardous [R3]; only qualified humanitarian and emergency operators can judge field deployment.
- The core scientific test should be **non-adversarial** disaster-style hazards with independent ground truth.

## 8. Intellectual continuity with previous project work

The 2026 swarm project studied cooperation to find resources. [Information foraging](information-foraging-airborne-observatory.md) studies cooperation to find valuable measurements. Here, sensing is chosen **to support an honest human-safety decision**. It uses the same core concerns as [false confidence](false-confidence-under-model-mismatch.md), [occluded aerial search](cooperative-aerial-search-under-occlusion.md), and [delayed communications](delayed-communication-tradeoff.md), with the fixed-wing system as an optional measurement platform.

This is an **additional candidate**, not an automatic replacement for the [September 18 recommendation](recommendation-2026-09-18.md) or [Learning to Soar Together](learning-to-soar-together.md). Historical CWSF medal analysis suggests research-design standards, not a probability of winning.

## 9. Decision gates and actionable next steps

1. [ ] Review the documentary's actual transcript if citing particular scenes; current inspiration-only link is sufficient otherwise.
2. [ ] Build a closest-work matrix of [R4] and [R5] plus observation-dependence/route-risk methods; state an exact difference.
3. [ ] Select one core failure mechanism (start with correlated missed observations).
4. [ ] Define an honest false-reassurance/coverage primary outcome before implementation.
5. [ ] Reproduce the simple and strong baselines in a small seeded simulator.
6. [ ] Run a pilot, retain failures, and determine the independent replicate count from variance.
7. [ ] Check novelty again, then pursue a controlled camera validation if feasible.
8. [ ] Make a *separate explicit decision* before promoting this idea above prior shortlisted concepts.

## 10. Annotated references and boundaries

External sources below were checked from academic abstracts or primary institutional pages on 2026-10-18; **full methods and code have not been independently reproduced**.

- **[R1] Inspiration:** https://www.youtube.com/watch?v=CyA9s4MEwnw (user supplied; full video/transcript unavailable for verification).
- **[R2] UN HRMMU (26 June 2025):** *Deadly Drones: Civilians at Risk from Short-Range Drones*, February 2022–April 2025. https://ukraine.ohchr.org/en/Deadly-drones-Civilians-at-risk-from-short-range-drones-in-frontline-areas-of-Ukraine-24-February-2022-30-April-2025
- **[R3] ICRC:** *How humanitarian corridors work to help people in conflict zones.* https://www.icrc.org/en/document/how-humanitarian-corridors-work
- **[R4] Nguyen & Akella (2026):** *Dynamic UGV-UAV Cooperative Path Planning in Uncertain Environments.* https://arxiv.org/abs/2604.25267
- **[R5] Choi et al. (2026):** *Integrated Exploration-Aware UAV Route Optimization and Path Planning.* https://arxiv.org/abs/2605.28654
- **[R6] Isaac-Medina et al. (2021):** Visual UAV detection/tracking benchmark. https://openaccess.thecvf.com/content/ICCV2021W/AntiUAV/html/Isaac-Medina_Unmanned_Aerial_Vehicle_Visual_Detection_and_Tracking_Using_Deep_Neural_ICCVW_2021_paper.html
- **[R7] ISED (2025):** Canadian jammer prohibitions. https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/safety-and-compliance/compliance-and-enforcement/jammers-are-prohibited-canada-thats-law
- **[R8] ISED:** RF-scanning receiver guidance. https://ised-isde.canada.ca/site/certification-engineering-bureau/en/notice-2024-drs0010
- **[R9] Transport Canada:** RPAS rules. https://tc.canada.ca/en/aviation/drone-safety/learn-rules-you-fly-your-drone
- **[R10] Internal research:** [CWSF Senior analysis](../../reports/analysis/README.md) · [Design implications](../../reports/analysis/cwsf2027-design-implications.md)
