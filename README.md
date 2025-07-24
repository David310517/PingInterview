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

<img width="606" height="276" alt="Picture4" src="https://github.com/user-attachments/assets/760925a2-2ac1-49c4-aa95-bd914085f4ee" />


```markdown
![Circuit Info Tool Screenshot](circuitinfo-tool-screenshot.png)
