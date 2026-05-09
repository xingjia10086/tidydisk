"""Scan view: scan progress + checklist of cleanable items."""
import threading
import queue
import tkinter as tk
from tkinter import ttk, messagebox

from core.scanner import scan_all
from assets.style import (
    COLOR_BG, COLOR_CARD, COLOR_TEXT, COLOR_TEXT_LIGHT, COLOR_PRIMARY,
    COLOR_BORDER, COLOR_DANGER, FONT_TITLE, FONT_LARGE, FONT_NORMAL, FONT_SMALL,
    PAD, format_size,
)


class ScanView(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg=COLOR_BG)
        self.app = app
        self.queue: queue.Queue = queue.Queue()
        self.items: list = []
        self.checks: dict[str, tk.BooleanVar] = {}
        self.size_labels: dict[str, tk.Label] = {}

        self._build_scanning()
        self._start_scan()

    # -------- Scanning view --------

    def _build_scanning(self):
        for w in self.winfo_children():
            w.destroy()

        tk.Label(
            self, text="Scanning C drive…",
            bg=COLOR_BG, fg=COLOR_TEXT, font=FONT_TITLE,
        ).pack(pady=(60, 20))

        self.progress = ttk.Progressbar(
            self, length=400, mode="determinate",
            style="Cleaner.Horizontal.TProgressbar",
        )
        self.progress.pack(pady=10)

        self.status = tk.Label(
            self, text="Preparing…",
            bg=COLOR_BG, fg=COLOR_TEXT_LIGHT, font=FONT_NORMAL,
        )
        self.status.pack(pady=10)

    def _start_scan(self):
        def progress_cb(done, total, name):
            self.queue.put(("progress", done, total, name))

        def worker():
            try:
                items = scan_all(progress_cb)
                self.queue.put(("done", items))
            except Exception as e:
                self.queue.put(("error", str(e)))

        threading.Thread(target=worker, daemon=True).start()
        self.after(50, self._poll_queue_scanning)

    def _poll_queue_scanning(self):
        try:
            while True:
                msg = self.queue.get_nowait()
                kind = msg[0]
                if kind == "progress":
                    _, done, total, name = msg
                    self.progress["maximum"] = total
                    self.progress["value"] = done
                    self.status.config(text=f"Checked: {name}  ({done}/{total})")
                elif kind == "done":
                    self.items = msg[1]
                    self._build_results()
                    return
                elif kind == "error":
                    self.status.config(text=f"Scan failed: {msg[1]}", fg=COLOR_DANGER)
                    return
        except queue.Empty:
            pass
        self.after(50, self._poll_queue_scanning)

    # -------- Results view --------

    def _build_results(self):
        for w in self.winfo_children():
            w.destroy()

        tk.Label(
            self, text="Scan complete — choose what to clean",
            bg=COLOR_BG, fg=COLOR_TEXT, font=FONT_TITLE,
        ).pack(pady=(20, 4))

        tk.Label(
            self, text="Safe items are pre-selected. Advanced items must be enabled manually.",
            bg=COLOR_BG, fg=COLOR_TEXT_LIGHT, font=FONT_SMALL,
        ).pack(pady=(0, 12))

        # Scrollable list
        outer = tk.Frame(self, bg=COLOR_BG)
        outer.pack(padx=PAD * 2, pady=8, fill="both", expand=True)

        canvas = tk.Canvas(outer, bg=COLOR_CARD, highlightthickness=1,
                           highlightbackground=COLOR_BORDER, height=300)
        scrollbar = ttk.Scrollbar(outer, orient="vertical", command=canvas.yview)
        inner = tk.Frame(canvas, bg=COLOR_CARD)

        inner.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=inner, anchor="nw", width=500)
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        def on_mousewheel(e):
            canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")
        canvas.bind_all("<MouseWheel>", on_mousewheel)

        for item in self.items:
            self._build_row(inner, item)

        # Footer: total + buttons
        bottom = tk.Frame(self, bg=COLOR_BG)
        bottom.pack(fill="x", padx=PAD * 2, pady=PAD)

        self.total_label = tk.Label(
            bottom, text="", bg=COLOR_BG, fg=COLOR_PRIMARY,
            font=(FONT_TITLE[0], 14, "bold"),
        )
        self.total_label.pack(side="left")

        ttk.Button(
            bottom, text="Back",
            style="Secondary.TButton",
            command=self.app.show_home,
        ).pack(side="right", padx=(8, 0))

        self.clean_btn = tk.Button(
            bottom, text="✨  Clean Now",
            font=(FONT_TITLE[0], 12, "bold"),
            bg=COLOR_PRIMARY, fg="white",
            activebackground="#1D4ED8", activeforeground="white",
            relief="flat", cursor="hand2",
            padx=24, pady=10,
            command=self._on_clean,
        )
        self.clean_btn.pack(side="right")

        self._update_total()

    def _build_row(self, parent, item):
        row = tk.Frame(parent, bg=COLOR_CARD)
        row.pack(fill="x", padx=PAD, pady=4)

        var = tk.BooleanVar(value=item.default_checked and item.size_bytes > 0)
        self.checks[item.id] = var

        cb = tk.Checkbutton(
            row, variable=var, bg=COLOR_CARD,
            activebackground=COLOR_CARD,
            command=self._update_total,
            cursor="hand2",
        )
        cb.pack(side="left")

        text_frame = tk.Frame(row, bg=COLOR_CARD)
        text_frame.pack(side="left", fill="x", expand=True, padx=(4, 8))

        name_color = COLOR_TEXT
        if item.risk == "medium":
            name_color = "#F59E0B"
        tk.Label(
            text_frame, text=item.name,
            bg=COLOR_CARD, fg=name_color, font=FONT_NORMAL,
            anchor="w",
        ).pack(fill="x")
        tk.Label(
            text_frame, text=item.description,
            bg=COLOR_CARD, fg=COLOR_TEXT_LIGHT, font=FONT_SMALL,
            anchor="w",
        ).pack(fill="x")

        size_text = format_size(item.size_bytes) if item.size_bytes > 0 else "—"
        size_label = tk.Label(
            row, text=size_text,
            bg=COLOR_CARD, fg=COLOR_TEXT, font=FONT_NORMAL,
            width=10, anchor="e",
        )
        size_label.pack(side="right")
        self.size_labels[item.id] = size_label

        if item.size_bytes == 0:
            cb.configure(state="disabled")

    def _update_total(self):
        total = 0
        for item in self.items:
            if self.checks.get(item.id) and self.checks[item.id].get():
                total += item.size_bytes
        self.total_label.config(text=f"Total to free: {format_size(total)}")

    def _on_clean(self):
        selected = [
            item for item in self.items
            if self.checks.get(item.id) and self.checks[item.id].get()
        ]
        if not selected:
            return
        if messagebox.askyesno(
            "Confirm Clean",
            f"This will clean {len(selected)} item(s). The action cannot be undone.\n\nContinue?",
            parent=self,
        ):
            self.app.show_progress(selected)
