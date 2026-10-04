"""Recompose original project vector drawings with redrawn control/PWM schematics."""
from pathlib import Path
import re,io
import gi,cairo
from PIL import Image,ImageChops
gi.require_version('Rsvg','2.0')
from gi.repository import Rsvg
OUT=Path(__file__).resolve().parents[1]/'assets/projects/robotic-weaving'
p=[]
def txt(x,y,s,size=20,color='#344651',bold=False):p.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{600 if bold else 400}">{s}</text>')
def rect(x,y,w,h,fill='white',stroke='#697780',rx=6):p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')
def path(d,c='#769dad',width=2,dash=False):p.append(f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{width}"'+(' stroke-dasharray="5 5"' if dash else '')+'/>')
def vector(name,x,y,w,h):
 s=(OUT/'hardware-sources'/f'{name}.svg').read_text();vb=list(map(float,re.search(r'viewBox="([^"]+)"',s)[1].split()));ww,hh=vb[2:];scale=1000/max(ww,hh)
 surf=cairo.ImageSurface(cairo.FORMAT_ARGB32,round(ww*scale),round(hh*scale));ctx=cairo.Context(surf);ctx.set_source_rgb(1,1,1);ctx.paint();ctx.scale(scale,scale);r=Rsvg.Rectangle();r.width=ww;r.height=hh;Rsvg.Handle.new_from_data(s.encode()).render_document(ctx,r);buf=io.BytesIO();surf.write_to_png(buf);im=Image.open(buf).convert('RGB');box=ImageChops.difference(im,Image.new('RGB',im.size,'white')).convert('L').point(lambda v:255 if v>22 else 0).getbbox();a,b,c,d=[v/scale for v in box];pad=8
 inner=s[s.index('>',s.index('<svg'))+1:s.rindex('</svg>')];inner=re.sub(r'stroke-width:[^;]+;', 'stroke-width:0.8;vector-effect:non-scaling-stroke;', inner);ids=re.findall('id="([^"]+)"',inner)
 for id in sorted(ids,key=len,reverse=True):inner=inner.replace(f'"{id}"',f'"{name}-{id}"').replace(f'#{id}',f'#{name}-{id}')
 p.append(f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="{a-pad} {b-pad} {c-a+2*pad} {d-b+2*pad}" preserveAspectRatio="xMidYMid meet">{inner}</svg>')
def servo(x,y,angle):
 p.append(f'<g transform="translate({x} {y})">');rect(-66,-38,132,76,'#edf0f1');rect(-82,-24,164,48,'none');p.append('<circle r="28" fill="#c8ced1" stroke="#53616a"/>');p.append(f'<g transform="rotate({angle})">');rect(-12,-58,24,116,'#d6dadd');rect(-58,-12,116,24,'#d6dadd');p.append('<circle r="11" fill="#aab5bc" stroke="#53616a"/>')
 for v in [-43,-29,29,43]:p.append(f'<circle cx="0" cy="{v}" r="3" fill="white" stroke="#53616a"/>')
 p.append('</g></g>')
def wave(x,y,width):
 path(f'M{x} {y+25} H{x+18} V{y} H{x+18+width} V{y+25} H{x+123} V{y} H{x+123+width} V{y+25} H{x+242}', '#697780',1.7)
p.append('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1220" height="1120" viewBox="0 0 1220 1120"><title>Robotic weaving hardware and servo control</title><rect width="1220" height="1120" fill="white"/><g font-family="Arial, DejaVu Sans, sans-serif">')
txt(28,38,'01  MECHANICAL ASSEMBLY',21,bold=True);txt(28,70,'Links · servo brackets · base · tool mount',17,'#71838d')
p.append('<g transform="translate(0 -80)">')
# Motor case faces shaded beneath the original vector linework.
for motor,points in {
 7:'411,235 428,221 446,224 450,251 433,266 415,262',
 6:'519,300 540,290 557,294 560,314 544,329 521,325',
 5:'29,634 59,606 83,616 106,661 70,692 44,679',
 4:'423,696 442,683 498,693 497,750 477,763 437,749 421,747',
 3:'345,849 382,800 422,815 396,868 362,857',
 2:'393,861 428,834 447,870 416,914 408,907',
 1:'109,891 153,867 176,879 177,930 138,953 112,942'
}.items():
 p.append(f'<polygon id="motor-{motor}-tint" points="{points}" fill="#dce4e9" fill-opacity="0.65"/>')
vector('arm',25,94,540,1100)
path('M744 105 V1170','#e2e7ea',1)
# Direct callouts attach to the motor geometry, following the supplied reference.
# Axis 2 uses two motors. Connector routes remain an explanatory wiring diagram.
for axis,motor,x,y,label_y,bend,port_y in [
 (6,7,430,241,241,729,694),
 (5,6,540,311,327,711,711),
 (4,5,65,638,638,693,728),
 (3,4,470,742,742,675,742),
 (2,3,410,838,823,693,762),
 (2,2,422,884,894,711,779),
 (1,1,150,911,972,729,796),
]:
 p.append(f'<circle cx="{x}" cy="{y}" r="2.3" fill="#53616a"/>')
 path(f'M{x} {y} V{label_y} H{bend} V{port_y+60} H{832}', '#71838d',1,True)
 txt(565,label_y-8,f'Axis {axis} (Motor {motor})',14)
 txt(565,label_y+17,{1:'α1 · 0–270°',2:'α2 · 10–110°',3:'α3 · 20–145°',4:'α4 · 0–180°',5:'α5 · 0–155°',6:'α6 · 0–180°'}[axis],13,'#71838d')

p.append('</g>')
txt(785,38,'02  THREADING TOOL',21,bold=True);vector('needle',785,85,365,165);txt(805,271,'Threading needle',18)
p.append('<g transform="translate(0 -20)">')
txt(785,363,'03  SERVO CONTROL',21,bold=True)
# Computer and power connections redrawn to match the supplied close-up.
rect(790,400,82,53,'white','#697780',1)
path('M791 443 H871 M831 453 V466 M812 466 H850','#697780',3)
path('M831 466 V535 H889 V591','#697780',3)
# Voltmeter centered above the pair of board power terminals.
p.append('<g transform="translate(-29 0)">')
rect(947,400,70,62,'#697780','#697780',10)
path('M957 435 A25 25 0 0 1 1007 435','white',3)
for x1,y1,x2,y2 in [(960,430,965,432),(966,416,970,421),(982,410,982,417),(997,416,993,421),(1003,430,998,432)]:
 path(f'M{x1} {y1} L{x2} {y2}','white',2)
path('M982 435 L996 421','white',3);txt(974,458,'V',22,'white',True)
p.append('</g>')
# Plug and external supply lead.
path('M988 446 H1124 V419','#697780',3)
path('M1117 400 V410 M1131 400 V410 M1114 410 H1134 V419 L1124 427 L1114 419 Z','#697780',2)
path('M1145 406 L1139 420 H1147 L1140 434','#697780',2)
txt(1051,472,'Power supply',16)
# Separate black and red conductors go to the board power connectors.
path('M950 463 V535 H938 V591','#697780',3)
path('M956 463 V535 H968 V591','#d25f59',3)
# Leader terminates at the switch already drawn on the board.
txt(1052,529,'Power switch',16)
path('M1145 537 H1004 V631','#697780',1,True)
vector('controller',790,566,302,365);txt(853,957,'Controller',18,bold=True)
# Editable labels reconstructed from the supplied controller close-up.
p.append('<g transform="translate(798 590) scale(.80)">')
txt(99,43,'USB',17);txt(252,117,'ON',11)
for label,x in [('GND',23),('5V',46)]:
 p.append(f'<text transform="translate({x} 78) rotate(-90)" font-size="9" fill="#71838d">{label}</text>')
for label,y in [('TX',100),('TR',124)]:txt(82,y,label,10)
txt(119,112,'TX',10)
for i in range(8):
 txt(82,147+i*23.5,f'S{i+1}',10)
 txt(266,147+i*23.5,f'S{24-i}',10)
 txt(94+i*23.5,319,f'S{i+9}',9)
for x in [20,301]:
 txt(x,95,'−',9);txt(x+23,95,'+',9)
for y,label in [(342,'+'),(365,'−'),(388,'•')]:txt(77,y,label,10)
p.append('</g>')
p.append('</g>')
p.append('</g></svg>');svg=''.join(p);(OUT/'hardware-control.svg').write_text(svg)
surface=cairo.ImageSurface(cairo.FORMAT_ARGB32,2440,2240);ctx=cairo.Context(surface);ctx.scale(2,2);r=Rsvg.Rectangle();r.width=1220;r.height=1120;Rsvg.Handle.new_from_data(svg.encode()).render_document(ctx,r);surface.write_to_png(str(OUT/'hardware-control.png'))
