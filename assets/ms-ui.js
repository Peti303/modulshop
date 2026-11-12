/**
 * Modulshop – light/dark mode switch.
 * Switches html[data-theme] with a circular "reveal" animation that grows from the
 * clicked switch (View Transitions API), falling back to a soft colour cross-fade.
 */
const STORAGE_KEY = 'ms-theme';
const root = document.documentElement;
const media = window.matchMedia('(prefers-color-scheme: dark)');

const getTheme = () => (root.getAttribute('data-theme') === 'dark' ? 'dark' : 'light');

function readStored() {
  try {
    const value = localStorage.getItem(STORAGE_KEY);
    return value === 'light' || value === 'dark' ? value : null;
  } catch {
    return null;
  }
}

function store(theme) {
  try {
    localStorage.setItem(STORAGE_KEY, theme);
  } catch {
    /* storage unavailable (private mode) – the choice lasts for this page only */
  }
}

function syncThemeColorMeta() {
  const color = getComputedStyle(root).getPropertyValue('--ms-bg').trim();
  if (!color) return;
  let meta = document.querySelector('meta[name="theme-color"]');
  if (!meta) {
    meta = document.createElement('meta');
    meta.name = 'theme-color';
    document.head.append(meta);
  }
  meta.content = color;
}

function apply(theme) {
  root.setAttribute('data-theme', theme);
  root.style.colorScheme = theme;
  document.querySelectorAll('ms-theme-toggle').forEach((el) => el.sync());
  syncThemeColorMeta();
  document.dispatchEvent(new CustomEvent('ms:theme-change', { detail: { theme } }));
}

const reducedMotion = () => window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/**
 * @param {string} theme
 * @param {{x:number,y:number}} [origin] viewport coordinates the reveal grows from
 */
function switchTheme(theme, origin) {
  if (theme === getTheme()) return;

  if (reducedMotion()) {
    apply(theme);
    return;
  }

  if (!document.startViewTransition) {
    root.classList.add('ms-theme-fade');
    apply(theme);
    window.setTimeout(() => root.classList.remove('ms-theme-fade'), 450);
    return;
  }

  const x = origin?.x ?? window.innerWidth - 40;
  const y = origin?.y ?? 40;
  const radius = Math.hypot(Math.max(x, window.innerWidth - x), Math.max(y, window.innerHeight - y));

  root.classList.add('ms-vt-theme');
  const transition = document.startViewTransition(() => apply(theme));

  transition.ready
    .then(() => {
      root.animate(
        { clipPath: [`circle(0px at ${x}px ${y}px)`, `circle(${radius}px at ${x}px ${y}px)`] },
        { duration: 650, easing: 'cubic-bezier(0.65, 0, 0.35, 1)', pseudoElement: '::view-transition-new(root)' }
      );
    })
    .catch(() => {});

  transition.finished.finally(() => root.classList.remove('ms-vt-theme'));
}

class MsThemeToggle extends HTMLElement {
  connectedCallback() {
    this.button = this.querySelector('button');
    this.button?.addEventListener('click', this.#onClick);
    this.sync();
  }

  disconnectedCallback() {
    this.button?.removeEventListener('click', this.#onClick);
  }

  sync() {
    const dark = getTheme() === 'dark';
    this.button?.setAttribute('aria-checked', String(dark));
    this.toggleAttribute('data-dark', dark);
  }

  #onClick = (event) => {
    const next = getTheme() === 'dark' ? 'light' : 'dark';
    const rect = this.button.getBoundingClientRect();
    const origin =
      event.clientX || event.clientY
        ? { x: event.clientX, y: event.clientY }
        : { x: rect.left + rect.width / 2, y: rect.top + rect.height / 2 };
    store(next);
    switchTheme(next, origin);
  };
}

if (!customElements.get('ms-theme-toggle')) customElements.define('ms-theme-toggle', MsThemeToggle);

// Follow the operating system setting until the visitor makes an explicit choice.
media.addEventListener('change', (event) => {
  if (!readStored()) switchTheme(event.matches ? 'dark' : 'light');
});

syncThemeColorMeta();

// Scroll reveal for elements marked .ms-reveal
const revealTargets = () => document.querySelectorAll('.ms-reveal:not(.is-visible)');
if ('IntersectionObserver' in window) {
  const io = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      }
    },
    { rootMargin: '0px 0px -8% 0px', threshold: 0.08 }
  );
  const observeAll = () => revealTargets().forEach((el) => io.observe(el));
  observeAll();
  document.addEventListener('shopify:section:load', observeAll);
  // Safety net: never leave content hidden (e.g. jump links, print, unusual scroll containers)
  window.addEventListener('load', () => {
    window.setTimeout(() => {
      revealTargets().forEach((el) => {
        if (el.getBoundingClientRect().top < window.innerHeight * 1.5) el.classList.add('is-visible');
      });
    }, 1200);
  });
  window.addEventListener('beforeprint', () => revealTargets().forEach((el) => el.classList.add('is-visible')));
} else {
  revealTargets().forEach((el) => el.classList.add('is-visible'));
}
