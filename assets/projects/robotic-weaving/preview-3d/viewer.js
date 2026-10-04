import {solve,mapPoint} from './kinematics.js';
const host=document.querySelector('#weaving-3d');
async function init(){
 const [model,data]=await Promise.all([fetch(new URL('./model.json',import.meta.url)).then(r=>r.json()),fetch(new URL('../toolpaths.json?v=corrected-anchors-3',import.meta.url),{cache:'no-store'}).then(r=>r.json())]);
 const pattern=data.patterns.find(p=>p.id==='III');
 const pts=pattern.anchors.map(a=>mapPoint(a.point,pattern,model));
 const canvas=host.querySelector('canvas'),ctx=canvas.getContext('2d'),play=host.querySelector('[data-play]'),slider=host.querySelector('[data-progress]'),status=host.querySelector('output');
 let progress=0,playing=false,az=-.9,elev=.62,zoom=1,previous=null,drag=null,raf=null;
 const project=p=>{const x=p[0]-130,y=p[1],z=p[2]-60;const u=Math.cos(az)*x-Math.sin(az)*y,v=Math.sin(az)*x+Math.cos(az)*y;const scale=Math.min(canvas.clientWidth/430,canvas.clientHeight/300)*zoom;return [canvas.clientWidth/2+u*scale,canvas.clientHeight/2+(Math.sin(elev)*v-Math.cos(elev)*z)*scale];};
 function line(a,b,color,width=1,dash=[]){const A=project(a),B=project(b);ctx.beginPath();ctx.setLineDash(dash);ctx.strokeStyle=color;ctx.lineWidth=width;ctx.moveTo(...A);ctx.lineTo(...B);ctx.stroke();ctx.setLineDash([]);}
 function dot(p,color,r=4){ctx.beginPath();ctx.fillStyle=color;ctx.arc(...project(p),r,0,Math.PI*2);ctx.fill();}
 function label(p,text,color='#687c8d'){ctx.fillStyle=color;ctx.font='12px system-ui';const a=project(p);ctx.fillText(text,a[0]+7,a[1]-7);}
 function render(){
  const w=canvas.clientWidth,h=canvas.clientHeight,dpr=devicePixelRatio||1;
  if(canvas.width!==Math.round(w*dpr)||canvas.height!==Math.round(h*dpr)){canvas.width=Math.round(w*dpr);canvas.height=Math.round(h*dpr);}
  ctx.setTransform(dpr,0,0,dpr,0,0);ctx.clearRect(0,0,w,h);ctx.fillStyle='#f3f6f8';ctx.fillRect(0,0,w,h);
  for(let i=-150;i<=350;i+=25){line([i,-150,0],[i,150,0],'#e0e7ec');line([-100,i,0],[350,i,0],'#e0e7ec');}
  const frame=pattern.frame.map(p=>mapPoint(p,pattern,model));frame.forEach((p,i)=>line(p,frame[(i+1)%4],'#bba887',5));
  if(host.querySelector('[data-reference]').checked)(pattern.referenceSegments||[]).forEach(([a,b])=>line(mapPoint(a,pattern,model),mapPoint(b,pattern,model),'#cbd4da',.7));
  const n=pattern.moves.length,t=progress*n,index=Math.min(Math.floor(t),n-1),f=progress===1?1:t-index;
  pattern.moves.forEach((m,i)=>{if(i<index||i===index&&progress===1)line(pts[m.from],pts[m.to],'#41998f',2);});
  const m=pattern.moves[index],a=pts[m.from],b=pts[m.to],target=a.map((v,i)=>v+(b[i]-v)*f);
  line(a,target,'#41998f',2);pts.forEach(p=>dot(p,'#899ba5',2));
  const pose=solve(target,model);
  for(const [end,c,name] of [[[42,0,0],'#c46c68','X'],[[0,42,0],'#65a17a','Y'],[[0,0,42],'#6a8fc0','Z']]){line([0,0,0],end,c,2);label(end,name,c);}
  line([-23,0,5],[23,0,5],'#667780',14);line([0,0,5],[0,0,model.baseHeight],'#7e8e98',16);
  if(pose){const q=pose.points;line(q[0],q[1],'#bdc8cf',14);line(q[0],q[1],'#657b89',3);line(q[1],q[2],'#bdc8cf',12);line(q[1],q[2],'#657b89',3);line(q[2],q[3],'#6b737a',3);q.slice(0,3).forEach(p=>{dot(p,'#405e71',8);dot(p,'#d1dce2',3);});
   host.querySelector('[data-angles]').textContent=pose.angles.map((v,i)=>`${['Base','Shoulder','Elbow','Wrist'][i]} ${(v*180/Math.PI).toFixed(1)}°`).join(' · ');
  }
  dot(b,'#a280c0',5);dot(target,'#e8a349',5);label(target,'TCP','#8a652d');
  status.textContent=pose?`Step ${progress===1?n:index+1} / ${n} · ${pattern.anchors[m.from].id} → ${pattern.anchors[m.to].id}`:'Target outside simplified arm reach';
  slider.value=Math.round(progress*1000);play.textContent=playing?'Pause':progress===1?'Replay':'Play';
 }
 function tick(time){if(playing&&previous!==null)progress=Math.min(1,progress+Math.min(time-previous,100)/1000/model.durationSeconds*Number(host.querySelector('[data-speed]').value));previous=time;if(progress===1)playing=false;render();raf=playing?requestAnimationFrame(tick):null;if(!playing)previous=null;}
 function start(){if(raf===null)raf=requestAnimationFrame(tick);}
 play.onclick=()=>{if(progress===1)progress=0;playing=!playing;previous=null;render();if(playing)start();};
 host.querySelector('[data-reset]').onclick=()=>{playing=false;progress=0;previous=null;render();};
 slider.oninput=()=>{progress=Number(slider.value)/1000;render();};
 host.querySelector('[data-home]').onclick=()=>{az=-.9;elev=.62;zoom=1;render();};
 host.querySelector('[data-reference]').onchange=render;
 canvas.onpointerdown=e=>{drag=[e.clientX,e.clientY];canvas.setPointerCapture(e.pointerId);};
 canvas.onpointermove=e=>{if(!drag)return;az+=(e.clientX-drag[0])*.008;elev=Math.max(.15,Math.min(1.4,elev+(e.clientY-drag[1])*.006));drag=[e.clientX,e.clientY];render();};
 canvas.onpointerup=canvas.onpointercancel=()=>drag=null;
 canvas.onwheel=e=>{e.preventDefault();zoom=Math.max(.6,Math.min(2,zoom-e.deltaY*.001));render();};
 canvas.onkeydown=e=>{if(['ArrowLeft','ArrowRight','ArrowUp','ArrowDown'].includes(e.key)){e.preventDefault();az+=e.key==='ArrowLeft'?-.1:e.key==='ArrowRight'?.1:0;elev=Math.max(.15,Math.min(1.4,elev+(e.key==='ArrowUp'?.1:e.key==='ArrowDown'?-.1:0)));render();}};
 new ResizeObserver(render).observe(canvas);document.addEventListener('visibilitychange',()=>{if(document.hidden){playing=false;render();}});render();host.querySelectorAll('button,input,select').forEach(e=>e.disabled=false);
}
init().catch(e=>{host.querySelector('output').textContent='Preview could not load: '+e.message;});
