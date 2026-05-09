"""TidyDisk entry point."""
import sys
from pathlib import Path

# Ensure project root is on sys.path (PyInstaller _MEIPASS friendly)
ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core.elevate import ensure_admin


def main():
    # 1. Ensure we have admin privileges (will relaunch elevated if not)
    ensure_admin()

    # 2. Launch UI
    from ui.app import App
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
