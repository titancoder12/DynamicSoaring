# DynamicSoaring

DynamicSoaring is the repository for a GVRSF/CWSF 2027 science fair project on albatross-inspired dynamic soaring and adaptive flight control. Albatrosses can gain flight energy by crossing layers of air moving at different speeds. The project asks whether a small glider can use that same wind shear to extend its flight and whether adaptive control improves energy performance and robustness compared with conventional control in uncertain or changing winds.

Start with the [GVRSF 2027 workspace](GVRSF2027/README.md) and the [project brief](GVRSF2027/docs/dynamic-soaring-project-brief.md) for the research background, aircraft concept, and evaluation plan.

## Project status

- **Simulation.** The JSBSim starter suite includes a recorded seven-case experiment that checks energy accounting in still air, uniform wind, and wind shear. It uses a standard sailplane and a simple glide controller. Dynamic-soaring and adaptive controllers are planned, so the controller comparison is still ahead. [Simulation setup and workflow](GVRSF2027/experiments/README.md) · [EXP-001 sanity checks](GVRSF2027/experiments/EXP-001-sanity-checks/README.md)
- **Wing construction.** The first CAD milestone produced a geometry-checked, 3D-printable wing-section coupon for testing panel alignment and fit. The review findings, slicing, and physical measurements remain open. [Build and test guide](GVRSF2027/docs/wing-section-v001-build-and-test.md) · [Independent review](GVRSF2027/validation/2026-11-12-wing-section-v001-independent-review.md)
- **Aircraft design.** Preliminary whole-aircraft design is planned and can proceed alongside coupon testing. Whole-aircraft performance remains unverified. [Aircraft design and test plan](GVRSF2027/docs/aircraft-design-and-test-plan.md) · [Task register](GVRSF2027/prompts/README.md)

## Supporting research

- [Technical dossier on adaptive dynamic soaring](docs/projects/ai-powered-adaptive-dynamic-soaring/README.md)
- [Science fair idea library](docs/ideas/README.md)
