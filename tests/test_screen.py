from monitor.screen_time import parse_app_name

def test_parse_app_name_chrome():
    title = "Inbox (12^) - user@gmail.com - Google Chrome"
    assert parse_app_name(title) == "Google Chrome"

def test_parse_app_name_vs_code():
    title = "main.py - screen-monitor - Visual Studio Code"
    assert parse_app_name(title) == "Visual Studio Code"

def test_parse_app_name_simple():
    title = "Notepad"
    assert parse_app_name(title) == "Notepad"

def test_parse_app_name_empty():
    assert parse_app_name("") == "Idle"
    assert parse_app_name("Unknown / Idle") == "Idle"
