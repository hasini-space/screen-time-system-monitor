import pygetwindow as gw

def get_active_window_title():
    try:
        active_window = gw.getActiveWindow()
        if active_window and active_window.title:
            return active_window.title
        return "Unknown / Idle"
    except Exception:
        return "System"

def parse_app_name(window_title):
    if not window_title or window_title == "Unknown / Idle":
        return "Idle"
    separators = [" - ", " | ", " - "]
    for sep in separators:
        if sep in window_title:
            return window_title.split(sep)[-1].strip()
    return window_title.strip()
