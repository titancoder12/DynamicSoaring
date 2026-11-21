# AI-Powered Adaptive Dynamic Soaring
## Albatross-Inspired Wind Energy Harvesting for a Small Fixed-Wing UAV

**CWSF 2027 | Supporting engineering / physics / AI research dossier**

**Documented:** 2026-10-18  
**Stage:** Concept and engineering plan; no completed build, test, or validated performance is established by this dossier.

**Origin:** Combination of **Idea 1: AI-powered adaptive flight control** and **Idea 5: albatross-inspired dynamic soaring**. NOT the earlier Idea 1 + 3 decentralized-swarm combination.

**Update — October 23, 2026:** Albatross-inspired dynamic soaring is now the selected science fair focus, organized as **nature, engineering, and applications**. Begin at the [science fair entry point](../../../GVRSF2027/docs/README.md) and [consolidated project brief](../../../GVRSF2027/docs/dynamic-soaring-project-brief.md). This dossier preserves the detailed October 18 proposals; earlier “candidate” wording in its chapters is historical. The exact AI method, airframe, main experiment, and application remain open.

> **Central goal:** Design, construct, and evaluate an autonomous fixed-wing aircraft that can exploit changes in wind speed with altitude to reduce propulsion energy, with an adaptive or learned controller inspired by albatross dynamic soaring.

> **Core research question:** Can adaptive AI-based flight control improve dynamic-soaring energy performance and flight robustness compared with conventional control, particularly when wind gradients are uncertain or changing?

### Project philosophy — an engineering-first Grade 11 project

We deliberately **do not require being the first researchers in the world to combine AI with dynamic soaring**. Professional literature is a foundation to learn from, reproduce responsibly, compare against, and cite. The student's engineering process and individual contribution are crucial: **Build → Understand → Reproduce → Experiment → Improve**.

- Build a real, stable fixed-wing platform and document the engineering.
- Understand aerodynamic and energy-exchange physics, including how and when soaring is possible.
- Reproduce a published dynamic-soaring baseline in a simulator with transparent assumptions.
- Build an adaptive/AI controller and run controlled, repeatable comparisons.
- Improve a measurable aspect of flight control or map where the method works/fails.
- Demonstrate realistic hardware validation to the extent feasible and safe by CWSF 2027.

**A strong project is not merely an AI autopilot, a pretty aircraft, or a simulation animation.** It is a functioning engineering effort supported by physics, measured performance, repeatable tests, honest comparison, and a clearly documented student contribution.

### Why this combination is coherent

An albatross exploits wind shear through a sequence of turns, climbs, and descents. For a UAV, that creates two coupled problems:

1. **Energy opportunity:** Where and when does atmospheric wind shear provide usable energy? Estimate wind and recognize uncertainty.
2. **Flight control:** What bank, heading, airspeed, pitch and altitude changes extract energy without stalling, exceeding bank/load limits, or wasting power?

An adaptive controller connects environment estimation to the real-time maneuver. The research question is **when adaptation improves performance**, not simply whether a neural network can produce commands.

### Engineering system at a glance

Environmental wind model / onboard wind estimate
→ decision whether to glide, attempt a dynamic-soaring cycle, or use propulsion
→ AI/planning controller proposes a safe trajectory or high-level references
→ conventional low-level autopilot stabilizes the airframe
→ flight dynamics, sensors and energy measurement
→ logs and quantitative evaluation.

### Two parallel development tracks

- **Physical aircraft (FW-01 candidate):** design, build/upgrade, tune, measure mass and aerodynamic performance, verify safe manual/assisted operation, collect sensor and power logs.
- **Physics + adaptive-control simulation:** validated dynamic-soaring physics, classical baseline, wind estimation, learned controller, hardware-in-loop integration and reproducible trials.

Do not wait for AI to work before building the aircraft; do not promise the aircraft can physically sustain dynamic soaring before modeling its limits.

### What success looks like

**Minimum credible result:** a functioning fixed-wing prototype with characterized gliding behavior, a validated model, and scientifically defensible simulation comparisons, even if no outdoor dynamic-soaring maneuver is attempted.

**Target result:** an adaptive controller improves one or more predeclared metrics over strong conventional baselines on held-out wind conditions, with safety limitations and uncertainty reported.

**Stretch goal:** hardware-in-loop and controlled physical validation of selected flight-control/energy-model claims; fully autonomous dynamic soaring in the field is **optional and high risk**.

**Negative results are valid:** discovering insufficient lift-to-drag ratio, unattainable wind shear, controller failure thresholds, or no advantage over classical control can still produce solid science if the method is rigorous.

### Dossier reading order

1. [Project proposal and hypotheses](01-project-proposal.md) — why, goals, hypotheses, scope and contribution.
2. [Dynamic-soaring physics and simulation](02-physics-and-modeling.md) — wind-gradient mechanism, equations, realism and physics-validation checks.
3. [Aircraft and AI control architecture](03-aircraft-and-control-architecture.md) — physical platform, sensors, autopilot, learning and integration.
4. [Testing and evaluation plan](04-experiments-and-evaluation.md) — baselines, variables, metrics, trials, and fair comparisons.
5. [Engineering milestones and notebook](05-roadmap-and-notebook.md) — parallel execution, dates, risk gates and recordkeeping.
6. [Papers and technical references](06-annotated-references.md) — annotated, linked source list and reading priorities.
7. [CWSF positioning and decisions](07-cwsf-story-risks-and-decisions.md) — individual contribution, judging story, decisions, caveats and fallbacks.
8. [Thermal vs. dynamic soaring](08-thermal-vs-dynamic-soaring.md) — eagle/vulture thermal lift, albatross wind shear, physics and alternative experiments.
9. [Why sailboats can tack upwind and what dynamic soaring shares](09-sailing-upwind-and-dynamic-soaring.md) — lift/keel mechanism, wind-layer analogy and upwind albatross papers.
10. [Other bio-inspired flight options](../../ideas/bio-inspired-flight-research-options-2026-10-18.md) — swifts, owls, hawks, dragonflies, whale tubercles, bees, frigatebirds and flying seeds, with primary references.

### Relevant earlier repository ideas

- [Original combined idea (Idea 1 + 5)](../../ideas/adaptive-ai-dynamic-soaring.md).
- [AI-powered adaptive fixed-wing flight control](../../ideas/adaptive-fixed-wing-flight-control.md).
- [Albatross-inspired dynamic soaring](../../ideas/bio-inspired-dynamic-soaring.md).
- [Separate Idea 1 + 3 swarm-control concept](../../ideas/wind-adaptive-decentralized-fixed-wing-swarms.md) — **different project, preserved as a historical alternative**.
- [Cooperative thermal-soaring/search project](../../ideas/learning-to-soar-together.md) — separate from wind-gradient dynamic soaring.

### Evidence boundaries

This is a proposed project, not a measured result or claim of unprecedented scientific novelty. Linked professional literature supports feasibility or prior art only within each paper's methods and assumptions. Papers' reported percentage improvements are **not predicted benefits** for our FW-01 platform. Do not confuse rising-air thermals with shear-driven dynamic soaring.
