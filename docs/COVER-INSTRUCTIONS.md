# How to export the cover images as PNG

Two HTML files in this folder render pixel-perfect marketing images:

| File | Output size | Where to use |
|------|-------------|--------------|
| `cover.html` | **1280 × 720** | Gumroad cover, Product Hunt gallery, Twitter card |
| `cover-square.html` | **600 × 600** | Gumroad thumbnail, Reddit thumbnail, X profile |

Pick whichever method is easiest. **Method 1 (Chrome DevTools) is the fastest.**

---

## Method 1 · Chrome DevTools (recommended, 30 seconds)

1. Open the HTML file in Chrome:
   - `file:///C:/Users/xingj/tidydisk/docs/cover.html`
2. Press <kbd>F12</kbd> to open DevTools.
3. Press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> to open the command palette.
4. Type `screenshot`, choose **"Capture node screenshot"**.
5. In the Elements panel, click on the `<div class="cover">` node (or `<div class="thumb">` for square).
6. The browser downloads a PNG at the exact element size.

That's it. The PNG is exactly 1280×720 (or 600×600), no cropping needed.

---

## Method 2 · One-line Puppeteer (if you have Node installed)

```powershell
npx puppeteer-cli screenshot file:///C:/Users/xingj/tidydisk/docs/cover.html `
  --selector ".cover" --output cover.png
```

Or, headless Chrome:

```powershell
& "C:\Program Files\Google\Chrome\Application\chrome.exe" `
  --headless --disable-gpu --hide-scrollbars `
  --window-size=1360,800 `
  --screenshot=cover-raw.png `
  "file:///C:/Users/xingj/tidydisk/docs/cover.html"
```

(then crop the 1280×720 region — Method 1 is simpler.)

---

## Method 3 · Windows Snipping Tool (manual, low-fi)

1. Open `cover.html` in Chrome at 100% zoom.
2. Press <kbd>Win</kbd>+<kbd>Shift</kbd>+<kbd>S</kbd>.
3. Drag a selection over the dark cover area.
4. Save the snip as PNG.

⚠️ Edges may not be exactly 1280×720, but for Gumroad it's good enough.

---

## Method 4 · Online conversion (zero install)

1. Push this folder to GitHub Pages (already configured).
2. Visit `https://htmlcsstoimage.com/` or `https://www.web2pdfconvert.com/url-to-image`.
3. Paste `https://xingjia10086.github.io/tidydisk/cover.html`.
4. Set viewport to 1320×760, capture only the `.cover` selector.
5. Download PNG.

---

## After exporting — where to upload

| File | Upload to |
|------|-----------|
| `cover.png` (1280×720) | Gumroad → Product → Cover image |
| `cover.png` (1280×720) | Product Hunt → Gallery (slot #1) |
| `cover-square.png` (600×600) | Gumroad → Product → Thumbnail |
| `cover-square.png` (600×600) | X / Twitter profile pinned post image |
| `cover.png` resized to 1500×500 | X / Twitter banner (crop top/bottom) |

---

## To customize before exporting

Open the HTML file in any text editor and tweak:

- **Headline copy**: `<h1>` tag inside `.left` (cover) or root (thumbnail)
- **Price**: search for `$9.99` and replace
- **Brand color**: change `#2563EB` to your preferred primary color
- **Demo numbers in mockup** (cover.html only): edit the `.stat-value` and `.item-size` text
- **Background gradient**: tweak the `radial-gradient` and `linear-gradient` on `.cover`

Reload Chrome (Ctrl+R) and re-export.
