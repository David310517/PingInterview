"""
Network Ping Utility Script
--------------------------

- Reads a list of IP addresses from a text file (ip_list.txt)
- Pings each IP address, one by one
- Prints whether each host is reachable or unreachable
- Logs all results with timestamps to a new file (ping_log_YYYYMMDD_HHMMSS.txt)

Author: David 
GitHub: https://github.com/David310517
Date: July 2025
"""

import os
import platform
import subprocess
from datetime import datetime

def ping_host(ip):
    """
    Pings a single IP address once.
    Returns True if reachable, False if not.
    Automatically uses the correct command for Windows or Unix systems.
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        output = subprocess.check_output(
            ["ping", param, "1", ip],
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    """
    Main logic:
    - Reads IPs from 'ip_list.txt'
    - Pings each, prints status, and logs with timestamp
    - Writes results to 'ping_log_YYYYMMDD_HHMMSS.txt'
    """
    input_file = "ip_list.txt"
    log_file = f"ping_log_{datetime.now():%Y%m%d_%H%M%S}.txt"

    # Check that the input file exists
    if not os.path.exists(input_file):
        print(f"Input file '{input_file}' not found.")
        return

    # Read all IPs (skip blank lines)
    with open(input_file) as f:
        ips = [line.strip() for line in f if line.strip()]

    results = []
    for ip in ips:
        reachable = ping_host(ip)
        status = "reachable" if reachable else "unreachable"
        print(f"{ip}: {status}")
        # Add a timestamp to each log entry
        results.append(f"{datetime.now():%Y-%m-%d %H:%M:%S} - {ip}: {status}")

    # Write log file
    with open(log_file, "w") as f:
        for line in results:
            f.write(line + "\n")

    print(f"\nLog saved to {log_file}")

if __name__ == "__main__":
    main()
