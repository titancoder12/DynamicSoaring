# 002 — Wing-section v001 review corrections

**Created:** 2026-11-12  
**Reviewed baseline:** `b101536cea00ea120e03c640eb2f1cc9cbc1e661`  
**Live status, dependencies and next action:** [Prompt register](README.md)

Address R1–R4 in the [independent review](../validation/2026-11-12-wing-section-v001-independent-review.md). Read `AGENTS.md`, the current project/design entry points, requirements, build guide and validation records. [Prompt 001](001-wing-section-v001-cad.md) remains the historical task specification. Inspect current remote state and local changes first; preserve unrelated work and report the actual working directory. The reviewed SHA identifies evidence, not a request to reset the branch.

Keep the default v001 dimensions, parameter values and printable geometry unchanged. Correct validation, portability and documentation; retain the distinction between calculated quantities, executed software checks and physical measurements.

The [aircraft design and test plan](../docs/aircraft-design-and-test-plan.md) also permits independent preliminary whole-aircraft work under [004](004-full-aircraft-preliminary-design.md). That work does not require this task or 003's physical testing to finish first, provided it preserves the open findings and does not treat unchecked modified coupon geometry as accepted. Complete this task against its own correction criteria.

## R1 — Reject incompatible bore spacing and check the full assembly

At the reviewed baseline, full generation incorrectly accepts `alignment_x_fraction = 0.33`. The nominal spar and assembled alignment pin intersect by **18.133099368762934 mm³**. Valid individual solids and separate bore checks do not establish assembly compatibility.

Require enough material between bore boundaries:

```text
d = chord_mm * (alignment_x_fraction - spar_x_fraction)
required_wall = sleeve_wall_mm
d >= spar_bore_radius + pin_bore_radius + required_wall
```

With the default diameters and sleeve wall, the minimum centre separation is `3.2 + 1.7 + 1.2 = 6.1 mm`. Use an explicit numerical tolerance consistent with the existing geometry checks. Explain this wall criterion in the requirements and validation documentation. Sleeves may share material: do not reject a valid union merely because their outer cylinders overlap.

Add full-generation regression cases, each using isolated temporary outputs:

- `alignment_x_fraction = 0.33`: reject overlapping bores/insufficient wall.
- `alignment_x_fraction = 0.35`: reject; 6.0 mm separation leaves only 1.1 mm between bores, below the required 1.2 mm.
- `alignment_x_fraction = 0.36`: accept and pass the solid, STL, STEP and assembly checks; overlapping sleeve material is permitted.
- Unchanged defaults: accept and reproduce the reviewed geometry.

Validate the assembled two panels with a continuous nominal spar and the centred alignment pin. Check spar–pin, spar–panels, pin–panels and panel–panel interference using positive intersection volume, allowing intended surface contact. Preserve existing bore-openness and export checks. Record actual results, thresholds and rejected-case messages in machine-readable validation evidence.

## R2 — Make the saved Blender scene portable

The reviewed `.blend` stores an absolute render destination in the old cloud workspace. Save this relative path instead:

```python
scene.render.filepath = "//../previews/wing-section-v001-assembly.png"
```

Use actual available Blender, in cloud or locally. Save the corrected scene, copy the required project tree to a different temporary directory, then reopen the copied `.blend` from a different current working directory. Render from that saved scene without rebuilding it. Verify that the image is created under the relocated `design/previews/`, and that the old checkout is not used as the output destination. Record Blender version, commands and observed output location. Keep temporary copies and renders out of Git.

## R3 — Preserve a reproducible saved-file readback

The independent review already reopened the original `.blend` successfully. The gap is durable, replayable evidence, not a demonstrated corrupt file.

Commit a small verification script and its JSON result. Run it in a fresh Blender process against the saved scene, without importing/rebuilding the parts first. Check metric units and scale, expected part names, dimensions against the geometry report within 0.03 mm, the reference-only spar designation and the relative render path. Record the checked `.blend` hash, relevant source/report hashes, Blender version and actual outcomes. Document the exact invocation. Keep the saved-file check distinct from the existing import-time checks.

## R4 — Clarify print quantities

Make the print guide and slicer notes agree: first print **one panel and one pin**; after fit review, print **one additional matching panel**. The completed coupon uses **two panels and one pin total**. Correct the ambiguous wording without claiming slicing or printing has occurred.

## Acceptance and publication

Regenerate and verify the corrected deliverables. Compare default dimensions, volumes, topology and export geometry with the reviewed baseline; explain metadata-only differences where applicable. Update generator/parameter/export hashes and affected validation records together. Preserve the dated independent review; add finding dispositions and links to the correction evidence rather than rewriting its historical results. Do not represent a failed or unavailable Blender check as completed.

Commit and push this checked milestone through the repository's permitted workflow using normal non-force updates. Verify the remote branch, full commit SHA and changed-file hashes. Keep dependencies, caches, backups and disposable outputs out of Git. Update the register only when its completion conditions are met.

Hand off R1–R4 dispositions, changed paths, commands/results, unchanged-default evidence, remaining blockers and the verified GitHub link. Prompt 003 can then continue with actual equipment checks and slicing. No aerodynamic, physical-strength, simulator or flight claim follows from these corrections.
