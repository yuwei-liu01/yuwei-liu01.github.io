"""Editable annotations reconstructed from the user's six-step reference.
Uses existing cropped source images; annotation placement is presentation-only.
"""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
D=ROOT/'assets/projects/robotic-weaving'
def text(x,y,s,anchor='start'):
 return f'<text x="{x}" y="{y}" text-anchor="{anchor}">{s}</text>'
def line(d):return f'<path d="{d}" fill="none" stroke="#70b9ca" stroke-width="1.7"/>'
def dot(x,y):return f'<circle cx="{x}" cy="{y}" r="2.7" fill="#70b9ca"/>'
def plane(x,y):
 s=f'<g transform="translate({x} {y}) skewY(-27)">'
 for i in range(7):
  z=i*10;s+=f'<path d="M{z} 0 V90 M0 {i*15} H60" stroke="#d6a6a6" stroke-width=".65" fill="none"/>'
 return s+'</g>'
overlays={
1:text(244,171,'End Effector','end')+text(324,168,'Target Point / TCP')+text(143,410,'Base Point')+'<ellipse cx="111" cy="405" rx="15" ry="7" fill="none" stroke="#70b9ca" stroke-width="1.5"/>',
2:text(244,171,'End Effector','end')+text(324,168,'Target Point / TCP')+text(66,373,'Base Height','end')+text(101,323,'Shift Length')+text(182,408,'1st Axis')+text(254,349,'α1')+line('M111 407 L282 332 L249 340 M282 332 V310 M111 407 L251 345')+'<path d="M282 175 V332" stroke="#999" stroke-width="1" stroke-dasharray="4 4" fill="none"/>'+dot(111,407),
3:text(170,42,'Radius = Length of Upper Arm')+text(126,208,'Point 1','end')+text(247,337,'Point 2')+text(42,457,'Radius = Length of Lower Arm')+dot(134,208)+dot(237,327)+dot(136,340)+dot(111,407),
4:plane(103,167)+line('M134 139 V273 M136 295 V391')+text(91,206,'3rd Axis','end')+text(143,208,'α3')+text(90,345,'2nd Axis','end')+text(145,339,'α2')+dot(134,208)+dot(136,340)+dot(111,407)+dot(282,162),
5:line('M155 181 L295 133 M159 187 L111 165 M133 208 V257')+text(95,151,'4th Axis','end')+text(142,258,'α4')+text(289,143,'α5')+text(212,247,'5th Axis')+dot(134,208)+dot(136,340)+dot(111,407)+dot(282,162),
6:line('M247 168 L220 151 M254 163 V122')+dot(134,208)+dot(136,340)+dot(111,407)+dot(197,190)+dot(282,162)
}
for i in range(1,7):
 p=D/f'kinematic-step-{i}.svg';old=p.read_text();data=re.search(r'href="(data:image/jpeg;base64,[^"]+)"',old)[1]
 p.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="500" height="475" viewBox="0 0 500 475"><title>Inverse kinematic model — annotated step {i}</title><svg width="500" height="475" viewBox="52 1073 1439 1368"><image width="2549" height="3300" href="{data}"/></svg><g font-family="Arial, sans-serif" font-size="10" fill="#363636">{overlays[i]}</g></svg>')
