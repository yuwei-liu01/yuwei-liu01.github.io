// Rendering and interaction only. Geometry and movement types live in toolpaths.json.
const NS = 'http://www.w3.org/2000/svg';
const svgNode = (tag, attrs = {}) => {
  const node = document.createElementNS(NS, tag);
  Object.entries(attrs).forEach(([name, value]) => node.setAttribute(name, value));
  return node;
};
const clamp = value => Math.max(0, Math.min(1, value));
const players = [];
let raf = null;
let lastTime = null;
let speed = 1;
const duration = 35000; // Presentation time only, never a robot execution time.

function requestFrame() {
  if (raf === null && players.some(p => p.playing)) raf = requestAnimationFrame(tick);
}
function tick(time) {
  raf = null;
  const elapsed = lastTime === null ? 0 : Math.min(time - lastTime, 100);
  lastTime = time;
  players.forEach(p => {
    if (!p.playing) return;
    p.progress = clamp(p.progress + elapsed * speed / duration);
    if (p.progress >= 1) p.playing = false;
    p.render();
  });
  if (players.some(p => p.playing)) requestFrame();
  else lastTime = null;
}

class Player {
  constructor(pattern, panel) {
    this.data = pattern;
    this.progress = 0;
    this.playing = false;
    const mount = panel.querySelector('.animation-mount');
    const prefix = `path-${pattern.id}`;
    mount.innerHTML = `<svg class="player-svg" viewBox="0 0 320 320" role="img" aria-labelledby="${prefix}-title ${prefix}-desc"></svg>
      <div class="player-controls"><button type="button" class="play" aria-label="Play pattern ${pattern.id}">Play</button><button type="button" class="reset" aria-label="Reset pattern ${pattern.id}">Reset</button></div>
      <label class="progress-label" for="${prefix}-progress">Progress</label>
      <input class="player-progress" id="${prefix}-progress" aria-label="Pattern ${pattern.id} progress" type="range" min="0" max="1000" step="1" value="0">
      <p class="player-status" role="status" aria-live="off"></p>
      <label class="reference-label"><input type="checkbox" class="reference-toggle" checked> Show full reference pattern</label>`;
    this.svg = mount.querySelector('svg');
    const title = svgNode('title', { id: `${prefix}-title` });
    title.textContent = `${pattern.name}: reconstructed endpoint animation`;
    const desc = svgNode('desc', { id: `${prefix}-desc` });
    desc.textContent = 'Gray frame and anchors, pale reference threads, teal completed threads, orange dashed repositioning, orange tool point, purple target ring and direction arrow. Movement order is illustrative.';
    this.svg.append(title, desc);
    const defs = svgNode('defs');
    const marker = svgNode('marker', { id: `${prefix}-arrow`, viewBox: '0 0 10 10', refX: 9, refY: 5, markerWidth: 5, markerHeight: 5, orient: 'auto-start-reverse' });
    marker.append(svgNode('path', { d: 'M 0 0 L 10 5 L 0 10 z', fill: '#b395df' }));
    defs.append(marker); this.svg.append(defs);
    this.svg.append(svgNode('polygon', { points: pattern.frame.map(p => p.join(',')).join(' '), fill: 'none', stroke: '#82909d', 'stroke-width': 1.3 }));
    this.reference = svgNode('g', { stroke: '#b9bfc7', opacity: .42, 'stroke-width': .75 });
    if (pattern.referenceSegments) {
      pattern.referenceSegments.forEach(([a,b]) => this.reference.append(svgNode('line', { x1:a[0], y1:a[1], x2:b[0], y2:b[1] })));
      (pattern.referenceAnchors || []).forEach(p => this.reference.append(svgNode('circle', { cx:p[0], cy:p[1], r:1.5, fill:'#82909d', stroke:'none' })));
    } else {
      pattern.chords.forEach(([a,b]) => this.reference.append(this.line(a,b)));
    }
    this.svg.append(this.reference);
    const completed = svgNode('g', { stroke: '#57aca3', 'stroke-width': 1.35, fill: 'none' });
    this.threadLines = pattern.moves.map(move => {
      if (move.kind !== 'weave') return null;
      const line = this.line(move.from, move.to); completed.append(line); return line;
    });
    this.svg.append(completed);
    const anchors = svgNode('g', { fill: '#82909d' });
    pattern.anchors.forEach(anchor => {
      const dot = svgNode('circle', { cx: anchor.point[0], cy: anchor.point[1], r: 2 });
      const name = svgNode('title'); name.textContent = anchor.id; dot.append(name); anchors.append(dot);
      if (pattern.showAnchorLabels) {
        const isBottom = anchor.id.startsWith('(3,');
        const label = svgNode('text', { x: anchor.point[0] + (isBottom ? 0 : -5), y: anchor.point[1] + (isBottom ? 14 : -5), 'font-size': 7, 'text-anchor': isBottom ? 'middle' : 'end', fill: '#536b80' });
        label.textContent = anchor.id; anchors.append(label);
      }
    });
    this.svg.append(anchors);
    this.activeLine = svgNode('line', { 'stroke-width': 1.9 });
    this.arrow = svgNode('line', { stroke: '#b395df', 'stroke-width': 1.7, 'marker-end': `url(#${prefix}-arrow)` });
    this.target = svgNode('circle', { r: 6, fill: 'none', stroke: '#b395df', 'stroke-width': 1.8 });
    this.tool = svgNode('circle', { r: 4.5, fill: '#f3b34c', stroke: '#634011', 'stroke-width': 1 });
    this.svg.append(this.activeLine, this.arrow, this.target, this.tool);
    this.playButton = mount.querySelector('.play');
    this.slider = mount.querySelector('.player-progress');
    this.status = mount.querySelector('.player-status');
    this.playButton.addEventListener('click', () => {
      if (!this.playing && this.progress === 1) this.progress = 0;
      this.playing = !this.playing; this.render(); requestFrame();
    });
    mount.querySelector('.reset').addEventListener('click', () => this.reset());
    this.slider.addEventListener('input', () => {
      this.progress = Number(this.slider.value) / 1000;
      if (this.progress === 1) this.playing = false;
      this.render();
    });
    mount.querySelector('.reference-toggle').addEventListener('change', event => {
      this.reference.style.display = event.target.checked ? '' : 'none';
    });
    this.render();
  }
  line(a,b) {
    const A = this.data.anchors[a].point, B = this.data.anchors[b].point;
    return svgNode('line', { x1: A[0], y1: A[1], x2: B[0], y2: B[1] });
  }
  reset() { this.playing = false; this.progress = 0; this.render(); }
  render() {
    const moves = this.data.moves, n = moves.length;
    const position = this.progress * n;
    const finished = this.progress === 1;
    const index = Math.min(Math.floor(position), n - 1);
    const fraction = finished ? 1 : position - index;
    const move = moves[index];
    const a = this.data.anchors[move.from], b = this.data.anchors[move.to];
    const A = a.point, B = b.point;
    const X = A.map((v,i) => v + (B[i] - v) * fraction);
    this.threadLines.forEach((line,i) => { if (line) line.style.display = i < Math.floor(position) ? '' : 'none'; });
    const setLine = (node,from,to) => {
      node.setAttribute('x1',from[0]); node.setAttribute('y1',from[1]);
      node.setAttribute('x2',to[0]); node.setAttribute('y2',to[1]);
    };
    setLine(this.activeLine, A, X);
    this.activeLine.setAttribute('stroke', move.kind === 'weave' ? '#57aca3' : '#d49a55');
    this.activeLine.setAttribute('stroke-dasharray', move.kind === 'travel' ? '5 4' : 'none');
    const dx = B[0]-A[0], dy = B[1]-A[1], length = Math.hypot(dx,dy);
    const middle = A.map((v,i) => v + (B[i]-v)*.5);
    setLine(this.arrow, [middle[0]-dx/length*9,middle[1]-dy/length*9], [middle[0]+dx/length*9,middle[1]+dy/length*9]);
    this.arrow.style.display = finished ? 'none' : '';
    this.activeLine.style.display = finished ? 'none' : '';
    this.target.setAttribute('cx',B[0]); this.target.setAttribute('cy',B[1]);
    this.tool.setAttribute('cx',X[0]); this.tool.setAttribute('cy',X[1]);
    this.slider.value = String(Math.round(this.progress * 1000));
    const step = finished ? n : this.progress === 0 ? 0 : index+1;
    const text = `Step ${step} / ${n} · ${finished ? 'Complete' : `${move.kind === 'weave' ? 'Thread' : 'Reposition'} → ${b.id}`}`;
    if (this.status.textContent !== text) this.status.textContent = text;
    this.slider.setAttribute('aria-valuetext', text);
    this.playButton.textContent = this.playing ? 'Pause' : finished ? 'Replay' : 'Play';
    this.playButton.setAttribute('aria-label', `${this.playing ? 'Pause' : finished ? 'Replay' : 'Play'} pattern ${this.data.id}`);
  }
}

function showPatterns(id) {
  document.querySelectorAll('.pattern-panel').forEach(p => { p.hidden = id !== 'all' && p.dataset.pattern !== id; });
  document.querySelector('#pattern-grid').classList.toggle('single', id !== 'all');
}
async function init() {
  const response = await fetch(new URL('./toolpaths.json?v=corrected-anchors-3', import.meta.url), { cache: 'no-store' });
  if (!response.ok) throw new Error('Pattern data could not be loaded.');
  const data = await response.json();
  data.patterns.forEach(pattern => {
    if (!pattern.moves.length || pattern.moves.some(m => !['weave','travel'].includes(m.kind) || !pattern.anchors[m.from] || !pattern.anchors[m.to] || m.from === m.to)) throw new Error('Invalid pattern data.');
    players.push(new Player(pattern, document.querySelector(`[data-pattern="${pattern.id}"]`)));
  });
  const view = document.querySelector('#pattern-view');
  document.querySelector('#play-all').addEventListener('click', () => {
    view.value = 'all'; showPatterns('all'); lastTime = null;
    players.forEach(p => { p.reset(); p.playing = true; p.render(); }); requestFrame();
  });
  document.querySelector('#pause-all').addEventListener('click', () => players.forEach(p => { p.playing = false; p.render(); }));
  document.querySelector('#reset-all').addEventListener('click', () => players.forEach(p => p.reset()));
  document.querySelector('#speed').addEventListener('change', event => { speed = Number(event.target.value); });
  view.addEventListener('change', () => { players.forEach(p => p.reset()); showPatterns(view.value); });
  document.querySelectorAll('.animation-toolbar button, .animation-toolbar select').forEach(control => { control.disabled = false; });
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) players.forEach(p => { p.playing = false; p.render(); });
    lastTime = null;
  });
}
init().catch(error => {
  const message = document.querySelector('#animation-error');
  message.hidden = false;
  message.textContent = `${error.message} The original drawings remain available. Reload this page through a local web server or GitHub Pages to retry.`;
});
