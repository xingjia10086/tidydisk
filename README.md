# TidyDisk

> The dead-simple Windows C-drive cleaner. **No bundleware. No telemetry. No subscription.**

[![Buy now — $9.99](https://img.shields.io/badge/Buy%20now-%249.99-2563EB?style=for-the-badge)](https://gumroad.com/l/tidydisk)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

![TidyDisk screenshot](docs/screenshot.png)

---

## Why TidyDisk?

CCleaner used to be the answer. Then they were [bought](https://www.theverge.com/2017/9/18/16325202/ccleaner-hack-malware-security), bundled adware, added telemetry, and got slower with every release.

TidyDisk is what CCleaner used to be — a **single-button** C-drive cleaner that:

- ⚡ **One button.** Scan → confirm → done.
- 🛡️ **No bundleware, ever.** No "free trial" of a different product. No browser-redirect "deals".
- 🔒 **No telemetry.** It does not phone home. Period.
- 🪶 **One file, 12 MB.** No installer. Drop it on your desktop.
- 🔓 **Source-available (MIT).** Audit the code yourself.
- 💰 **One-time purchase, $9.99.** Lifetime updates. No subscription.

## What it cleans

| Item | Description | Risk |
|------|-------------|------|
| User Temp Files | `%LOCALAPPDATA%\Temp` | Safe |
| System Temp Files | `C:\Windows\Temp` | Safe |
| Recycle Bin | All drives | Safe |
| Windows Update Cache | Already-installed update downloads | Safe |
| Browser Cache | Edge / Chrome / Firefox / Brave | Safe |
| Error Reports | `WER\ReportArchive`, `ReportQueue` | Safe |
| Thumbnail Cache | `thumbcache_*.db` (auto-rebuilds) | Safe |
| Prefetch | `C:\Windows\Prefetch` | Safe |
| Delivery Optimization | Update peer-to-peer cache | Safe |
| Hibernation File | `hiberfil.sys` (`powercfg /h off`) | Advanced (manual select) |

## Safety promise

- **All paths are hardcoded** in [`core/tasks.py`](core/tasks.py). Source is open — read it.
- The app **never touches** `System32`, `Program Files`, your Documents/Desktop/Pictures.
- Nothing is deleted until you confirm. Twice.
- No network calls. Audit it with Wireshark; you'll see nothing.

## Buy

👉 **[gumroad.com/l/tidydisk](https://gumroad.com/l/tidydisk)** — $9.99, one-time.

You get:
- `TidyDisk.exe` (signed binary) — instant download
- Lifetime free updates (every release, free)
- Email support (response within 24 h)

## Build it yourself

The source is MIT-licensed. You're welcome to compile it yourself:

```powershell
git clone https://github.com/xingjia10086/tidydisk.git
cd tidydisk
pip install -r requirements.txt
python build.py
# dist/TidyDisk.exe
```

If that's not your scene — paying $9.99 saves you 5 minutes and supports indie dev.

## License

[MIT](LICENSE) — code is free, but the polished binary + updates + support is what you're paying for.
