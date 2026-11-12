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

/* ==========================================================================
   „Feszültség alatt" – élő elemek
   ========================================================================== */

// Feladás-visszaszámláló: budapesti idő szerint számol a napi határidőig.
function budapestNow() {
  const parts = new Intl.DateTimeFormat('en-GB', {
    timeZone: 'Europe/Budapest', hour12: false, weekday: 'short', hour: '2-digit', minute: '2-digit', second: '2-digit',
  }).formatToParts(new Date());
  const get = (type) => parts.find((p) => p.type === type)?.value;
  const days = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 };
  return { day: days[get('weekday')], secs: (Number(get('hour')) % 24) * 3600 + Number(get('minute')) * 60 + Number(get('second')) };
}

function tickShipTimers() {
  const timers = document.querySelectorAll('[data-ms-ship-timer]');
  if (!timers.length) return;
  const now = budapestNow();
  for (const el of timers) {
    const [h, m] = (el.dataset.cutoff || '10:00').split(':').map(Number);
    const days = (el.dataset.days || '1,2,3,4,5').split(',').map(Number);
    const left = days.includes(now.day) ? h * 3600 + (m || 0) * 60 - now.secs : 0;
    const live = left > 0;
    el.querySelectorAll('[data-live]').forEach((n) => (n.hidden = !live));
    el.querySelectorAll('[data-late]').forEach((n) => (n.hidden = live));
    if (live) {
      const pad = (x) => String(x).padStart(2, '0');
      const text = `${pad(Math.floor(left / 3600))}:${pad(Math.floor(left / 60) % 60)}:${pad(left % 60)}`;
      el.querySelectorAll('[data-time]').forEach((n) => (n.textContent = text));
    }
  }
}
tickShipTimers();
window.setInterval(tickShipTimers, 1000);
document.addEventListener('shopify:section:load', tickShipTimers);

// Gépelő kereső: a keresőgomb példákat „gépel" (terméknév és cikkszám).
function startTyping(el) {
  if (el.dataset.msTypedOn || reducedMotion()) return;
  el.dataset.msTypedOn = '1';
  const words = (el.dataset.msTyped || '').split('|').map((w) => w.trim()).filter(Boolean);
  if (!words.length) return;
  let w = 0, i = 0, dir = 1, hold = 0;
  window.setInterval(() => {
    if (!el.isConnected || document.hidden) return;
    if (hold > 0) { hold -= 1; return; }
    const word = words[w];
    i += dir;
    el.textContent = word.slice(0, i);
    if (i >= word.length) { dir = -1; hold = 16; }
    if (i <= 0) { dir = 1; w = (w + 1) % words.length; hold = 4; }
  }, 85);
}
const initTyping = () => document.querySelectorAll('[data-ms-typed]').forEach(startTyping);
initTyping();
document.addEventListener('shopify:section:load', initTyping);

// Nyitó termékváltó
class MsStage extends HTMLElement {
  connectedCallback() {
    this.slides = [...this.querySelectorAll('[data-slide]')];
    this.ticks = [...this.querySelectorAll('[data-tick]')];
    this.index = 0;
    this.ticks.forEach((tick, i) => tick.addEventListener('click', () => { this.show(i); this.restart(); }));
    this.addEventListener('pointerenter', () => this.stop());
    this.addEventListener('pointerleave', () => this.restart());
    this.addEventListener('focusin', () => this.stop());
    this.addEventListener('focusout', () => this.restart());
    this.show(0);
    this.restart();
  }
  disconnectedCallback() { this.stop(); }
  show(i) {
    this.index = i;
    this.slides.forEach((s, n) => { s.classList.toggle('is-on', n === i); s.toggleAttribute('inert', n !== i); });
    this.ticks.forEach((t, n) => { t.classList.remove('is-on'); if (n === i) { void t.offsetWidth; t.classList.add('is-on'); } t.setAttribute('aria-current', String(n === i)); });
  }
  stop() { window.clearInterval(this.timer); this.classList.add('is-paused'); }
  restart() {
    this.stop();
    this.classList.remove('is-paused');
    if (this.slides.length < 2 || reducedMotion()) return;
    this.timer = window.setInterval(() => this.show((this.index + 1) % this.slides.length), Number(this.dataset.interval || 5000));
  }
}
if (!customElements.get('ms-stage')) customElements.define('ms-stage', MsStage);

// Forrszem-fény: a sötét sáv pontrácsa felgyullad a kurzor körül.
document.addEventListener('pointermove', (event) => {
  if (event.pointerType !== 'mouse') return;
  const band = event.target instanceof Element ? event.target.closest('[data-ms-glow]') : null;
  if (!band) return;
  const rect = band.getBoundingClientRect();
  band.style.setProperty('--mx', `${((event.clientX - rect.left) / rect.width) * 100}%`);
  band.style.setProperty('--my', `${((event.clientY - rect.top) / rect.height) * 100}%`);
}, { passive: true });

// Kosár-visszajelzés: a kosárjelvény felpattan, amikor változik a kosár.
document.addEventListener('shopify:cart:lines-update', () => {
  document.querySelectorAll('.cart-bubble').forEach((bubble) => {
    bubble.classList.remove('ms-pop');
    void bubble.offsetWidth;
    bubble.classList.add('ms-pop');
  });
});

// Kereső lenyíló találatokkal (felugró ablak helyett)
class MsSearch extends HTMLElement {
  connectedCallback() {
    this.input = this.querySelector('input[type="search"]');
    this.box = this.querySelector('[data-results]');
    if (!this.input || !this.box) return;
    this.active = -1;
    this.input.addEventListener('input', () => this.onInput());
    this.input.addEventListener('focus', () => { if (this.box.childElementCount) this.open(); });
    this.input.addEventListener('keydown', (event) => this.onKey(event));
    document.addEventListener('pointerdown', (event) => { if (!this.contains(event.target)) this.close(); });
  }
  open() { this.box.hidden = false; this.input.setAttribute('aria-expanded', 'true'); }
  close() { this.box.hidden = true; this.input.setAttribute('aria-expanded', 'false'); this.active = -1; }
  onInput() {
    const term = this.input.value.trim();
    this.classList.toggle('has-value', this.input.value.length > 0);
    window.clearTimeout(this.timer);
    if (term.length < 2) { this.box.replaceChildren(); this.close(); return; }
    this.timer = window.setTimeout(() => this.search(term), 180);
  }
  async search(term) {
    this.controller?.abort();
    this.controller = new AbortController();
    const params = new URLSearchParams({
      q: term,
      'resources[type]': 'product,collection',
      'resources[limit]': '6',
      'resources[options][fields]': 'title,product_type,variants.sku,variants.title,tag',
      'resources[options][unavailable_products]': 'last',
    });
    try {
      const response = await fetch(`${this.dataset.url}.json?${params}`, { signal: this.controller.signal, headers: { Accept: 'application/json' } });
      if (!response.ok) throw new Error(String(response.status));
      const data = await response.json();
      this.render(term, data.resources?.results ?? {});
    } catch (error) {
      if (error.name !== 'AbortError') this.close();
    }
  }
  el(tag, className, text) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text != null) node.textContent = text;
    return node;
  }
  money(value) {
    const amount = Math.round(Number(value));
    if (!Number.isFinite(amount)) return '';
    return `${String(amount).replace(/\B(?=(\d{3})+(?!\d))/g, ' ')} Ft`;
  }
  render(term, results) {
    const products = results.products ?? [];
    const collections = results.collections ?? [];
    const nodes = [];
    if (collections.length) {
      nodes.push(this.el('p', 'ms-searchbar__group', 'Kategóriák'));
      for (const c of collections.slice(0, 3)) {
        const a = this.el('a', 'ms-searchbar__item ms-searchbar__item--plain');
        a.href = c.url;
        a.append(this.el('span', 'ms-searchbar__item-title', c.title), this.el('span', '', '→'));
        nodes.push(a);
      }
    }
    if (products.length) {
      nodes.push(this.el('p', 'ms-searchbar__group', 'Termékek'));
      for (const p of products) {
        const a = this.el('a', 'ms-searchbar__item');
        a.href = p.url;
        const ph = this.el('span', 'ms-ph');
        const src = p.featured_image?.url || p.image;
        if (src) { const img = document.createElement('img'); img.src = src + (src.includes('?') ? '&' : '?') + 'width=120'; img.alt = ''; img.loading = 'lazy'; ph.append(img); }
        const meta = this.el('span');
        meta.append(this.el('span', 'ms-searchbar__item-title', p.title));
        const stock = this.el('span', `ms-stock ms-stock--${p.available ? 'ok' : 'off'}`);
        stock.append(this.el('span', `ms-led ms-led--${p.available ? 'ok' : 'off'}`), document.createTextNode(p.available ? 'Raktáron' : 'Elfogyott'));
        meta.append(stock);
        a.append(ph, meta, this.el('span', 'ms-price', this.money(p.price)));
        nodes.push(a);
      }
    }
    if (!nodes.length) nodes.push(this.el('p', 'ms-searchbar__empty', `Nincs találat erre: „${term}”. Próbáld cikkszámmal vagy rövidebb kifejezéssel.`));
    else {
      const all = this.el('a', 'ms-searchbar__all');
      all.href = `${this.dataset.searchUrl}?q=${encodeURIComponent(term)}`;
      all.append(this.el('span', '', `Összes találat erre: „${term}”`), this.el('span', '', '→'));
      nodes.push(all);
    }
    this.box.replaceChildren(...nodes);
    this.active = -1;
    this.open();
  }
  onKey(event) {
    if (event.key === 'Escape') { this.close(); return; }
    if (event.key !== 'ArrowDown' && event.key !== 'ArrowUp') return;
    const links = [...this.box.querySelectorAll('a')];
    if (!links.length || this.box.hidden) return;
    event.preventDefault();
    this.active = (this.active + (event.key === 'ArrowDown' ? 1 : -1) + links.length) % links.length;
    links.forEach((link, i) => link.classList.toggle('is-active', i === this.active));
    links[this.active].focus();
    links[this.active].addEventListener('keydown', (e) => {
      if (e.key === 'Escape') { this.close(); this.input.focus(); }
      if (e.key === 'ArrowDown' || e.key === 'ArrowUp') { e.preventDefault(); this.input.focus(); this.onKey(e); }
    }, { once: true });
  }
}
if (!customElements.get('ms-search')) customElements.define('ms-search', MsSearch);
