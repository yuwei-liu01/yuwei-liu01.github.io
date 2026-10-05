// Back-to-top button behavior
const backToTopButton = document.getElementById('back-to-top');

if (backToTopButton) {
  window.addEventListener('scroll', () => {
    if (window.scrollY > 420) {
      backToTopButton.classList.add('show');
    } else {
      backToTopButton.classList.remove('show');
    }
  });

  backToTopButton.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

// Shared in-page viewer for links to image assets.
(() => {
  const dialog = document.createElement('dialog');
  dialog.className = 'image-viewer';
  dialog.setAttribute('aria-label', 'Image preview');
  dialog.innerHTML = `<div class="image-viewer-toolbar">
    <button type="button" data-action="out" aria-label="Zoom out">−</button>
    <button type="button" data-action="reset">Fit</button>
    <button type="button" data-action="in" aria-label="Zoom in">+</button>
    <button type="button" data-action="close" aria-label="Close image preview">×</button>
  </div><div class="image-viewer-stage"><img draggable="false" alt=""></div>
  <p class="image-viewer-hint" role="status">Scroll to zoom · Drag to move · Esc to close</p>`;
  document.body.append(dialog);
  const stage = dialog.querySelector('.image-viewer-stage');
  const img = stage.querySelector('img');
  const hint = dialog.querySelector('.image-viewer-hint');
  const pointers = new Map();
  let scale = 1, x = 0, y = 0, opener, oldOverflow;
  const draw = () => { img.style.transform = `translate(${x}px, ${y}px) scale(${scale})`; };
  const reset = () => { scale = 1; x = y = 0; draw(); };
  const zoom = (factor, px = 0, py = 0) => {
    const next = Math.max(1, Math.min(8, scale * factor));
    const ratio = next / scale;
    x = px - (px - x) * ratio; y = py - (py - y) * ratio;
    scale = next;
    if (scale === 1) x = y = 0;
    draw();
  };
  const center = () => {
    const r = stage.getBoundingClientRect();
    return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
  };
  document.addEventListener('click', event => {
    const link = event.target.closest('a[href]');
    if (!link || link.hasAttribute('download') || event.button !== 0 || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
    const url = new URL(link.href, location.href);
    if (!/\.(png|jpe?g|webp|gif|svg|avif)$/i.test(url.pathname) || url.origin !== location.origin) return;
    event.preventDefault();
    opener = link; oldOverflow = document.body.style.overflow;
    pointers.clear(); reset();
    img.alt = link.querySelector('img')?.alt || link.getAttribute('aria-label') || 'Full-size image';
    hint.textContent = 'Scroll or pinch to zoom · Drag to move · Esc to close';
    img.src = url.href;
    dialog.showModal(); document.body.style.overflow = 'hidden';
    dialog.querySelector('[data-action="close"]').focus();
  });
  img.addEventListener('error', () => { hint.textContent = 'Image could not be loaded. Close and try again.'; });
  dialog.addEventListener('close', () => {
    pointers.clear(); document.body.style.overflow = oldOverflow || '';
    img.removeAttribute('src'); opener?.focus();
  });
  dialog.addEventListener('click', event => {
    const action = event.target.closest('[data-action]')?.dataset.action;
    if (action === 'close') dialog.close();
    if (action === 'reset') reset();
    if (action === 'in') zoom(1.25);
    if (action === 'out') zoom(0.8);
    if (event.target === dialog) dialog.close();
  });
  stage.addEventListener('wheel', event => {
    event.preventDefault();
    const c = center();
    const delta = event.deltaY * (event.deltaMode === 1 ? 16 : event.deltaMode === 2 ? stage.clientHeight : 1);
    zoom(Math.exp(-Math.max(-200, Math.min(200, delta)) * 0.003), event.clientX - c.x, event.clientY - c.y);
  }, { passive: false });
  stage.addEventListener('pointerdown', event => {
    if (event.pointerType === 'mouse' && event.button !== 0) return;
    pointers.set(event.pointerId, {x:event.clientX, y:event.clientY});
    stage.setPointerCapture(event.pointerId);
  });
  stage.addEventListener('pointermove', event => {
    const previous = pointers.get(event.pointerId);
    if (!previous) return;
    const before = [...pointers.values()];
    pointers.set(event.pointerId, {x:event.clientX, y:event.clientY});
    const after = [...pointers.values()];
    if (after.length === 2) {
      const mid = a => ({x:(a[0].x+a[1].x)/2,y:(a[0].y+a[1].y)/2});
      const distance = a => Math.hypot(a[0].x-a[1].x,a[0].y-a[1].y);
      const a = mid(before), b = mid(after), c = center();
      if (distance(before) > 0) zoom(distance(after)/distance(before),a.x-c.x,a.y-c.y);
      if (scale > 1) { x += b.x-a.x; y += b.y-a.y; draw(); }
    } else if (after.length === 1 && scale > 1) {
      x += event.clientX-previous.x; y += event.clientY-previous.y; draw();
    }
  });
  for (const name of ['pointerup','pointercancel','lostpointercapture']) stage.addEventListener(name,event=>pointers.delete(event.pointerId));
  window.addEventListener('resize', () => { if (dialog.open) reset(); });
})();
