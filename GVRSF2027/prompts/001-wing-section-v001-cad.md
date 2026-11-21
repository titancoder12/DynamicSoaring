# Prompt 001 — First wing-section CAD prototype

**Created:** 2026-11-12  
**Canonical ID:** 001  
**Original path:** `GVRSF2027/prompts/work-drone-cad.md`  
**Completion evidence:** [CAD milestone b101536](https://github.com/eugenelin89/cwsf2027-research/commit/b101536cea00ea120e03c640eb2f1cc9cbc1e661)

This is the completed initial construction-coupon assignment. Its original instructions are preserved below as historical context. Completion refers to the first CAD milestone; it does not establish a full aircraft, a successful print, or flight performance. The subsequent [independent review](../validation/2026-11-12-wing-section-v001-independent-review.md) records open corrections.

Read the [prompt register](README.md) for current task status and the next authorized handoff. Do not restart this completed assignment merely because an older message links to its original path.

---

# Work handoff — drone CAD and 3D printing

**Updated:** 2026-11-12  
**Repository:** https://github.com/eugenelin89/cwsf2027-research  
**Project workspace:** `GVRSF2027/`

Help me develop a real, 3D-printable fixed-wing drone for my GVRSF/CWSF 2027 science project. Continue through practical design work, create usable files, and save completed milestones to the GitHub repository.

## Project goal

The research question is: **Can adaptive AI flight control capture wind energy more effectively and reliably than a conventional controller when wind conditions change?**

The project is inspired by albatross dynamic soaring. The eventual controller comparison must use the same airframe, starting conditions, sensing assumptions, and evaluation winds, with held-out evaluation conditions. Energy accounting must distinguish wind-energy extraction from motor input and changes caused by losing altitude. The immediate task is to establish the aircraft requirements and create an initial CAD construction prototype.

## Repository and storage instructions

Use `https://github.com/eugenelin89/cwsf2027-research`. Read `AGENTS.md`, its required references, and `GVRSF2027/README.md` before substantive edits. Inspect the current remote branch and any existing local changes. Use an existing suitable checkout or obtain a working copy, preserving unrelated work. Report the actual absolute working directory.

The documentation relocation has already been completed: current science-fair documents are in `GVRSF2027/docs/`. Use that layout; do not recreate the old folder. Store new files as follows:

| Repository path | Contents |
| --- | --- |
| `GVRSF2027/docs/` | Requirements, design rationale, research notes, and assembly/printing instructions. |
| `GVRSF2027/design/cad/` | Editable CAD source, generator scripts, parameters, and airfoil data. |
| `GVRSF2027/design/blender/` | Blender projects and Blender-specific scripts. |
| `GVRSF2027/design/exports/` | Reviewed STL/STEP and other geometry exports, organized by revision. |
| `GVRSF2027/design/printing/` | Slicer projects, print profiles, and plate layouts. |
| `GVRSF2027/design/previews/` | Dimensioned views, assembly illustrations, and selected renders. |
| `GVRSF2027/validation/` | Actual geometry checks, print observations, measurements, and test reports. |
| `GVRSF2027/prompts/` | Updated handoffs for subsequent Work sessions. |

Read `GVRSF2027/design/README.md` for naming and reproducibility conventions. Source files and final deliverables should be part of the repository record, not left only as chat attachments or temporary workspace files.

**Commit and push completed, checked milestones.** This task authorizes saving its design work to this repository. Follow repository rules and branch protections. If changes must go through a pull request, push the working branch and open a pull request; report that its contents are not yet on the default branch. Preserve unrelated changes and use normal non-force pushes.

After pushing, verify the commit exists remotely and report its branch, full commit SHA, GitHub link, and changed paths. If a push or artifact upload fails, say exactly what remains local and why. For files exceeding supported limits, use the repository's supported large-file workflow where available; otherwise preserve the artifact and regeneration source, and report the blocker without claiming the file is uploaded. Exclude dependencies, caches, automatic backups, and disposable intermediate renders.

## Context and evidence status

- Blender is installed on my computer. Its version and your ability to access it have not been checked.
- A previous session found CAD tools in its own environment. Check your actual tools and distinguish your cloud workspace from my computer.
- No completed drone CAD model was produced in the preceding conversation.
- A validated simulator, completed experiments, demonstrated AI advantage, and flight-tested aircraft have not been established by that conversation. Inspect repository evidence and report any verified later progress.
- The science plan prioritizes experiment design and simulator physics checks before outdoor aircraft experiments. Small CAD and construction prototypes can develop the manufacturing approach in parallel.

Earlier provisional design ideas were an approximately **850 mm flying wing**, pusher motor, belly landing, printed sections with carbon-fibre spar reinforcement, and a Bambu P1S printer. Possible materials were LW-PLA, PLA, and PETG.

Previously discussed candidate components include an A2217 1250 KV motor, 8060 propeller, 40 A ESC, 3S 1100–1300 mAh battery, MG90 servos, Matek F405-Wing V2, and RadioMaster Pocket ELRS equipment. These are a shortlist, not confirmation of purchases, exact dimensions, suitability, or a finalized design. Verify relevant details before creating final mounting interfaces. Evaluate the 850 mm flying wing as a candidate rather than assuming it is adequate for dynamic soaring.

## Existing sources

- Start with `GVRSF2027/docs/README.md` and `GVRSF2027/docs/dynamic-soaring-project-brief.md`.
- The supporting engineering dossier remains at `docs/projects/ai-powered-adaptive-dynamic-soaring/`.
- Teacher/project folder: https://drive.google.com/drive/folders/1r_lu_vsgYFwE9P2iYyl2XbXs4FyoQBtl

Use accessible relevant sources before asking for information already recorded. Identify sources actually read. If a source is unavailable, state the gap and continue useful work from this handoff. Preserve dated decisions and distinguish published findings, proposals, simulations, and measurements.

## First tasks

1. **Check the tools.** Identify which CAD programs you can actually execute and whether local Blender or Bambu Studio is accessible. Use existing tools where practical and choose a minimal modeling workflow.
2. **Create a requirements table.** Separate confirmed details, provisional assumptions, and essential missing measurements. Cover geometry, target mass, printing material/nozzle, spar dimensions, hardware dimensions, and assembly method. Ask only questions that materially block the next useful step.
3. **Establish the editable model definition.** Keep important dimensions and airfoil coordinates explicit and adjustable. Choose scripted CAD, Blender Python, or another appropriate method, and preserve the source needed to regenerate the geometry.
4. **Build a small construction-test wing section.** Include a representative shell, spar channel, and joint or alignment feature for fit, mass, and stiffness testing. Use confirmed measurements where available. Label representative airfoils and assumed dimensions explicitly. This is a construction prototype.

## First-prototype deliverables and checks

- Editable source, recorded software versions, and regeneration instructions.
- STL files for the printable parts.
- A Blender project or compatible Blender script/import workflow, matched to the available version.
- STEP files if the chosen CAD workflow supports meaningful solid-geometry export.
- A preview showing the parts, key dimensions, and assembly relationships.
- Printing and measurement instructions stating units, orientation, material assumptions, and what I should measure after printing.
- A verification record describing exactly what ran and what remains pending.

Run the generation process where possible and inspect the actual output. Check geometry, dimensions, clearances, intended print orientation, and export scale. Verify scale and slicing in the slicer when available. Distinguish a geometry-only 3MF from a configured slicer project.

Distinguish calculated estimates, slicer estimates, and physical measurements. Printable geometry does not establish aerodynamic performance, structural adequacy for flight, endurance, or dynamic-soaring capability.

Progress autonomously on reversible work using explicitly labeled assumptions, obtain missing physical measurements when necessary, and commit/push each completed coherent milestone. End with the actual working path, delivered files, completed checks, open questions, and verified GitHub commit or pull-request link.

**Begin with the repository/tool checks and requirements review, then carry the first prototype as far as the available information supports.**
