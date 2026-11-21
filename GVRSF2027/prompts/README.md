# Work prompt register

**Established:** 2026-11-12  
**Repository:** https://github.com/eugenelin89/cwsf2027-research

This is the authoritative register for saved Work tasks, their dependencies, and the next task to run. Read the current remote repository state and `AGENTS.md` before executing a prompt. The numbered documents are handoff instructions; saving them does not start or schedule a Work session.

## Current tasks

**Next task on the coupon track: [002 — Resolve the independent review findings](002-wing-section-v001-review-fixes.md).** The dated [independent review](../validation/2026-11-12-wing-section-v001-independent-review.md) is the evidence for that task. Its findings remain open until a later correction milestone verifies their resolution.

**Prepared whole-aircraft task: [004 — Preliminary complete-aircraft design](004-full-aircraft-preliminary-design.md).** This is planned and has not started. It can run alongside 002 and 003; it does not require a successful coupon print. Read the [aircraft design and test plan](../docs/aircraft-design-and-test-plan.md) for the scope and evidence dependencies. The user's current request was to document this approach before implementation.

| ID | Canonical prompt | Status | Dependency and completion evidence |
| --- | --- | --- | --- |
| 001 | [First wing-section CAD prototype](001-wing-section-v001-cad.md) | Completed for the first CAD milestone | Requirements: [8cb57d0](https://github.com/eugenelin89/cwsf2027-research/commit/8cb57d0878e012a21e79f05cb96b7e24a3222bf0). Geometry and deliverables: [b101536](https://github.com/eugenelin89/cwsf2027-research/commit/b101536cea00ea120e03c640eb2f1cc9cbc1e661). Subsequent review findings are tracked by 002. This does not mean the whole aircraft or physical tests are complete. |
| 002 | [Review corrections and reproducible checks](002-wing-section-v001-review-fixes.md) | Ready | Read the independent review of `b101536`. Completion requires corrections, executed evidence, and a verified remote commit; no completion commit yet. |
| 003 | [Slicer preparation and staged fit test](003-wing-section-v001-slice-and-fit.md) | Blocked by 002 | Start after 002's acceptance criteria are satisfied and its remote correction commit is recorded. Hardware access and actual measurements may limit how far this task can proceed. No slicing or physical completion is recorded. |
| 004 | [Preliminary complete-aircraft design](004-full-aircraft-preliminary-design.md) | Planned — handoff prepared, not started | Can proceed independently of 003's physical results and alongside 002. Read the design/test plan, inspect the current repository/tools, and label unknown component data. No implementation or completion commit yet. |

The delivered model currently covers a small construction coupon: two 40 mm span panels and one pin. Prompt 004 now defines a future complete-aircraft concept milestone; no complete-wing or aircraft-body model has been implemented by this planning update. Its numbering does not imply that 003 must finish first.

## Naming and ordering rules

1. Use `NNN-descriptive-task-name.md`, with a permanent three-digit task ID. Future new tasks receive the next unused ID, beginning with `005`.
2. Never renumber or reuse a published ID. If priorities change, update dependencies and the next-task entry rather than renaming old tasks. IDs record the workflow sequence established when tasks are registered; they need not reproduce the creation dates of earlier unnumbered drafts.
3. Keep task IDs separate from design revisions. `002` identifies a Work task; `v001` identifies the construction design it concerns. More than one task can concern the same design revision.
4. Give every prompt its purpose, required reading, starting evidence, scope, acceptance criteria, and expected handoff. Specify repository paths, and require inspection of the actual tools and current branch.
5. Keep live status here. Use **Planned**, **Ready**, **In progress**, **Blocked**, **Completed**, or **Superseded**, with a brief reason and evidence. A task is complete only when its stated criteria are met and the relevant remote commit is verified; record partial milestones without marking the entire task complete.
6. Preserve completed instructions as history. Make substantive new work a new numbered prompt, and link its predecessor. Preserve dated reviews; record their resolutions separately with evidence and commits.
7. Before a future session ends, update this register with actual progress, remaining blockers, the next task, and available completion links. When a commit cannot name its own SHA, use an earlier verified implementation commit or add the final link in a subsequent documentation checkpoint; do not invent a self-referential commit ID.

## Compatibility with existing instructions

| Previously shared path | Meaning now |
| --- | --- |
| [work-drone-cad.md](work-drone-cad.md) | Pointer to the preserved original assignment, now prompt 001, and this register. |
| [work-drone-cad-next.md](work-drone-cad-next.md) | Pointer to this register. Its earlier slicer/physical handoff is now prompt 003 and follows the review corrections. |

These short pointers preserve links in existing conversations. Edit the numbered prompt rather than creating a second full copy at an old path. The original 001 task content is preserved; 003 adapts the previous handoff to the findings and ordering established by this review.

## Starting a future Work session

Provide the repository URL and ask Work to read `AGENTS.md` and this register, then execute the selected task with its actual prerequisites checked. Use 002 to continue the coupon corrections or select 004 to begin the preliminary whole-aircraft layout. Selecting 004 does not waive 002's findings or complete 003; these are separate tracks. A new session still needs the repository or project context; these links make the instructions discoverable once it opens the repository.

[Project workspace](../README.md) · [Aircraft design and test plan](../docs/aircraft-design-and-test-plan.md) · [Independent review](../validation/2026-11-12-wing-section-v001-independent-review.md) · [Design conventions](../design/README.md)
