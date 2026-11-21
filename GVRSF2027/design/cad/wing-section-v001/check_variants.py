"""Meaningful parametric checks; run with python check_variants.py."""
import copy
import json
import tempfile
from pathlib import Path
import generate as g

p = json.loads((g.HERE/'parameters.json').read_text())
results = []
# Regenerate a changed chord/span/spar diameter in isolated scratch, including exports.
variant = copy.deepcopy(p)
variant.update(chord_mm=140,section_span_mm=30,spar_nominal_od_mm=5,shell_mm=1.0,trailing_edge_mm=1.0)
with tempfile.TemporaryDirectory() as tmp:
    path = Path(tmp)/'variant.json'
    path.write_text(json.dumps(variant))
    report = g.generate(path,Path(tmp)/'exports')
    results.append({'case':'140 mm chord / 30 mm span / 5 mm spar / 1 mm shell',
                    'result':'pass','dimensions_mm':report['parts']['panel']['dimensions_mm']})
for label,changes in [('oversized spar',{'spar_nominal_od_mm':20}),
                       ('negative clearance',{'pin_diametral_clearance_mm':-.1}),
                       ('unsupported units',{'units':'inch'}),
                       ('swapped bore stations',{'spar_x_fraction':.8}),
                       ('excessive pin chamfer',{'pin_chamfer_mm':2})]:
    case = copy.deepcopy(p); case.update(changes)
    try:
        g.build(case)
    except ValueError as e:
        results.append({'case':label,'result':'rejected as expected','message':str(e)})
    else:
        raise AssertionError(f'Invalid case accepted: {label}')
out = g.PROJECT/'validation/wing-section-v001-parameter-checks.json'
out.write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
