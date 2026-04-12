// Theme toggle with dark default and persistent user choice
const themeToggle = document.getElementById('theme-toggle');
const savedTheme = localStorage.getItem('theme');

if (savedTheme === 'light') {
  document.body.classList.add('light');
  if (themeToggle) themeToggle.textContent = '☾';
} else {
  // Default is dark
  document.body.classList.remove('light');
  if (themeToggle) themeToggle.textContent = '☀';
}

if (themeToggle) {
  themeToggle.addEventListener('click', () => {
    document.body.classList.toggle('light');
    const isLight = document.body.classList.contains('light');
    themeToggle.textContent = isLight ? '☾' : '☀';
    localStorage.setItem('theme', isLight ? 'light' : 'dark');
  });
}

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
