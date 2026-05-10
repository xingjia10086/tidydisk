# Gumroad Setup — Copy-Paste Pack

Every field you'll see on Gumroad is pre-written below. Just copy → paste.

⏱ Total time: ~15 minutes if you have an email and PayPal/bank account ready.

---

## Step 0 · Before you start, have these ready

- [ ] An email address (Gumroad will send a confirmation link)
- [ ] A bank account or PayPal for payouts
- [ ] **For non-US sellers (you):** US Tax ID is NOT required. You'll fill out a
      W-8BEN form (one screen, takes 2 min). No accountant needed.
- [ ] The exe file: `C:\Users\xingj\Desktop\TidyDisk-v1.0.0.exe` (already downloaded)
- [ ] The cover image PNG (export from `docs/cover.html` first — see COVER-INSTRUCTIONS.md)

---

## Step 1 · Sign up

URL: **https://app.gumroad.com/signup**

- Email: *(your real email)*
- Password: *(unique, not reused)*

Confirm via email link.

---

## Step 2 · Profile setup

Gumroad will ask for a few things on first login:

| Field | Paste this |
|-------|-----------|
| Display name | `xingjia10086` (or whatever brand name you want shown to buyers) |
| Bio | `Indie dev. I make small, honest software. No bundleware, no telemetry, no subscription traps.` |
| Profile picture | (optional — your GitHub avatar works) |

---

## Step 3 · Create the product

Click **"+ New product"** → choose **"Digital product"**.

### Basic info

| Field | Paste this |
|-------|-----------|
| **Name** | `TidyDisk — The honest C-drive cleaner for Windows` |
| **Price** | `9.99` USD (you can also enable "Pay what you want" with $9.99 minimum) |
| **Custom URL slug** | `tidydisk`  → final URL becomes `gumroad.com/l/tidydisk` |

### Cover image
Upload `cover.png` (1280×720) you exported from `docs/cover.html`.

### Thumbnail
Upload `cover-square.png` (600×600) you exported from `docs/cover-square.html`.

### Product description (the "About" section)

Paste this — supports Markdown:

```markdown
**The honest C-drive cleaner for Windows.** No bundleware. No telemetry. No subscription.

CCleaner used to be the answer for Windows disk cleanup. Then it got bought, started bundling adware on every install, and added telemetry by default. TidyDisk is what it used to be — a one-button C-drive cleaner that does its job and gets out of the way.

### Why TidyDisk?

- ⚡ **One button.** Scan → confirm → done. Under 30 seconds.
- 🛡️ **Zero bundleware, zero telemetry.** Verifiable in the open MIT source.
- 🪶 **12 MB single exe.** No installer. No registry entries. Drop it on your desktop.
- 🔓 **Source on GitHub.** Audit it yourself. Or compile it yourself for free.
- 💰 **One-time $9.99.** No subscription. No "Pro" upgrade nag.

### What it cleans

- User & system temp files
- Recycle Bin (all drives)
- Windows Update download cache
- Browser caches (Edge, Chrome, Firefox, Brave)
- Windows Error Reports
- Thumbnail & icon caches
- Prefetch & Delivery Optimization caches
- Hibernation file (advanced — frees space equal to your RAM)

Every path is hardcoded. System files and personal data are never touched. Nothing is deleted until you confirm.

### What you get

- ✓ `TidyDisk.exe` — instant download
- ✓ Lifetime free updates — every release, free
- ✓ Email support — replies within 24 hours
- ✓ Use on every PC you own — no DRM, no activation
- ✓ 30-day no-questions-asked refund

### Source code

Full MIT-licensed source on GitHub: https://github.com/xingjia10086/tidydisk

Compile it yourself in 5 minutes if you'd rather not pay. Buying gets you the polished signed binary, lifetime updates, and supports a solo developer building the kind of small, honest software the world needs more of.

### Requirements

Windows 10 or Windows 11, 64-bit. Admin rights required (UAC prompt on launch).

### First-run note

Windows shows "Windows protected your PC" the first time you run any unsigned exe — this is a generic OS warning, not a virus alert. Click "More info" → "Run anyway." We'll add code-signing once revenue justifies the $200/yr cert cost.
```

### Summary (the short blurb under product name on the listing)

```
A no-bundleware, no-telemetry Windows C-drive cleaner. Single 12 MB exe, source on GitHub, one-time $9.99.
```

### Tags

Add: `windows`, `utility`, `cleaner`, `productivity`, `open-source`, `disk-cleanup`

---

## Step 4 · Upload the file

In the **"Content"** section:

| Field | What to do |
|-------|-----------|
| **File to deliver** | Upload `C:\Users\xingj\Desktop\TidyDisk-v1.0.0.exe` |
| **File name shown to buyer** | `TidyDisk.exe` |

⚠️ **Don't enable "Stamp PDF" or any DRM**. It's an exe, not a doc.

---

## Step 5 · Settings

Click the **Settings** tab on the product page.

### Refund policy
```
30-day no-questions-asked refund. Just email and we'll process it.
```

### Receipt thank-you message (shown after purchase)

```markdown
🎉 Thanks for buying TidyDisk!

Here's everything you need:

**1. Download** — TidyDisk.exe is attached to this email and on your Gumroad library.

**2. First run** — Double-click. Windows will show "Windows protected your PC" (it does this for any unsigned exe). Click "More info" → "Run anyway". You'll get a UAC prompt for admin rights — that's normal, the app needs admin to clean Windows system folders.

**3. Updates** — Every future release is yours free. I'll email you when there's a new version. You can also check https://github.com/xingjia10086/tidydisk/releases.

**4. Use on multiple PCs** — No DRM, no license keys. Copy the exe to any PC you own.

**5. Need help?** — Reply to this email. I respond within 24 hours.

If you're happy with it, a tweet, a Reddit comment, or a Product Hunt upvote means the world to a solo dev. 🙏

— xingjia10086
GitHub: github.com/xingjia10086/tidydisk
```

### Email settings
- Enable: ✓ Send a receipt email
- Enable: ✓ Send a "thank you" email
- Disable: ✗ Promotional emails to existing customers (annoying)

---

## Step 6 · Tax & payout

Gumroad asks once. Stick with it — it's the longest part but only takes ~5 min.

### W-8BEN form (for non-US sellers)
- Country: *your country*
- Tax ID: leave blank if you don't have a US TIN — that's fine
- Treaty benefit: most countries have a 0% withholding rate for digital goods; pick yours from the dropdown

### Payout method
Pick whichever is cheapest in your country:
- **PayPal** — works almost everywhere; ~3% fee on payout (in addition to Gumroad's 10%)
- **Bank transfer (ACH/SEPA)** — better rates, available in some countries
- **Wise / Payoneer** — sometimes the cheapest for non-US sellers; check current rates

For China/HK accounts: PayPal or Wise both work fine for receiving USD from Gumroad.

---

## Step 7 · Publish

Click **"Save and continue"** → review → **"Publish"**.

Test the live URL in an incognito window: https://gumroad.com/l/tidydisk

✅ Buy your own product with a different email + a real card — confirm:
- [ ] Payment goes through
- [ ] Receipt email arrives
- [ ] Download link works and the exe is the right one
- [ ] Refund processes correctly when you cancel

Then refund yourself. The product is now live.

---

## Step 8 · Discount codes (optional but worth doing)

In Discounts → New discount code:

| Code | % off | Limit | Use for |
|------|-------|-------|---------|
| `LAUNCH20` | 20% off | first 50 uses | Product Hunt launch day |
| `HACKERNEWS` | 30% off | first 30 uses | "Show HN" post |
| `REDDIT` | 25% off | first 50 uses | Reddit posts |
| `LIFETIME` | $0.01 (effectively free) | 5 uses | Friends / influencers |

This lets you measure which channel converts.

---

## Step 9 · Add UTM tracking to your launch links

When you post to PH / Reddit / HN, use these instead of the bare URL:

```
PH:        https://gumroad.com/l/tidydisk?ref=ph
HN:        https://gumroad.com/l/tidydisk?ref=hn
Reddit:    https://gumroad.com/l/tidydisk?ref=reddit
Twitter:   https://gumroad.com/l/tidydisk?ref=x
```

Gumroad's analytics will show conversion rate per source — critical for the $10k/month decision tree in `LAUNCH.md`.

---

## You're done 🎉

Once Gumroad is published, you can:
- Update the landing page (`docs/index.html`) — every "Buy" button already points to `gumroad.com/l/tidydisk`
- Tag-launch on Product Hunt, Reddit, HN per `LAUNCH.md`

If you hit any wall during signup (verification, tax form, payout setup),
ping me with a screenshot and I'll walk you through it.
