# Wing-section v001 — requirements and evidence

Reviewed 2026-11-12 (America/Vancouver). Baseline: `e12f10327d36210981db4b19d82fa0637ab229f4` on `main`.

This revision is a small construction coupon for fit, mass and exploratory stiffness observations. It does not select the final airframe or establish flight suitability.

## Requirements and assumptions

| Item | Evidence status | v001 choice / unresolved measurement |
| --- | --- | --- |
| Research purpose | Confirmed in saved handoff | Fair adaptive versus conventional dynamic-soaring comparison; manufacturing work proceeds in parallel. |
| Geometry | 850 mm flying wing is a candidate | Two identical straight 40 mm sections, each 120 mm chord; assembled span 80 mm. No sweep, taper, twist or elevons. |
| Airfoil | No final profile selected | Symmetric NACA 0012-derived construction profile with explicitly thickened 0.8 mm trailing edge. Not a selected flying-wing airfoil; pitching moment, reflex and trim remain open. |
| Aircraft mass | Unknown | No all-up mass target asserted. Need weighed component inventory and wing-area/flight-envelope study. Coupon mass is calculated separately. |
| Shell | Assumed | 0.8 mm inward normal offset, with solid nose/tail where the cavity closes. Two 1.2 mm chordwise-width webs attach bore sleeves to both skins. |
| Main spar | No measured purchased spar | Nominal 6.0 mm round spar; 6.4 mm bore; 0.4 mm diametral clearance (0.2 mm radial). Sleeve wall 1.2 mm; centre at 30% chord. Measure actual OD in several places before revision. |
| Alignment | Assumed | Separate nominal 3.0 mm pin, 12 mm long, with lead-in chamfers; 3.4 mm through-bore at 62.5% chord. 0.4 mm diametral clearance; 6 mm nominal engagement per side when centred manually. |
| Assembly | Proposed bench method | Butt ends on a continuous external spar plus alignment pin. No designed retention, adhesive joint qualification or bending-load rating. Fit first without adhesive. |
| Printer | Bambu P1S in handoff, current setup unverified | No slicer accessible in this environment. Confirm actual printer, usable bed and installed nozzle. |
| Filament/nozzle | Historical PLA/printer access; current spool/nozzle unverified | Standard non-foaming PLA and 0.4 mm nozzle assumed; 0.20 mm layer height starting point. LW-PLA/PETG need separate calibration. |
| Propulsion/control hardware | Candidate list only | A2217 1250 KV, 8060 prop, 40 A ESC, 3S 1100–1300 mAh, MG90, Matek F405-Wing V2, Pocket ELRS. No final mounts are made. Need exact models, envelopes, hole spacing, wire routes and masses. |
| Acceptance now | Geometry-only gate | Valid single solids; mesh manifold/orientation/volume checks; STEP roundtrip; bore openness and clearance; dimensional and Blender import checks. Slicing and print evidence remain separate. |
| Physical evidence | Missing | Record slicer settings and estimates, actual part mass, dimensions, insertion fit, joint gap and deflection with fixture/load details. |

None of the missing hardware measurements blocks a labelled construction coupon. They do block finalized spar, servo and motor interfaces and flight-ready design.

## Why 850 mm is still a candidate

Span alone cannot establish soaring feasibility. Wing area, aspect ratio, all-up mass, trim, aerodynamic polar at relevant Reynolds numbers, bank/turn losses and structural limits are still unknown. The representative symmetric coupon cannot establish tailless-aircraft pitch stability. Keep the option of a more efficient glider open and evaluate the same characterized airframe for both controllers. Do not scale this coupon into a full wing without that work.

## Sources actually reviewed

- Repository `AGENTS.md` and all eight required entry documents at the baseline above; `GVRSF2027/design/README.md`, `validation/README.md`, and saved CAD prompt.
- Technical dossier chapters [aircraft/control](../../docs/projects/ai-powered-adaptive-dynamic-soaring/03-aircraft-and-control-architecture.md) and [physics/modeling](../../docs/projects/ai-powered-adaptive-dynamic-soaring/02-physics-and-modeling.md).
- [Albert folder](https://drive.google.com/drive/folders/1r_lu_vsgYFwE9P2iYyl2XbXs4FyoQBtl): three documents listed. Directly read the [experiment plan](https://docs.google.com/document/d/1rOHL4tqCEpjFEhksQYDjGyODTuxQw9m6IJh9dI08yZA/edit) and [simplified physics checks](https://docs.google.com/document/d/1QnXpgBGR7fP7YKiDxHwqi_SkJmgUzN7p0sbt2q0vmzk/edit). The core-paper-notes document was listed, not reviewed in this CAD task.
- [PDAS thickness definition](https://www.pdas.com/naca456thick4.html), read for the analytic profile, and [CadQuery export documentation](https://cadquery.readthedocs.io/en/stable/importexport.html). Local installed APIs are the execution reference.

The November 11 physics document reports an assistant-run 2-D demonstration with still-air/uniform-wind checks, not a complete dynamic-soaring simulator. It explicitly leaves Christopher's own rerun unverified. Albert's annotations identify JSBSim as the choice in Christopher's E-002 proposal; E-002 itself was not reviewed here. This task does not independently rerun or certify those physics results. The plan includes an unresolved student choice of energy frame. No AI advantage, physical print or flight result was found in the reviewed sources.

## Immediate next measurements

Confirm the nozzle and filament; measure the available spar OD (or choose a coupon-only gauge); measure component masses/envelopes before full-aircraft CAD. After slicing, print one panel and the pin first, inspect fit, then print the second matching panel. Freeze any later structural-comparison protocol separately.
