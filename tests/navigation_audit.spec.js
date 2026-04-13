// tests/navigation_audit.spec.js
const { test, expect } = require('@playwright/test');

test.describe('PN26 Event Navigation Audit', () => {
  // CORRECCIÓN: Rutas relativas (sin el / inicial) para que funcionen en la subcarpeta de GitHub
  const navbarLinks = [
    { label: 'PN26', path: './' },
    { label: 'Programa', path: 'program/' },
    { label: 'Sesiones', path: 'talks/' },
    { label: 'Salas', path: 'salas/' },
    { label: 'Escenarios en Vivo', path: 'escenarios-en-vivo/' },
    { label: 'Stands', path: 'stands/' },
    { label: 'Ponentes', path: 'speakers/' },
    { label: 'Instituciones', path: 'instituciones/' },
  ];

  test.beforeEach(async ({ page }) => {
    page.on('console', msg => {
      if (msg.type() === 'error') console.error(`[CONSOLE ERROR] at ${page.url()}: ${msg.text()}`);
    });

    page.on('response', response => {
      if (response.status() === 404) console.error(`[404 ERROR] Resource not found: ${response.url()}`);
    });
  });

  for (const item of navbarLinks) {
    test(`Audit link: ${item.label}`, async ({ page }) => {
      // Usamos la ruta relativa
      await page.goto(item.path);

      // 1. Verificación de carga (Título no debe ser 404)
      await expect(page).not.toHaveTitle(/404/);

      // 2. Validación específica de secciones
      if (item.label === 'Programa') {
        await page.screenshot({ path: 'tests/evidence/program-section.png' });
        const firstTalk = page.locator('a[href*="/talks/"], a[href*="talks/"]').first();
        if (await firstTalk.count() > 0) {
          await firstTalk.click();
          await expect(page.locator('h1')).not.toBeEmpty();
        }
      }

      if (item.label === 'Ponentes') {
        await page.screenshot({ path: 'tests/evidence/speakers-section.png' });
        const firstSpeaker = page.locator('a[href*="/speakers/"], a[href*="speakers/"]').first();
        if (await firstSpeaker.count() > 0) {
          await firstSpeaker.click();
          await expect(page.locator('h1')).toBeVisible();
        }
      }
    });
  }
});