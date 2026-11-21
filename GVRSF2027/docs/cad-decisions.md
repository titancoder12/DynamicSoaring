# Aircraft CAD decisions

## CAD-001 — construction coupon before full airframe

Date: 2026-11-12 (America/Vancouver). Status: selected for v001 only.

Use CadQuery Python plus JSON dimensions as the authoritative editable model. Provide STL, solid STEP and a Blender 4.3 import/assembly script. Start with two identical open-ended extrusions, integrated spar/alignment sleeves and connecting webs, plus a separate alignment pin. All dimensions are provisional as recorded in [requirements](wing-section-v001-requirements.md).

This is a manufacturing demonstration, not a change to the main controller-comparison protocol or a final airfoil selection. Use a NACA 0012-derived profile with a smooth linear thickness addition to make the trailing edge 0.8 mm; preserve generated coordinates so the modification is auditable. Use a true inward polygon offset for the cavity. No artificial aerodynamic coefficients or strength ratings are assigned.

Keep the science-plan priority on Christopher's physics checks. A CAD coupon can proceed independently without treating previous planning text or assistant-run demonstrations as measured aircraft results.

## CAD-002 — Develop the complete-aircraft layout alongside coupon testing

**Date:** 2026-11-12  
**Status:** Documented working plan; implementation status is maintained in the [prompt register](../prompts/README.md).

### Decision and reason

Develop a preliminary, adjustable complete-aircraft layout in parallel with the small construction coupon's correction and physical-testing work. The user asked for this recommendation to be documented clearly before proceeding. The [aircraft design and test plan](aircraft-design-and-test-plan.md) defines the scope, deliverables, dependencies, and completion boundaries.

Starting the overall layout does not require a successful coupon print. Mass, component positions, wing geometry, CG, controls, and structure influence one another, so they should be developed together. Coupon evidence informs manufacturing decisions; it cannot establish the complete wing's aerodynamics, stability, or structural adequacy.

### Consequences

- Prepare [prompt 004](../prompts/004-full-aircraft-preliminary-design.md) for an integrated concept, component/assumption table, mass/CG calculation, views, and reproducible checks. Its preliminary completion criteria do not require the physical results from 003.
- Preserve the dependency of 003's accepted coupon/slicer work on the corrections in 002. Independent concept work can proceed alongside those tasks; unresolved findings remain visible.
- Keep the approximately 850 mm flying wing, unmeasured components, flight airfoil, and allowable CG range provisional. Do not scale the coupon into a flight-wing design by assumption.
- Use measurements and the relevant aerodynamic/structural analysis before finalizing the affected manufacturing details. A missing measurement holds the dependent decision, not all useful design work.
- Preserve Christopher's experiment-plan and physics-baseline priorities. This documentation milestone creates no CAD, print, simulator result, or flight claim.

### Relationship to CAD-001

CAD-001 records why the first implemented artifact was a construction coupon. It does not require all coupon testing to finish before whole-aircraft concept work begins. CAD-002 clarifies the parallel work after that initial milestone; the coupon's original design and evidence remain unchanged.
