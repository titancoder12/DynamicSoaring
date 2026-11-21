# GVRSF2027 project workspace

**Established:** 2026-11-12  
**Project:** Albatross-inspired dynamic soaring with adaptive flight control  
**Stage:** Initial wing-section construction coupon generated and geometry-checked; slicing, physical measurements and aircraft performance remain unverified.

This is the active workspace for the GVRSF/CWSF 2027 aircraft project. The existing science-fair documents were moved here from `docs/GVRSF2027/` into `GVRSF2027/docs/`. The move preserves their research content and updates their links.

## Start here

1. [Research overview](docs/README.md).
2. [Consolidated dynamic-soaring project brief](docs/dynamic-soaring-project-brief.md).
3. [Design-file conventions](design/README.md).
4. [Aircraft design and test plan: what can proceed in parallel](docs/aircraft-design-and-test-plan.md).
5. [Work prompt register and next task](prompts/README.md).
6. [Independent wing-section v001 review](validation/2026-11-12-wing-section-v001-independent-review.md).

## First construction prototype — v001

[Build, print and measure](docs/wing-section-v001-build-and-test.md) · [Requirements](docs/wing-section-v001-requirements.md) · [Executed checks](validation/2026-11-12-wing-section-v001.md) · [Independent review](validation/2026-11-12-wing-section-v001-independent-review.md) · [Work task register](prompts/README.md)

The November 12 CAD milestone provides parameterized source, two printable part types (print two panels and one alignment pin), solid STEP exports, a Blender scene and dimensioned previews. One panel is 120 × 14.5536 × 40 mm, with provisional spar and pin interfaces. This is a manufacturing coupon, not a selected flight airfoil or a flight-ready wing. Slicer and physical-print evidence remain pending.

The completed initial CAD task covers this small wing-section coupon. A complete wing, aircraft body, and full aircraft assembly remain to be designed. The independent review records the checked default geometry and the corrections needed for parameter validation, Blender portability, and documentation. Follow the prompt register for their current disposition and the next task.

## Whole-aircraft design alongside coupon testing

The [aircraft design and test plan](docs/aircraft-design-and-test-plan.md) records the working approach: develop an adjustable layout of the complete aircraft while the small construction coupon is corrected, printed, and measured. Coupon results inform final clearances, construction details, and mass estimates; they do not block preliminary equipment layout, mass/CG calculations, or aerodynamic/structural planning.

[Prompt 004](prompts/004-full-aircraft-preliminary-design.md) is the prepared handoff for that preliminary layout. Its status is in the [register](prompts/README.md). The plan and handoff do not establish an implemented full-aircraft model or test result.

## File locations

All paths below are relative to this folder.

| Folder | Contents |
| --- | --- |
| [docs/](docs/README.md) | Research plans, requirements, design rationale, references, and assembly instructions. |
| [design/cad/](design/cad/) | Editable CAD generators, parameters, airfoil coordinates, and source models. |
| [design/blender/](design/blender/) | Blender projects and Blender-specific import/build scripts. |
| [design/exports/](design/exports/) | Reviewed STL, STEP, and other geometry exports, organized by design revision. |
| [design/printing/](design/printing/) | Slicer projects, print profiles, plate layouts, and material/nozzle settings. |
| [design/previews/](design/previews/) | Dimensioned views, assembly illustrations, screenshots, and selected renders. |
| [validation/](validation/README.md) | Geometry checks, print observations, measured fit/mass/stiffness, and evidence linked to the tested revision. |
| [prompts/](prompts/README.md) | Numbered Work handoffs, dependencies, status, and completion evidence. |

Use the existing [technical dossier](../docs/projects/ai-powered-adaptive-dynamic-soaring/README.md) and [idea library](../docs/ideas/README.md) as supporting references. Those historical source folders remain in their original locations.

## Working files and GitHub

In a local Work task, create files inside the selected local checkout of `eugenelin89/cwsf2027-research`. In a cloud task, use its repository working copy. Report the actual absolute working path after inspecting the environment; this document does not prescribe a path on the user's Mac.

The durable project record is the remote GitHub repository. For the authorized CAD task, commit and push completed, checked milestones using the permitted branch workflow. Verify the remote commit before reporting the milestone as uploaded. Include the branch, commit SHA, changed paths, and GitHub link in the handoff. Report any artifact that remains only in the working environment.

Keep model source and final deliverables together. Preserve unrelated changes. Exclude local environments, caches, Blender backups, and temporary renders. If an artifact exceeds the supported upload/storage limits, use the repository's supported large-file workflow when available and document the exact disposition; do not silently omit it.

The [repository instructions](../AGENTS.md) and [D-021 relocation decision](../docs/07-decision-log.md#d-021--create-the-root-gvrsf2027-workspace-and-repository-backed-cad-workflow) describe the scope of this organization change.

[Repository home](../README.md)

