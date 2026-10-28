// Native anchor navigation and video controls keep the project page usable
// without JavaScript. Highlight the current section for keyboard and pointer users.
const links = [...document.querySelectorAll('.section-nav a')];
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        links.forEach(link => {
          if (link.hash === '#' + entry.target.id) link.setAttribute('aria-current', 'location');
          else link.removeAttribute('aria-current');
        });
      }
    });
  }, {rootMargin: '-8% 0px -65% 0px'});
  document.querySelectorAll('section[id]').forEach(section => observer.observe(section));
}
