"""Editable workflow diagrams; export PNG with system Python, Cairo and librsvg."""
from pathlib import Path
from html import escape
import gi, cairo
gi.require_version('Rsvg','2.0')
from gi.repository import Rsvg
OUT=Path(__file__).resolve().parents[1]/'assets/projects/robotic-weaving'
INK='#29333f'; BLUE='#56869c'; MUTED='#73808c'; PALE='#f3f6f8'
def build(mobile=False):
 w,h=(600,1544) if mobile else (1600,580)
 offset=129 if mobile else 149
 p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">Robotic weaving workflow</title><desc id="desc">Weaving targets and a kinematic model feed joint-angle calculation. Hardware initialization supports control separately. The computer sends serial commands to the controller, which outputs servo signals.</desc><defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10" fill="{BLUE}"/></marker></defs><rect width="100%" height="100%" fill="white"/><g transform="translate(0 -{offset})" font-family="Arial, DejaVu Sans, sans-serif">']
 def text(x,y,t,size=17,bold=False,color=MUTED):
  p.append(f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{700 if bold else 400}">{escape(t)}</text>')
 def rect(x,y,ww,hh,fill=PALE,stroke='none'):
  p.append(f'<rect x="{x}" y="{y}" width="{ww}" height="{hh}" rx="15" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')
 def box(x,y,ww,hh,title,lines):
  rect(x,y,ww,hh,'white','#d8e2e9');p.append(f'<path d="M{x+2} {y+17} V{y+hh-17}" stroke="{BLUE}" stroke-width="4" stroke-linecap="round"/>')
  text(x+20,y+34,title,20,True,INK)
  for i,line in enumerate(lines):text(x+20,y+63+i*24,line,16)
 def arrow(d,dashed=False):
  p.append(f'<path d="{d}" fill="none" stroke="{BLUE}" stroke-width="2.3"'+(' stroke-dasharray="6 5"' if dashed else '')+' marker-end="url(#arrow)"/>')
 if not mobile:
  rect(18,165,845,198);text(40,195,'01  WEAVING TASK PREPARATION',15,True,BLUE)
  box(40,221,240,110,'Patterns & frames',['Weaving Pattern I / II / III'])
  box(316,221,236,110,'Anchor sequence',['Coordinates + visit order'])
  box(588,221,252,110,'Ordered TCP targets',['Tool position + orientation'])
  arrow('M280 276 H314');arrow('M552 276 H586')
  rect(18,403,845,310);text(40,434,'02  ROBOT PREPARATION',15,True,BLUE)
  box(40,502,240,130,'Hardware components',['Mechanical parts','Servos + control board'])
  box(316,502,236,130,'Arm assembly',['Desktop robotic arm','Threading tool'])
  box(588,463,252,105,'Kinematic model',['Grasshopper · links + frames'])
  box(588,592,252, 96,'Servo initialization',['Prepare the physical arm'])
  arrow('M280 567 H314');arrow('M552 567 H570 V515 H586');arrow('M570 567 V640 H586')
  box(916,321,292,144,'Joint-angle calculation',['TCP targets + robot model','Inverse kinematics','Output: joint commands'])
  arrow('M840 276 H878 V354 H914');arrow('M840 515 H878 V430 H914')
  box(1260,321,312,144,'Control & weaving test',['Computer → serial commands','Controller → servo signals','Physical robot execution'])
  arrow('M1208 393 H1258')
  box(1260,516,312,110,'Execution observations',['Tool motion + woven sample'])
  arrow('M1416 465 V514')
  # A support path, not feedback: starts at initialization and enters control.
  arrow('M840 640 H1234 V438 H1258',True);text(920,624,'Hardware ready',16,False,BLUE)
 else:
  rect(18,145,564,432);text(38,179,'01  WEAVING TASK PREPARATION',16,True,BLUE)
  for y,title,ls in [(203,'Patterns & frames',['Weaving Pattern I / II / III']),(329,'Anchor sequence',['Coordinates + visit order']),(455,'Ordered TCP targets',['Tool position + orientation'])]:box(58,y,484,96,title,ls)
  arrow('M300 299 V327');arrow('M300 425 V453')
  rect(18,603,564,466);text(38,637,'02  ROBOT PREPARATION',16,True,BLUE)
  box(58,661,484,96,'Hardware components',['Mechanical parts · servos · control board'])
  box(58,787,484,96,'Arm assembly',['Desktop robotic arm + threading tool']);arrow('M300 757 V785')
  box(38,937,252,104,'Kinematic model',['Link geometry','+ robot frames'])
  box(316,937,244,104,'Servo initialization',['Prepare the','physical arm'])
  arrow('M300 883 V910 H164 V935');arrow('M300 910 H438 V935')
  box(58,1153,484,144,'Joint-angle calculation',['TCP targets + robot model','Inverse kinematics → joint commands'])
  # Target route travels in the outside gutter; no modules are crossed.
  arrow('M58 503 H8 V1195 H56')
  arrow('M164 1041 V1151')
  box(58,1357,484,144,'Control & weaving test',['Computer → serial commands','Controller → servo signals','Physical robot execution']);arrow('M300 1297 V1355')
  arrow('M560 989 H590 V1410 H544',True)
  box(58,1557,484,100,'Execution observations',['Tool motion + woven sample']);arrow('M300 1501 V1555')
 p.append('</g></svg>');return ''.join(p)
for mobile in [False,True]:
 name='system-overview-mobile' if mobile else 'system-overview'
 (OUT/(name+'.svg')).write_text(build(mobile))
 if not mobile:
  surface=cairo.ImageSurface(cairo.FORMAT_ARGB32,4800,1740);ctx=cairo.Context(surface);ctx.scale(3,3)
  r=Rsvg.Rectangle();r.x=0;r.y=0;r.width=1600;r.height=580
  Rsvg.Handle.new_from_file(str(OUT/(name+'.svg'))).render_document(ctx,r)
  surface.write_to_png(str(OUT/(name+'.png')))
