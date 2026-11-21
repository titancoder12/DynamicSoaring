"""Construction coupon, millimetres. CadQuery 2.7.0; NOT a flight airfoil selection.

Run from any directory: python /path/to/generate.py
Parameterize with --params FILE; use --output-dir DIR for experimental exports.
"""
import argparse
import csv
import hashlib
import json
import math
import platform
from pathlib import Path

import cadquery as cq
import numpy as np
import OCP
from OCP.Bnd import Bnd_Box
from OCP.BRepBndLib import BRepBndLib

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[2]


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def profile(p):
    """NACA symmetric thickness + linear TE thickening; cosine-sampled polygon.

    PDAS: https://www.pdas.com/naca456thick4.html . Its coefficients are 5x
    the conventional ones used here. This added thickness is our modification.
    """
    n = p['profile_intervals_per_side']
    c, t = p['chord_mm'], p['thickness_ratio']
    baseline_te_half = 5*t*c*(.2969-.1260-.3516+.2843-.1015)
    added_te_half = p['trailing_edge_mm']/2 - baseline_te_half
    require(added_te_half >= 0, 'Trailing edge must not thin the baseline profile')
    top = []
    for i in range(n+1):
        u = (1-math.cos(math.pi*i/n))/2
        y = 5*t*c*(.2969*math.sqrt(u)-.1260*u-.3516*u*u+.2843*u**3-.1015*u**4)
        top.append((c*u, y+added_te_half*u))
    return top + [(x, -y) for x, y in top[-1:0:-1]]


def extrude(wire, span):
    return cq.Workplane('XY').add(wire).toPending().extrude(span).val()


def cylinder(x, radius, span):
    return cq.Solid.makeCylinder(radius, span, cq.Vector(x, 0, 0))


def dimensions(solid):
    # Do not let export-created triangulation change BRep dimension checks.
    box = Bnd_Box()
    BRepBndLib.AddOptimal_s(solid.wrapped, box, False, False)
    a,b,c,d,e,f = box.Get()
    return [d-a,e-b,f-c]


def build(p):
    require(p['units'] == 'mm', 'Only millimetres are supported')
    for k, v in p.items():
        if isinstance(v, (float, int)):
            require(math.isfinite(v) and v > 0, f'{k} must be positive and finite')
    require(isinstance(p['profile_intervals_per_side'], int) and
            p['profile_intervals_per_side'] >= 40, 'Use at least 40 integer profile intervals')
    require(.08 <= p['thickness_ratio'] <= .25, 'Coupon thickness ratio outside supported range')
    require(0 < p['spar_x_fraction'] < p['alignment_x_fraction'] < 1, 'Bore order/location invalid')
    require(p['pin_chamfer_mm'] < min(p['pin_od_mm']/2, p['pin_length_mm']/2), 'Pin chamfer too large')
    require(p['pin_length_mm'] < 2*p['section_span_mm'], 'Pin longer than assembled span')
    pts = profile(p)
    wire = cq.Workplane('XY').polyline(pts).close().val()
    inner_wires = wire.offset2D(-p['shell_mm'], 'intersection')
    require(len(inner_wires) == 1, 'Shell offset must leave one cavity')
    length = p['section_span_mm']
    outer, cavity = extrude(wire, length), extrude(inner_wires[0], length)
    require(cavity.Volume() < outer.Volume(), 'Shell offset did not form an inner cavity')
    panel = outer.cut(cavity)
    stations = [
        ('spar', p['chord_mm']*p['spar_x_fraction'],
         p['spar_nominal_od_mm']+p['spar_diametral_clearance_mm']),
        ('alignment', p['chord_mm']*p['alignment_x_fraction'],
         p['pin_od_mm']+p['pin_diametral_clearance_mm']),
    ]
    for name, x, bore in stations:
        sleeve = cylinder(x, bore/2+p['sleeve_wall_mm'], length)
        require(abs(sleeve.intersect(cavity).Volume()-sleeve.Volume()) < 1e-5,
                f'{name} sleeve does not fit inside shell cavity')
        web = cq.Workplane('XY').center(x, 0).rect(p['web_mm'], p['chord_mm']).extrude(length).val()
        panel = panel.fuse(sleeve, web.intersect(outer)).clean()
    for _, x, bore in stations:
        panel = panel.cut(cylinder(x, bore/2, length)).clean()
    pin = cq.Workplane('XY').circle(p['pin_od_mm']/2).extrude(p['pin_length_mm'])
    pin = pin.edges('%Circle').chamfer(p['pin_chamfer_mm']).val()
    for name, solid in [('panel', panel), ('pin', pin)]:
        require(solid.isValid() and len(solid.Solids()) == 1 and solid.Volume() > 0,
                f'{name} must be one valid positive-volume solid')
    return panel, pin, pts, wire, inner_wires[0], stations


def check_stl(path, solid):
    """Independent binary-STL topology, winding, bounds and signed-volume checks."""
    data = Path(path).read_bytes()
    count = int.from_bytes(data[80:84], 'little')
    require(len(data) == 84 + 50*count, 'Unexpected STL size or encoding')
    dtype = np.dtype([('normal','<f4',(3,)), ('v','<f4',(3,3)), ('attr','<u2')])
    facets = np.frombuffer(data, dtype=dtype, count=count, offset=84)
    v = facets['v'].astype(float)
    require(np.isfinite(v).all(), 'Non-finite STL coordinate')
    unique, indices = np.unique(v.reshape(-1,3), axis=0, return_inverse=True)
    f = indices.reshape(-1,3)
    edges = np.concatenate([f[:,[0,1]], f[:,[1,2]], f[:,[2,0]]])
    undirected, inverse, counts = np.unique(np.sort(edges,axis=1),axis=0,return_inverse=True,return_counts=True)
    require(np.all(counts == 2), 'STL boundary or non-manifold edge')
    winding = np.bincount(inverse, weights=np.where(edges[:,0] < edges[:,1], 1, -1))
    require(np.all(winding == 0), 'STL inconsistent edge winding')
    cross = np.cross(v[:,1]-v[:,0],v[:,2]-v[:,0])
    require(np.all(np.linalg.norm(cross,axis=1) > 1e-10), 'Degenerate STL triangle')
    volume = float(np.einsum('ij,ij->i',v[:,0],np.cross(v[:,1],v[:,2])).sum()/6)
    require(volume > 0, 'STL normals face inward')
    volume_error = abs(volume-solid.Volume())/solid.Volume()
    require(volume_error < .005, 'STL volume differs by >= 0.5%')
    bbox = np.ptp(unique,axis=0)
    require(np.max(np.abs(bbox-np.array(dimensions(solid)))) < .03, 'STL dimensions differ by >= 0.03 mm')
    # Every mesh vertex must be reachable through mesh edges.
    parent = list(range(len(unique)))
    def root(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for a,b in undirected:
        parent[root(int(a))] = root(int(b))
    components = len({root(i) for i in range(len(unique))})
    require(components == 1, 'Disconnected STL surface')
    return dict(triangles=count, vertices=len(unique), connected_components=components,
                all_edges_two_faces=True, consistent_winding=True,
                dimensions_mm=bbox.tolist(), volume_mm3=volume, relative_volume_error=volume_error)


def validate(p, panel, pin, wire, inner, stations):
    expected = [p['chord_mm'], max(y for _, y in profile(p))*2, p['section_span_mm']]
    require(max(abs(a-b) for a,b in zip(dimensions(panel),expected)) < 1e-5, 'Panel dimensions incorrect')
    wall = wire.distance(inner)
    require(abs(wall-p['shell_mm']) < 1e-5, 'Minimum shell offset incorrect')
    tests = {}
    for name,x,bore in stations:
        nominal = p['spar_nominal_od_mm'] if name == 'spar' else p['pin_od_mm']
        clearance = bore - nominal
        fit = cylinder(x, nominal/2, p['section_span_mm'])
        empty = cylinder(x, bore/2-.001, p['section_span_mm'])
        oversize = cylinder(x, bore/2+.05, p['section_span_mm'])
        require(panel.intersect(fit).Volume() < 1e-7, f'{name} nominal gauge collides')
        require(panel.intersect(empty).Volume() < 1e-7, f'{name} bore not through/open')
        require(panel.intersect(oversize).Volume() > .1, f'{name} bore missing or oversized')
        tests[name] = dict(x_mm=x, bore_diameter_mm=bore, diametral_clearance_mm=clearance,
                           radial_clearance_mm=clearance/2, nominal_gauge_collision_mm3=panel.intersect(fit).Volume())
    span = p['section_span_mm']
    second = panel.translate((0,0,span))
    assembled_pin = pin.translate((stations[1][1],0,span-p['pin_length_mm']/2))
    require(panel.intersect(second).Volume() < 1e-7, 'Panels overlap')
    require(panel.fuse(second).intersect(assembled_pin).Volume() < 1e-7, 'Assembled pin collides')
    return dict(minimum_shell_offset_mm=wall, interfaces=tests,
                assembled_span_mm=2*span, pin_engagement_each_side_mm=p['pin_length_mm']/2,
                assembly_interference_check='pass', print_axis='+Z span; flat open end at Z=0')


def generate(params_path, output):
    p = json.loads(params_path.read_text())
    panel,pin,pts,wire,inner,stations = build(p)
    checks = validate(p,panel,pin,wire,inner,stations)
    output.mkdir(parents=True,exist_ok=True)
    canonical = output.resolve() == (PROJECT/'design/exports/wing-section-v001').resolve()
    coordinates = HERE/'profile-coordinates.csv' if canonical else output/'profile-coordinates.csv'
    report_path = PROJECT/'validation/wing-section-v001-geometry.json' if canonical else output/'geometry-checks.json'
    report_path.parent.mkdir(parents=True,exist_ok=True)
    with coordinates.open('w',newline='') as f:
        writer = csv.writer(f,lineterminator='\n'); writer.writerow(['x_mm','y_mm'])
        writer.writerows(pts)
    report = dict(revision=p['revision'], evidence_type='executed geometry checks and calculated estimates',
                  software=dict(python=platform.python_version(),cadquery=cq.__version__,OCP=OCP.__version__),
                  units='mm', parameters=p,
                  source_sha256={str(HERE.name+'/generate.py'):sha256(__file__),params_path.name:sha256(params_path)},
                  checks=checks, parts={})
    for name,solid in [('panel',panel),('alignment-pin',pin)]:
        stl,step = output/(name+'.stl'),output/(name+'.step')
        solid.exportStl(str(stl),tolerance=p['stl_linear_tolerance_mm'],
                        angularTolerance=p['stl_angular_tolerance_rad'],relative=False,parallel=False)
        cq.exporters.export(solid,str(step),opt={'write_pcurves':False})
        mesh = check_stl(stl,solid)
        imported = cq.importers.importStep(str(step)).val()
        require(imported.isValid() and len(imported.Solids()) == 1, 'STEP roundtrip invalid')
        require(abs(imported.Volume()-solid.Volume())/solid.Volume() < 1e-6, 'STEP volume mismatch')
        require(max(abs(a-b) for a,b in zip(dimensions(imported),dimensions(solid))) < 1e-5, 'STEP dimension mismatch')
        report['parts'][name] = dict(valid_solid=True,solid_count=1,dimensions_mm=dimensions(solid),
            volume_mm3=solid.Volume(),calculated_solid_pla_mass_g=solid.Volume()/1000*p['assumed_solid_pla_density_g_cm3'],
            stl=mesh,step_roundtrip='pass',sha256={stl.name:sha256(stl),step.name:sha256(step)})
    report['parts']['panel']['print_quantity'] = 2
    report['parts']['alignment-pin']['print_quantity'] = 1
    report['pending'] = ['slicer scale and toolpaths','physical print','measured material density/mass/fit',
                         'structural load characterization','aerodynamics and flight']
    report_path.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({name:{k:val for k,val in v.items() if k in ['dimensions_mm','volume_mm3','calculated_solid_pla_mass_g']}
                      for name,v in report['parts'].items()},indent=2))
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--params',type=Path,default=HERE/'parameters.json')
    parser.add_argument('--output-dir',type=Path,default=PROJECT/'design/exports/wing-section-v001')
    args = parser.parse_args()
    generate(args.params,args.output_dir)
