"""Extract original PDF chord geometry. Sequence is illustrative, NOT robot code.
Usage: python extract-weaving-data.py "/path/to/OP2-Mechanical Arm"
Requires pypdf. Does not modify the source files.
"""
from pathlib import Path
import json, math, sys
from pypdf import PdfReader

def mul(a,b):
    A,B,C,D,E,F=a;g,h,i,j,k,l=b
    return [A*g+C*h,B*g+D*h,A*i+C*j,B*i+D*j,A*k+C*l+E,B*k+D*l+F]

def extract(page):
    c=[1,0,0,1,0,0];stack=[];path=[];pos=None;lines=[]
    def xy(v):
        x,y=map(float,v);a,b,d,e,f,g=c
        return [a*x+d*y+f,b*x+e*y+g]
    for args,op in page.get_contents().operations:
        if op==b'q': stack.append(c[:])
        elif op==b'Q': c=stack.pop()
        elif op==b'cm': c=mul(c,list(map(float,args)))
        elif op==b'm':pos=xy(args)
        elif op==b'l':
            end=xy(args);path.append([pos,end]);pos=end
        elif op==b'c':pos=xy(args[-2:])
        elif op in [b'S',b's',b'B',b'B*',b'b',b'b*']:lines+=path;path=[]
        elif op in [b'n',b'f',b'f*']:path=[]
    return lines

source=Path(sys.argv[1]);out=Path(__file__).resolve().parents[1]/'assets/projects/robotic-weaving'
patterns=[]
for numeral,pdf,bounds in [('I','M2',(198.6091,121.604,636.9061,501.18)),('II','M3',(240.10489,71.61505,597.59906,523.18665)),('III','M1',(177.2645,72.9238,534.7587,524.4955))]:
    x0,y0,x1,y1=bounds
    def normalize(p):
        x,y=(p[0]-x0)/(x1-x0),(p[1]-y0)/(y1-y0)
        if numeral=='II':x,y=y,1-x # rotate the source C-shaped drawing clockwise
        if numeral=='I':return [round(32+256*x,3),round(270-221.7*y,3)]
        return [round(32+256*x,3),round(288-256*y,3)]
    frame=[[32,270],[288,270],[160,48.3]] if numeral=='I' else [[32,32],[288,32],[288,288],[32,288]]
    def edge(p):
        found=set()
        for i,a in enumerate(frame):
            b=frame[(i+1)%len(frame)];dx,dy=b[0]-a[0],b[1]-a[1]
            if abs(dx*(p[1]-a[1])-dy*(p[0]-a[0]))/math.hypot(dx,dy)<.03: found.add(i)
        return found
    anchors=[]
    def anchor(p):
        for i,q in enumerate(anchors):
            if math.dist(p,q['point'])<.03:return i
        anchors.append({'id':f'A{len(anchors)+1:02d}','point':p});return len(anchors)-1
    chords=[];seen=set()
    for raw in extract(PdfReader(source/'素材'/f'{pdf}.pdf').pages[0]):
        a,b=map(normalize,raw)
        if any(min(p)<31.97 or max(p)>288.03 for p in [a,b]):continue
        ea,eb=edge(a),edge(b)
        if not ea or not eb:continue
        ia,ib=anchor(a),anchor(b)
        if ea&eb or ia==ib:continue # frame-following strokes are not interior threads
        key=tuple(sorted([ia,ib]))
        if key in seen:continue
        seen.add(key);chords.append([ia,ib])
    # Retain source chord order only for reproducibility, not as a motion claim.
    # Each gap is an explicitly schematic non-weaving reposition.
    moves=[];last=None
    for a,b in chords:
        if last is not None and last!=a:moves.append({'from':last,'to':a,'kind':'travel'})
        moves.append({'from':a,'to':b,'kind':'weave'});last=b
    patterns.append({'id':numeral,'name':f'Weaving Pattern {numeral}', 'source':f'素材/{pdf}.pdf',
        'provenance':'Original PDF vector endpoints; reconstructed visitation sequence.',
        'coordinateSpace':'Normalized 2D drawing coordinates, not calibrated TCP positions.',
        'frame':frame,'anchors':anchors,'chords':chords,'moves':moves})
    print(numeral,len(anchors),'anchors',len(chords),'chords',len(moves),'steps')
(out/'toolpaths.json').write_text(json.dumps({'version':1,'patterns':patterns},indent=2)+'\n')

# Apply the user correction: M1 is a multi-unit composition, not the single unit.
import runpy
runpy.run_path(str(Path(__file__).with_name("reconstruct-pattern-iii.py")), run_name="__main__")
