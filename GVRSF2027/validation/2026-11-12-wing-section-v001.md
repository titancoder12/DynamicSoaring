# Wing-section v001 — executed verification

Date: 2026-11-12 (America/Vancouver). Evidence: cloud-executed geometry checks and calculated quantities; **no slicing or physical test**.

## Source and reproduction

Repository starting commit: `e12f10327d36210981db4b19d82fa0637ab229f4`. Requirements milestone: [`8cb57d0878e012a21e79f05cb96b7e24a3222bf0`](https://github.com/eugenelin89/cwsf2027-research/commit/8cb57d0878e012a21e79f05cb96b7e24a3222bf0). Source revision: **wing-section-v001**, with exact generator/parameter SHA-256 and export hashes recorded in [geometry JSON](wing-section-v001-geometry.json). The checked source and outputs are committed together.

Working path: `/workspace/scratch/5aeb3b0e05c5/cwsf2027-research`. Software versions and commands are in [the guide](../docs/wing-section-v001-build-and-test.md). The GitHub connector preserves the complete remote tree; local files are a scoped snapshot, not a full clone. The older checkout was left untouched.

## Executed results

| Check | Actual result |
| --- | --- |
| CadQuery generation | Both parts built as one valid positive-volume solid each. |
| Panel exact bounds | 120 × 14.553557089 × 40 mm. |
| Pin exact bounds | 3 × 3 × 12 mm, with 0.3 mm end chamfers. |
| Minimum outer-to-inner shell offset | 0.800000 mm, checked with BRep wire distance. |
| Spar / alignment bores | 6.4 / 3.4 mm; nominal gauges have zero solid intersection; near-bore gauges pass through; 0.1 mm larger-diameter gauges intersect the sleeve. |
| Assembly | Two panels at Z=0–40 and 40–80 have no volume overlap; centred pin does not intersect the panels; 6 mm nominal engagement each side. |
| STL mesh topology | Panel 3,684 triangles; pin 1,892. One connected surface each; every undirected edge has two incident faces; paired edge winding consistent; no degenerate triangles; positive signed volume. |
| STL versus solid volume | Panel relative difference 0.003936%; pin 0.028151%; both below the predeclared 0.5% check. |
| STL bounds | Within 0.03 mm of exact solids; pin Y mesh extent is 2.999407 mm. |
| STEP reimport | One valid solid each; volume relative error < 1e-6 and dimension differences < 1e-5 mm. Solid exchange files, not faceted mesh wrappers. |
| Parametric variant | Changed to 140 mm chord, 30 mm span, 5 mm spar, 1 mm shell and 1 mm trailing edge; regenerated and passed solid, STL and STEP checks. |
| Invalid parameters | Oversized spar, negative clearance, inch units, reversed bore order and excessive pin chamfer rejected. See [parameter checks](wing-section-v001-parameter-checks.json). |
| Blender | 4.3.2 executed import at 0.001 m per STL coordinate, saved `.blend`, rendered PNG; each imported part matched expected mm bounds within 0.03 mm. Reopened the saved `.blend` in a fresh process and read back its metric units, part names and dimensions successfully. See [import checks](wing-section-v001-blender.json). |
| Preview review | Inspected the dimensioned cross-section/assembly illustration and actual Blender render; hollow cavities, sleeves, webs, pin and external reference spar are visible. |
| Print orientation | Geometric review: constant cross-section extruded along +Z; no intended internal overhangs; open end at bed. Slicer confirmation pending. |

The STL checks do not implement a general triangle-triangle self-intersection detector; confidence additionally relies on the valid source BRep and the checked mesh volume/topology. Mesh validity alone does not prove reliable toolpaths or physical strength.

## Calculated estimates, not measurements

At an assumed 1.24 g/cm³ full-density PLA: panel volume **9,944.602830 mm³**, mass **12.331308 g**; pin volume **84.031320 mm³**, mass **0.104199 g**. Two panels plus pin total **24.766814 g**, excluding spar, brim, supports, adhesives and waste. Slicer extrusion choices, material density and process variation will change actual mass.

## Failures found and resolved during development

- An initial piecewise trailing-edge thickness clamp caused an inward-offset failure. Replaced it with the documented smooth linear thickness addition before accepting any export.
- The first STEP comparison used a bounding-box query that could use export-generated triangulation. The exact BRep and reimported STEP agreed; the checker was changed to `BRepBndLib.AddOptimal` with triangulation disabled. Strict geometry tolerances remain in force.
- Blender initially failed at denoising because this build lacks OpenImageDenoise. Disabled denoising, then completed rendering; no missing render is represented as successful.
- The initial render was overexposed and too tightly framed; adjusted illumination/framing and inspected the replacement.

## Pending evidence and limits

No Bambu Studio/PrusaSlicer execution, configured slicer 3MF, physical print, hardware fit, actual mass, bending result, aerodynamic analysis or flight validation was performed. The user's Mac applications were not accessed. The 850 mm flying wing and candidate hardware are not finalized. The airfoil is a construction surrogate, and the pin/spar butt joint has no designed retention or load rating.

Read the existing science notes for the separate assistant-run simplified physics demonstration; this CAD task does not independently verify it or Christopher's own rerun. Next useful evidence: actual nozzle/filament/spar measurements, slicer preview, first printed fit coupon, then a recorded matched pair and exploratory stiffness observations.
