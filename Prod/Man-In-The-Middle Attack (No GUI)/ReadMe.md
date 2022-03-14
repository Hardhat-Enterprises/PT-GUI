# MITM Attack Tool Guide

<img src="https://img.shields.io/badge/language-python-brightgreen?logo=python&style=for-the-badge"/>

---
## Overview

#### MITM Attack Tool

This tool functions to automatically create ARP packets so it can trick the router and victim and intercept the communication happening between the two.

The tool requires 2 inputs to perform the attack. 
1- victim machine's IP address
2- Gateway/ router IP address
Once it has these two IPs the script can craft ARP packets and start flooding both the victim and router with spoofed ARP packets.
---
## How To Use (Terminal)

#### Start
Type in **python3 MITMAttack.py** to the terminal to start the program.

#### Enter the victim IP: (this is the interface of the victim machine)
Victim IP: can be found using nmap scanner tool from the toolkit.

#### Enter the gatway IP: ( this is the address of the router or gatway of the network on which victim is)
Gateway IP: can be found using nmap scanner tool from the toolkit.

---
## Limitations
MITMAttack is only possible if the attacker machine is on the same network as victim and both the victim machine IP and router IP is known.