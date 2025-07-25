"""
Ping Utility GUI (Python, PySide6)
----------------------------------
- Select a text file with IP addresses.
- Pings each IP address, shows if reachable or unreachable in a table.
- Logs results with timestamps to a file.
- Professional look with qdarkstyle.
Author: David
GitHub: https://github.com/David310517
"""

import os
import platform
import subprocess
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTableWidget, QTableWidgetItem, QPushButton, QFileDialog, QLabel
)
import qdarkstyle

# ========== Ping Logic ==========
def ping_host(ip):
    """
    Pings a single IP address using OS ping.
    Returns True if reachable, False if not.
    Automatically selects the right parameters for Windows/Linux/Mac.
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        subprocess.check_output(["ping", param, "1", ip], stderr=subprocess.STDOUT, universal_newlines=True)
        return True
    except subprocess.CalledProcessError:
        return False

# ========== GUI Application ==========
class PingGUI(QMainWindow):
    """
    Main Window for the Ping Utility GUI.
    - File picker for .txt list of IPs
    - Table for displaying ping results
    - "Start" button to run pings and log results
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ping Utility GUI")
        self.setMinimumSize(500, 400)
        central = QWidget(); self.setCentralWidget(central)
        vbox = QVBoxLayout(central)

        # --- File picker row ---
        file_row = QHBoxLayout()
        self.file_label = QLabel("No file selected")
        btn_file = QPushButton("Choose IP List")
        btn_file.clicked.connect(self.choose_file)
        file_row.addWidget(self.file_label)
        file_row.addWidget(btn_file)
        vbox.addLayout(file_row)

        # --- Table for results ---
        self.table = QTableWidget(0, 2)
        self.table.setHorizontalHeaderLabels(["IP Address", "Status"])
        vbox.addWidget(self.table)

        # --- Start button ---
        btn_start = QPushButton("Start")
        btn_start.clicked.connect(self.start_ping)
        vbox.addWidget(btn_start)

        # --- Variables to store IPs and path ---
        self.ips = []
        self.file_path = ""

    # --- File picker logic ---
    def choose_file(self):
        """
        Open file dialog to select .txt file with IPs.
        Loads IPs into self.ips and resets the result table.
        """
        path, _ = QFileDialog.getOpenFileName(self, "Select IP List", filter="Text Files (*.txt)")
        if path:
            self.file_path = path
            self.file_label.setText(os.path.basename(path))
            with open(path) as f:
                self.ips = [line.strip() for line in f if line.strip()]
            self.table.setRowCount(0)  # Clear previous results

    # --- Run ping and display/log results ---
    def start_ping(self):
        """
        Pings each loaded IP address.
        Updates the results table and writes a timestamped log file.
        """
        if not self.ips:
            self.file_label.setText("No IPs loaded!")
            return
        log_name = f"ping_log_{datetime.now():%Y%m%d_%H%M%S}.txt"
        results = []
        self.table.setRowCount(0)
        for ip in self.ips:
            reachable = ping_host(ip)
            status = "reachable" if reachable else "unreachable"
            results.append(f"{datetime.now():%Y-%m-%d %H:%M:%S} - {ip}: {status}")
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(ip))
            self.table.setItem(row, 1, QTableWidgetItem(status))
        with open(log_name, "w") as f:
            for line in results:
                f.write(line + "\n")
        self.file_label.setText(f"Done! Log: {log_name}")

# ========== Run the App ==========
if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    win = PingGUI()
    win.show()
    app.exec()
