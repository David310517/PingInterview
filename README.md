# Cisco Circuit Info Tool (Python + GUI)

This tool automates the extraction of circuit-related information from Cisco routers using SSH. It was designed to assist with SD-WAN migrations and WAN inventory audits by providing a fast, Excel-based overview of tunnel interfaces, private subinterfaces, VRF assignments, and QoS data.

## 🔧 Features

- ✅ GUI-based tool (PySide6)
- 🔐 Secure SSH connections via Netmiko
- 📋 Reads device IPs from an Excel file
- 📥 Runs commands like:
  - `show run`
  - `show ip int brief`
  - `show ip route vrf`
  - `show interface description`
  - `show cdp neighbors`
- 📤 Outputs a clean Excel file with:
  - One column per device
  - Circuit descriptions and routing blocks
- 💡 Auto-detects tunnels, VRFs, private interfaces
- 🧠 Optional: fiber handoff hints, CDP fallback

## 🖼️ Screenshot

![circuitinfo-tool-screenshot](screenshot.png)

## 📂 Folder Structure

├── circuitinfo19.py # Main Python script
├── /inputs # Folder for your IP Excel list
├── /outputs # Generated circuit Excel report
├── requirements.txt # Python dependencies

markdown
Copy
Edit

## 📋 Requirements

- Python 3.8+
- Install dependencies:
```bash
pip install -r requirements.txt
🚀 How to Use
Run the script:

bash
Copy
Edit
python circuitinfo19.py
Select your Excel file with router IPs (must have a column titled IP)

Enter your SSH credentials in the popup

Let it run — the output will be saved in /outputs

📌 Notes
Only the IP address is required per device; hostname is optional

SSH access must be available from your machine to the routers

Output Excel contains raw interface data + organized circuit descriptions

📘 Example Use Case
A network team uses this tool before an SD-WAN migration to:

Discover physical and logical WAN circuits

Identify VRFs and subinterfaces

Create a migration inventory automatically

📄 License
This tool is intended for internal network engineering use. Feel free to fork or improve with attribution.

