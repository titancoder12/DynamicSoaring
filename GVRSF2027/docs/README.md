# CWSF 2027 — Albatross-Inspired Dynamic Soaring

**Start here for the science fair project.**
**Focus selected:** October 23, 2026
**Current stage:** Research and engineering planning, with an initial wing-section construction coupon generated and geometry-checked. Complete-aircraft design and physical/flight results remain to be established.

The science fair now focuses on **dynamic soaring inspired by albatrosses**, organized around three connected questions:

| Step | Question | Project content |
| --- | --- | --- |
| **1. Inspiration by nature — Albatross** | How does an albatross use its wings and changing winds to sustain efficient flight? | Wind shear, soaring maneuvers, aerodynamic efficiency, maneuver loads, and the distinction from thermal soaring. |
| **2. Engineering** | How can those principles guide a small aircraft, a wing structure, and its control? | Airfoil and wing design, model-guided structural tests, verified energy calculations, AI-powered adaptive flight control, conventional baselines, and fair experiments. |
| **3. Applications** | What useful work could the demonstrated capability support? | Longer or less energy-intensive environmental, coastal, and marine observations, evaluated against a defined mission. |

**Project aim:** Investigate how albatross-inspired flight and engineering design could improve endurance or useful distance for a small fixed-wing aircraft. The engineering direction carries forward the combination discussed in **Flight CWSF Ideas: AI-powered adaptive flight control (Idea 1) + albatross-inspired dynamic soaring (Idea 5)**. The exact airframe, AI method, primary measurement, and application remain to be refined.

**Combined-concept question:** Can adaptive AI flight control improve dynamic-soaring energy performance and robustness over credible conventional controllers when wind conditions are uncertain or changing? The [technical dossier](../../docs/projects/ai-powered-adaptive-dynamic-soaring/README.md) records the detailed proposal; the [conversation coverage map](dynamic-soaring-project-brief.md#flight-cwsf-ideas-coverage-audit) shows where its details are preserved and the limits of the available conversation record.

## Main document

**[Dynamic soaring — consolidated project brief](dynamic-soaring-project-brief.md)** collects the relevant project conversations, existing repository plans, standalone FSL work, research references, decisions, and unresolved questions.

Read it in this order:

1. [Project direction and status](dynamic-soaring-project-brief.md#project-direction-and-status).
2. [Inspiration by nature: albatrosses](dynamic-soaring-project-brief.md#1-inspiration-by-nature-albatrosses).
3. [Engineering](dynamic-soaring-project-brief.md#2-engineering).
4. [Applications](dynamic-soaring-project-brief.md#3-applications).
5. [Work plan and open decisions](dynamic-soaring-project-brief.md#work-plan-and-open-decisions).
6. [Reading map](dynamic-soaring-project-brief.md#reading-map) and [sources and provenance](dynamic-soaring-project-brief.md#sources-and-provenance).

## CAD progress and Work handoffs

The first CAD milestone provides a small construction coupon, with two identical panel instances and one alignment pin. Read the [build guide](wing-section-v001-build-and-test.md), [independent review and findings](../validation/2026-11-12-wing-section-v001-independent-review.md), and [Work prompt register](../prompts/README.md). The register owns task status and ordering; it keeps completed assignments separate from the next task. Geometry checks do not establish a successful print or a complete aircraft.

The [aircraft design and test plan](aircraft-design-and-test-plan.md) explains what can be designed before those tests, which details depend on measurements, and the acceptance criteria for a preliminary complete-aircraft layout. That layout can proceed alongside coupon testing. [Prompt 004](../prompts/004-full-aircraft-preliminary-design.md) preserves the future implementation handoff; no new aircraft model is claimed by the planning document.

## Supporting material

| Resource | Use it for |
| --- | --- |
| [AI-powered adaptive dynamic soaring dossier](../../docs/projects/ai-powered-adaptive-dynamic-soaring/README.md) | Detailed physics, aircraft/control architecture, comparative experiments, roadmap, and annotated papers for the combined concept. |
| [Standalone FSL plan: model-guided wing design](https://docs.google.com/document/d/1LFuOe8CJivYmTWZOr8HUuY-tF338UO4iVYqqSEPBuMM/edit) | The proposed reduced soaring model, predicted spar redesign, and independent structural tests. |
| [Standalone FSL plan: wing mass and bending response](https://docs.google.com/document/d/1dZmtxMwA-xtempr4vKt8oG2OuoJ9H_wThzoe6ApOfPU/edit) | The earlier, narrower fixed-geometry spar comparison. |
| [Original combined idea](../../docs/ideas/adaptive-ai-dynamic-soaring.md) | The history of combining adaptive control with albatross dynamic soaring: Idea 1 + Idea 5. |
| [Reference index](../../docs/ideas/reference-index.md) | The wider bibliography from earlier discussions. |
| [Research decision log](../../docs/07-decision-log.md) | D-020 records the selected focus and this entry point. |
| [Historical CWSF design lessons](../../reports/analysis/cwsf2027-design-implications.md) | Research-question, comparison, validation, and evidence principles. |

The FSL documents remain standalone investigations. Their proposed methods can inform this project without making FSL completion depend on an entire aircraft or AI system.

## How to use this folder going forward

- Begin new science fair planning and review here; update the brief when a decision changes.
- Keep the three-part story connected: **biological principle → engineering question and evidence → application supported by that evidence**.
- Identify each item as a decision, proposal, published finding, simulation result, bench result, or flight result.
- Link actual CAD, code, notebooks, data, and figures as they are produced. Proposed experiments are not completed work.
- Keep older idea documents as dated background. Their earlier “candidate” or “no final topic selected” wording does not override the October 23 topic decision.

**Next planning priorities:** choose one primary engineering question and metric; establish the actual aircraft/component inventory and test access; reproduce one appropriate physics baseline before expanding the design or AI scope.

[Project workspace and design files](../README.md) · [Repository home](../../README.md)
