# Uncertainty-aware route assessment for civilian evacuation and disaster response

**Documented:** 2026-10-18  
**Status:** Unselected candidate. No simulation, field validation, verified novelty, or operational route recommendation exists yet.  
**Origin:** User idea of planning safer civilian movement in war/disaster zones rather than attacking; inspired by [this documentary](https://www.youtube.com/watch?v=CyA9s4MEwnw). No exact scenes are attributed without a reviewed transcript.

[Idea library](README.md) · [Integrated proposal](search-for-safety-humanitarian-aerial-intelligence.md) · [Occluded search](cooperative-aerial-search-under-occlusion.md)

## 1. Why this is a research problem

After disasters, roads may be blocked, destroyed or uncertain. Some reports are old, incomplete or based on overlapping camera views. A shortest-path planner can recommend a road that only *appears* passable. A conservative planner can avoid all uncertain roads and delay assistance unnecessarily.

For the research, "lower risk" is an **evidence-bounded assessment**, not a claim that a route is safe. Active conflict adds unpredictable human threats, legal/humanitarian coordination and rapidly changing conditions, making real-time route advice inappropriate for a student prototype.

## 2. Proposed scientific question and hypotheses

> Under limited sensing time, observation errors and uncertain road conditions, can decision-aware aerial inspection plus calibrated abstention reduce **false-low-risk route recommendations**, compared with credible existing route/inspection methods?

The most tractable initial question is how **correlated missed observations** affect confidence that a road segment is passable. Observation staleness can be studied later as a second mechanism.

- **H1:** Treating correlated negative inspections as independent leads to overconfident wrong passability estimates.
- **H2:** Inspecting a road segment because it could *change the route decision*, rather than merely because it is uncertain, helps reduce false-low-risk conclusions under some sensing budgets.
- **H3:** In fully visible/easy networks, the extra verification may waste time and offer no advantage.
- **H4:** Abstaining when evidence is insufficient reduces unsupported confident choices but increases delay and the fraction of unresolved cases.

Each hypothesis may fail. A negative comparison is acceptable scientific evidence.

## 3. Proposed simulation and experiment

**World:** Synthetic road graph with hidden ground-truth passable/blocked edges, uncertain reports, inspection costs, and a fixed travel/sensing budget. Start with benign disaster-like hazards: floodwater, debris or damaged bridges. The hidden true state is visible to the scorer but **never to the decision algorithm**.

**Pilot A — establish a confidence failure:** Give a simple belief updater multiple observations affected by one shared occlusion/error source. Quantify when its reported confidence and actual passability disagreement diverge. Validate simulator mechanics first.

**Pilot B — fair planner comparison:** Give each method exactly the same initial reports, ground-sensor capabilities, camera assumptions, computation/tuning opportunity and total inspection budget.

| Baseline/policy | Purpose |
|---|---|
| Optimistic shortest path | Common simple reference |
| Conservative route with no inspections | Tests whether mere caution is sufficient |
| Uniform fixed inspection | Non-adaptive sensing baseline |
| Uncertainty-first inspection | Standard active-sensing baseline |
| Published joint UAV–road planning algorithm or explicit approximation | Strong closest-work reference |
| Proposed decision-aware verification/abstention | Isolates additional method |

**Pilot C — generalization:** Freeze tuning and test unseen road graphs, noise seeds, obstacle placements and easier/harder regimes. Later vary observation freshness independently instead of changing every assumption together.

**Pilot D — controlled physical mini-world:** Build a tabletop/mock road network. Use a static camera or safely moved sensor to inspect benign hidden obstacles, with independent ground-truth labels. A permitted small aircraft is an optional validation *extension*, not prerequisite.

### Proposed variables and success metric

| Kind | Values |
|---|---|
| Independent | Error correlation, partial observability, inspection budget, observation freshness (later), planner choice |
| Dependent | False-low-risk recommendation rate, recommendation coverage, delay, path cost, inspection effort, calibration |
| Controlled | Same map/obstacle distributions, starting observations, sensor reliability, tuning and budget |
| Replication | Independently generated maps/scenarios, not frames or adjacent road edges |

**Primary endpoint:** false-low-risk route assessment rate **at a declared minimum recommendation coverage and fixed inspection budget**. Also report abstention and elapsed time. A planner that refuses every route is not automatically successful. Use paired scenarios, confidence intervals, unchanged holdouts and honest accounting of failed trials. An omniscient planner may provide a diagnostic upper bound, but is not a fair deployable competitor.

**Success:** A reproducible reduction in false reassurance for a named failure regime without disproportionate cost. **Failure:** A simpler policy is equally good. **Inconclusive:** Leakage of ground truth, unequal resource budgets, little independent replication, or no realistic error mechanism.

## 4. Existing research is already close

The general claim "UAVs inspect risky roads to help ground vehicles find routes" is not novel. Nguyen & Akella (2026) address uncertain road-edge inspection with UAVs and UGVs. Choi et al. (2026) address evolving hazard beliefs and replanning within a UAV exploration budget. Han et al. (2023) study multi-agent disaster crowdsensing routes.

The closest-work comparison should explicitly inspect prior systems for *false reassurance, correlation of observations, stale reports, decision-relevant information value, refusal to recommend and treatment of risk*. None is yet established as an untouched research gap.

## 5. Humanitarian safeguard

No real war-zone movement maps, active hazard locations, checkpoints, convoy routes or real-time civilian advice. An algorithm cannot create a humanitarian corridor; the ICRC describes such corridors as arrangements between parties, and warns that even agreed routes may remain dangerous. Use the results to test inference reliability under safe disaster analogues, not to direct real people into hazardous areas.

## 6. Connections and next decision gates

Continues [information foraging](information-foraging-airborne-observatory.md), [false confidence](false-confidence-under-model-mismatch.md), [occlusion-aware search](cooperative-aerial-search-under-occlusion.md), and [delayed communication](delayed-communication-tradeoff.md). It can stand on its own without a finished aircraft or swarm.

1. Closest-work matrix versus the two 2026 road-inspection papers.
2. Choose *one* initial mechanism: shared blind spots, then staleness later.
3. Show a baseline can become confidently wrong under credible assumptions.
4. Reproduce a strong existing policy and perform held-out comparisons.
5. Demonstrate a controlled physical sensing effect only if the first result survives.

## References (abstract/institutional-page level; full methods not reproduced)

- User documentary: https://www.youtube.com/watch?v=CyA9s4MEwnw
- Nguyen & Akella (2026), *Dynamic UGV-UAV Cooperative Path Planning in Uncertain Environments*: https://arxiv.org/abs/2604.25267
- Choi et al. (2026), *Integrated Exploration-Aware UAV Route Optimization and Path Planning*: https://arxiv.org/abs/2605.28654
- Han et al. (2023), *Collaborative Route Planning of UAVs, Workers and Cars for Crowdsensing in Disaster Response*: https://arxiv.org/abs/2308.11088
- ICRC, *How humanitarian corridors work*: https://www.icrc.org/en/document/how-humanitarian-corridors-work
