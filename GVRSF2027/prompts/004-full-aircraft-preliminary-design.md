# 004 — Full-aircraft preliminary design

**Prepared:** 2026-11-12  
**Canonical plan:** [Aircraft design and test plan](../docs/aircraft-design-and-test-plan.md)  
**Live status, dependencies and next action:** [Prompt register](README.md)

When this task is selected, develop an adjustable preliminary layout of the complete aircraft: the wing, central body, propulsion, controls, reinforcement and component locations as one coherent visual assembly. Produce editable source and useful sizing calculations. This milestone establishes a provisional design for review; it does not establish a complete manufacturing design or flight suitability.

## Start from the current project

Read `AGENTS.md`, its required references, the canonical plan, current requirements, CAD review and relevant aircraft/control documentation. Inspect the current remote branch and existing changes; preserve unrelated work and report the actual working directory and starting commit. Check which CAD and Blender tools actually execute in this session, distinguishing cloud tools from the user's computer.

The approximately 850 mm flying wing, pusher arrangement and earlier component shortlist remain candidates. Evaluate them against the research purpose and available evidence. Do not simply scale the construction coupon into a full wing or adopt its modified NACA 0012 profile as the final flight airfoil.

This task can proceed before prompt 003 produces physical coupon results. It may also proceed alongside prompt 002's corrections, provided it neither reuses unchecked modified coupon geometry nor represents unresolved findings as fixed. Preserve prompts 001–003 and the existing v001 coupon. Identify any particular interface or decision that genuinely requires a pending measurement; continue independent layout work with explicit assumptions.

## Requirements, sizing and mass accounting

Create a requirements and assumptions table distinguishing **measured**, **manufacturer-specified**, **estimated**, **assumed** and **unknown** values, with sources, dates and uncertainty or plausible ranges. Cover component dimensions/masses, span, chord distribution, sweep, wing area, airfoil/trim questions, control surfaces, reinforcement, battery access, propulsion clearance and printing/assembly constraints. Do not turn candidate hardware into confirmed purchases or silently treat unknown masses as zero.

Use wing area, estimated all-up mass, aerodynamic efficiency and stability/trim questions to inform provisional geometry. Record unresolved choices and their consequences; an attractive assembly alone does not resolve them. Explain any preliminary airfoil or centre-of-gravity target and its basis. Label the target **preliminary and unvalidated**; do not present a generic percentage of chord as a verified safe CG location for this aircraft.

Define the coordinate origin, axes, units and reference dimensions. Build a component mass/position ledger including estimated airframe, reinforcement, motor/propeller, battery, electronics, servos, wiring and assembly allowances, without double counting. Calculate all-up mass and CG using `CG = sum(mass × position) / sum(mass)` for each axis. Preserve the inputs and calculations in CSV/JSON, with estimated values visibly separated from measured ones.

Model a candidate battery adjustment envelope and calculate how its positions change CG. Compare the resulting CG positions with a preliminary target only if the target has a recorded analytical basis; otherwise mark the allowable CG range as unresolved. An unresolved allowable range does not by itself block this concept milestone. Report the effect of uncertain component masses where it materially changes a layout decision. No computed CG value alone establishes stability, trim or flight readiness.

## Editable assembly and deliverables

Keep all work under `GVRSF2027/`:

- `design/cad/aircraft-layout-v001/`: authoritative parametric source, configuration, component ledger, calculation inputs/results and reproducible generation instructions.
- `design/blender/`: the assembled visual scene and its import/build script when Blender is available; record the actual version and scale convention.
- `design/previews/`: selected assembly, top and side views showing overall dimensions, component placement, reinforcement, control surfaces, battery travel and CG references.
- `design/exports/aircraft-layout-v001-concept/`: optional exchange geometry, clearly labelled **preliminary concept — not final print parts**. Provide STEP only when the workflow supports meaningful valid solid geometry. STL files are not required for this milestone.
- `docs/` and `validation/`: dated design rationale, assumption log, actual checks, unresolved decisions and the next handoff.

Use labelled component placeholders where exact geometry is unavailable. Distinguish these reference objects from designed airframe parts in the source, scene and exports; they are not printable hardware. Make the complete assembly adjustable and visually intelligible without implying that every joint, mount, wire route or printable section is finalized.

## Acceptance and handoff

Run the available generation/import workflow and inspect the actual results. Verify overall dimensions and units, assembled placement, known clearances/interferences, battery travel and CG arithmetic against the recorded inputs. Check scale in Blender and any exchange format actually supplied. Report the commands, versions, artifacts and checks that ran, including failures and unavailable checks. A placeholder-based clearance check remains provisional until the relevant dimensions are measured.

Accept this milestone when the documented complete-aircraft preliminary assembly, editable inputs, views and mass/CG calculations are coherent and reviewable. Pending physical coupon results do not by themselves block completion; record specific dependent decisions as pending. Keep experiment design, physics-baseline verification and controller research progressing in parallel.

Commit and push the checked milestone through the permitted branch workflow using normal non-force updates and expected-remote-head checks. Verify the remote branch, full commit SHA and changed-file hashes; exclude dependencies, caches, backups and disposable outputs. Update the register accurately and hand off the GitHub link, delivered paths, checks, assumptions, unresolved decisions and next justified design/test step.
