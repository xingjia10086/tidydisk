"""Scanner: compute size of each cleanup item in parallel."""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Callable

from .tasks import CleanupItem, all_tasks, calc_size


def scan_all(progress_cb: Callable[[int, int, str], None] | None = None) -> list[CleanupItem]:
    """Scan all cleanup items in parallel.

    progress_cb(done, total, current_name) is invoked after each item completes.
    """
    items = all_tasks()
    total = len(items)
    done = 0

    with ThreadPoolExecutor(max_workers=min(8, total)) as pool:
        futures = {pool.submit(calc_size, item): item for item in items}
        for fut in as_completed(futures):
            item = futures[fut]
            try:
                item.size_bytes = fut.result()
            except Exception:
                item.size_bytes = 0
            done += 1
            if progress_cb:
                try:
                    progress_cb(done, total, item.name)
                except Exception:
                    pass

    return items


def get_drive_info(drive: str = "C") -> tuple[int, int, int]:
    """Return (used_bytes, free_bytes, total_bytes)."""
    import ctypes
    free = ctypes.c_ulonglong(0)
    total = ctypes.c_ulonglong(0)
    available = ctypes.c_ulonglong(0)
    ctypes.windll.kernel32.GetDiskFreeSpaceExW(
        ctypes.c_wchar_p(f"{drive}:\\"),
        ctypes.byref(available),
        ctypes.byref(total),
        ctypes.byref(free),
    )
    used = total.value - free.value
    return used, free.value, total.value
