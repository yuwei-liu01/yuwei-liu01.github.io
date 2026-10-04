// Geometric base-yaw + planar two-link IK. Tool is held vertically by wrist pitch.
export function solve(target, model) {
  const [x,y,z]=target, r=Math.hypot(x,y), dz=z+model.toolLength-model.baseHeight;
  const a=model.upperArm,b=model.forearm, c=(r*r+dz*dz-a*a-b*b)/(2*a*b);
  if(Math.abs(c)>1) return null;
  const elbow=-Math.acos(c), shoulder=Math.atan2(dz,r)-Math.atan2(b*Math.sin(elbow),a+b*Math.cos(elbow));
  const yaw=Math.atan2(y,x), wrist=-Math.PI/2-shoulder-elbow;
  const point=(rad,height)=>[Math.cos(yaw)*rad,Math.sin(yaw)*rad,height];
  const base=[0,0,model.baseHeight];
  const joint=point(a*Math.cos(shoulder),model.baseHeight+a*Math.sin(shoulder));
  const tip=point(a*Math.cos(shoulder)+b*Math.cos(shoulder+elbow),model.baseHeight+a*Math.sin(shoulder)+b*Math.sin(shoulder+elbow));
  return {angles:[yaw,shoulder,elbow,wrist],points:[base,joint,tip,[tip[0],tip[1],tip[2]-model.toolLength]]};
}
export function mapPoint(p,pattern,model) {
 const xs=pattern.frame.map(p=>p[0]),ys=pattern.frame.map(p=>p[1]);
 return [model.frameOrigin[0]+(p[0]-Math.min(...xs))/(Math.max(...xs)-Math.min(...xs))*model.frameSize[0],model.frameOrigin[1]+(p[1]-Math.min(...ys))/(Math.max(...ys)-Math.min(...ys))*model.frameSize[1],model.frameOrigin[2]];
}
