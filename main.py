from ui.dashboard import MonitorApp
import time
from monitor.screen_time import get_active_window_title, parse_app_name

if __name__ == '__main__':
    print('=== Tracker Debug Mode ===')
    print('Current Active Window test:')
    raw = get_active_window_title()
    print(f'Raw Title: {raw}')
    print(f'Parsed App: {parse_app_name(raw)}')
    print('---------------------------')
    print('Launching Dashboard UI...')
    
    app = MonitorApp()
    app.mainloop()
