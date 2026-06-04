import time
from monitor.system_stats import get_cpu_usage, get_ram_usage
from monitor.screen_time import get_active_window_title, parse_app_name
from monitor.database import init_db, log_app_time

def run_tracker():
    init_db()
    print('Screen Time Background Tracker Started...')
    while True:
        try:
            raw_window = get_active_window_title()
            app_name = parse_app_name(raw_window)
            
            # Log 1 second of active usage to the database
            log_app_time(app_name, 1)
            
            # Sleep for 1 second before checking again
            time.sleep(1)
        except Exception as e:
            time.sleep(2)  # Avoid crashing on unexpected system hitches

if __name__ == "__main__":
    run_tracker()
