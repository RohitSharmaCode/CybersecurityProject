# Cybersecurity Monitoring Dashboard

A real-time cybersecurity monitoring dashboard built with Python that provides live visibility into system resources, network activity, running processes, and potentially risky network ports. The project is designed for educational purposes, cybersecurity awareness, and system monitoring.

---

## 📌 Features

### 🖥 System Monitoring

* Operating System information
* Hostname detection
* Local IP address detection
* Real-time CPU usage monitoring
* Real-time RAM usage monitoring

### 🌐 Network Monitoring

* Displays active network connections
* Shows local and remote addresses
* Displays connection states (ESTABLISHED, LISTEN, etc.)
* Highlights connections using potentially risky ports

### ⚙ Process Monitoring

* Lists currently running processes
* Displays Process IDs (PID)
* Shows CPU consumption per process
* Sorts processes by CPU utilization

### 🚨 Security Awareness

The dashboard identifies connections involving commonly targeted or historically insecure ports such as:

| Port | Service                       |
| ---- | ----------------------------- |
| 21   | FTP                           |
| 23   | Telnet                        |
| 135  | RPC                           |
| 139  | NetBIOS                       |
| 445  | SMB                           |
| 3389 | Remote Desktop Protocol (RDP) |

---

## 📷 Dashboard Overview

The dashboard consists of three primary sections:

### Header

Displays:

* Project title
* Current date and time

### System Information Panel

Displays:

* Operating System
* Hostname
* Local IP Address
* CPU Usage
* RAM Usage

### Active Connections Panel

Displays:

* Local Address
* Remote Address
* Connection Status
* Risk Indicator

### Running Processes Panel

Displays:

* PID
* Process Name
* CPU Utilization

---

## 🛠 Technology Stack

### Programming Language

* Python 3.8+

### Libraries

* psutil
* rich
* socket
* platform
* datetime

---

## 📂 Project Structure

```text
Cybersecurity-Monitoring-Dashboard/
│
├── cybersecurity_dashboard.py
├── README.md
└── requirements.txt
```

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Cybersecurity-Monitoring-Dashboard.git

cd Cybersecurity-Monitoring-Dashboard
```

### 2. Create Virtual Environment (Recommended)

Windows:

```bash
python -m venv venv

venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv

source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install psutil rich
```

---

## 📄 requirements.txt

```text
psutil
rich
```

---

## ▶ Running the Application

```bash
python cybersecurity_dashboard.py
```

The dashboard will automatically refresh every second and display the latest monitoring information.

---

## 🔍 How It Works

### System Information Collection

The application gathers:

```python
platform.system()
platform.release()
socket.gethostname()
psutil.cpu_percent()
psutil.virtual_memory()
```

to generate live system statistics.

---

### Network Connection Monitoring

The dashboard uses:

```python
psutil.net_connections()
```

to inspect active network connections and identify suspicious ports.

---

### Process Monitoring

The application continuously checks:

```python
psutil.process_iter()
```

to collect process information and rank them according to CPU usage.

---

## 🎯 Use Cases

### Cybersecurity Learning

Useful for students learning:

* Cybersecurity Fundamentals
* Network Security
* System Administration
* Security Monitoring
* Digital Forensics Basics

### Academic Projects

Can be used as:

* Final Year Project
* Internship Project
* Security Lab Assignment
* Resume Project

### Personal Monitoring

Users can:

* Monitor system health
* Identify unusual connections
* Track resource consumption
* Observe active services

---

## 🔒 Security Considerations

This project:

✅ Does not modify system settings

✅ Does not perform offensive security activities

✅ Does not exploit vulnerabilities

✅ Does not collect user data

✅ Operates entirely on the local machine

This project is intended solely for defensive monitoring and educational purposes.

---

## 🚀 Future Improvements

Potential enhancements include:

### Security Features

* Malware process detection
* Threat intelligence integration
* Blacklisted IP detection
* Suspicious process alerts
* File integrity monitoring

### Dashboard Improvements

* GUI version using PyQt
* Web dashboard using Flask
* Dark/Light themes
* Historical monitoring graphs

### Advanced Monitoring

* Packet capture analysis
* IDS integration
* SIEM-style logging
* Event correlation engine

### Notifications

* Email alerts
* Telegram alerts
* Discord alerts
* Slack integration

---

## 📚 Learning Outcomes

After understanding this project, you will gain knowledge about:

* System Monitoring
* Process Management
* Network Connections
* Cybersecurity Fundamentals
* Defensive Security Techniques
* Real-Time Monitoring Systems
* Python System Programming

---

## 🤝 Contributing

Contributions are welcome.

Possible contributions include:

* New security detection rules
* Performance optimizations
* User interface improvements
* Additional monitoring modules
* Documentation improvements

Steps:

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to your branch
5. Open a Pull Request

---

## ⚠ Disclaimer

This project is intended for educational, research, and defensive cybersecurity purposes only.

The author is not responsible for any misuse of this software. Users should ensure compliance with applicable laws, regulations, and organizational policies when monitoring systems.

---

## 📜 License

This project is released under the MIT License.

```text
MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge,
to any person obtaining a copy of this software
and associated documentation files...
```

---

## 👨‍💻 Author

**Rohit Sharma**

* MERN Stack Developer
* AI & Cybersecurity Enthusiast
* Competitive Programmer

