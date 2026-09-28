"""Redraw the environment-localization subset of the supplied workshop diagram.
Only editable SVG geometry and text; no embedded screenshots or raster artwork.
Run with Python 3. Optional preview: cairosvg.svg2png(url=..., write_to=...).
"""
from pathlib import Path
from html import escape
OUT = Path(__file__).resolve().parent
parts = ['''<svg xmlns="http://www.w3.org/2000/svg" width="680" height="880" viewBox="0 0 680 880" role="img" aria-labelledby="title desc">
<title id="title">Environment localization and spatial planning concepts</title>
<desc id="desc">Redrawn from the team workshop diagram. Left: LiDAR, SLAM mapping, indoor map, scan matching, mobile-base localization. Right: spatial point clouds, RViz visualization, electronic fence, and path planning. These are documented functional concepts, not measured results or a verified software implementation.</desc>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M2 1 L7 5 L2 9" fill="none" stroke="#84979f" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<style>text{font-family:Arial,Helvetica,sans-serif;fill:#283b46}.label{font-size:24px;font-weight:600}.sub{font-size:20px;fill:#607680}.heading{font-size:18px;font-weight:700;letter-spacing:1.3px}.icon{fill:none;stroke:#68838f;stroke-width:2.5;stroke-linecap:round;stroke-linejoin:round}.flow{fill:none;stroke:#84979f;stroke-width:2;stroke-dasharray:2 7;stroke-linecap:round;marker-end:url(#arrow)}</style>
<rect width="680" height="880" rx="12" fill="#fff"/>
<rect x="20" y="20" width="312" height="840" rx="12" fill="#f2f5f6"/>
<rect x="348" y="20" width="312" height="840" rx="12" fill="#f6f6f3"/>
<text class="heading" x="176" y="55" text-anchor="middle">MAPPING &amp; LOCALIZATION</text>
<text class="heading" x="504" y="55" text-anchor="middle">SPATIAL PLANNING</text>''']
icons = {
'lidar': '<circle r="33"/><path d="M-7-19 A21 21 0 1 0 21 2 M0 0V-33 M0 0L29-17"/><path d="M4-31 A32 32 0 0 1 28-17 L4-3Z" fill="#dce6e9" stroke="none"/><circle r="3" fill="#68838f"/>',
'map': '<path d="M-34-18 L-12-26 12-17 34-25 V26 L12 34-12 25-34 33Z M-12 4V25 M12-17V34"/><path d="M-12-4 C-31-26-21-39-12-39 C0-39 9-26-12-4Z" fill="#f2f5f6"/><circle cx="-12" cy="-26" r="4"/>',
'match': '<path d="M-32-13V-30H-15 M15-30H32V-13 M32 13V30H15 M-15 30H-32V13 M-22 0H22 M0-22V22"/><circle r="10" stroke-dasharray="2 5"/><circle r="3" fill="#68838f"/>',
'base': '<rect x="-35" y="-32" width="70" height="64" rx="13"/><path d="M-22-15H22 M-22 15H22 M-20-15V15 M20-15V15 M0-15V15"/><g fill="#f2f5f6"><rect x="-27" y="-22" width="12" height="20" rx="3"/><rect x="15" y="-22" width="12" height="20" rx="3"/><rect x="-27" y="4" width="12" height="20" rx="3"/><rect x="15" y="4" width="12" height="20" rx="3"/></g><circle r="5"/>',
'cloud': '<path d="M0-34 L33-16 V22 L0 38-33 22V-16Z M-33-16L0 1 33-16 M0 1V38"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="2" fill="#68838f" stroke="none"/>' for x,y in [(-10,-17),(2,-24),(13,-15),(-21,0),(-11,9),(-23,17),(12,7),(24,2),(15,24)]),
'rviz': '<path d="M-30-25V30H32 M-30 30L-9 9"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="2" fill="#68838f" stroke="none"/>' for x,y in [(-16,5),(-10,-5),(-4,0),(3,-14),(8,-3),(16,-15),(24,-9),(19,4),(25,13),(7,13),(-4,14),(-17,17),(13,20),(-8,-14),(2,-23),(12,-26)]),
'fence': '<path d="M-30-20L26-29 32 24-16 34Z" stroke-dasharray="5 5"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="#f6f6f3"/>' for x,y in [(-30,-20),(26,-29),(32,24),(-16,34)]),
'path': '<path d="M-31-29H31V30H-31Z" stroke="#c2cdcf"/><path d="M-20 20L-5 4H9L20-17"/><path d="M13-16L21-20 23-11"/><circle cx="-20" cy="20" r="4" fill="#f6f6f3"/><path d="M-15-16H-2V-4H-15Z M10 13H24V25H10Z" fill="#e3e9e8" stroke="none"/>'
}
def label(x,y,lines,cls='label'):
    for i,line in enumerate(lines): parts.append(f'<text x="{x}" y="{y+i*27}" class="{cls}" text-anchor="middle">{escape(line)}</text>')
def node(x,y,icon,lines,sub=None):
    parts.append(f'<g class="icon" transform="translate({x} {y})">{icons[icon]}</g>')
    label(x,y+64,lines)
    if sub: label(x,y+64+len(lines)*27,sub,'sub')
def arrow(x,y1,y2,note=None):
    parts.append(f'<path class="flow" d="M{x} {y1}V{y2}"/>')
    if note:
        parts.append(f'<rect x="{x-89}" y="{(y1+y2)/2-16}" width="178" height="29" rx="6" fill="#f2f5f6"/>')
        label(x,(y1+y2)/2+5,[note],'sub')
for x,items in [(176,[('lidar',['LiDAR']),('map',['Indoor map']),('match',['Scan matching']),('base',['Mobile-base','localization'])]),(504,[('cloud',['Spatial point clouds']),('rviz',['Point-cloud view']),('fence',['Electronic fence']),('path',['Path planning'])])]:
    for i,(icon,lines) in enumerate(items):
        y=120+i*210
        node(x,y,icon,lines, ['RViz'] if icon=='rviz' else None)
        if i<3: arrow(x,y+(128 if icon=='rviz' else 90),y+165,'SLAM mapping' if icon=='lidar' else None)
parts.append('</svg>')
(OUT/'environment-localization.svg').write_text('\n'.join(parts))
print(OUT/'environment-localization.svg')
