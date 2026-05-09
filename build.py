"""PyInstaller build script. Usage: python build.py"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

# Force UTF-8 output (Windows CI defaults to cp1252)
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
BUILD = ROOT / "build"

BUILD_NAME = "TidyDisk"


def main():
    # Clean previous artifacts
    for d in (DIST, BUILD):
        if d.exists():
            shutil.rmtree(d, ignore_errors=True)

    icon = ROOT / "assets" / "icon.ico"
    icon_arg = ["--icon", str(icon)] if icon.exists() else []

    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--windowed",
        "--uac-admin",
        "--name", BUILD_NAME,
        "--add-data", f"{ROOT / 'assets'}{os.pathsep}assets",
        *icon_arg,
        str(ROOT / "main.py"),
    ]

    print("Running PyInstaller ...")
    r = subprocess.run(cmd, cwd=ROOT)
    if r.returncode != 0:
        sys.exit(r.returncode)

    exe = DIST / f"{BUILD_NAME}.exe"
    if exe.exists():
        size_mb = exe.stat().st_size / 1024 / 1024
        print(f"\nBuild OK: {exe} ({size_mb:.1f} MB)")
    else:
        print("Build failed: exe not found")
        sys.exit(1)


if __name__ == "__main__":
    main()
