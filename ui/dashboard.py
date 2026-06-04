import customtkinter as ctk
import pandas as pd
import sqlite3
from datetime import date
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from monitor.system_stats import get_cpu_usage, get_ram_usage, get_system_uptime, format_uptime
from monitor.screen_time import get_active_window_title, parse_app_name
from monitor.database import init_db, log_app_time, get_today_usage, DB_FILE

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class MonitorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        init_db()
        self.title("Screen Time & System Monitor")
        self.geometry("800x550")
        self.resizable(False, False)

        # Left Panel: Numerical Statistics & Action Buttons
        self.left_frame = ctk.CTkFrame(self, width=350)
        self.left_frame.pack(side="left", fill="both", expand=True, padx=15, pady=15)

        self.title_lbl = ctk.CTkLabel(self.left_frame, text="System Dashboard", font=("Arial", 20, "bold"))
        self.title_lbl.pack(pady=15)

        self.cpu_lbl = ctk.CTkLabel(self.left_frame, text="CPU Usage: 0%", font=("Arial", 14))
        self.cpu_lbl.pack(pady=5)

        self.ram_lbl = ctk.CTkLabel(self.left_frame, text="RAM Usage: 0%", font=("Arial", 14))
        self.ram_lbl.pack(pady=5)

        self.uptime_lbl = ctk.CTkLabel(self.left_frame, text="System Uptime: Loading...", font=("Arial", 14))
        self.uptime_lbl.pack(pady=5)

        self.app_lbl = ctk.CTkLabel(self.left_frame, text="Active App: Tracked Here", font=("Arial", 14, "bold"), text_color="#1f538d")
        self.app_lbl.pack(pady=15)

        self.export_btn = ctk.CTkButton(self.left_frame, text="Export Logs to Excel", command=self.export_to_excel)
        self.export_btn.pack(side="bottom", pady=20)

        # Right Panel: Visual Analytics Breakdown
        self.right_frame = ctk.CTkFrame(self, width=400, fg_color="transparent")
        self.right_frame.pack(side="right", fill="both", expand=True, padx=15, pady=15)

        self.chart_title = ctk.CTkLabel(self.right_frame, text="Today's Time Breakdown", font=("Arial", 16, 'bold'))
        self.chart_title.pack(pady=5)

        # Embed Matplotlib Dark Canvas
        plt.style.use("dark_background")
        self.fig, self.ax = plt.subplots(figsize=(4, 4), dpi=100)
        self.fig.patch.set_facecolor("#2b2b2b")
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.right_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

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

        # Re-render the Dynamic Pie Chart
        usage_data = get_today_usage()
        self.ax.clear()
        if usage_data:
            labels = [item[0] for item in usage_data]
            sizes = [item[1] for item in usage_data]
            self.ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 9})
        else:
            self.ax.text(0.5, 0.5, 'No tracking data recorded yet today.', ha='center', va='center')
        self.ax.axis('equal')
        self.canvas.draw()

        self.after(1000, self.update_stats)

    def export_to_excel(self):
        try:
            conn = sqlite3.connect(DB_FILE)
            df = pd.read_sql_query('SELECT usage_date as Date, app_name as Application, duration_seconds as [Duration (Sec)] FROM app_usage', conn)
            conn.close()
            
            filename = f'ScreenTime_Report_{date.today()}.xlsx'
            df.to_excel(filename, index=False)
            self.export_btn.configure(text='Export Successful!', fg_color='green')
            self.after(3000, lambda: self.export_btn.configure(text='Export Logs to Excel', fg_color=['#3a7ebf', '#1f538d']))
        except Exception as e:
            print(f'Export failed: {e}')