# Wing-section v001 — proposed slicer setup

**Not sliced or printed in this session. No configured slicer project is supplied.** Bambu Studio is not available in the cloud environment and access to the user's Mac is not exposed.

| Setting | Proposed starting point / check |
| --- | --- |
| Printer | Confirm actual P1S and build plate; select its real printer profile. |
| Nozzle / filament | Assumed 0.4 mm / standard non-foaming PLA. Use a suitable manufacturer profile for the actual spool and plate; record temperatures and cooling. |
| Units / scale | mm, 100%; panel X/Y/Z = 120 / 14.5536 / 40; pin = 3 / 3 / 12 mm. |
| Layer height | 0.20 mm starting point; record actual first layer. |
| Orientation | Panel and pin upright, span/bores along printer Z. Open panel end on bed. |
| Walls | Start with two perimeter loops and variable-width wall generation; inspect that the 0.8 mm skin and 1.2 mm webs survive everywhere. |
| Infill | 100% only within modeled solid regions. The CAD-defined cavities and bores must remain empty. Verify the preview rather than assuming infill settings preserve them. |
| Top / bottom | 3 layers starting point. Check that no membrane is created across an open cavity or bore; top/bottom layers apply to modeled material, not empty space. |
| Supports | Proposed off: constant extruded cross-section has no intended internal bridges; pin end chamfers need preview review. |
| Adhesion | Consider an outer brim, especially for the pin. Inspect removal access and first-layer expansion at bore mouths. Record brim width/gap and elephant-foot compensation. |
| Placement | Print one panel + pin first with adequate clearance; two panels + pin after fit review. Check actual bed limits including brim and printer exclusion regions. |

Before printing, inspect first layer, middle layers and final layers for continuous skins, connected sleeve/web paths, empty 6.4/3.4 mm bores, missing thin regions, unintended bridges or automatic repair warnings. Record any warning and inspect its cause rather than accepting an unseen repair. Save plate screenshot, slicer estimated mass/time and the configured `.3mf` here after validation. Neither estimate currently exists.

[Assembly and measurement guide](../../../docs/wing-section-v001-build-and-test.md)
