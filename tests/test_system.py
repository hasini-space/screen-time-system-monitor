from monitor.system_stats import get_cpu_usage, get_ram_usage, format_uptime

def test_cpu_usage_range():
    cpu = get_cpu_usage()
    assert 0 <= cpu <= 100

def test_ram_usage_range():
    ram = get_ram_usage()
    assert 0 <= ram <= 100

def test_format_uptime():
    assert format_uptime(3665) == "1h 1m 5s"
    assert format_uptime(60) == "0h 1m 0s"
