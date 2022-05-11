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
    "Reconnaissance Tools", "Port Scanner", "Nmap", "Banner Grabber", "Shodan", #Recon
    "Enumeration Tools", "Sniffer", "Mac Changer", "Image Metadata Extractor", "Hash Analyzer", "HTTP Header Analyzer", "SNMP Checker" #Enumeration
    "Execution Tools", "VulnExploit", "Msfconsole Listener", "Mimt + Dns Spoof", #Execution 1
    "FPT Brute Forcer", "Wordlist generator", "ICMP Ping Flooder", "TCP SYN Flooder", #Execution 2
    "Fuzzers", "Directory Traversal Fuzzer", #Fuzzers
    "Initial Access Tools", "SSH Bruteforce", "Password Hash Cracker", "ZIP File Brute Forcer", #Initial Access
    "Payloads", "Msfvenom Payload Generator", #Payloads
    "Resource Development Tools", "Notepad", #Resource Dev
    "Help", "Command Prompt", "API Key Handler", #Help
    #Walkthroughs
    "Buffer Overflow"]



    searchlinks = [#pages
    "Page", "Page", "Page", "Page", "Page", "Page", 
    #Attack Vectors
    "Attack Vector", "Attack Vector", "Attack Vector", "Attack Vector", "Attack Vector", "Attack Vector", "Attack Vector", 
    #Tools
    "Page", "Tool", "Tool", "Tool", "Tool",
    "Page", "Tool", "Tool", "Tool", "Tool", "Tool", "Tool", 
    "Page", "Tool", "Tool", "Tool", "Tool", "Tool", "Tool", "Tool", 
    "Page", "Tool", 
    "Page", "Tool", "Tool", "Tool", 
    "Page", "Tool", 
    "Page", "Tool", 
    "Page", "Tool", "Tool", 
    #Walkthroughs
    "Walkthrough"]



    pagelinks = [#pages
    "StartPage", "AboutPage", "VectorsPage", "ToolsPage", "WalkthroughClass", "ReferencesPage",
    #Attack Vectors
    "AttackVectorOne", "AttackVectorTwo", "AttackVectorThree", 
    "AttackVectorFour", "AttackVectorSeven", 
    "AttackVectorEight", "AttackVectorNine",
    #Tools
    "ToolsPage", "PortScan", "ToolsPage", "BannerGrab", "ShodanScript", #Recon... nmap redirects to tools page
    "ToolsPage", "TestSniff", "MacChange", "IMDExtractor", "HashAn", "HTTPheaders", "SNMPCheck" #Enumeration
    "ToolsPage", "ToolsPage", "MsfListener", "MimtDnsSpoof", #Execution 1... vulnexploit redirects to tools page
    "FTPBruteForce", "ToolsPage", "ICMP", "ToolsPage", #Execution 2... wordlist and tcp/syn flood redirects to tools page
    "ToolsPage", "DTFuzz", #Fuzzers
    "ToolsPage", "SshBrute", "PHCracker", "ZipBF", #Initial Access
    "ToolsPage", "MsfPayloadGen", #Payloads
    "ToolsPage", "ToolsPage", #Resource Dev... notepad redirects to tools page
    "ToolsPage", "Command Prompt", "API_Keys", #Help... cmd prompt redirects to tools page
    #Walkthroughs
    "WalkthroughClass"]
