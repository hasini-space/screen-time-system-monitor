import psutil
import time

def get_cpu_usage():
    return psutil.cpu_percent(interval=None)

def get_ram_usage():
    return psutil.virtual_memory().percent

def get_system_uptime():
    boot_time = psutil.boot_time()
    current_time = time.time()
    return int(current_time - boot_time)

def format_uptime(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours}h {minutes}m {seconds}s"
