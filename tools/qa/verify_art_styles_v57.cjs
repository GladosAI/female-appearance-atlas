const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const {pathToFileURL} = require('node:url');
const {chromium} = require('./runtime.cjs').playwright;
const root = path.resolve(__dirname, '../..');
const read = file => JSON.parse(fs.readFileSync(path.join(root, file), 'utf8'));

(async () => {
  const data = read('data/catalog.json'), nav = read('data/navigation.json');
  const entries = data.entries.filter(e => e.art_style_reference);
  assert.equal(entries.length, 24);
  assert.equal(data.meta.missing_image_count, 0);
  assert.equal(new Set(data.entries.map(e => e.id)).size, data.entries.length);
  assert.equal(nav.groups.find(g => g.id === 'art_styles').count, 24);
  assert.equal(nav.groups.length, 9);
  for (const entry of entries) {
    assert(entry.visual && fs.existsSync(path.join(root, entry.visual.image)), entry.id);
    const crop = entry.visual.crop;
    assert.deepEqual([crop.width, crop.height, crop.sheet_width, crop.sheet_height], [768, 512, 1536, 1024]);
  }
  const browser = await chromium.launch({...require('./runtime.cjs').browserOptions,headless:true});
  const page = await browser.newPage({viewport:{width:1280,height:900}});
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  const url = pathToFileURL(path.join(root, 'index.html')).href;
  await page.goto(url + '?section=topic_art_styles');
  await page.waitForSelector('article.entry');
  assert.equal(await page.locator('article.entry').count(), 24);
  assert(await page.locator('body').innerText().then(s => s.includes('画风与视觉表现')));
  assert(await page.locator('body').innerText().then(s => s.includes('摄影与写实影像')));
  const background = await page.locator('article.entry .thumb').first().evaluate(e => getComputedStyle(e).backgroundImage);
  assert(background.includes('sheet-xa001-xa004.png'));
  await page.goto(url + '?section=all&q=' + encodeURIComponent('像素'));
  await page.waitForSelector('article.entry');
  assert(await page.locator('body').innerText().then(s => s.includes('像素游戏画风')));
  await page.goto(url + '?section=art_photography');
  await page.waitForSelector('article.entry');
  assert.equal(await page.locator('article.entry').count(), 4);
  assert(await page.locator('body').innerText().then(s => s.includes('模拟')));
  assert.deepEqual(errors, []);
  await browser.close();
  console.log(JSON.stringify({passed:true, styles:entries.length, categories:6, images:6, browser:'passed', search:'像素', photo_simulation_disclosed:true}));
})().catch(error => {console.error(error);process.exitCode=1});
