# PentestingTools

# About This Project
This repository contains various security-related scripts that I have written as part of my learning journey in cybersecurity and ethical hacking.

I am passionate about understanding network security, penetration testing, and system vulnerabilities, and these scripts help me practice and improve my skills in a safe and responsible way.

Everything here is designed for educational purposes only and should be used ethically and legally.
# Disclaimer & Legal Notice
This project is strictly for learning, research, and ethical hacking purposes.

🚫 Do not use these scripts on any system you do not own or have explicit permission to test.
⚠ I am not responsible for any misuse of this code.

Cybersecurity is a powerful skill—use it responsibly.

# Why I Am Writing These Scripts
I created this repository because:

* I want to learn cybersecurity by coding my own tools instead of just using existing ones.
* I believe in learning by doing, and scripting helps me understand how attacks and defenses work.
* I am exploring topics like network security, penetration testing, and vulnerability assessment.
* I am always open to feedback, so if you have suggestions or improvements, feel free to share!

# ✅ Allowed Use Cases
✔ Learning about network security & ethical hacking.
✔ Practicing in a controlled environment (e.g., CTFs, lab setups).
✔ Testing your own systems for vulnerabilities (with permission).
✔ Understanding how attacks work to build stronger defenses.

# 🚫 Strictly Forbidden Uses
❌ Running these scripts against unauthorized systems.
❌ Using them for malicious hacking, illegal access, or data theft.
❌ Disrupting or harming real-world services.
❌ Violating any cybersecurity laws or ethical guidelines.


# B_HTTP_header_inspector.py
This Python script allows you to inspect HTTP headers from any URL. It retrieves and displays key header information like Date, Server, Content-Type, and more.

## Usage:
* Run the script.
* Enter a URL starting with http:// or https://.
* View the HTTP headers.
* Type exit to quit.
## Installation:
* Ensure Python 3.x is installed.
* Install dependencies with:
  pip install requests

# B_port_scan.py
This Python script is a simple port scanner that allows you to check the open or closed status of ports on a target IP address. It supports three types of scans:

* Full scan: Scans all ports from 1 to 65535.
* Single port scan: Scans a specific port.
* Custom range scan: Scans a user-defined range of ports.
## Usage:
* Full scan: B-Port-Scan$ {TARGET_IP}
* Single port scan: B-Port-Scan$ {TARGET_IP} {PORT}
* Range scan: B-Port-Scan$ {TARGET_IP} {FLOOR_PORT} {CEILING_PORT}
* Type /help to view available commands and instructions.


