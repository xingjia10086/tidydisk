"""Cleanup executor: clean items one by one, yielding progress events."""
from __future__ import annotations

from typing import Iterator

from .tasks import CleanupItem, execute_task


def clean_items(items: list[CleanupItem]) -> Iterator[dict]:
    """Clean each item in order, yielding progress events.

    Event types:
      {"type": "start", "index": i, "total": n, "name": str}
      {"type": "done", "index": i, "name": str, "size": int, "deleted": int, "skipped": int}
      {"type": "error", "index": i, "name": str, "error": str}
      {"type": "all_done", "total_freed": int}
    """
    total = len(items)
    total_freed = 0

    for i, item in enumerate(items):
        yield {"type": "start", "index": i, "total": total, "name": item.name}
        try:
            deleted, skipped = execute_task(item)
            total_freed += item.size_bytes
            yield {
                "type": "done",
                "index": i,
                "name": item.name,
                "size": item.size_bytes,
                "deleted": deleted,
                "skipped": skipped,
            }
        except Exception as e:
            yield {
                "type": "error",
                "index": i,
                "name": item.name,
                "error": str(e),
            }

    yield {"type": "all_done", "total_freed": total_freed}
