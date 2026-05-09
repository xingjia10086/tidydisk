"""UI style constants."""

# Colors
COLOR_BG = "#F5F7FA"
COLOR_CARD = "#FFFFFF"
COLOR_PRIMARY = "#2563EB"
COLOR_PRIMARY_HOVER = "#1D4ED8"
COLOR_SUCCESS = "#10B981"
COLOR_DANGER = "#EF4444"
COLOR_TEXT = "#1F2937"
COLOR_TEXT_LIGHT = "#6B7280"
COLOR_BORDER = "#E5E7EB"

# Fonts (use Segoe UI on EN locale; fall back if absent)
FONT_FAMILY = "Segoe UI"
FONT_TITLE = (FONT_FAMILY, 18, "bold")
FONT_LARGE = (FONT_FAMILY, 14)
FONT_NORMAL = (FONT_FAMILY, 11)
FONT_SMALL = (FONT_FAMILY, 9)
FONT_BUTTON = (FONT_FAMILY, 12, "bold")

# Sizes
WINDOW_WIDTH = 580
WINDOW_HEIGHT = 600
PAD = 16


def format_size(size_bytes: int) -> str:
    """Format bytes as a human-readable string."""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    if size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    if size_bytes < 1024 ** 3:
        return f"{size_bytes / 1024 ** 2:.1f} MB"
    return f"{size_bytes / 1024 ** 3:.2f} GB"
