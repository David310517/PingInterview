# Cisco Circuit Info Tool (Python + GUI)

This tool automates the extraction of circuit-related information from Cisco routers using SSH.  
It's designed to support SD-WAN migrations and WAN inventory audits by generating a fast, Excel-based overview of:

- Tunnel interfaces
- Private subinterfaces
- VRF assignments
- QoS blocks
- CDP neighbors (fallback)

---

## 🔧 Features

- ✅ GUI-based tool using PySide6
- 🔐 SSH access via Netmiko
- 📋 Reads router IPs from Excel
- 🧠 Intelligent parsing of tunnel, VRF, and private subinterface blocks
- 📤 Outputs a clean Excel file:
  - One column per device
  - Circuit descriptions and routing layout
- 💡 Optional: CDP-based discovery and fiber handoff hints

---

## 📸 Screenshot


<img width="949" height="668" alt="collector" src="https://github.com/user-attachments/assets/f2731530-6142-48ab-be0d-96c229499b10" />


```markdown
![Circuit Info Tool Screenshot](circuitinfo-tool-screenshot.png)
