"""Blender 4.3.2: import checked STL in mm, verify scale, save assembly and render.
blender --background --python GVRSF2027/design/blender/import-wing-section-v001.py
The rendered assembly is exploded. Imported printable parts retain their geometry.
"""
import json
from pathlib import Path
import bpy
from mathutils import Vector

PROJECT = Path(__file__).resolve().parents[2]
EXPORT = PROJECT/'design/exports/wing-section-v001'
DEST = PROJECT/'design/blender/wing-section-v001.blend'
PREVIEW = PROJECT/'design/previews/wing-section-v001-assembly.png'
VALIDATION = PROJECT/'validation/wing-section-v001-blender.json'
p = json.loads((PROJECT/'design/cad/wing-section-v001/parameters.json').read_text())
geometry = json.loads((PROJECT/'validation/wing-section-v001-geometry.json').read_text())
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
scene = bpy.context.scene
scene.unit_settings.system = 'METRIC'
scene.unit_settings.scale_length = 1.0
scene.unit_settings.length_unit = 'MILLIMETERS'


def material(name, color, metallic=0):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = (*color,1)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get('Principled BSDF')
    bsdf.inputs['Base Color'].default_value = (*color,1)
    bsdf.inputs['Metallic'].default_value = metallic
    bsdf.inputs['Roughness'].default_value = .32
    return mat


blue = material('Panel A',(.03,.29,.48))
cyan = material('Panel B',(.10,.55,.63))
green = material('Alignment pin',(.38,.69,.15))
dark = material('REFERENCE only - assumed spar',(.045,.055,.07))
checks = {}


def imported(name, filename, mat):
    bpy.ops.wm.stl_import(filepath=str(EXPORT/filename),global_scale=.001,use_scene_unit=False)
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(mat)
    actual = [v*1000 for v in obj.dimensions]
    part = 'panel' if filename == 'panel.stl' else 'alignment-pin'
    expected = geometry['parts'][part]['dimensions_mm']
    error = max(abs(a-b) for a,b in zip(actual,expected))
    if error >= .03:
        raise RuntimeError(f'Blender import scale failed: {actual} vs {expected}')
    checks[name] = {'dimensions_mm':actual,'max_error_mm':error,'scale_check':'pass'}
    return obj


a = imported('Panel A - print 1 of 2','panel.stl',blue)
b = imported('Panel B - print 2 of 2','panel.stl',cyan)
gap = .018
b.location.z = p['section_span_mm']/1000+gap
pin = imported('Alignment pin - print 1','alignment-pin.stl',green)
pin.location = (p['chord_mm']*p['alignment_x_fraction']/1000,0,
                p['section_span_mm']/1000+(gap-p['pin_length_mm']/1000)/2)
# Purchased spar illustration: explicitly not a printable or validated part.
total = (2*p['section_span_mm'])/1000+gap+.012
bpy.ops.mesh.primitive_cylinder_add(vertices=64,radius=p['spar_nominal_od_mm']/2000,depth=total,
    location=(p['chord_mm']*p['spar_x_fraction']/1000,0,total/2-.006))
spar = bpy.context.object
spar.name = 'REFERENCE ONLY - assumed 6 mm purchased spar, not supplied'
spar.data.materials.append(dark)
spar['not_for_printing'] = True
scene['assembly_gap_mm'] = 18
scene['note'] = 'Construction coupon; exploded preview; not flight validated. Spar is reference only.'

bpy.ops.object.camera_add(location=(.235,-.22,.20))
camera = bpy.context.object
target = Vector((.060,0,.045))
camera.rotation_euler = (target-camera.location).to_track_quat('-Z','Y').to_euler()
camera.data.type = 'ORTHO'
camera.data.ortho_scale = .215
scene.camera = camera
for name,loc,power,size in [('Key',(.12,-.12,.25),.35,.15),('Fill',(-.10,-.03,.10),.16,.12),('Rim',(.08,.12,.18),.40,.12)]:
    bpy.ops.object.light_add(type='AREA',location=loc)
    obj = bpy.context.object; obj.name = name
    obj.data.energy = power; obj.data.shape = 'DISK'; obj.data.size = size
    obj.rotation_euler = (target-obj.location).to_track_quat('-Z','Y').to_euler()
scene.world.color = (.6,.6,.6)
scene.render.engine = 'CYCLES'
scene.cycles.device = 'CPU'
scene.cycles.samples = 64
scene.cycles.use_denoising = False
scene.render.threads_mode = 'FIXED'
scene.render.threads = 4
scene.render.resolution_x = 1300
scene.render.resolution_y = 950
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = 'PNG'
scene.render.film_transparent = False
scene.view_settings.view_transform = 'AgX'
PREVIEW.parent.mkdir(parents=True,exist_ok=True)
scene.render.filepath = str(PREVIEW)
# Preserve a useful opening view and relative paths.
for screen in bpy.data.screens:
    for area in screen.areas:
        if area.type == 'VIEW_3D':
            area.spaces.active.region_3d.view_perspective = 'CAMERA'
bpy.ops.wm.save_as_mainfile(filepath=str(DEST),compress=True)
bpy.ops.render.render(write_still=True)
VALIDATION.write_text(json.dumps({'blender':bpy.app.version_string,'unit_system':'metric',
    'metres_per_blender_unit':1,'stl_import_scale':.001,'checks':checks,
    'assembly_gap_mm':18,'reference_spar':'illustration only; not exported as print part',
    'saved_blend':str(DEST.relative_to(PROJECT)), 'render':str(PREVIEW.relative_to(PROJECT))},indent=2)+'\n')
print('BLENDER_IMPORT_SCALE_PASS')
