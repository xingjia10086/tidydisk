# Product Hunt 文案库（v2）

发布前最后一遍：**全部不要超过字符上限**，PH 截断会让文案看起来很蠢。

---

## 方案 A · "Anti-CCleaner"（推荐）

打反差牌。CCleaner 用户痛点足够多，借势比从零教育市场快 10 倍。

### Tagline (60 char max)
```
What CCleaner used to be — before the bundleware
```
✏️ 47 char

### Tagline 备选
```
The honest C-drive cleaner for Windows
The one-button Windows cleaner that doesn't sell you out
A 12 MB Windows cleaner with zero bundleware
```

### Description (260 char max)
```
CCleaner used to be the answer for Windows disk cleanup — until it got bought, bundled adware, and started phoning home. TidyDisk is what it used to be: one button, no bundleware, no telemetry, no subscription. $9.99 one-time. Source on GitHub.
```
✏️ 245 char

### Maker comment (最关键 · 发布后 5 分钟内置顶)
```
Hey PH! 👋

I'm an indie dev. I built TidyDisk because I got tired of two things:
1. CCleaner getting acquired and slowly bundling adware on every install
2. Every "cleaner" on the Microsoft Store being either a scam, a fake "registry optimizer," or a subscription trap

I wanted the simple one-button thing CCleaner used to be — so I made one.

What's different:
→ Zero bundleware. Zero telemetry. Verifiable in the open MIT source.
→ Single 12 MB exe. No installer. No registry entries. Drop it on your desktop, delete it when done.
→ One-time $9.99. Lifetime updates. No subscription, no Pro nag screens, no upgrade tiers.
→ Or: compile it yourself for free. Source is fully open — paying gets you the polished binary + supports a solo developer.

It's intentionally narrow. It cleans 10 specific Windows paths (temp, recycle bin, browser caches, Windows Update cache, hibernation file, etc.). It doesn't pretend to be a "system optimizer."

Happy to answer anything about the technical side (Python + tkinter + PyInstaller, all paths hardcoded, uses standard SHEmptyRecycleBin / powercfg APIs) or the indie business side ($10/sale economics, why I picked Gumroad, etc.).

Feedback genuinely welcome — especially if you spot something it should clean and doesn't!
```

### Topics (选 3 个)
- **Productivity** (主)
- **Windows**
- **Open Source**

### First-day reply templates (准备好待用)

**当有人问 "free 替代品是什么":**
> Built-in "Storage Sense" in Windows is decent for the basics. BleachBit is open source and powerful but feels like 2008. PrivaZer is solid but very busy UI. TidyDisk is intentionally narrow — if you want one button and out, that's the niche.

**当有人质疑定价 ("$9.99 太贵 / 应该免费"):**
> Totally fair! The source is MIT — free to compile yourself, ~10 minutes with Python installed. The $9.99 is for the polished binary, lifetime updates, and supporting solo dev work. About the price of a pizza, and you can use it forever on every PC you own.

**当有人问 "和 BleachBit 比有什么不同":**
> BleachBit is more powerful and totally free — for power users who want every option, it's the right pick. TidyDisk is for "I just want my C drive cleaned and quit." Different audiences. If BleachBit fits, use BleachBit!

**当有人问 "为什么不开源 + 免费":**
> Source IS open (MIT on GitHub). The binary is what's paid. Same model as Sindre Sorhus's macOS apps, BeeKeeper Studio, Tabby. You vote with $9.99 if you want indie devs to keep building this kind of stuff instead of taking jobs at Big Tech.

---

## 方案 B · "Indie dev story"

更真诚、更慢热。适合发布在工作日下午（PH 流量低但留存好）。

### Tagline
```
A no-bundleware Windows cleaner — built by one dev
```

### Description
```
First paid product launch. After watching CCleaner go from beloved tool to bundleware factory, I built the simple one-button cleaner I wanted. 12 MB single exe, no installer, source on GitHub. $9.99 one-time. Lifetime updates. Ship one good thing > 10 mediocre ones.
```

### Maker comment
```
This is my first paid product on Product Hunt 🫣

I've been writing software for years but always shipped free open-source stuff.
This time I wanted to test if I could build something people pay for.

The product is small on purpose:
- It cleans your Windows C drive in one click
- 10 specific cleanup categories, all hardcoded paths
- 12 MB single exe, no installer, no registry, no telemetry, no bundleware

The pricing is intentionally simple:
- $9.99 one-time. That's it.
- Source is MIT on GitHub — you can compile it yourself for free.
- Paying gets you the polished binary + lifetime updates + email support + supports a solo dev.

I'm trying to validate whether $9.99 utility software has buyers in 2026.
Honest feedback (even brutal feedback) is appreciated.

If you've launched a $9.99 utility on PH before — would love to hear how it went.
```

---

## 方案 C · "Manifesto"

最冒险但最有可能爆。适合周末发，HN-friendly。

### Tagline
```
Windows cleaners are a scam. Here's an honest one.
```

### Description
```
Every "cleaner" on the Microsoft Store is either a scam, fake "registry optimizer," or subscription trap. CCleaner sold out in 2017. TidyDisk is the boring honest one — 12 MB, single exe, MIT source, $9.99 one-time, no nonsense.
```

### Maker comment
```
Unpopular opinion: 95% of Windows "cleaner" software is malware-adjacent.

→ "Registry cleaners" don't speed up Windows. They never did.
→ "PC optimizers" are mostly placebo with subscription billing attached.
→ Microsoft Store is full of $19.99/year renamed BleachBit forks.
→ CCleaner literally got hacked in 2017 and shipped malware to 2.27 million users.

What people actually want is small: empty temp folders, the recycle bin,
Windows Update cache, browser caches. That's a 200-line Python script.

I packaged it cleanly, open-sourced it, and put a $9.99 price on the binary.
Compile it yourself for free if you want. Pay if you want to support a solo dev
who's tired of watching this category be terrible.

Source: https://github.com/xingjia10086/tidydisk
Buy: https://gumroad.com/l/tidydisk
```

---

## 我对你的建议

1. **首选方案 A**。反差感强、信息密度高、对"是否值得 $9.99"给出明确答案。
2. **B 留作后备**。如果 A 上线 4 小时还排在 #15 之外，删掉重发 B 版。
3. **C 不要发**。在 PH 太刺激，会被踩；适合 HN 或 X 长推文。

---

## 上线前 30 分钟最后检查

- [ ] Gumroad 商品页可以下单
- [ ] gumroad.com/l/tidydisk 链接 200 OK
- [ ] xingjia10086.github.io/tidydisk 落地页正常
- [ ] PH gallery 里至少 4 张：
  - [ ] 主截图（home view）
  - [ ] 扫描结果（scan view，显示有内容）
  - [ ] 完成页（result view，"Freed 8.4 GB"）
  - [ ] 演示 GIF（30s 全流程）
- [ ] 同事/朋友的"上线后 30 分钟内点赞 + 评论"安排好（不要超过 10 个，PH 反作弊会标记）
- [ ] Twitter/X 推文已写好待发
- [ ] 退款条款已在 Gumroad 配置（30 天无条件退）
