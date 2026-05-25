/* ════════════════════════════════════════════
   ASSANE PORTFOLIO — main.js
════════════════════════════════════════════ */

/* ── 1. Navbar : ombre au scroll ── */
const nav = document.getElementById('mainNav');
window.addEventListener('scroll', () => {
  nav.classList.toggle('scrolled', window.scrollY > 30);
}, { passive: true });

/* ── 2. Lien actif selon la section visible ── */
const sections = document.querySelectorAll('section[id]');
const navLinks  = document.querySelectorAll('.nav-lk');

const sectionObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    const id = entry.target.id;
    navLinks.forEach(lk => {
      lk.classList.toggle('active', lk.getAttribute('href') === '#' + id);
    });
  });
}, { rootMargin: '-40% 0px -55% 0px' });

sections.forEach(s => sectionObserver.observe(s));

/* ── 3. Fermer le menu mobile au clic sur un lien ── */
const navCollapse = document.getElementById('navMenu');
if (navCollapse) {
  navLinks.forEach(lk => {
    lk.addEventListener('click', () => {
      const bsCollapse = bootstrap.Collapse.getInstance(navCollapse);
      if (bsCollapse) bsCollapse.hide();
    });
  });
}

/* ── 4. Animation d'apparition au scroll ── */
const revealEls = document.querySelectorAll(
  '.pcard, .stack-card, .cert-row, .tl-item, .client-box, .about-main-photo'
);

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('revealed');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

/* Appliquer état initial puis observer */
revealEls.forEach((el, i) => {
  el.style.opacity  = '0';
  el.style.transform = 'translateY(22px)';
  el.style.transition = `opacity .5s ease ${(i % 6) * 70}ms, transform .5s ease ${(i % 6) * 70}ms`;
  revealObserver.observe(el);
});

/* Classe revealed = visible */
document.head.insertAdjacentHTML('beforeend', `
  <style>
    .revealed { opacity: 1 !important; transform: translateY(0) !important; }
  </style>
`);

/* ── 5. Feedback bouton formulaire contact ── */
const contactForm = document.getElementById('contactForm');
if (contactForm) {
  contactForm.addEventListener('submit', function () {
    const btn = this.querySelector('.btn-submit');
    if (!btn) return;
    btn.textContent = 'Envoi en cours…';
    btn.style.opacity = '0.7';
    btn.disabled = true;
  });
}
