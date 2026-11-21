# Validation records

Save checks and physical observations for the aircraft project here. Distinguish executed software checks from slicing, bench measurements, simulator results, and flight results.

## Wing-section v001 records

| Record | Purpose |
| --- | --- |
| [Original executed verification](2026-11-12-wing-section-v001.md) | The generating Work session's methods, checks, and limitations. |
| [Independent review](2026-11-12-wing-section-v001-independent-review.md) | Assessment of commit `b101536`, verified deliverables, four open findings at review, and correction criteria. |
| [Independent review evidence JSON](2026-11-12-wing-section-v001-independent-review.json) | Retained numeric results, parameter replay, source/export hashes, and default STL comparisons. |
| [Observation template](wing-section-v001-observations-template.md) | Blank form for future physical observations; it contains no measured results. |

Use the [Work prompt register](../prompts/README.md) for current task status and dependencies. Preserve each dated assessment; add a resolution record tied to the actual corrected source and verified remote commit instead of rewriting old findings as if the correction already existed.

## Record requirements

For each checked design revision, record:

- The source/export paths and Git revision used.
- Software versions, units, commands, and relevant settings.
- Geometry, dimensions, clearances, and print-orientation checks actually performed.
- Slicer settings and findings, when slicing has been performed.
- Measured fit, mass, deflection, or other observations, including instruments and conditions.
- Failures, uncertainty, open questions, and the next design change supported by the evidence.

Use explicit labels such as **calculated estimate**, **slicer estimate**, **bench measurement**, **simulation result**, or **flight measurement**. Keep original measurements traceable and preserve them when interpretations change.

Organize new records by date and design revision. Link the record from the relevant design or assembly notes, and include it in the same checked repository milestone as the associated design files when practical.

[Project workspace](../README.md) · [Design-file conventions](../design/README.md)
