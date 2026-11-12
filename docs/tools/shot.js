// Screenshot the preview theme: node docs/tools/shot.js "/" home [--modes=light,dark] [--sizes=desktop,tablet,mobile]
// Env: SHOT_DIR (output dir), STORE_PASSWORD (storefront password)
const { chromium } = require('playwright');
const STORE = 'https://modulshop-hu-dd1b00hc.myshopify.com';
const THEME = '192355959112';
const path = process.argv[2] || '/';
const name = process.argv[3] || 'page';
const arg = (k, d) => (process.argv.find((a) => a.startsWith(`--${k}=`)) || `=${d}`).split('=')[1].split(',');
const modes = arg('modes', 'light,dark');
const sizes = { desktop: [1440, 900], tablet: [820, 1180], mobile: [390, 844] };
const want = arg('sizes', 'desktop,tablet,mobile');
const full = !process.argv.includes('--viewport');
const out = process.env.SHOT_DIR || '.';
(async () => {
  const b = await chromium.launch();
  for (const m of modes) {
    const ctx = await b.newContext({ locale: 'hu-HU', colorScheme: m });
    const p = await ctx.newPage();
    await p.goto(`${STORE}/password`);
    const pw = await p.$('input[type="password"]');
    if (pw) { await pw.fill(process.env.STORE_PASSWORD || ''); await p.click('button[type="submit"], input[type="submit"]'); await p.waitForURL((u) => !u.pathname.startsWith('/password'), { timeout: 15000 }).catch(() => {}); }
    const errors = [];
    p.on('console', (msg) => msg.type() === 'error' && errors.push(msg.text().slice(0, 160)));
    p.on('pageerror', (e) => errors.push('PAGEERROR ' + e.message.slice(0, 160)));
    for (const s of want) {
      await p.setViewportSize({ width: sizes[s][0], height: sizes[s][1] });
      const sep = path.includes('?') ? '&' : '?';
      await p.goto(`${STORE}${path}${sep}preview_theme_id=${THEME}&pb=0`, { waitUntil: 'networkidle', timeout: 45000 }).catch(() => {});
      await p.waitForTimeout(800); const ok = await p.$('#shopify-pc__banner__btn-decline, button:has-text("Decline"), button:has-text("Elutasítás")'); if (ok) { await ok.click().catch(() => {}); await p.waitForTimeout(500); }
      await p.addStyleTag({ content: '#shopify-pc__banner, #preview-bar-iframe, #PBarNextFrameWrapper { display: none !important; } html, body, .page-wrapper { overflow: visible !important; height: auto !important; }' }).catch(() => {});
      await p.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise((r) => setTimeout(r, 120)); } window.scrollTo(0, 0); document.querySelectorAll('.ms-reveal').forEach((e) => e.classList.add('is-visible')); });
      await p.waitForTimeout(600);
      const file = `${out}/${name}-${s}-${m}.png`;
      await p.screenshot({ path: file, fullPage: full });
      const info = await p.evaluate(() => ({ toggle: (() => { const t = document.querySelector('ms-theme-toggle--header, .ms-theme-toggle--header'); if (!t || !t.offsetParent) return 'hidden'; const c = (e) => { const r = t.querySelector(e).getBoundingClientRect(); return Math.round((r.x + r.width / 2) * 10) / 10; }; return [c('.ms-theme-toggle__thumb'), c('.ms-theme-toggle__icon--sun'), c('.ms-theme-toggle__icon--moon')]; })(), theme: window.Shopify?.theme?.id, mode: document.documentElement.dataset.theme, h: document.body.scrollHeight }));
      console.log(file, JSON.stringify(info));
    }
    if (errors.length) console.log('console errors:', [...new Set(errors)].slice(0, 8).join(' | '));
    await ctx.close();
  }
  await b.close();
})();
