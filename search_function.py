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
    "Cryptography Tools", "Encryption", "Encoding", "Hashing", #Cryptography Tools
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
    "Page", "Tool", "Tool", "Tool",
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
    "ToolsPage", "Encryption", "Encoding", "Hashing",
    "ToolsPage", "Command Prompt", "API_Keys", #Help... cmd prompt redirects to tools page
    #Walkthroughs
    "WalkthroughClass"]

searchlists = search
quicksearch = [] #for direct sequential matches, e.g. search for "too" yields "tools"
quicksearch2 = [] #for indirect sequential matches, e.g. search for "canne" yields "port scanner"

##on enter key pressed in the search bar, may build a search page
def build_search(event, search_field, search_canvas, controller):
    ##serves as the frame. is a canvas that covers the frame (whereever user searched from)
    ##is displaced by search_leave()... 
    search_canvas.place(relx=0, rely=0.08, relheight=0.92, relwidth=1)
    search_canvas.tk.call('raise', search_canvas._w)

    ##this is the input from user search
    input = search_field.get()
    
    #proof of concept to be able to dynamically pass the "search" input variable to page content.
    templabel = tk.Label(search_canvas, text=input, bg='#3B5262', fg='white', anchor="c")
    templabel.place(rely=0.08, relheight=0.12, relwidth=1)


def clean_quicksearch():
    for term in quicksearch:
        term.place_forget()
    while (len(quicksearch) > 0):
        quicksearch.pop()
    for term in quicksearch2:
        term.place_forget()
    while (len(quicksearch2)>0):
        quicksearch2.pop()

def search_check(input, search_field, frame, search_canvas, controller):
    lowest=0
    for idx, entry in enumerate(searchlists.searchterms):
        if(len(input) <= len(entry)):
            if(entry[0:len(input)].lower() == input.lower()): #if the first (however many characters) matches a search term (case insensitive)
                tempidx = idx
                quicksearch.append(ttk.Button(frame,text=entry, style="Accent.TButton", command = lambda i=tempidx: [search_field.delete(0, 'end'), search_leave(search_canvas), controller.show_frame(searchlists.pagelinks[i]), clean_quicksearch()])) #make a quicksearch button
                quicksearch[len(quicksearch)-1].place(rely=0.04 + (len(quicksearch)*0.04), relx=1 - 0.11 * 7 - 7 * 0.01) #place it under search bar
            elif(len(input)>1): 
                tempidx = idx
                for x in range (len(entry)-len(input)): #if searched item < 1, looks for indirect sequential matches, e.g. search for "canne" yields "port scanner"
                    if(entry[x+1:x+1+len(input)].lower() == input.lower()):
                        quicksearch2.append(ttk.Button(frame,text=entry, style="Accent.TButton", command = lambda i=tempidx: [search_field.delete(0, 'end'), search_leave(search_canvas), controller.show_frame(searchlists.pagelinks[i]), clean_quicksearch()])) #make a quicksearch button
    for idx, entry in enumerate(quicksearch2):
        quicksearch2[idx].place(rely=0.04 + ((len(quicksearch)+1*0.04) + idx*0.04), relx=1 - 0.11 * 7 - 7 * 0.01) #place it under search bar
def search_event(event, search_field, frame, search_canvas, controller):
    #previous suggestions are removed
    clean_quicksearch()

    #gets string of the user input
    input = search_field.get()
    if(len(input)>0):
        search_check(input, search_field, frame, search_canvas, controller) #searches

#replace with simple .place forget... navbar MUST call this when changing page away from a searchpage (search_canvas in build_search)
def search_leave(search_canvas):
    search_canvas.place_forget()
    search_canvas.delete("all")
