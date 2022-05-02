# pylint: disable=global-statement
# pylint: disable=unused-import

from tkinter import *
from tkinter import ttk
import tkinter as tk

class search:
    searchterms = [#pages
                   "Home", "About", "Attack Vectors", "Tools", "Walkthroughs", "References",
                   #Attack Vectors
                   "Reverse TCP Shell", "Directory Traversal & IDOR", "Unpatched Vulnerabilities and Exploits", 
                   "Web Application Attacks: Automated XSS and SQLinjection attack", "NFS Privilege Escalation", 
                   "Apache Webserver Exploit", "Authentication Bypass Attack",
                   #Tools
                   "Reconnaissance Tools", "Port Scanner", "Nmap", "Banner Grabber", #Recon
                   "Enumeration Tools", "Sniffer", "Mac Changer", "Image Metadata Extractor", "Hash Analyzer", "HTTP Header Analyzer", #Enumeration
                   "Execution Tools", "VulnExploit", "Msfconsole Listener", "Mimt + Dns Spoof", #Execution 1
                   "FPT Brute Forcer", "Wordlist generator", "ICMP Ping Flooder", "TCP SYN Flooder", #Execution 2
                   "Fuzzers", "Directory Traversal Fuzzer", #Fuzzers
                   "Initial Access Tools", "SSH Bruteforce", "Password Hash Cracker", "ZIP File Brute Forcer", #Initial Access
                   "Payloads", "Msfvenom Payload Generator", #Payloads
                   "Resource Development Tools", "Notepad", #Resource Dev
                   "Help", "Command Prompt", #Help
                   #Walkthroughs
                   "Buffer Overflow"]
    searchlinks = [#pages
                   "Page", "Page", "Page", "Page", "Page", "Page", 
                   #Attack Vectors
                   "Attack Vector", "Attack Vector", "Attack Vector", "Attack Vector", "Attack Vector", "Attack Vector", "Attack Vector", 
                   #Tools
                   "Page", "Tool", "Tool", "Tool", 
                   "Page", "Tool", "Tool", "Tool", "Tool", "Tool", 
                   "Page", "Tool", "Tool", "Tool", "Tool", "Tool", "Tool", "Tool", 
                   "Page", "Tool", 
                   "Page", "Tool", "Tool", "Tool", 
                   "Page", "Tool", 
                   "Page", "Tool", 
                   "Page", "Tool", 
                   #Walkthroughs
                   "Walkthrough"]
    pagelinks = []




