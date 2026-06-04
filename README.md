# 🖥️ Advanced Screen Time & System Performance Monitor

An automated, asynchronous desktop monitoring package built in Python that tracks real-time window-level productivity analytics along with hardware core utilization. Logs engine data natively into an isolated SQLite tracking layer.

## 🚀 Core Architectural Engine
- **Continuous Silent Service Daemon**: Decoupled asynchronous foreground application listener running via independent headless virtualization.
- **Relational Ledger Analytics Engine**: Built-in SQLite3 transactional abstraction layer to handle continuous telemetry stream indexing.
- **Dark-Mode Matrix GUI Dashboard**: Client analytics visualization frame rendered completely native via CustomTkinter and Matplotlib.

## 🛠️ Technology Stack
* **Interface Frame**: CustomTkinter (Modernized Tkinter UX Engine)
* **Telemetry Core**: Psutil, PyGetWindow
* **Mathematical Pipelines**: Matplotlib, Pandas, OpenPyXL
* **Database Architecture**: SQLite3 Layer
* **Test Driven Engine**: Pytest Ecosystem

## 📦 Complete Deployment Architecture

### 1. Package Virtualization & Requirements Hydration
```bash
# Initialize and spin up local isolated workspace
python -m venv venv
venv\Scripts\activate

# Hydrate package distribution bindings
pip install -r requirements.txt
