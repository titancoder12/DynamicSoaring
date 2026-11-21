# Information-foraging airborne observatory

**Status:** Umbrella concept / intellectual direction, not a final research question.  
**Planning target:** CWSF 2027 Senior.

## Core idea

A distributed airborne sensing system does not merely move through space or cover area. It decides **where the next measurement would be most scientifically valuable**.

The conceptual continuation from the earlier swarm-robotics work is:

> A biological swarm can search for food; an engineered swarm can search for information.

Possible platforms include drones, fixed-wing aircraft, balloons, or heterogeneous aerial vehicles. Possible scientific targets include atmospheric fields, environmental anomalies, rare events, search targets, or physical parameters.

## Why this is interesting

The concept connects:

- swarm robotics;
- active sensing;
- aerospace;
- distributed scientific instruments;
- uncertainty-aware decision making;
- adaptive measurement.

It can produce a visually compelling system while still supporting a rigorous scientific question.

## Important prior-art constraint

The broad framing is **not novel by itself**. Information-theoretic sensor placement and multi-robot informative sensing are established research areas. A 2027 contribution must therefore focus on a narrower failure mode, tradeoff, measurement problem, or physical inference task.

Examples developed elsewhere in this idea library include:

- false confidence under model mismatch;
- recalibration versus exploration;
- communication delay;
- adaptive atmospheric profiling;
- rare-event detection versus mapping;
- model-discriminating measurements;
- heterogeneous sensor assignment.

## Scientific-question template

A useful final project should look like:

```text
important physical / sensing problem
        ↓
specific uncertainty or failure mode
        ↓
testable hypothesis
        ↓
resource-matched alternatives
        ↓
independent truth / reference measurements
        ↓
measured operating boundary or new inference
        ↓
practical airborne implementation
```

The airborne swarm is the experimental platform, not the entire intellectual contribution.

## CWSF-analysis connection

The historical analysis recommends **measurement + inference + controlled engineering evaluation** as a particularly useful design combination. It also warns that sophisticated hardware, AI, controls and field testing occur across medal levels, so they cannot substitute for a clear contribution and evidence chain.

Relevant internal reports:

- [Project archetypes](../../reports/analysis/project-archetypes.md)
- [Engineering and robotics patterns](../../reports/analysis/engineering-robotics-patterns.md)
- [CWSF 2027 design implications](../../reports/analysis/cwsf2027-design-implications.md)
- [Seven candidate architectures](../../reports/analysis/cwsf2027-candidate-architectures.md)

## Practical solution layer

A practical system should eventually demonstrate that adaptive measurement improves a real task, such as:

- detecting a hidden search target;
- estimating an environmental field;
- detecting a rare anomaly;
- identifying a physical model;
- monitoring a changing atmosphere.

The project should not optimize only an internal information score. The final outcome must be checked against an independently measured quantity or task result.

## References

1. **Krause, Singh & Guestrin (2008).** Near-optimal sensor placements in Gaussian processes: mutual information and robust placement. JMLR.  
   https://www.jmlr.org/papers/v9/krause08a.html

2. **Singh, Krause, Guestrin & Kaiser (2009).** Efficient informative sensing using multiple robots. JAIR.  
   https://arxiv.org/abs/1401.3462

3. **Hollinger & Sukhatme (2014).** Sampling-based robotic information gathering algorithms. IJRR.  
   https://journals.sagepub.com/doi/10.1177/0278364914533443

4. **Cao, Low & Dolan (2013 preprint).** Multi-robot informative path planning for active sensing.  
   https://arxiv.org/abs/1302.0723

5. **Wehbe & Williams (2022).** Informative planning with unreliable shared information / communication uncertainty.  
   https://arxiv.org/abs/2206.11789

6. **Jakkala & Akella (2026).** Differentiable multi-robot sensor placement/path planning with varied sensor types. IJRR.  
   https://journals.sagepub.com/doi/10.1177/02783649251384993

7. **Cao et al. (2026 preprint).** Decentralized informative planning with stale beliefs and uncertain correlations.  
   https://arxiv.org/abs/2609.05515

8. **Rossano, Lim & How (2026 preprint).** Adaptive communication/rendezvous tradeoffs during exploration.  
   https://arxiv.org/abs/2609.12502
