# 🔥 DarkForge - Ultimate Hacking Toolkit

<div align="center">

```
██████╗  █████╗ ██████╗ ██╗  ██╗███████╗ ██████╗ ██████╗  ██████╗ ███████╗
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔════╝
██║  ██║███████║██████╔╝█████╔╝ █████╗  ██║   ██║██████╔╝██║  ███╗█████╗  
██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝  
██████╔╝██║  ██║██║  ██║██║  ██╗██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
```

**🛡️ The Ultimate Penetration Testing & Security Research Toolkit**

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg)](https://github.com/sentinelzxofc/DarkForge)
[![Version](https://img.shields.io/badge/Version-2.1.0-red.svg)](https://github.com/sentinelzxofc/DarkForge/releases)

</div>

## 📋 Table of Contents

- [🎯 Overview](#-overview)
- [✨ Features](#-features)
- [🚀 Quick Installation](#-quick-installation)
- [📖 Usage](#-usage)
- [🛠️ Tools Included](#️-tools-included)
- [📱 Screenshots](#-screenshots)
- [🔧 Manual Installation](#-manual-installation)
- [🐧 Supported Platforms](#-supported-platforms)
- [🤝 Contributing](#-contributing)
- [⚖️ Legal Disclaimer](#️-legal-disclaimer)
- [📄 License](#-license)
- [👨‍💻 Author](#-author)

## 🎯 Overview

**DarkForge** is a comprehensive penetration testing and security research toolkit designed for cybersecurity professionals, ethical hackers, and security researchers. Built with Python, it provides a unified interface for various security testing tools and techniques.

### 🌟 Why DarkForge?

- **🔧 All-in-One Solution**: 19+ integrated security tools in a single interface
- **🎨 User-Friendly**: Intuitive menu-driven interface with colored output
- **⚡ Fast & Efficient**: Optimized for speed with multi-threading support
- **🔒 Educational Focus**: Perfect for learning cybersecurity concepts
- **🌐 Cross-Platform**: Works on Linux, macOS, and Windows
- **📚 Well-Documented**: Comprehensive documentation and examples

## ✨ Features

### 🔍 **Network & Infrastructure**
- **Network Scanner**: Discover active hosts on any network
- **Port Scanner**: Identify open ports and running services
- **WiFi Scanner**: Detect nearby wireless networks
- **Network Sniffer**: Monitor network connections in real-time
- **Subdomain Finder**: Enumerate subdomains for target domains

### 🛡️ **Vulnerability Assessment**
- **Vulnerability Scanner**: Automated web application security testing
- **SQL Injection Tester**: Test for SQL injection vulnerabilities
- **Web Crawler**: Discover hidden directories and files

### 🔐 **Cryptography & Encoding**
- **Encoder/Decoder**: Support for Base64, URL, Hex, ROT13, MD5, SHA256
- **Hash Cracker**: Dictionary-based hash cracking
- **Password Generator**: Generate secure passwords with custom parameters
- **Steganography**: Hide and extract secret messages

### 💥 **Payload Generation**
- **Reverse Shell Generator**: Bash, Python, and Netcat payloads
- **XSS Payload Library**: Cross-site scripting attack vectors
- **SQL Injection Payloads**: Database attack vectors
- **Command Injection**: System command injection payloads

### 🌍 **Information Gathering**
- **IP Locator**: Geolocation and ISP information
- **System Information**: Detailed system reconnaissance
- **File Metadata Extractor**: Extract hidden file information
- **Text Obfuscator**: Multiple text obfuscation techniques

### 💻 **System Tools**
- **Terminal Shell**: Interactive command execution
- **Ping Flood**: Network stress testing
- **File Analysis**: Comprehensive file examination

## 🚀 Quick Installation

### One-Line Installation (Recommended)

```bash
curl -sSL https://raw.githubusercontent.com/sentinelzxofc/DarkForge/main/install.sh | bash
```

### Alternative Installation Methods

<details>
<summary>📥 Download and Run</summary>

```bash
# Download the installer
wget https://raw.githubusercontent.com/sentinelzxofc/DarkForge/main/install.sh

# Make it executable
chmod +x install.sh

# Run the installer
./install.sh
```

</details>

<details>
<summary>🔄 Git Clone Method</summary>

```bash
# Clone the repository
git clone https://github.com/sentinelzxofc/DarkForge.git

# Navigate to directory
cd DarkForge

# Run the installer
chmod +x install.sh && ./install.sh
```

</details>

## 📖 Usage

### 🎮 Running DarkForge

After installation, you can run DarkForge in several ways:

```bash
# Method 1: Global command (if installed with installer)
darkforge

# Method 2: Direct execution
cd ~/.darkforge && python3 main.py

# Method 3: From source directory
python3 main.py
```

### 🎯 Quick Start Guide

1. **Launch DarkForge**:
   ```bash
   darkforge
   ```

2. **Select a tool** from the main menu (01-19)

3. **Follow the prompts** for each tool

4. **View results** in the colored terminal output

### 📋 Example Usage

```bash
# Network scanning example
darkforge
# Select option [01] Network Scanner
# Enter network: 192.168.1.0/24
# View discovered hosts

# Port scanning example
# Select option [02] Port Scanner  
# Enter target: example.com
# Enter port range: 1-1000
# View open ports and services
```

## 🛠️ Tools Included

| Tool | Description | Use Case |
|------|-------------|----------|
| 🌐 **Network Scanner** | Discover active hosts | Network reconnaissance |
| 🔍 **Port Scanner** | Identify open ports | Service enumeration |
| 💥 **Ping Flood** | Network stress testing | DoS testing |
| 🔤 **Encoder/Decoder** | Text encoding/decoding | Data manipulation |
| 🚀 **Payload Generator** | Create attack payloads | Penetration testing |
| 📍 **IP Locator** | Geolocation lookup | OSINT gathering |
| 🕵️ **Network Sniffer** | Monitor connections | Traffic analysis |
| 🕷️ **Web Crawler** | Website enumeration | Web reconnaissance |
| 💉 **SQL Injection Tester** | Database vulnerability testing | Web app security |
| 🔍 **Subdomain Finder** | Subdomain enumeration | Domain reconnaissance |
| 🔐 **Password Generator** | Secure password creation | Security hardening |
| 🔓 **Hash Cracker** | Password hash cracking | Credential recovery |
| 📡 **WiFi Scanner** | Wireless network discovery | WiFi security |
| 💻 **System Info** | System reconnaissance | Information gathering |
| 📄 **File Metadata** | File analysis | Digital forensics |
| 🎭 **Text Obfuscator** | Text manipulation | Evasion techniques |
| 🛡️ **Vulnerability Scanner** | Web security testing | Security assessment |
| 🔒 **Steganography** | Hidden message techniques | Covert communication |
| 💻 **Terminal Shell** | Command execution | System interaction |

## 📱 Screenshots

<details>
<summary>🖼️ View Screenshots</summary>

### Main Menu
```
╔═══════════════════════════════════════════════════════════════╗
║                        MAIN MENU                              ║
╠═══════════════════════════════════════════════════════════════╣
║  [01] Network Scanner          [11] Password Generator        ║
║  [02] Port Scanner             [12] Hash Cracker              ║
║  [03] Ping Flood               [13] WiFi Scanner              ║
║  [04] Encoder/Decoder          [14] System Info               ║
║  [05] Payload Generator        [15] File Metadata             ║
║  [06] IP Locator               [16] Text Obfuscator           ║
║  [07] Network Sniffer          [17] Vulnerability Scanner     ║
║  [08] Web Crawler              [18] Steganography             ║
║  [09] SQL Injection Tester     [19] Terminal Shell            ║
║  [10] Subdomain Finder         [00] Exit                      ║
╚═══════════════════════════════════════════════════════════════╝
```

### Network Scanner Output
```
[+] 192.168.1.1 - ACTIVE
[+] 192.168.1.10 - ACTIVE
[+] 192.168.1.15 - ACTIVE
[+] 192.168.1.20 - ACTIVE
[*] Scan complete! Found 4 active hosts
```

### Port Scanner Results
```
[+] Port 22/tcp - OPEN (SSH)
[+] Port 80/tcp - OPEN (HTTP)
[+] Port 443/tcp - OPEN (HTTPS)
[+] Port 3306/tcp - OPEN (MySQL)
[*] Scan complete! Found 4 open ports
```

</details>

## 🔧 Manual Installation

### Prerequisites

- **Python 3.6+**
- **pip3**
- **Internet connection**

### Dependencies

#### Python Packages
```bash
pip3 install requests colorama
```

#### System Tools (Linux/macOS)
```bash
# Debian/Ubuntu
sudo apt-get install python3 python3-pip net-tools iputils-ping netcat nmap curl wget git wireless-tools dnsutils

# Red Hat/CentOS/Fedora
sudo yum install python3 python3-pip net-tools iputils nc nmap curl wget git wireless-tools bind-utils

# Arch Linux
sudo pacman -S python python-pip net-tools iputils gnu-netcat nmap curl wget git wireless_tools bind-tools

# macOS (with Homebrew)
brew install python nmap netcat curl wget git
```

### Manual Setup

1. **Clone Repository**:
   ```bash
   git clone https://github.com/sentinelzxofc/DarkForge.git
   cd DarkForge
   ```

2. **Install Dependencies**:
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Make Executable**:
   ```bash
   chmod +x main.py
   ```

4. **Run DarkForge**:
   ```bash
   python3 main.py
   ```

## 🐧 Supported Platforms

| Platform | Status | Notes |
|----------|--------|-------|
| 🐧 **Linux** | ✅ Fully Supported | All features available |
| 🍎 **macOS** | ✅ Supported | Some tools require Homebrew |
| 🪟 **Windows** | ⚠️ Partial Support | Limited functionality |
| 🐳 **Docker** | ✅ Supported | Container available |
| ☁️ **Cloud** | ✅ Supported | Works on VPS/Cloud instances |

### Tested Distributions

- **Ubuntu** 18.04, 20.04, 22.04
- **Debian** 9, 10, 11
- **CentOS** 7, 8
- **Fedora** 34, 35, 36
- **Arch Linux**
- **Kali Linux**
- **Parrot Security OS**
- **macOS** 10.15+

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### 🐛 Bug Reports

1. Check existing issues first
2. Create detailed bug reports with:
   - OS and version
   - Python version
   - Steps to reproduce
   - Expected vs actual behavior
   - Error messages/logs

### 💡 Feature Requests

1. Search existing feature requests
2. Describe the feature clearly
3. Explain the use case
4. Provide implementation ideas if possible

### 🔧 Code Contributions

1. **Fork** the repository
2. **Create** a feature branch
3. **Make** your changes
4. **Test** thoroughly
5. **Submit** a pull request

### 📝 Development Setup

```bash
# Fork and clone your fork
git clone https://github.com/yourusername/DarkForge.git
cd DarkForge

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows

# Install development dependencies
pip install -r requirements-dev.txt

# Make your changes and test
python3 main.py
```

### 🎯 Contribution Guidelines

- Follow PEP 8 style guidelines
- Add docstrings to new functions
- Include error handling
- Test on multiple platforms
- Update documentation as needed

## ⚖️ Legal Disclaimer

> **⚠️ IMPORTANT: READ CAREFULLY BEFORE USING**

### 🎓 Educational Purpose

DarkForge is developed **exclusively for educational purposes** and **authorized security testing**. This tool is intended to help:

- **Security professionals** learn penetration testing techniques
- **Students** understand cybersecurity concepts
- **Researchers** conduct authorized security assessments
- **System administrators** test their own systems

### 🚫 Prohibited Uses

**DO NOT USE** this tool for:
- ❌ Unauthorized access to systems
- ❌ Illegal hacking activities
- ❌ Malicious attacks
- ❌ Any activity that violates local, state, or federal laws

### 👤 User Responsibility

By using DarkForge, you agree that:

1. **You are responsible** for complying with all applicable laws
2. **You will only use** this tool on systems you own or have explicit permission to test
3. **You understand** the legal implications of security testing
4. **You will not hold** the author responsible for any misuse

### 🛡️ Author Disclaimer

The author (@sentinelzxofc) of DarkForge:

- **Is not responsible** for any illegal use of this tool
- **Does not encourage** malicious activities
- **Provides this tool** "as-is" without warranties
- **Reserves the right** to modify or discontinue the project

### 📋 Best Practices

- ✅ Always obtain **written permission** before testing
- ✅ Use only in **controlled environments**
- ✅ Follow **responsible disclosure** practices
- ✅ Respect **privacy and data protection** laws
- ✅ Document your **testing activities**

### 🏛️ Legal Compliance

Users must ensure compliance with:
- Local and international laws
- Computer Fraud and Abuse Act (CFAA)
- General Data Protection Regulation (GDPR)
- Industry-specific regulations
- Organizational policies

**Remember: With great power comes great responsibility. Use DarkForge ethically and legally.**

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### MIT License Summary

- ✅ **Commercial use** allowed
- ✅ **Modification** allowed
- ✅ **Distribution** allowed
- ✅ **Private use** allowed
- ❌ **Liability** not provided
- ❌ **Warranty** not provided

## 👨‍💻 Author

<div align="center">

**[@sentinelzxofc](https://github.com/sentinelzxofc)**

*Cybersecurity Researcher & Ethical Hacker*

[![GitHub](https://img.shields.io/badge/GitHub-sentinelzxofc-black?style=for-the-badge&logo=github)](https://github.com/sentinelzxofc)
[![Twitter](https://img.shields.io/badge/Twitter-@sentinelzxofc-blue?style=for-the-badge&logo=twitter)](https://twitter.com/sentinelzxofc)

</div>

### 🤝 Connect & Support

- 🐛 **Report Issues**: [GitHub Issues](https://github.com/sentinelzxofc/DarkForge/issues)
- 💡 **Feature Requests**: [GitHub Discussions](https://github.com/sentinelzxofc/DarkForge/discussions)
- 📧 **Contact**: [Email](mailto:sentinelzxofc@proton.me)
- 💬 **Community**: [Discord Server](https://discord.gg/darkforge)

### ☕ Support the Project

If DarkForge has been helpful to you, consider supporting its development:

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-support-yellow?style=for-the-badge&logo=buy-me-a-coffee)](https://buymeacoffee.com/sentinelzxofc)
[![PayPal](https://img.shields.io/badge/PayPal-donate-blue?style=for-the-badge&logo=paypal)](https://paypal.me/sentinelzxofc)

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

**🔒 Remember: Use responsibly and ethically**

*Made with ❤️ by [@sentinelzxofc](https://github.com/sentinelzxofc)*

</div>
