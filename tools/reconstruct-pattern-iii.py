"""Pattern III: user-annotated anchor family and continuous serpentine visit rule.
Coordinates sampled from the annotated reference; not calibrated robot targets.
"""
import json
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]/'assets/projects/robotic-weaving'
# Pixel positions in the user's 722px-wide annotated image. Preserve its aspect ratio.
left=[(138,89),(96,89),(80,115),(80,155),(80,196),(80,237),(80,278)]
bottom=[(223,538),(246,538),(270,538),(293,538),(317,538),(341,538),(364,538)]
def point(p):return [round(32+(p[0]-80)*256/568,3),round(55+(p[1]-89)*256/568,3)]
anchors=[{'id':f'({edge},{i})','point':point(p)} for edge,ps in [(0,left),(3,bottom)] for i,p in enumerate(ps)]
# User explicitly supplies 06 → 36 → 35 → 05; continue the same alternating rule.
order=[]
for i in range(6,-1,-1):order.extend([i,7+i] if i%2==0 else [7+i,i])
moves=[{'from':a,'to':b,'kind':'weave'} for a,b in zip(order,order[1:])]
pattern={'id':'III','name':'Weaving Pattern III','source':'User-annotated Pattern III reference, codex-clipboard-9545fc1d-889f-4562-a978-d24aad1b47e0.png','provenance':'User-specified 06 → 36 → 35 → 05 sequence, extended by the same alternating rule. Anchor locations sampled from annotation; not original robot instructions. Boundary links retain thread; no lift or wrap simulated.','coordinateSpace':'Approximate normalized 2D coordinates sampled from annotated image.','frame':[point(p) for p in [(80,89),(648,89),(648,538),(80,538)]],'anchors':anchors,'chords':[[m['from'],m['to']] for m in moves],'moves':moves,'showAnchorLabels':False,'visitOrder':[anchors[i]['id'] for i in order]}
# Keep the complete original composition separate from the animated subset.
source=json.loads((OUT/'pattern-III-source.json').read_text())
def landscape(pt):
 return [round(320-pt[1],3),round(55+(pt[0]-32)*449/568,3)]
pattern['referenceSegments']=[[landscape(source['anchors'][a]['point']),landscape(source['anchors'][b]['point'])] for a,b in source['chords']]
pattern['referenceAnchors']=[landscape(a['point']) for a in source['anchors']]
p=json.loads((OUT/'toolpaths.json').read_text())
p['patterns']=[pattern if x['id']=='III' else x for x in p['patterns']]
for item in p['patterns']:
 if item['id'] not in ('I','II'):continue
 # Chords retain the full original figure. Only moves are limited to one half.
 chosen=item['chords'][:len(item['chords'])//2]
 item['animatedChordIndices']=list(range(len(chosen)))
 item['moves']=[];last=None
 for a,b in chosen:
  if last is not None and last!=a:item['moves'].append({'from':last,'to':a,'kind':'travel'})
  item['moves'].append({'from':a,'to':b,'kind':'weave'});last=b
(OUT/'toolpaths.json').write_text(json.dumps(p,indent=2)+'\n')
