# Independent review — wing-section v001

**Review date:** 2026-11-12  
**Repository:** `eugenelin89/cwsf2027-research`  
**Reviewed branch and commit:** `main` at [`b101536cea00ea120e03c640eb2f1cc9cbc1e661`](https://github.com/eugenelin89/cwsf2027-research/commit/b101536cea00ea120e03c640eb2f1cc9cbc1e661)  
**Scope:** The first parameterized wing-section construction coupon and its source, exports, Blender scene, instructions, and validation evidence.  
**Evidence:** Independent software execution, file comparisons, and computed geometry; no slicing or physical testing.

This is a dated assessment of the commit above. Preserve its findings as history. Record later fixes in a separate resolution record with their source revision, executed checks, and verified remote commit. The [Work prompt register](../prompts/README.md) owns current task status; [prompt 002](../prompts/002-wing-section-v001-review-fixes.md) defines the correction work.

## Assessment

The Work session delivered the requested first CAD milestone. The default coupon regenerates successfully, its committed STL and STEP files match the source geometry, and the saved Blender scene opens with the expected scale. The default files are suitable for the next slicer inspection; successful printing and hardware fit remain to be established.

One medium-priority parameter-validation defect and one low-priority Blender portability issue remain open at the reviewed commit. Two smaller documentation/evidence gaps should be closed with them. None of these findings invalidates the committed default STL geometry. The documentation milestone that adds this review does not implement the CAD fixes.

## What exists, and what remains to be designed

| Item | Evidence at the reviewed commit |
| --- | --- |
| Editable model | CadQuery generator, JSON parameters, and generated profile coordinates for `wing-section-v001`. |
| Printable part types | One panel model and one alignment-pin model, each exported as STL and solid STEP. The intended complete coupon uses **two panels and one pin**. |
| Panel size | 120 mm chord × 14.553557 mm maximum thickness × 40 mm span. Two joined panels give an 80 mm span coupon. |
| Construction | 0.8 mm shell; 1.2 mm sleeve walls and webs; 6.4 mm spar bore for an assumed 6 mm external spar; 3.4 mm alignment bore for the 3 mm × 12 mm pin. Clearances are 0.4 mm diametral, or 0.2 mm radial. |
| Visualization | A Blender scene/import script and dimensioned/assembly previews. The displayed spar is a reference object, not a supplied printable spar. |
| Complete wing or aircraft body | Not present. There is no full wing planform, central equipment bay/body, finished hardware mounting layout, or complete aircraft assembly. |
| Physical evidence | No configured slicer project, print, measured hardware fit, measured mass, stiffness result, aerodynamic validation, or flight test. |

The profile uses a symmetric NACA 0012-derived thickness distribution with an added linear trailing-edge thickness adjustment to reach 0.8 mm. It is a construction surrogate, not a selected flight airfoil. The earlier approximately 850 mm flying-wing concept and component shortlist remain provisional. The current pin is manually centered with nominal 6 mm engagement in each panel; retention and a flight-load rating have not been designed. See the [requirements](../docs/wing-section-v001-requirements.md), [build guide](../docs/wing-section-v001-build-and-test.md), and [original geometry record](wing-section-v001-geometry.json).

## Independent checks completed

The review used a scoped snapshot of 49 files, verified against the Git blob hashes in the remote tree. The two Work milestones changed 29 distinct paths, all under `GVRSF2027/`. The entire repository was not cloned, and this scoped snapshot must never replace the complete remote tree.

| Check | Observed result |
| --- | --- |
| Source/export provenance | Both recorded source SHA-256 values and all four STL/STEP SHA-256 values matched the committed files. |
| Default regeneration | The generator completed; the two regenerated STL files were byte-for-byte identical to the committed STLs in the checked environment. This does not assert determinism across software versions. |
| Committed STEP geometry | Each file contained one valid solid. Bidirectional Boolean differences between the regenerated solid and the committed STEP solid had zero computed volume for both parts. |
| Committed STL checks | Panel: 3,684 triangles. Pin: 1,892 triangles. Closed edge topology, connected surface, consistent winding, positive volume, and dimensional checks passed. |
| Existing parameter suite | The 140 mm chord / 30 mm span / 5 mm spar / 1 mm shell / 1 mm trailing-edge variant passed. All five supplied invalid cases were rejected: oversized spar, negative clearance, inch units, reversed bore order, and excessive chamfer. |
| Blender reopening | The committed scene reopened in Blender 4.3.2 with metric units, the expected panel dimensions, the two-panel exploded layout, and the spar marked `not_for_printing`. No external assets were required. |
| Preview and links | The assembly and dimension previews were visually inspected. Ninety local Markdown destinations were checked against the full remote path manifest with no broken file/directory destinations. |

The CAD checks used Python 3.12.14, CadQuery 2.7.0, and OCP 7.8.1.1. Retained numerical outputs, parameter-suite results, and verified hashes are preserved in the [companion evidence JSON](2026-11-12-wing-section-v001-independent-review.json). The Blender reopening was independently observed; a separate raw console transcript was not retained in that JSON. Finding R3 addresses reproducible persistence of this check for future milestones.

The STL checker does not implement a general triangle-triangle self-intersection test. The valid source solids, checked mesh topology, and volume comparisons add evidence, but do not establish reliable slicer toolpaths or physical strength.

## Findings at the reviewed commit

### R1 — Medium: assembly validation accepts an overlapping spar and pin

**Status at review:** Open. **Effect:** Some modified parameter sets can receive a passing validation report even though the intended hardware cannot occupy the assembly simultaneously. The unchanged default parameter set does not have this collision.

In [`generate.py`, lines 76–78](https://github.com/eugenelin89/cwsf2027-research/blob/b101536cea00ea120e03c640eb2f1cc9cbc1e661/GVRSF2027/design/cad/wing-section-v001/generate.py#L76-L78), bore locations are checked for order, but their required separation is not enforced. The [assembly checks, lines 155–173](https://github.com/eugenelin89/cwsf2027-research/blob/b101536cea00ea120e03c640eb2f1cc9cbc1e661/GVRSF2027/design/cad/wing-section-v001/generate.py#L155-L173) check gauges against the panel and the pin against the joined panels. They omit the continuous spar against the assembled pin.

Changing only `alignment_x_fraction` from `0.625` to `0.33` reproduced the defect through full generation, STL checks, and STEP checks:

| Computed quantity | Default `0.625` | Modified `0.33` |
| --- | ---: | ---: |
| Spar X position | 36 mm | 36 mm |
| Pin X position | 75 mm | 39.6 mm |
| Center separation | 39 mm | 3.6 mm |
| Sum of nominal hardware radii | 4.5 mm | 4.5 mm |
| Generator result / reported assembly check | Pass / pass | Pass / pass |
| Spar–pin solid intersection | 0 mm³ | **18.133099368762934 mm³** |

The intersection is a computed CAD quantity, not a physical measurement.

**Required correction:** Reject overlapping bores and insufficient material between them, then validate the complete intended assembly: both panels, continuous nominal external spar, and centered pin. For this two-bore construction, a proposed minimum separation rule is `distance >= spar_bore_radius + pin_bore_radius + required_wall`, with a documented numerical tolerance. Using `sleeve_wall_mm` as the required wall gives 3.2 + 1.7 + 1.2 = **6.1 mm** at the defaults. Sleeves may share material; requiring their outer cylinders to be disjoint would unnecessarily impose 7.3 mm.

Add targeted cases for the reproduced `0.33` collision, the insufficient-wall `0.35` case (1.1 mm remaining versus 1.2 mm required), and an adequately separated `0.36` case. The latter two are proposed regression inputs based on the separation calculation; they were not executed in this independent review. Preserve the accepted default geometry and its parameters unless a separately justified revision is needed.

#### Reproducing R1

Use a disposable checkout of the reviewed commit, with the dependencies in the CAD `requirements.txt` installed. From the repository root, run the following Python code. It writes experimental exports only into a temporary directory.

```python
import importlib.util
import json
import tempfile
from pathlib import Path

source = Path("GVRSF2027/design/cad/wing-section-v001")
spec = importlib.util.spec_from_file_location("coupon", source / "generate.py")
coupon = importlib.util.module_from_spec(spec)
spec.loader.exec_module(coupon)
parameters = json.loads((source / "parameters.json").read_text())
parameters["alignment_x_fraction"] = 0.33

with tempfile.TemporaryDirectory(prefix="wing-review-") as directory:
    scratch = Path(directory)
    parameter_file = scratch / "parameters.json"
    parameter_file.write_text(json.dumps(parameters))
    report = coupon.generate(parameter_file, scratch / "exports")
    panel, pin, *_ = coupon.build(parameters)
    span = parameters["section_span_mm"]
    spar = coupon.cylinder(
        parameters["chord_mm"] * parameters["spar_x_fraction"],
        parameters["spar_nominal_od_mm"] / 2,
        2 * span,
    )
    assembled_pin = pin.translate((
        parameters["chord_mm"] * parameters["alignment_x_fraction"],
        0,
        span - parameters["pin_length_mm"] / 2,
    ))
    print(report["checks"]["assembly_interference_check"])
    print(spar.intersect(assembled_pin).Volume())
```

Expected at the reviewed commit: a reported `pass` followed by approximately `18.133099368762934` mm³. A corrected implementation should reject this parameter set rather than reproduce that passing result.

### R2 — Low: the Blender scene stores an absolute render-output path

**Status at review:** Open. **Effect:** Rendering operations that write to the saved scene output path can target the previous cloud checkout or fail when that location is unavailable. Opening the scene and printing the STL files are unaffected.

The [import script, lines 101–109](https://github.com/eugenelin89/cwsf2027-research/blob/b101536cea00ea120e03c640eb2f1cc9cbc1e661/GVRSF2027/design/blender/import-wing-section-v001.py#L101-L109) assigns the resolved absolute preview path to `scene.render.filepath` before saving. Independent reopening found this stored value:

```text
/workspace/scratch/5aeb3b0e05c5/cwsf2027-research/GVRSF2027/design/previews/wing-section-v001-assembly.png
```

**Required correction:** Save a Blender-relative destination such as `//../previews/wing-section-v001-assembly.png`, regenerate/resave the scene, and verify the resolved destination after opening it from another checkout location. Preserve the correct model scale and object layout. This is specifically an output-path issue; it does not mean every interactive render fails.

### R3 — Low: the fresh-process Blender reopen lacks a saved reproduction check

**Status at review:** Open. The [original verification narrative](2026-11-12-wing-section-v001.md) describes reopening the scene, but the [committed Blender JSON](wing-section-v001-blender.json) and import script record import-time checks rather than a separately reproducible reopen check. The documented regeneration commands do not preserve that additional check.

Independent reopening succeeded, so this is an evidence-preservation gap, not a demonstrated defect in the `.blend` file. Save a runnable fresh-process check and its actual results, including units, object identities/dimensions, reference-spar designation, and the resolved output path. Record the actual Blender version and command used.

### R4 — Low: clarify the staged print quantities

**Status at review:** Open. The [printing README](https://github.com/eugenelin89/cwsf2027-research/blob/b101536cea00ea120e03c640eb2f1cc9cbc1e661/GVRSF2027/design/printing/wing-section-v001/README.md#L17) describes one panel plus pin first, followed by two panels plus pin after review. A reader could interpret the second phrase as an additional complete set.

State the cumulative sequence consistently: **print one panel and one pin; measure and review their fit; then print one additional matching panel. The complete coupon uses two panels and one pin total.** Any replacement or changed-revision specimens should be identified separately.

## Follow-through and limits

Use the [prompt register](../prompts/README.md) to select the current task. The intended progression is to close the software/documentation findings with evidence, then inspect actual slicer output and obtain the nozzle, filament, and spar measurements needed for the physical coupon. Record physical observations using the [measurement template](wing-section-v001-observations-template.md); an empty form is not a result.

The recorded approximately **24.77 g** for two panels plus pin is a calculated full-density PLA estimate using an assumed 1.24 g/cm³. It excludes the spar, brim, supports, adhesive, and waste. Neither that estimate nor software validation establishes printed mass, stiffness, flight suitability, dynamic-soaring performance, or an AI advantage.

[Validation index](README.md) · [Project workspace](../README.md) · [Work prompt register](../prompts/README.md)
