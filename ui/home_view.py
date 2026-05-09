"""Home view: drive usage card + Scan Now button."""
import tkinter as tk
from tkinter import ttk

from core.scanner import get_drive_info
from assets.style import (
    COLOR_BG, COLOR_CARD, COLOR_TEXT, COLOR_TEXT_LIGHT, COLOR_PRIMARY,
    COLOR_BORDER, FONT_TITLE, FONT_LARGE, FONT_NORMAL, FONT_SMALL,
    PAD, format_size,
)


class HomeView(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg=COLOR_BG)
        self.app = app
        self._build()

    def _build(self):
        # Title
        title = tk.Label(
            self, text="TidyDisk",
            bg=COLOR_BG, fg=COLOR_TEXT, font=(FONT_TITLE[0], 24, "bold"),
        )
        title.pack(pady=(40, 6))

        subtitle = tk.Label(
            self, text="Reclaim your C drive in one click. No bundleware. No telemetry.",
            bg=COLOR_BG, fg=COLOR_TEXT_LIGHT, font=FONT_NORMAL,
        )
        subtitle.pack(pady=(0, 30))

        # Drive info card
        card = tk.Frame(
            self, bg=COLOR_CARD,
            highlightbackground=COLOR_BORDER, highlightthickness=1,
        )
        card.pack(padx=PAD * 2, pady=10, fill="x")

        used, free, total = get_drive_info("C")
        pct = used / total * 100 if total else 0

        info_frame = tk.Frame(card, bg=COLOR_CARD)
        info_frame.pack(fill="x", padx=PAD, pady=PAD)

        left = tk.Frame(info_frame, bg=COLOR_CARD)
        left.pack(side="left")
        tk.Label(left, text="Free Space", bg=COLOR_CARD, fg=COLOR_TEXT_LIGHT,
                 font=FONT_SMALL).pack(anchor="w")
        tk.Label(left, text=format_size(free), bg=COLOR_CARD,
                 fg=COLOR_PRIMARY, font=(FONT_TITLE[0], 20, "bold")).pack(anchor="w")

        right = tk.Frame(info_frame, bg=COLOR_CARD)
        right.pack(side="right")
        tk.Label(right, text="Total", bg=COLOR_CARD, fg=COLOR_TEXT_LIGHT,
                 font=FONT_SMALL).pack(anchor="e")
        tk.Label(right, text=format_size(total), bg=COLOR_CARD,
                 fg=COLOR_TEXT, font=FONT_LARGE).pack(anchor="e")

        # Progress bar
        progress = ttk.Progressbar(
            card, length=400, mode="determinate",
            style="Cleaner.Horizontal.TProgressbar",
        )
        progress["maximum"] = 100
        progress["value"] = pct
        progress.pack(padx=PAD, pady=(0, 8), fill="x")

        # Usage text
        usage_color = "#EF4444" if pct >= 90 else (COLOR_TEXT if pct >= 70 else COLOR_TEXT_LIGHT)
        tk.Label(
            card,
            text=f"Used {format_size(used)} / {pct:.1f}%",
            bg=COLOR_CARD, fg=usage_color, font=FONT_NORMAL,
        ).pack(pady=(0, PAD))

        # Warning if critical
        if pct >= 90:
            tk.Label(
                self, text="⚠ Disk space is critical — clean now",
                bg=COLOR_BG, fg="#EF4444", font=FONT_NORMAL,
            ).pack(pady=(20, 0))

        # Scan button
        btn = tk.Button(
            self, text="🔍  Scan Now",
            font=(FONT_TITLE[0], 14, "bold"),
            bg=COLOR_PRIMARY, fg="white",
            activebackground="#1D4ED8", activeforeground="white",
            relief="flat", cursor="hand2",
            padx=40, pady=14,
            command=self.app.show_scan,
        )
        btn.pack(pady=40)

        # Hint
        hint = tk.Label(
            self,
            text="Scans temp files, recycle bin, browser caches, and more.\nNothing is deleted until you confirm.",
            bg=COLOR_BG, fg=COLOR_TEXT_LIGHT, font=FONT_SMALL,
            justify="center",
        )
        hint.pack(pady=(0, 20))
