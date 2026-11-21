# 003 — Wing-section v001 slicing and first fit measurements

**Created:** 2026-11-12  
**Origin:** Next-session handoff at reviewed commit `b101536cea00ea120e03c640eb2f1cc9cbc1e661`, sequenced after review corrections.  
**Live status, dependencies and next action:** [Prompt register](README.md)

Read `AGENTS.md`, the register, the current project README, requirements, build/print guide, geometry validation and [independent review](../validation/2026-11-12-wing-section-v001-independent-review.md). [Prompt 001](001-wing-section-v001-cad.md) remains the historical task specification. Use current remote files and preserve unrelated work.

## Prerequisite and available tools

Verify that [002](002-wing-section-v001-review-fixes.md) has been completed, committed, pushed and checked remotely. Record its commit and correction evidence. If a prerequisite remains unresolved, record the precise blocker; useful equipment/source checks may proceed, but do not silently waive a required correction or report this task complete.

This dependency applies to the coupon work. Under the [aircraft design and test plan](../docs/aircraft-design-and-test-plan.md), [004](004-full-aircraft-preliminary-design.md) can develop the preliminary complete-aircraft layout alongside this task. Missing physical access or measurements here do not block that concept milestone; keep the affected manufacturing details provisional and return actual observations to the later design revision.

Inspect this session's actual tools and report the working directory. The earlier CAD session used cloud Linux Blender, not the user's Mac. Its scoped snapshot was not a full clone, and its absolute path must not be assumed available. Determine whether a slicer and the user's local files/apps are accessible. Cloud Blender availability does not establish local Bambu Studio access. Continue the supported work and identify the specific user handoff where real equipment or measurements are required.

## Slicing and first specimen

1. Confirm the real printer, build plate, nozzle and filament. Obtain measured spar OD at several positions/orientations, or explicitly identify a coupon-only gauge. A nominal 6 mm spar, standard non-foaming PLA and 0.4 mm nozzle were assumptions. Record actual values; revise geometry in a new revision if measurements require it. Do not silently alter v001.
2. When a slicer is available, import `panel.stl` and `alignment-pin.stl` as millimetres at 100% scale. Verify approximately **120 × 14.5536 × 40 mm** for the panel and **3 × 3 × 12 mm** for the pin. Keep span/bores vertical along Z, with the open panel end on the plate. Use the existing proposed settings as an inspection starting point.
3. Review first, middle and final layers for continuous thin skins, connected sleeves/webs, open bores, unintended bridges, repair warnings and adhesion/removal access. Save the actual configured slicer project, selected screenshots, settings and version under `GVRSF2027/design/printing/wing-section-v001/`. Label slicer mass/time as estimates. An unconfigured geometry file is not a configured print project.
4. Have the user print **one panel and one pin** first. Record actual part mass, dimensions, spar/pin fit and defects using a copy of the blank observation form. Preserve original observations and specimen IDs. Log brim removal, sanding, reaming or other modifications; do not substitute assumed values for measurements.
5. After acceptable fit, print **one additional matching panel**: **two panels plus one pin total**. Assemble on the measured spar, document joint gap, twist, pin engagement and any temporary retention. The joint has no designed retention or flight-load rating.

Exploratory stiffness observations may follow the documented fixture/load guidance when suitable equipment is available. Record force, support/load positions, deflection, residual motion, instrument resolution and failures. Use measurements to justify v002; full-aircraft CAD still needs a mass budget, aerodynamic/trim work and measured interfaces.

## Evidence and handoff

Keep slicer estimates, physical observations and calculations separate. Preserve the science provenance: the assistant-run simplified 2-D physics demonstration does not establish Christopher's rerun, the project simulator or an AI advantage. CAD/print success does not establish flight suitability.

Commit and push completed checked milestones through the permitted workflow with normal non-force updates; verify the remote branch, full SHA and changed-file hashes. Report evidence paths, actual completed checks, source/export identifiers, measured findings and precise remaining blockers. Update the register to reflect only verified progress. Missing local access or physical observations must remain explicit, with the next user action stated.
