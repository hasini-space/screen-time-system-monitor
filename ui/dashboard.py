import customtkinter as ctk
from monitor.system_stats import get_cpu_usage, get_ram_usage, get_system_uptime, format_uptime
from monitor.screen_time import get_active_window_title, parse_app_name
from monitor.database import init_db, log_app_time, get_today_usage

ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('blue')

class MonitorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        init_db()
        self.title('Screen Time & System Monitor')
        self.geometry('500x500')
        self.resizable(False, False)

        self.title_lbl = ctk.CTkLabel(self, text='System & Screen Time Dashboard', font=('Arial', 20, 'bold'))
        self.title_lbl.pack(pady=15)

        self.cpu_lbl = ctk.CTkLabel(self, text='CPU Usage: 0%', font=('Arial', 14))
        self.cpu_lbl.pack(pady=5)

        self.ram_lbl = ctk.CTkLabel(self, text='RAM Usage: 0%', font=('Arial', 14))
        self.ram_lbl.pack(pady=5)

        self.uptime_lbl = ctk.CTkLabel(self, text='System Uptime: Loading...', font=('Arial', 14))
        self.uptime_lbl.pack(pady=5)

        self.app_lbl = ctk.CTkLabel(self, text='Active App: Tracked Here', font=('Arial', 14, 'bold'), text_color='#1f538d')
        self.app_lbl.pack(pady=15)

        self.usage_frame = ctk.CTkFrame(self)
        self.usage_frame.pack(pady=10, fill='x', padx=20)
        
        self.usage_title = ctk.CTkLabel(self.usage_frame, text="Today's Screen Time:", font=('Arial', 14, 'bold'))
        self.usage_title.pack(pady=5)

        self.stat_labels = []
        for i in range(3):
            lbl = ctk.CTkLabel(self.usage_frame, text='', font=('Arial', 13))
            lbl.pack(pady=2)
            self.stat_labels.append(lbl)

        self.update_stats()

    def update_stats(self):
        cpu = get_cpu_usage()
        ram = get_ram_usage()
        uptime_sec = get_system_uptime()
        raw_window = get_active_window_title()
        app_name = parse_app_name(raw_window)

        log_app_time(app_name, 1)

        self.cpu_lbl.configure(text=f'CPU Usage: {cpu}%')
        self.ram_lbl.configure(text=f'RAM Usage: {ram}%')
        self.uptime_lbl.configure(text=f'System Uptime: {format_uptime(uptime_sec)}')
        self.app_lbl.configure(text=f'Active App: {app_name}')

        usage_data = get_today_usage()
        for idx, lbl in enumerate(self.stat_labels):
            if idx < len(usage_data):
                name, secs = usage_data[idx]
                lbl.configure(text=f'{name}: {format_uptime(secs)}')
            else:
                lbl.configure(text='')

        self.after(1000, self.update_stats)
