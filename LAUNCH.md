# TidyDisk Launch Playbook

Goal: validate paying-customer demand. Target: **first 10 sales within 7 days**.

If you hit 10 sales/week organically, scaling to $10k/month becomes a math problem
(more channels, more polish, paid ads). If you can't hit 10 sales in 7 days, the
product or pricing needs rework before you spend more time on it.

---

## Pre-flight checklist (do these BEFORE launching)

- [ ] **Set up Gumroad product** at https://gumroad.com/products/new
  - Product name: `TidyDisk — Honest C-drive Cleaner for Windows`
  - Price: $9.99 (mark "or more" to allow tipping)
  - URL slug: `tidydisk` (so the URL is `gumroad.com/l/tidydisk`)
  - Upload `TidyDisk.exe` from the latest release as the deliverable
  - Cover image: take a screenshot of the app's home screen
  - Description: copy the GitHub README hero
  - Refund policy: 30 days, no questions
- [ ] **Enable GitHub Pages** at https://github.com/xingjia10086/tidydisk/settings/pages
  - Source: Deploy from branch → `main` / `/docs`
  - Verify the page goes live at https://xingjia10086.github.io/tidydisk/
- [ ] **Take 3 screenshots** of the running app (home, scan results, done)
  - Save to `docs/screenshot-1.png`, `screenshot-2.png`, `screenshot-3.png`
  - Use these on Gumroad + GitHub README + Product Hunt
- [ ] **Make a 30-second demo GIF** (use ScreenToGif, free)
  - Record: launch → scan → check items → clean → done screen
  - Compress to <5 MB
  - Embed in README + landing page
- [ ] **Test the purchase flow yourself** — buy your own product on Gumroad with
  a different email, confirm download works, then refund

---

## Launch day order (do in this sequence)

### 1. Product Hunt (T+0, the highest-leverage single action)

**Schedule for 12:01 AM Pacific Time** on a Tuesday or Wednesday — that's when
the 24-hour ranking window starts and PH staff are most active.

- **Tagline (60 char):** "The honest C-drive cleaner for Windows. No bundleware."
- **Description:**
  > CCleaner used to be the answer for Windows disk cleanup. Then it got bought,
  > bundled adware, and started phoning home. TidyDisk is what CCleaner used to be —
  > a one-button C-drive cleaner with no bundleware, no telemetry, no subscription.
  > Source-available on GitHub, $9.99 one-time.
- **Topics:** Productivity, Windows, Developer Tools, Open Source
- **Maker comment** (post immediately after launch):
  > Hi PH! 👋 Indie dev here. I built TidyDisk after watching CCleaner get acquired
  > and slowly bundle adware over the years. I wanted the simple one-button cleaner
  > it used to be — so I made one.
  >
  > Three things make it different:
  > 1. **Zero bundleware, zero telemetry** — verifiable in the open MIT source.
  > 2. **One-time $9.99** instead of "free with Pro nag screens forever".
  > 3. **One 12 MB exe** — no installer, no registry entries.
  >
  > Code is fully open on GitHub. You can compile it yourself for free. Paying
  > $9.99 gets the polished signed binary + lifetime updates + email support.
  >
  > Happy to answer anything!
- **First-day priorities:**
  - Reply to every single comment within 1 hour
  - DM 20–30 friends/colleagues to upvote (NOT spam — only real users)
  - Cross-post the PH link on Twitter / X with a thread

### 2. Reddit posts (T+0 day, 4 hours after PH)

Stagger by ~30 min between subs. Read each sub's rules first.

| Subreddit | Subscribers | Angle |
|-----------|-------------|-------|
| r/windows | 600k | "Built a no-bundleware alternative to CCleaner — would love your feedback" |
| r/Windows10 | 400k | Same |
| r/Windows11 | 250k | Same |
| r/SideProject | 200k | "I'm an indie dev — launching my first paid product today" |
| r/coolgithubprojects | 60k | Lead with the GitHub repo, mention the paid binary as bonus |
| r/Entrepreneur | 4M | Frame as "first paid product launch day, here's what I built and why" |
| r/sysadmin | 1M | DON'T self-promote here without contributing first; lurk for a week |

**Title template (r/windows):**
> I got tired of CCleaner's bundleware so I built a 12 MB single-exe alternative — TidyDisk

**Body template:**
> Hey r/windows. I'm an indie dev. I made TidyDisk because:
> - CCleaner now bundles adware on install
> - Most "cleaners" on Microsoft Store are scams or fake "registry cleaners"
> - I just wanted a one-button thing that cleans temp/recycle/cache and quits
>
> TidyDisk is:
> - 12 MB single exe (no installer)
> - Source on GitHub, MIT license — audit it yourself
> - No telemetry, no bundleware, ever
> - $9.99 one-time, lifetime updates (or compile it yourself for free)
>
> Source: [github link]
> Buy: [gumroad link]
>
> Built it solo over a few weekends. Honest feedback welcome — especially if you
> spot something it should clean and doesn't.

⚠️ **Do not post the same text to multiple subs** — Reddit auto-flags as spam.
Rewrite each post in a different style.

### 3. Hacker News "Show HN" (T+1 day)

Post at 8–10 AM Pacific (peak HN traffic).

- **Title:** `Show HN: TidyDisk – A no-bundleware C-drive cleaner for Windows ($9.99)`
- **Self-comment immediately:**
  > Hi HN. Source is MIT on GitHub: [link]. Compile it yourself if you don't want
  > to pay; $9.99 gets the binary + updates + supports a solo developer.
  >
  > Why I built it: CCleaner went from $25M acquisition to bundled adware in a few
  > years. I wanted a small, honest tool that does one thing.
  >
  > AMA on the technical bits — it's Python + tkinter + PyInstaller, all clean
  > paths hardcoded, plus standard `SHEmptyRecycleBin` / `powercfg /h off` calls.

### 4. Twitter/X thread (T+0 day, in parallel with PH)

7-tweet thread. Quote-tweet the PH link. Hashtags: `#buildinpublic` `#indiehackers`

### 5. Indie Hackers post (T+1 or T+2 day)

Frame as "first paid launch — here's the funnel after 24 hours". Real numbers
get more upvotes than marketing copy.

---

## After launch: what to track

Set up a simple spreadsheet:

| Date | Channel | Visitors | Conversions | $ revenue | Notes |
|------|---------|----------|-------------|-----------|-------|
|      |         |          |             |           |       |

Sources of traffic (use Gumroad's referrer data + UTMs):
- `?ref=ph` for Product Hunt
- `?ref=hn` for Hacker News
- `?ref=reddit_windows` for r/windows
- etc.

**After 7 days, decide:**

| Outcome | Verdict | Next move |
|---------|---------|-----------|
| 0–2 sales | Demand isn't there at $9.99 | Try $4.99, OR pivot to feature expansion (startup manager, dupe finder) before relaunching |
| 3–9 sales | Marginal — there IS some demand | Iterate on landing page conversion, add 1–2 features, relaunch in 2 weeks |
| 10+ sales | Validated! | Now invest in: code signing ($200/yr), more launch channels (AppSumo deal, paid ads), feature expansion |
| 30+ sales | Strong signal | Start working toward $10k/month — needs feature expansion + steady content marketing |

---

## Honest math for the $10k/month target

At $9.99 per sale, after Gumroad's ~5% cut:
- **$10k/month = ~1,055 sales/month = ~35 sales/day**

That's hard but not impossible if you have:
- A YouTube channel about Windows tips with 50k+ subscribers (each video = 5–20 sales)
- Affiliate program where bloggers earn $3 per referral (drives long-tail traffic)
- 4–5 viral threads per quarter on X/Reddit/HN

If after 1 month you're at <100 sales/month, the realistic path to $10k is to
add a $49/year "Pro" tier (scheduled cleaning, multi-PC license, advanced features
like startup manager) and shift the funnel toward annual recurring revenue.
