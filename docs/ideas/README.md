# CWSF 2027 idea library

**Current science fair focus, selected October 23, 2026:** [Albatross-Inspired Dynamic Soaring — start here](../../GVRSF2027/docs/README.md). The new entry folder organizes the relevant history around nature, engineering, and applications.

This directory preserves the distinct CWSF 2027 concepts discussed in the strategy thread. Each idea has its own document so research questions, prior art, experiments and feasibility can evolve independently.

The documents preserve their original **candidate-concept history**. Their earlier selection language does not override the October 23 topic decision; none establishes verified novelty, completed performance, or a medal prediction.

## Umbrella concept

- [Information-foraging airborne observatory](information-foraging-airborne-observatory.md) — broad intellectual direction: airborne agents choose scientifically valuable measurements rather than merely covering space.

## Core research architectures from the historical analysis

- [False confidence under model mismatch](false-confidence-under-model-mismatch.md) — detect when an information-seeking system becomes confidently wrong.
- [Recalibration versus exploration](recalibration-versus-exploration.md) — decide when sensing effort should go to new territory versus sensor/reference checks.
- [Delayed communication tradeoff](delayed-communication-tradeoff.md) — measure when sharing stale information helps or hurts.
- [Adaptive atmospheric profiling with balloons](adaptive-atmospheric-profiling-balloons.md) — choose constrained altitude measurements to infer atmospheric structure.
- [Mapping versus rare-event detection](mapping-versus-rare-event-detection.md) — trade global map quality against fast detection of localized events.
- [Measurement selection for physical-model discrimination](model-discrimination-sampling.md) — determine which observations distinguish competing explanations, not merely reduce prediction error.
- [Heterogeneous sensor assignment](heterogeneous-sensor-assignment.md) — determine when a team should deploy fast/noisy versus slow/accurate sensors.

## Aerospace / search-and-rescue refinements

- [Cooperative aerial search under occlusion](cooperative-aerial-search-under-occlusion.md) — **earlier practical-aerospace candidate**; search new territory versus obtain genuinely independent verification views.
- [Reconfigurable flying camera array](reconfigurable-flying-camera-array.md) — use a swarm as a distributed/synthetic-aperture imaging instrument.
- [Distributed acoustic search](distributed-acoustic-search.md) — coordinate airborne listening under propulsion/self-noise.
- [Fixed-wing autonomous search](fixed-wing-autonomous-search.md) — energy- and detection-aware search using autonomous aeroplanes / powered gliders.
- [Cooperative thermal soaring for search](cooperative-thermal-soaring-search.md) — exploit rising air while balancing energy and mission urgency.
- **[Learning to Soar Together](learning-to-soar-together.md)** — performance-aware cooperative search combining the individual-soaring research of Flato et al. with the SKYSURF mission framework. Tests whether accounting for measured soaring capability improves the team beyond the straightforward combination; includes an A–E experiment and a staged physical validation plan.

## Flight-physics, adaptive UAV and environmental monitoring ideas — 2026-10-18

- **[AI-Powered Adaptive Dynamic Soaring — supporting engineering dossier](../projects/ai-powered-adaptive-dynamic-soaring/README.md)** — combines **Idea 1 + Idea 5**, with proposed FW-01 characterization, published-model reproduction, wind-shear simulation, and adaptive/classical control comparisons. The broader albatross-inspired dynamic-soaring topic is now selected; use the [science fair entry folder](../../GVRSF2027/docs/README.md) for current scope and open implementation decisions. No completed performance is implied.
- [AI-powered adaptive fixed-wing flight control — Idea 1](adaptive-fixed-wing-flight-control.md).
- [Energy-aware environmental UAV sensing — Idea 2](energy-aware-environmental-uav-sensing.md).
- [Bio-inspired cooperative fixed-wing flight — Idea 3](bio-inspired-cooperative-fixed-wing-flight.md).
- [Morphing wings — Idea 4](morphing-wings-flight-efficiency.md).
- [Albatross-inspired dynamic soaring — Idea 5](bio-inspired-dynamic-soaring.md).
- [Autonomous marine wildlife monitoring — Idea 6](autonomous-marine-wildlife-uav-monitoring.md).
- [Original compact Idea 1 + 5 concept note](adaptive-ai-dynamic-soaring.md).
- [Separate Idea 1 + 3 (adaptive flight + swarms)](wind-adaptive-decentralized-fixed-wing-swarms.md) — earlier alternative, **not** the intended current combination.

- **[Other bio-inspired flight engineering options](bio-inspired-flight-research-options-2026-10-18.md)** — eagles/vultures, swift morphing wings, owl silent flight, hawk slots, dragonfly corrugations, whale tubercles, bee optic flow, frigatebirds and flying seeds; linked research papers and CWSF experiment possibilities.
- [Thermal vs. dynamic soaring](../projects/ai-powered-adaptive-dynamic-soaring/08-thermal-vs-dynamic-soaring.md) — how rising-air and wind-shear energy harvesting differ, with practical build implications.
- [Sailboat tacking vs. albatross upwind dynamic soaring](../projects/ai-powered-adaptive-dynamic-soaring/09-sailing-upwind-and-dynamic-soaring.md) — the shared relative-motion concept and different force/energy mechanisms.

## Humanitarian protection ideas — 2026-10-18

Inspired by a [user-shared documentary](https://www.youtube.com/watch?v=CyA9s4MEwnw), these unselected concepts investigate **civilian protection rather than attacking targets**. They are retained as historical alternatives; they do not establish the selected dynamic-soaring application, propose live conflict routing, or claim verified novelty.

- **[Search for Safety — integrated humanitarian aerial intelligence](search-for-safety-humanitarian-aerial-intelligence.md)** — an umbrella proposal to avoid confidently incorrect route assessments, prioritize useful inspections and abstain when evidence is insufficient.
- **[Fixed-wing small-drone observation](humanitarian-fixed-wing-drone-detection.md)** — test passive visual reliability, moving-viewpoint errors and calibration using benign data.
- **[Uncertainty-aware civilian route assessment](uncertainty-aware-civilian-route-assessment.md)** — test inspection decisions with uncertain road conditions and correlated or stale evidence.
- **[Passive drone early warning](passive-drone-early-warning.md)** — test camera/acoustic fusion and warning reliability; no drone disabling, jamming or interception.

Each concept has a research question, testable hypotheses, experimental comparisons, validity/ethics limitations, prior-art risks, and decision gates. See [consolidated references](reference-index.md).

## Optional deployment extensions

- **[Rocket-assisted launch for autonomous gliders](rocket-assisted-glider-launch.md)** — rocket-provided initial climb followed by gliding, optional soaring, and a search mission. Records the two configuration families, transition challenge, fair energy/mission comparisons, and annotated rocketry/aviation references. Preserve as a later extension of Learning to Soar Together, not a prerequisite for its core research or a selected launch system.

## Historical recommendation and later refinements

See [September 18 recommendation and selection reasoning](recommendation-2026-09-18.md). The selected October 23 subject is recorded in the [science fair entry folder](../../GVRSF2027/docs/README.md).

**Later concept refinement, documented 2026-09-21:** [Learning to Soar Together](learning-to-soar-together.md) records the user's interest in combining the two soaring papers and the proposed scientific contribution between local control and team planning. It is a candidate for serious investigation, not a final selection or an automatic replacement of the recommendation dated 2026-09-18. Its annotated references include both the SKYSURF arXiv manuscript and the subsequently identified journal record.

For a consolidated bibliography across all concepts, see [Reference index](reference-index.md).

The recommendation is a strategy judgment informed by the historical CWSF analysis and current prior-art checks. It is not an empirical medal-probability model.

## Common evaluation standard

Every serious candidate should eventually support:

```text
important real problem
        ↓
precise scientific / technical question
        ↓
falsifiable hypothesis or testable objective
        ↓
original contribution relative to closest prior art
        ↓
controlled comparison against credible alternatives
        ↓
quantitative evidence
        ↓
independent / held-out validation
        ↓
new scientific or technical knowledge
        ↓
practical system that uses the finding
```

Two persistent questions:

1. **What do we learn beyond “the system works”?**
2. **What do we still learn if the hypothesis is wrong or the proposed method loses?**

## Internal analysis sources

- [Senior historical analysis overview](../../reports/analysis/README.md)
- [Gold vs. Silver/Bronze](../../reports/analysis/gold-vs-silver-bronze.md)
- [Platinum / Best vs. other Gold](../../reports/analysis/platinum-vs-gold.md)
- [Project archetypes](../../reports/analysis/project-archetypes.md)
- [Engineering and robotics patterns](../../reports/analysis/engineering-robotics-patterns.md)
- [CWSF 2027 design implications](../../reports/analysis/cwsf2027-design-implications.md)
- [Original seven research architectures](../../reports/analysis/cwsf2027-candidate-architectures.md)
- [Prior-art checkpoint](../../reports/analysis/prior-art-checkpoint.md)
