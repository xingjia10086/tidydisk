"""Result view shown when cleanup finishes."""
import tkinter as tk
from tkinter import ttk

from core.scanner import get_drive_info
from assets.style import (
    COLOR_BG, COLOR_CARD, COLOR_TEXT, COLOR_TEXT_LIGHT, COLOR_PRIMARY,
    COLOR_SUCCESS, COLOR_BORDER, FONT_TITLE, FONT_LARGE, FONT_NORMAL,
    FONT_SMALL, PAD, format_size,
)


class ResultView(tk.Frame):
    def __init__(self, parent, app, total_freed, errors):
        super().__init__(parent, bg=COLOR_BG)
        self.app = app
        self.total_freed = total_freed
        self.errors = errors
        self._build()

    def _build(self):
        # Big checkmark
        tk.Label(
            self, text="✅",
            bg=COLOR_BG, fg=COLOR_SUCCESS,
            font=("Segoe UI Emoji", 48),
        ).pack(pady=(50, 8))

        tk.Label(
            self, text="All done",
            bg=COLOR_BG, fg=COLOR_TEXT, font=FONT_TITLE,
        ).pack(pady=(0, 30))

        # Freed-space card
        card = tk.Frame(
            self, bg=COLOR_CARD,
            highlightbackground=COLOR_BORDER, highlightthickness=1,
        )
        card.pack(padx=PAD * 3, pady=10, fill="x")

        tk.Label(
            card, text="Freed this run",
            bg=COLOR_CARD, fg=COLOR_TEXT_LIGHT, font=FONT_NORMAL,
        ).pack(pady=(PAD, 4))

        tk.Label(
            card, text=format_size(self.total_freed),
            bg=COLOR_CARD, fg=COLOR_SUCCESS,
            font=(FONT_TITLE[0], 28, "bold"),
        ).pack()

        # Current free space
        used, free, total = get_drive_info("C")
        tk.Label(
            card, text=f"C drive: {format_size(free)} free of {format_size(total)}",
            bg=COLOR_CARD, fg=COLOR_TEXT, font=FONT_NORMAL,
        ).pack(pady=(8, PAD))

        # Skipped errors
        if self.errors:
            err_frame = tk.Frame(self, bg=COLOR_BG)
            err_frame.pack(padx=PAD * 3, pady=PAD, fill="x")
            tk.Label(
                err_frame,
                text=f"⚠ {len(self.errors)} item(s) skipped (locked or no permission)",
                bg=COLOR_BG, fg="#F59E0B", font=FONT_SMALL,
            ).pack()

        # Done button
        btn = tk.Button(
            self, text="Done",
            font=(FONT_TITLE[0], 12, "bold"),
            bg=COLOR_PRIMARY, fg="white",
            activebackground="#1D4ED8", activeforeground="white",
            relief="flat", cursor="hand2",
            padx=40, pady=12,
            command=self.app.destroy,
        )
        btn.pack(pady=30)

        # Scan again
        ttk.Button(
            self, text="Scan Again",
            style="Secondary.TButton",
            command=self.app.show_home,
        ).pack()
