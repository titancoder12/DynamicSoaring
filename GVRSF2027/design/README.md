# Aircraft design files

Keep all new aircraft design files under `GVRSF2027/design/` and use the following destinations.

| Folder | Purpose |
| --- | --- |
| [cad/](cad/) | Authoritative editable model definition, generator source, dimensions, parameters, and airfoil inputs. |
| [blender/](blender/) | `.blend` assemblies and Blender-specific scripts, with Blender version recorded. |
| [exports/](exports/) | Printable meshes and CAD exchange geometry: STL, STEP, or other supported outputs. |
| [printing/](printing/) | Bambu Studio or other slicer projects and their actual printer/material/nozzle settings. |
| [previews/](previews/) | Selected dimensioned views, assembly illustrations, and useful inspection images. |

## Naming and reproducibility

- Use a clear part or assembly name and design revision, for example `wing-section-v001`.
- Keep dimensions, airfoil coordinates, spar interfaces, and clearances explicit in the source. Label provisional values; do not turn a candidate component into a confirmed purchase.
- State the coordinate convention and model/export units. Confirm size again after importing into a slicer.
- Record the generating command, software versions, dependencies, and the source revision associated with each export.
- Save instructions and design reasoning in `GVRSF2027/docs/`; save actual check results and measurements in `GVRSF2027/validation/`.
- A geometry-only 3MF belongs with exports. A 3MF containing a configured slicer project belongs with printing settings. Do not label one as the other.
- Export STEP through a CAD workflow that actually supports solid geometry. Keep the native source or script needed to reproduce the parameterized design; an exchange file does not replace that source.

## Construction coupon and preliminary aircraft layout

The initial construction task uses a short wing section with a representative shell, spar channel, and panel joint or alignment feature. Determine dimensions from the requirements review; label any illustrative airfoil or dimension as provisional.

This first artifact supports fit, mass, and stiffness testing. Geometry checks and successful slicing do not establish aerodynamic performance, structural adequacy for flight, or dynamic-soaring capability. Record estimates, slicer outputs, and measurements separately.

Use the [aircraft design and test plan](../docs/aircraft-design-and-test-plan.md) for parallel development of a complete preliminary layout. Equipment placement, candidate geometry, and mass/CG analysis can proceed before coupon measurements. Keep provisional component envelopes distinct from printed parts, and concept exchange files distinct from manufacturing exports. The plan identifies which final details need measured fit, mass, aerodynamic, or structural evidence. The [004 handoff](../prompts/004-full-aircraft-preliminary-design.md) defines the preliminary-layout deliverables.

## Delivery

Commit source files and reviewed deliverables for a coherent revision, push through the permitted repository workflow, and verify the remote commit. Use the supported large-file mechanism when required. Exclude environments, caches, backup files, and disposable render outputs.

## Review and task history

Before extending `wing-section-v001`, read its [independent review](../validation/2026-11-12-wing-section-v001-independent-review.md) and the [Work prompt register](../prompts/README.md). The review fixes and the slicer/fit handoff have separate numbered prompts. The register identifies current status and dependencies; a completed coupon task does not establish a complete wing or aircraft.

[Project workspace](../README.md) · [Work prompt register](../prompts/README.md)
