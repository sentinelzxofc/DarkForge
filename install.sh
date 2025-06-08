#!/bin/bash

# DarkForge - Ultimate Hacking Toolkit Installer
# Version: 2.1.1
# Author: @sentinelzxofc
# Repository: github.com/sentinelzxofc/DarkForge
# Updated: Added Android/Termux support

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m' # No Color

# Banner
show_banner() {
    clear
    echo -e "${RED}"
    echo "██████╗  █████╗ ██████╗ ██╗  ██╗███████╗ ██████╗ ██████╗  ██████╗ ███████╗"
    echo "██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔════╝"
    echo "██║  ██║███████║██████╔╝█████╔╝ █████╗  ██║   ██║██████╔╝██║  ███╗█████╗  "
    echo "██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝  "
    echo "██████╔╝██║  ██║██║  ██║██║  ██╗██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗"
    echo "╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝"
    echo -e "${NC}"
    echo -e "${CYAN}                    ╔══════════════════════════════════════╗"
    echo "                     ║        ULTIMATE HACKING TOOLKIT         ║"
    echo "                     ║              Version 2.1.1              ║"
    echo "                     ║          by: @sentinelzxofc             ║"
    echo "                     ║      github.com/sentinelzxofc/DarkForge ║"
    echo -e "                     ╚══════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${YELLOW}[!] WARNING: This tool is for educational purposes only!${NC}"
    echo -e "${GREEN}[+] Installing DarkForge on $(uname -s) $(uname -r)${NC}"
    echo ""
}

# Check if running as root
check_root() {
    if [[ $EUID -eq 0 ]]; then
        echo -e "${YELLOW}[!] Running as root - some features may require non-root privileges${NC}"
        sleep 2
    fi
}

# Detect OS
detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        if command -v apt-get &> /dev/null; then
            OS="debian"
            PACKAGE_MANAGER="apt-get"
        elif command -v yum &> /dev/null; then
            OS="redhat"
            PACKAGE_MANAGER="yum"
        elif command -v pacman &> /dev/null; then
            OS="arch"
            PACKAGE_MANAGER="pacman"
        else
            OS="linux"
            PACKAGE_MANAGER="unknown"
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
        PACKAGE_MANAGER="brew"
    elif [[ $(uname -o) == "Android" ]] || [[ -d "/data/data/com.termux" ]]; then
        OS="android"
        PACKAGE_MANAGER="pkg"
    else
        OS="unknown"
        PACKAGE_MANAGER="unknown"
    fi
    
    echo -e "${BLUE}[*] Detected OS: $OS${NC}"
}

# Install Python dependencies
install_python_deps() {
    echo -e "${BLUE}[*] Installing Python dependencies...${NC}"
    
    # Check if pip is installed
    if ! command -v pip3 &> /dev/null && ! command -v pip &> /dev/null; then
        echo -e "${YELLOW}[!] pip not found, installing...${NC}"
        case $OS in
            "debian")
                sudo $PACKAGE_MANAGER update
                sudo $PACKAGE_MANAGER install -y python3-pip
                ;;
            "redhat")
                sudo $PACKAGE_MANAGER install -y python3-pip
                ;;
            "arch")
                sudo $PACKAGE_MANAGER -S python-pip
                ;;
            "macos")
                if ! command -v brew &> /dev/null; then
                    echo -e "${RED}[!] Homebrew not found. Please install it first.${NC}"
                    exit 1
                fi
                brew install python
                ;;
            "android")
                pkg install python -y
                python -m ensurepip --upgrade
                ;;
        esac
    fi
    
    # Install required Python packages
    echo -e "${BLUE}[*] Installing required Python packages...${NC}"
    if command -v pip3 &> /dev/null; then
        pip3 install --user requests colorama
    elif command -v pip &> /dev/null; then
        pip install --user requests colorama
    else
        echo -e "${RED}[!] Failed to install Python packages - pip not available${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}[+] Python dependencies installed successfully${NC}"
}

# Install system dependencies
install_system_deps() {
    echo -e "${BLUE}[*] Installing system dependencies...${NC}"
    
    case $OS in
        "debian")
            sudo $PACKAGE_MANAGER update
            sudo $PACKAGE_MANAGER install -y \
                python3 \
                python3-pip \
                net-tools \
                iputils-ping \
                netcat \
                nmap \
                curl \
                wget \
                git \
                wireless-tools \
                dnsutils
            ;;
        "redhat")
            sudo $PACKAGE_MANAGER install -y \
                python3 \
                python3-pip \
                net-tools \
                iputils \
                nc \
                nmap \
                curl \
                wget \
                git \
                wireless-tools \
                bind-utils
            ;;
        "arch")
            sudo $PACKAGE_MANAGER -S \
                python \
                python-pip \
                net-tools \
                iputils \
                gnu-netcat \
                nmap \
                curl \
                wget \
                git \
                wireless_tools \
                bind-tools
            ;;
        "macos")
            if command -v brew &> /dev/null; then
                brew install python nmap netcat curl wget git
            else
                echo -e "${YELLOW}[!] Some tools may not be available on macOS without Homebrew${NC}"
            fi
            ;;
        "android")
            pkg update -y
            pkg install -y \
                python \
                nmap \
                netcat-openbsd \
                curl \
                wget \
                git \
                dnsutils
            ;;
        *)
            echo -e "${YELLOW}[!] Unknown OS. Please install dependencies manually:${NC}"
            echo -e "${YELLOW}    - Python 3${NC}"
            echo -e "${YELLOW}    - pip3${NC}"
            echo -e "${YELLOW}    - net-tools${NC}"
            echo -e "${YELLOW}    - nmap${NC}"
            echo -e "${YELLOW}    - netcat${NC}"
            ;;
    esac
    
    echo -e "${GREEN}[+] System dependencies installed successfully${NC}"
}

# Create installation directory
create_install_dir() {
    if [[ "$OS" == "android" ]]; then
        INSTALL_DIR="$HOME/DarkForge"
    else
        INSTALL_DIR="$HOME/.darkforge"
    fi
    
    echo -e "${BLUE}[*] Creating installation directory: $INSTALL_DIR${NC}"
    
    if [ -d "$INSTALL_DIR" ]; then
        echo -e "${YELLOW}[!] DarkForge directory already exists. Backing up...${NC}"
        mv "$INSTALL_DIR" "$INSTALL_DIR.backup.$(date +%s)"
    fi
    
    mkdir -p "$INSTALL_DIR"
    echo -e "${GREEN}[+] Installation directory created${NC}"
}

# Download DarkForge
download_darkforge() {
    echo -e "${BLUE}[*] Downloading DarkForge...${NC}"
    
    if command -v git &> /dev/null; then
        git clone https://github.com/sentinelzxofc/DarkForge.git "$INSTALL_DIR"
    else
        echo -e "${YELLOW}[!] Git not found, downloading via curl...${NC}"
        curl -L https://github.com/sentinelzxofc/DarkForge/archive/main.zip -o /tmp/darkforge.zip
        unzip /tmp/darkforge.zip -d /tmp/
        mv /tmp/DarkForge-main/* "$INSTALL_DIR/"
        rm -rf /tmp/darkforge.zip /tmp/DarkForge-main
    fi
    
    chmod +x "$INSTALL_DIR/main.py"
    echo -e "${GREEN}[+] DarkForge downloaded successfully${NC}"
}

# Create launcher script
create_launcher() {
    echo -e "${BLUE}[*] Creating launcher script...${NC}"
    
    if [[ "$OS" == "android" ]]; then
        LAUNCHER_PATH="$PREFIX/bin/darkforge"
    else
        LAUNCHER_PATH="/usr/local/bin/darkforge"
    fi
    
    cat > /tmp/darkforge_launcher << 'EOF'
#!/bin/bash
INSTALL_DIR="$HOME/.darkforge"
if [[ "$OSTYPE" == "linux-android"* ]] || [[ -d "/data/data/com.termux" ]]; then
    INSTALL_DIR="$HOME/DarkForge"
fi
cd "$INSTALL_DIR"
python3 main.py "$@"
EOF
    
    if [[ "$OS" == "android" ]]; then
        mv /tmp/darkforge_launcher "$LAUNCHER_PATH"
        chmod +x "$LAUNCHER_PATH"
        echo -e "${GREEN}[+] Launcher created at $LAUNCHER_PATH${NC}"
        echo -e "${GREEN}[+] You can now run 'darkforge' from anywhere${NC}"
    elif [ -w "/usr/local/bin" ]; then
        sudo mv /tmp/darkforge_launcher "$LAUNCHER_PATH"
        sudo chmod +x "$LAUNCHER_PATH"
        echo -e "${GREEN}[+] Launcher created at $LAUNCHER_PATH${NC}"
        echo -e "${GREEN}[+] You can now run 'darkforge' from anywhere${NC}"
    else
        mkdir -p "$HOME/.local/bin"
        mv /tmp/darkforge_launcher "$HOME/.local/bin/darkforge"
        chmod +x "$HOME/.local/bin/darkforge"
        echo -e "${GREEN}[+] Launcher created at $HOME/.local/bin/darkforge${NC}"
        echo -e "${YELLOW}[!] Make sure $HOME/.local/bin is in your PATH${NC}"
        echo -e "${YELLOW}[!] Add this to your ~/.bashrc or ~/.zshrc:${NC}"
        echo -e "${YELLOW}    export PATH=\"\$HOME/.local/bin:\$PATH\"${NC}"
    fi
}

# Create desktop entry (Linux only)
create_desktop_entry() {
    if [[ "$OS" == "linux" ]] || [[ "$OS" == "debian" ]] || [[ "$OS" == "redhat" ]] || [[ "$OS" == "arch" ]]; then
        echo -e "${BLUE}[*] Creating desktop entry...${NC}"
        
        DESKTOP_DIR="$HOME/.local/share/applications"
        mkdir -p "$DESKTOP_DIR"
        
        cat > "$DESKTOP_DIR/darkforge.desktop" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=DarkForge
Comment=Ultimate Hacking Toolkit
Exec=gnome-terminal -- bash -c 'cd ~/.darkforge && python3 main.py; exec bash'
Icon=utilities-terminal
Terminal=true
Categories=Development;Security;
Keywords=hacking;security;penetration;testing;
EOF
        
        chmod +x "$DESKTOP_DIR/darkforge.desktop"
        echo -e "${GREEN}[+] Desktop entry created${NC}"
    fi
}

# Verify installation
verify_installation() {
    echo -e "${BLUE}[*] Verifying installation...${NC}"
    
    if [ -f "$INSTALL_DIR/main.py" ]; then
        echo -e "${GREEN}[+] DarkForge main script found${NC}"
    else
        echo -e "${RED}[!] DarkForge main script not found${NC}"
        exit 1
    fi
    
    if python3 -c "import requests, colorama" 2>/dev/null; then
        echo -e "${GREEN}[+] Python dependencies verified${NC}"
    else
        echo -e "${YELLOW}[!] Some Python dependencies may be missing${NC}"
    fi
    
    echo -e "${GREEN}[+] Installation verification complete${NC}"
}

# Show completion message
show_completion() {
    echo ""
    echo -e "${GREEN}╔══════════════════════════════════════════════════════════════╗"
    echo -e "║                                                              ║"
    echo -e "║  ██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗          ║"
    echo -e "║  ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║          ║"
    echo -e "║  ██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║          ║"
    echo -e "║  ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║          ║"
    echo -e "║  ██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗     ║"
    echo -e "║  ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝     ║"
    echo -e "║                                                              ║"
    echo -e "║              DarkForge installed successfully!               ║"
    echo -e "║                                                              ║"
    echo -e "╚══════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${CYAN}[*] Installation completed successfully!${NC}"
    echo -e "${CYAN}[*] Installation directory: $INSTALL_DIR${NC}"
    echo ""
    echo -e "${YELLOW}[*] Usage:${NC}"
    echo -e "${WHITE}    darkforge                 ${CYAN}# Run from anywhere (if in PATH)${NC}"
    echo -e "${WHITE}    cd $INSTALL_DIR && python3 main.py  ${CYAN}# Run directly${NC}"
    echo ""
    echo -e "${YELLOW}[*] Features:${NC}"
    echo -e "${WHITE}    • Network Scanner         • Password Generator${NC}"
    echo -e "${WHITE}    • Port Scanner            • Hash Cracker${NC}"
    echo -e "${WHITE}    • Vulnerability Scanner   • WiFi Scanner${NC}"
    echo -e "${WHITE}    • SQL Injection Tester    • Steganography${NC}"
    echo -e "${WHITE}    • Payload Generator        • And much more!${NC}"
    echo ""
    echo -e "${RED}[!] IMPORTANT DISCLAIMER:${NC}"
    echo -e "${RED}    This tool is for educational and authorized testing purposes only.${NC}"
    echo -e "${RED}    Users are responsible for complying with all applicable laws.${NC}"
    echo -e "${RED}    The author is not responsible for any misuse of this tool.${NC}"
    echo ""
    echo -e "${GREEN}[+] Happy hacking! (Ethically, of course)${NC}"
    echo ""
}

# Main installation function
main() {
    show_banner
    check_root
    detect_os
    
    echo -e "${BLUE}[*] Starting DarkForge installation...${NC}"
    echo ""
    
    install_system_deps
    install_python_deps
    create_install_dir
    download_darkforge
    create_launcher
    create_desktop_entry
    verify_installation
    
    show_completion
}

# Handle interruption
trap 'echo -e "\n${RED}[!] Installation interrupted by user${NC}"; exit 1' INT

# Check for help flag
if [[ "$1" == "-h" ]] || [[ "$1" == "--help" ]]; then
    echo "DarkForge Installer"
    echo ""
    echo "Usage: $0 [options]"
    echo ""
    echo "Options:"
    echo "  -h, --help     Show this help message"
    echo "  --uninstall    Uninstall DarkForge"
    echo ""
    echo "This script will install DarkForge and all its dependencies."
    echo "Run without arguments to start the installation."
    exit 0
fi

# Handle uninstall
if [[ "$1" == "--uninstall" ]]; then
    echo -e "${YELLOW}[!] Uninstalling DarkForge...${NC}"
    
    # Determine installation directory
    if [[ -d "/data/data/com.termux" ]]; then
        INSTALL_DIR="$HOME/DarkForge"
        LAUNCHER_PATH="$PREFIX/bin/darkforge"
    else
        INSTALL_DIR="$HOME/.darkforge"
        LAUNCHER_PATH="/usr/local/bin/darkforge"
    fi
    
    # Remove installation directory
    if [ -d "$INSTALL_DIR" ]; then
        rm -rf "$INSTALL_DIR"
        echo -e "${GREEN}[+] Removed installation directory${NC}"
    fi
    
    # Remove launcher
    if [ -f "$LAUNCHER_PATH" ]; then
        rm -f "$LAUNCHER_PATH"
        echo -e "${GREEN}[+] Removed launcher${NC}"
    fi
    
    if [ -f "$HOME/.local/bin/darkforge" ]; then
        rm -f "$HOME/.local/bin/darkforge"
        echo -e "${GREEN}[+] Removed user launcher${NC}"
    fi
    
    # Remove desktop entry
    if [ -f "$HOME/.local/share/applications/darkforge.desktop" ]; then
        rm -f "$HOME/.local/share/applications/darkforge.desktop"
        echo -e "${GREEN}[+] Removed desktop entry${NC}"
    fi
    
    echo -e "${GREEN}[+] DarkForge uninstalled successfully${NC}"
    exit 0
fi

# Run main installation
main