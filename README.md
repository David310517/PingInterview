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

## 📂 Folder Structure

.
├── Circuitinfo19.py # Main Python script
├── /inputs/ # Folder for input Excel IP list
├── /outputs/ # Folder for generated Excel report
├── requirements.txt # Python dependencies
└── README.md

Copy
Edit
📋 2. Requirements
Explain how to install dependencies.

markdown
Copy
Edit
## 📋 Requirements

- Python 3.8 or higher
- Install dependencies:

```bash
pip install -r requirements.txt
yaml
Copy
Edit

---

### 🚀 3. How to Use (step-by-step)

Clear steps to run the tool:

```markdown
## 🚀 How to Use

1. Run the script:
   ```bash
   python circuitinfo19.py
Select the Excel file with router IPs (IP column required)

Enter SSH credentials in the GUI prompt

Wait for the tool to extract data

Output Excel will appear in /outputs/

yaml
Copy
Edit

---

### 📘 4. Example Use Case

Shows what the tool is for in real life:

```markdown
## 📘 Example Use Case

A network engineer preparing for an SD-WAN migration needs:

- All tunnel and private circuit details
- VRF and routing info per site
- An Excel inventory to pass to deployment teams

This tool automates that — no manual CLI work required.

