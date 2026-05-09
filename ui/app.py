"""Main app: tkinter window manager + view switching."""
from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from assets.style import (
    COLOR_BG, COLOR_TEXT, FONT_FAMILY,
    WINDOW_WIDTH, WINDOW_HEIGHT,
)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TidyDisk — One-Click C Drive Cleaner")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.configure(bg=COLOR_BG)
        self.resizable(False, False)

        # Center on screen
        self.update_idletasks()
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - WINDOW_WIDTH) // 2
        y = (sh - WINDOW_HEIGHT) // 2
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")

        self._setup_styles()

        self.container = tk.Frame(self, bg=COLOR_BG)
        self.container.pack(fill="both", expand=True)

        self.current_view: tk.Frame | None = None
        self.show_home()

    def _setup_styles(self):
        style = ttk.Style(self)
        try:
            style.theme_use("vista")
        except tk.TclError:
            style.theme_use("clam")

        style.configure(
            "Primary.TButton",
            font=(FONT_FAMILY, 12, "bold"),
            padding=(20, 10),
        )
        style.configure(
            "Secondary.TButton",
            font=(FONT_FAMILY, 11),
            padding=(16, 8),
        )
        style.configure(
            "Cleaner.Horizontal.TProgressbar",
            thickness=12,
        )

    def switch_view(self, view_factory):
        if self.current_view is not None:
            self.current_view.destroy()
        self.current_view = view_factory(self.container, self)
        self.current_view.pack(fill="both", expand=True)

    def show_home(self):
        from ui.home_view import HomeView
        self.switch_view(HomeView)

    def show_scan(self):
        from ui.scan_view import ScanView
        self.switch_view(ScanView)

    def show_progress(self, items):
        from ui.progress_view import ProgressView
        self.switch_view(lambda parent, app: ProgressView(parent, app, items))

    def show_result(self, total_freed: int, errors: list):
        from ui.result_view import ResultView
        self.switch_view(lambda parent, app: ResultView(parent, app, total_freed, errors))
