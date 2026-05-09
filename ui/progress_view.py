"""Cleanup progress view."""
import threading
import queue
import tkinter as tk
from tkinter import ttk

from core.cleaner import clean_items
from assets.style import (
    COLOR_BG, COLOR_TEXT, COLOR_TEXT_LIGHT, COLOR_PRIMARY, COLOR_DANGER,
    FONT_TITLE, FONT_LARGE, FONT_NORMAL, FONT_SMALL, PAD,
)


class ProgressView(tk.Frame):
    def __init__(self, parent, app, items):
        super().__init__(parent, bg=COLOR_BG)
        self.app = app
        self.items = items
        self.queue: queue.Queue = queue.Queue()
        self.errors: list = []
        self.total_freed = 0

        self._build()
        self._start()

    def _build(self):
        tk.Label(
            self, text="Cleaning…",
            bg=COLOR_BG, fg=COLOR_TEXT, font=FONT_TITLE,
        ).pack(pady=(60, 8))

        self.subtitle = tk.Label(
            self, text="Please don't close this window",
            bg=COLOR_BG, fg=COLOR_TEXT_LIGHT, font=FONT_NORMAL,
        )
        self.subtitle.pack(pady=(0, 30))

        self.progress = ttk.Progressbar(
            self, length=440, mode="determinate",
            style="Cleaner.Horizontal.TProgressbar",
        )
        self.progress.pack(pady=10)
        self.progress["maximum"] = len(self.items)

        self.current = tk.Label(
            self, text="Preparing…",
            bg=COLOR_BG, fg=COLOR_PRIMARY, font=FONT_LARGE,
        )
        self.current.pack(pady=20)

        self.detail = tk.Label(
            self, text="",
            bg=COLOR_BG, fg=COLOR_TEXT_LIGHT, font=FONT_SMALL,
        )
        self.detail.pack()

    def _start(self):
        def worker():
            try:
                for event in clean_items(self.items):
                    self.queue.put(event)
            except Exception as e:
                self.queue.put({"type": "fatal", "error": str(e)})

        threading.Thread(target=worker, daemon=True).start()
        self.after(50, self._poll)

    def _poll(self):
        try:
            while True:
                event = self.queue.get_nowait()
                t = event["type"]
                if t == "start":
                    self.current.config(text=f"Cleaning: {event['name']}")
                    self.progress["value"] = event["index"]
                elif t == "done":
                    self.detail.config(
                        text=f"Cleaned {event['deleted']} item(s), skipped {event['skipped']}"
                    )
                elif t == "error":
                    self.errors.append((event["name"], event["error"]))
                elif t == "all_done":
                    self.total_freed = event["total_freed"]
                    self.progress["value"] = len(self.items)
                    self.after(500, lambda: self.app.show_result(
                        self.total_freed, self.errors
                    ))
                    return
                elif t == "fatal":
                    self.current.config(text=f"Cleanup error: {event['error']}", fg=COLOR_DANGER)
                    return
        except queue.Empty:
            pass
        self.after(50, self._poll)
