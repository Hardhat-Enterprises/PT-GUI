# DNS Spoofer Tool Guide

<img src="https://img.shields.io/badge/language-python-brightgreen?logo=python&style=for-the-badge"/>

---
## Overview

#### DNS Spoofer Tool

This tool functions to automatically create spoofed reply packets for DNS request so an attacker can redirect the victim to a malicious website.

The tool requires 2 steps before launch. 
1- starting web server services on the attacker machine which hosts the malicious website.
2- Turning off ipv4 packet forwarding in the attacker machine so the packets can be controlled by the script. 
---
## How To Use (Terminal)

#### Start
Type in **python3 DNSSpoofer.py** to the terminal to start the program.

#### Enter the interface: (this is the interface to listen at for DNS requests)
Type in the value based on the interface attacker machine is on in the network.

#### Enter the attacker's server IP: ( this is the address of the server that is hosting the malcious website i.e. attacker machine's IP address)
Attacker's IP: Type in your local network IP address which can be found by typing **ipconfig** (in Windows terminal) or **ifconfig** (in Linux terminal)

---
## Limitations
DNS Spoofer is dependant on pre-existing Man-In-The-Middle Attack.