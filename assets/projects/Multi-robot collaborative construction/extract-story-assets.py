from pathlib import Path
import copy,re,xml.etree.ElementTree as E
src=Path(__file__).resolve().parent/'system-overview-hd.svg'
out=Path(__file__).resolve().parent
E.register_namespace('','http://www.w3.org/2000/svg');E.register_namespace('xlink','http://www.w3.org/1999/xlink')
r=E.parse(src).getroot();items=[e for e in r.iter() if e.tag.endswith('}svg')][1:]
for idx,name in [(0,'structure-model'),(1,'assembly-action-a'),(2,'assembly-action-b'),(3,'assembly-action-c'),(4,'workspace-study'),(13,'end-effector-detail')]:
 e=copy.deepcopy(items[idx]);e.attrib.pop('x',None);e.attrib.pop('y',None)
 w,h=map(float,e.get('viewBox').split()[2:]);e.set('width',str(round(w)));e.set('height',str(round(h)))
 text=E.tostring(e,encoding='unicode');ids={x.get('id') for x in e.iter() if x.get('id')}
 refs=set(re.findall(r'url\(#([^)]*)\)',text))
 assert refs<=ids,(name,refs-ids)
 (out/f'{name}.svg').write_text(text)
 print(name,round(w),round(h),len(text))
