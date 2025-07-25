🚦 Ping Utility Scripts

Welcome! This repo contains two simple network tools built in Python for basic connectivity checks and interviews.

---

## 🖥️ 1. **Ping Utility – CLI Version**

A command-line tool to:
- Read a list of IP addresses from a `.txt` file
- Ping each IP address
- Print and log whether each host is **reachable** or **unreachable**
- Save results to a timestamped log file

**How to use:**
1. Create `ip_list.txt` (one IP per line).
2. Run:
   ```bash
   python Pinger.py
Results are printed in the terminal and saved in ping_log_YYYYMMDD_HHMMSS.txt.

Dependencies:
None (uses Python standard libraries)

🖱️ 2. Ping Utility – GUI Version (PySide6)
A user-friendly, modern GUI app to:

Select a .txt file with IP addresses 📄

Click "Start" to ping all hosts

View results in a table instantly (IP, status ✅/❌)

Log results (with timestamps) to a file 🕑

Stylish dark theme thanks to qdarkstyle 🌑

How to use:

Prepare your ip_list.txt file as above.

Install dependencies:

pip install PySide6 qdarkstyle
Run:

python pingergui.py
Use the GUI to select your IP list and view results.

🛠️ Requirements
Python 3.8 or higher

For GUI version:
pip install PySide6 qdarkstyle

