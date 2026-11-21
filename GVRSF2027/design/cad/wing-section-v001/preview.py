"""Dimensioned engineering view of actual generated geometry (Matplotlib)."""
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, Rectangle
import generate as g

p = json.loads((g.HERE/'parameters.json').read_text())
panel,pin,pts,outer,inner,stations = g.build(p)
# Use the actual planar BRep faces at the open end, including every cavity.
faces = [f for f in panel.Faces() if abs(f.Center().z) < 1e-7]
fig = plt.figure(figsize=(12,8),facecolor='#f4f7fa')
fig.text(.055,.94,'WING SECTION  /  v001',fontsize=23,weight='bold',color='#16384e')
fig.text(.055,.903,'Construction coupon • assumed dimensions • millimetres • not flight validated',fontsize=11,color='#486073')
ax = fig.add_axes([.07,.50,.86,.34]);ax.set_aspect('equal');ax.axis('off')
for face in faces:
    for i,wire in enumerate([face.outerWire()]+face.innerWires()):
        # Sample the complete ordered wire, including actual bore/cavity loops.
        points = wire.sample(500)[0]
        xy = [(v.x,v.y) for v in points]
        ax.add_patch(Polygon(xy,closed=True,facecolor='#2186a2' if i==0 else '#f4f7fa',edgecolor='#16384e',lw=.6))
ax.set_xlim(-8,128);ax.set_ylim(-19,25)
def dimension(ax,a,b,text,offset=(0,0)):
    ax.annotate('',xy=a,xytext=b,arrowprops=dict(arrowstyle='<->',color='#486073',lw=.8))
    ax.text((a[0]+b[0])/2+offset[0],(a[1]+b[1])/2+offset[1],text,fontsize=9,ha='center',va='center',color='#16384e',bbox=dict(facecolor='#f4f7fa',edgecolor='none',pad=1))
dimension(ax,(0,-14),(120,-14),'120.00 chord')
for x in [0,120]:ax.plot([x,x],[-1,-16],color='#91a5b4',lw=.6)
ax.annotate('6.40 bore / nominal 6.00 spar\ncentre X = 36.00',xy=(36,0),xytext=(10,18),fontsize=9,color='#16384e',arrowprops=dict(arrowstyle='-',color='#486073'))
ax.annotate('3.40 bore / 3.00 pin\ncentre X = 75.00',xy=(75,0),xytext=(70,18),fontsize=9,color='#16384e',arrowprops=dict(arrowstyle='-',color='#486073'))
ax.annotate('0.80 shell',xy=(15,5),xytext=(-5,10),fontsize=9,color='#16384e',arrowprops=dict(arrowstyle='-',color='#486073'))
ax.annotate('0.80 trailing edge',xy=(120,0),xytext=(97,10),fontsize=9,color='#16384e',arrowprops=dict(arrowstyle='-',color='#486073'))

bottom = fig.add_axes([.07,.105,.47,.35]);bottom.set_aspect('equal');bottom.axis('off')
bottom.set_xlim(-15,140);bottom.set_ylim(-8,110)
for z,color in [(0,'#c4e5ee'),(58,'#d1edf0')]:
    bottom.add_patch(Rectangle((0,z),120,40,facecolor=color,edgecolor='#2186a2',lw=1.3))
    for _,x,d in stations:
        for dx in [-d/2,d/2]:bottom.plot([x+dx,x+dx],[z,z+40],color='#486073',ls='--',lw=.8)
bottom.plot([36,36],[-5,104],color='#333f49',lw=3)
bottom.plot([75,75],[43,55],color='#71a52f',lw=4)
bottom.text(1,105,'EXPLODED PLAN VIEW',fontsize=10,weight='bold',color='#16384e')
dimension(bottom,(131,0),(131,40),'40',offset=(1,0))
dimension(bottom,(131,58),(131,98),'40',offset=(1,0))
bottom.text(85,47,'18 display gap',fontsize=8,color='#486073')
bottom.text(4,18,'Panel A',fontsize=10,color='#16384e')
bottom.text(4,77,'Panel B',fontsize=10,color='#16384e')
fig.text(.58,.42,'ASSEMBLY + PRINT NOTES',fontsize=13,weight='bold',color='#16384e')
fig.text(.58,.365,'2 × identical panels, 1 × alignment pin\nButt together: 80 mm total span\nPin: Ø3 × 12; 0.3 mm end chamfers\nCentre the pin: 6 mm engagement each side',fontsize=11,color='#16384e',linespacing=1.6,va='top')
fig.text(.58,.245,'Dark line: external spar, reference only\nBoth bores: 0.40 mm diametral clearance\nPrint span vertically (+Z), open end on bed\nNo slicer or physical print validation yet',fontsize=10,color='#486073',linespacing=1.6,va='top')
fig.text(.055,.045,'Modified NACA 0012 thickness profile • maximum thickness 14.554 mm • source: generate.py + parameters.json',fontsize=9,color='#486073')
dest = g.PROJECT/'design/previews';dest.mkdir(parents=True,exist_ok=True)
for ext in ['png','svg']:
    fig.savefig(dest/('wing-section-v001-dimensions.'+ext),dpi=180,facecolor=fig.get_facecolor())
