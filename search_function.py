# pylint: disable=global-statement
# pylint: disable=unused-import

from tkinter import *
from tkinter import ttk
import tkinter as tk


class Search:
    """
    keeps search related info.
    """
    SearchTerms = [  # pages
        "Home", "About", "Attack Vectors", "Tools", "Walkthroughs", "References",
        # Attack Vectors
        "Reverse TCP Shell", "Directory Traversal & IDOR","Unpatched Vulnerabilities and Exploits",
        "Web Application Attacks: Automated XSS and SQLinjection attack","NFS Privilege Escalation",
        "Apache Webserver Exploit","Authentication Bypass Attack",
        # Tools
        #   Recon
        "Reconnaissance Tools", "Port Scanner", "Nmap", "Banner Grabber", "Shodan",
        #   Enumeration1
        "Enumeration Tools","Sniffer","Mac Changer","Image Metadata Extractor","Hash Analyzer",
        #   Enumeration2
        "HTTP Header Analyzer", "SNMP Checker"
        #   Execution 1
        "Execution Tools", "VulnExploit", "Msfconsole Listener", "Mimt + Dns Spoof",
        #   Execution 2
        "FPT Brute Forcer","Wordlist generator","ICMP Ping Flooder","TCP SYN Flooder",
        #   Fuzzers
        "Fuzzers", "Directory Traversal Fuzzer",
        #   Initial Access
        "Initial Access Tools","SSH Bruteforce","Password Hash Cracker","ZIP File Brute Forcer",
        #   Payloads
        "Payloads", "Msfvenom Payload Generator",
        #   Resource Dev
        "Resource Development Tools", "Notepad",
        #   Cryptography Tools
        "Cryptography Tools", "Encryption", "Encoding", "Hashing",
        #   Help
        "Help", "Command Prompt", "API Key Handler",
        #   Walkthroughs
        "Buffer Overflow"]

    SearchLinks = [  # pages
        "Page", "Page", "Page", "Page", "Page", "Page",
        # Attack Vectors
        "Attack Vector", "Attack Vector", "Attack Vector", "Attack Vector",
        "Attack Vector", "Attack Vector", "Attack Vector",
        # Tools
        "Page", "Tool", "Tool", "Tool", "Tool",
        "Page", "Tool", "Tool", "Tool", "Tool", "Tool", "Tool",
        "Page", "Tool", "Tool", "Tool", "Tool", "Tool", "Tool", "Tool",
        "Page", "Tool",
        "Page", "Tool", "Tool", "Tool",
        "Page", "Tool",
        "Page", "Tool",
        "Page", "Tool", "Tool", "Tool",
        "Page", "Tool", "Tool",
        # Walkthroughs
        "Walkthrough"]

    PageLinks = [  # pages
        "StartPage","AboutPage","VectorsPage","ToolsPage","WalkthroughClass","ReferencesPage",
        # Attack Vectors
        "AttackVectorOne", "AttackVectorTwo", "AttackVectorThree",
        "AttackVectorFour", "AttackVectorSeven",
        "AttackVectorEight", "AttackVectorNine",
        # Tools
        # Recon... nmap redirects to tools page
        "ToolsPage", "PortScan", "ToolsPage", "BannerGrab", "ShodanScript",
        # Enumeration
        "ToolsPage","TestSniff","MacChange","IMDExtractor","HashAn","HTTPheaders","SNMPCheck"
        # Execution 1... vulnexploit redirects to tools page
        "ToolsPage", "ToolsPage", "MsfListener", "MimtDnsSpoof",
        # Execution 2... wordlist and tcp/syn flood redirects to tools page
        "FTPBruteForce", "ToolsPage", "ICMP", "ToolsPage",
        "ToolsPage", "DTFuzz",  # Fuzzers
        "ToolsPage", "SshBrute", "PHCracker", "ZipBF",  # Initial Access
        "ToolsPage", "MsfPayloadGen",  # Payloads
        "ToolsPage", "ToolsPage",  # Resource Dev... notepad redirects to tools page
        "ToolsPage", "Encryption", "Encoding", "Hashing",
        # Help... cmd prompt redirects to tools page
        "ToolsPage", "Command Prompt", "API_Keys",
        # Walkthroughs
        "WalkthroughClass"]
    def get_search_terms(self):
        """
        for pylint, but also returns SearchTerms.
        """
        return self.SearchTerms
    def get_page_links(self):
        """
        for pylint, but also returns PageLinks.
        """
        return self.PageLinks

SearchLists = Search
quicksearch = []
quicksearch2 = []


def build_search(search_field, search_canvas, controller):
    """
    builds a search page on a canvas based on input from entry
    """
    search_canvas.place(relx=0, rely=0.08, relheight=0.92, relwidth=1)
    search_canvas.tk.call('raise', search_canvas)
    uinput = search_field.get()

    shodanframe = tk.Label(
        search_canvas,
        text=uinput,
        bg='#3B5262',
        fg='white',
        anchor="c")
    shodanframe.place(rely=0.08, relheight=0.12, relwidth=1)
    if uinput == "Home":
        controller.show_frame("StartPage")

def clean_quicksearch():
    """
    cleans quicksearch
    """
    for term in quicksearch:
        term.place_forget()
    while len(quicksearch) > 0:
        quicksearch.pop()
    for term in quicksearch2:
        term.place_forget()
    while len(quicksearch2) > 0:
        quicksearch2.pop()


def search_check(uinput, search_field, frame, search_canvas, controller):
    """
    builds a search page on a canvas based on input from entry
    """
    for idx, entry in enumerate(SearchLists.SearchTerms):
        if len(uinput) <= len(entry):
            # if the first (however many characters) matches a search term
            # (case insensitive)
            if entry[0:len(uinput)].lower() == uinput.lower():
                tempidx = idx
                quicksearch.append(
                    ttk.Button(
                        frame,
                        text=entry,
                        style="Accent.TButton",
                        command=lambda i=tempidx: [
                            search_field.delete(
                                0,
                                'end'),
                            search_leave(search_canvas),
                            controller.show_frame(
                                SearchLists.PageLinks[i]),
                            clean_quicksearch()]))  # make a quicksearch button
                quicksearch[len(quicksearch) -
                            1].place(rely=0.04 +
                                     (len(quicksearch) *
                                      0.04), relx=1 -
                                     0.11 *
                                     7 -
                                     7 *
                                     0.01)  # place it under search bar
            elif len(uinput) > 1:
                tempidx = idx
                for inc in range(len(entry) - len(uinput)):
                    if entry[inc + 1:inc + 1 + len(uinput)].lower() == uinput.lower():
                        quicksearch2.append(
                            ttk.Button(
                                frame,
                                text=entry,
                                style="Accent.TButton",
                                command=lambda i=tempidx: [
                                    search_field.delete(
                                        0,
                                        'end'),
                                    search_leave(search_canvas),
                                    controller.show_frame(
                                        SearchLists.PageLinks[i]),
                                    clean_quicksearch()]))  # make a quicksearch button
    for idx, entry in enumerate(quicksearch2):
        quicksearch2[idx].place(rely=0.04 +
                                ((len(quicksearch) +
                                  1 *
                                  0.04) +
                                 idx *
                                 0.04), relx=1 -
                                0.11 *
                                7 -
                                7 *
                                0.01)  # place it under search bar


def search_event(search_field, frame, search_canvas, controller):
    """
    starts a quicksearch
    """
    # previous suggestions are removed
    clean_quicksearch()

    # gets string of the user input
    uinput = search_field.get()
    if len(uinput) > 0:
        search_check(
            uinput,
            search_field,
            frame,
            search_canvas,
            controller)  # searches

# replace with simple .place forget


def search_leave(search_canvas):
    """
    exits a search_page
    """
    search_canvas.place_forget()
    search_canvas.delete("all")
