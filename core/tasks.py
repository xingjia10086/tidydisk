"""Cleanup task definitions. Each task: scan paths + clean function + metadata."""
from __future__ import annotations

import os
import shutil
import subprocess
import glob
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable


@dataclass
class CleanupItem:
    id: str
    name: str
    description: str
    risk: str  # "safe" | "medium"
    default_checked: bool
    paths: list[Path] = field(default_factory=list)
    size_bytes: int = 0
    custom_clean: Callable | None = None  # Special tasks that bypass default delete


def _expand(path: str) -> Path:
    return Path(os.path.expandvars(path))


def _dir_size(path: Path) -> int:
    if not path.exists():
        return 0
    total = 0
    try:
        for root, _, files in os.walk(path, onerror=lambda _: None):
            for f in files:
                try:
                    total += os.path.getsize(os.path.join(root, f))
                except OSError:
                    pass
    except Exception:
        pass
    return total


def _clear_dir_contents(path: Path) -> tuple[int, int]:
    """Delete all entries inside `path` (keep the directory itself).
    Returns (deleted, skipped)."""
    if not path.exists():
        return 0, 0
    deleted = skipped = 0
    for entry in path.iterdir():
        try:
            if entry.is_dir() and not entry.is_symlink():
                shutil.rmtree(entry, ignore_errors=False)
            else:
                entry.unlink()
            deleted += 1
        except Exception:
            skipped += 1
    return deleted, skipped


# ---------- Scan helpers ----------

def scan_user_temp() -> list[Path]:
    return [_expand("%LOCALAPPDATA%\\Temp")]


def scan_windows_temp() -> list[Path]:
    return [Path("C:/Windows/Temp")]


def scan_recycle_bin() -> list[Path]:
    return [Path("C:/$Recycle.Bin")]


def scan_windows_update() -> list[Path]:
    return [Path("C:/Windows/SoftwareDistribution/Download")]


def scan_browser_cache() -> list[Path]:
    paths = []
    edge = _expand("%LOCALAPPDATA%\\Microsoft\\Edge\\User Data\\Default\\Cache")
    chrome = _expand("%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Cache")
    firefox = _expand("%LOCALAPPDATA%\\Mozilla\\Firefox\\Profiles")
    brave = _expand("%LOCALAPPDATA%\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Cache")
    for p in (edge, chrome, firefox, brave):
        if p.exists():
            paths.append(p)
    return paths


def scan_wer() -> list[Path]:
    paths = []
    for p in [
        Path("C:/ProgramData/Microsoft/Windows/WER/ReportArchive"),
        Path("C:/ProgramData/Microsoft/Windows/WER/ReportQueue"),
        Path("C:/ProgramData/Microsoft/Windows/WER/Temp"),
    ]:
        if p.exists():
            paths.append(p)
    return paths


def scan_thumbcache() -> list[Path]:
    p = _expand("%LOCALAPPDATA%\\Microsoft\\Windows\\Explorer")
    return [p] if p.exists() else []


def scan_font_cache() -> list[Path]:
    p = _expand("%LOCALAPPDATA%\\FontCache")
    return [p] if p.exists() else []


def scan_prefetch() -> list[Path]:
    return [Path("C:/Windows/Prefetch")]


def scan_delivery_optimization() -> list[Path]:
    return [Path("C:/Windows/SoftwareDistribution/DeliveryOptimization")]


def scan_hibernate() -> list[Path]:
    p = Path("C:/hiberfil.sys")
    return [p] if p.exists() else []


# ---------- Custom clean handlers ----------

def clean_recycle_bin(item: CleanupItem) -> tuple[int, int]:
    """Empty Recycle Bin via Windows API."""
    import ctypes
    SHERB_NOCONFIRMATION = 0x1
    SHERB_NOPROGRESSUI = 0x2
    SHERB_NOSOUND = 0x4
    flags = SHERB_NOCONFIRMATION | SHERB_NOPROGRESSUI | SHERB_NOSOUND
    try:
        result = ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, flags)
        return (1, 0) if result == 0 else (0, 1)
    except Exception:
        return (0, 1)


def clean_windows_update(item: CleanupItem) -> tuple[int, int]:
    """Stop wuauserv, clear cache, restart service."""
    try:
        subprocess.run(["net", "stop", "wuauserv"], capture_output=True, timeout=30)
    except Exception:
        pass
    deleted = skipped = 0
    for p in item.paths:
        d, s = _clear_dir_contents(p)
        deleted += d
        skipped += s
    try:
        subprocess.run(["net", "start", "wuauserv"], capture_output=True, timeout=30)
    except Exception:
        pass
    return deleted, skipped


def clean_thumbcache(item: CleanupItem) -> tuple[int, int]:
    """Delete only thumbcache_*.db / iconcache_*.db files."""
    deleted = skipped = 0
    for p in item.paths:
        if not p.exists():
            continue
        for f in glob.glob(str(p / "thumbcache_*.db")) + glob.glob(str(p / "iconcache_*.db")):
            try:
                os.unlink(f)
                deleted += 1
            except Exception:
                skipped += 1
    return deleted, skipped


def clean_hibernate(item: CleanupItem) -> tuple[int, int]:
    """Disable hibernation (auto-deletes hiberfil.sys)."""
    try:
        r = subprocess.run(
            ["powercfg", "/h", "off"],
            capture_output=True, timeout=15, text=True
        )
        return (1, 0) if r.returncode == 0 else (0, 1)
    except Exception:
        return (0, 1)


# ---------- Task list ----------

def all_tasks() -> list[CleanupItem]:
    return [
        CleanupItem(
            id="user_temp",
            name="User Temp Files",
            description="Temporary files from your user account — safe to delete",
            risk="safe",
            default_checked=True,
            paths=scan_user_temp(),
        ),
        CleanupItem(
            id="windows_temp",
            name="System Temp Files",
            description="Windows system-wide temporary files",
            risk="safe",
            default_checked=True,
            paths=scan_windows_temp(),
        ),
        CleanupItem(
            id="recycle_bin",
            name="Recycle Bin",
            description="Empty Recycle Bin (cannot be undone)",
            risk="safe",
            default_checked=True,
            paths=scan_recycle_bin(),
            custom_clean=clean_recycle_bin,
        ),
        CleanupItem(
            id="windows_update",
            name="Windows Update Cache",
            description="Download cache for already-installed updates",
            risk="safe",
            default_checked=True,
            paths=scan_windows_update(),
            custom_clean=clean_windows_update,
        ),
        CleanupItem(
            id="browser_cache",
            name="Browser Cache",
            description="Edge, Chrome, Firefox & Brave cached data",
            risk="safe",
            default_checked=True,
            paths=scan_browser_cache(),
        ),
        CleanupItem(
            id="wer",
            name="Error Reports",
            description="Windows Error Reporting (WER) logs",
            risk="safe",
            default_checked=True,
            paths=scan_wer(),
        ),
        CleanupItem(
            id="thumbcache",
            name="Thumbnail Cache",
            description="Explorer thumbnail cache (rebuilds automatically)",
            risk="safe",
            default_checked=True,
            paths=scan_thumbcache(),
            custom_clean=clean_thumbcache,
        ),
        CleanupItem(
            id="prefetch",
            name="Prefetch",
            description="App launch acceleration cache (rebuilds automatically)",
            risk="safe",
            default_checked=True,
            paths=scan_prefetch(),
        ),
        CleanupItem(
            id="delivery_opt",
            name="Delivery Optimization",
            description="Windows update peer-to-peer cache",
            risk="safe",
            default_checked=True,
            paths=scan_delivery_optimization(),
        ),
        CleanupItem(
            id="hibernate",
            name="Hibernation File (Advanced)",
            description="Disable hibernation — frees space equal to RAM. Sleep mode unaffected",
            risk="medium",
            default_checked=False,
            paths=scan_hibernate(),
            custom_clean=clean_hibernate,
        ),
    ]


def calc_size(item: CleanupItem) -> int:
    """Compute size for a single cleanup item."""
    if item.id == "hibernate":
        p = Path("C:/hiberfil.sys")
        if p.exists():
            try:
                return p.stat().st_size
            except Exception:
                return 0
        return 0
    if item.id == "thumbcache":
        total = 0
        for p in item.paths:
            for f in glob.glob(str(p / "thumbcache_*.db")) + glob.glob(str(p / "iconcache_*.db")):
                try:
                    total += os.path.getsize(f)
                except Exception:
                    pass
        return total
    if item.id == "recycle_bin":
        # Sum recycle bins across all drives
        total = 0
        for drive_letter in "CDEFGH":
            rp = Path(f"{drive_letter}:/$Recycle.Bin")
            if rp.exists():
                total += _dir_size(rp)
        return total
    return sum(_dir_size(p) for p in item.paths)


def execute_task(item: CleanupItem) -> tuple[int, int]:
    """Execute cleanup. Returns (deleted, skipped)."""
    if item.custom_clean:
        return item.custom_clean(item)
    deleted = skipped = 0
    for p in item.paths:
        d, s = _clear_dir_contents(p)
        deleted += d
        skipped += s
    return deleted, skipped
