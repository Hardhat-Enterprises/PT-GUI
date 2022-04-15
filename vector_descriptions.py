# pylint: disable=line-too-long

REVERSE_TCP_DESC = "The purpose of this attack vector is to provide a step-by-step walk through of how to carry out " \
                   "a reverse shell attack through simplified use of the Metasploit framework. This attack consists " \
                   "of two major parts, generation of the malicious payload to execute on the victim machine, as " \
                   "well as launching the listener on the attack machine to allow communication with the shell on " \
                   "the victim machine. #PLEASE NOTE: The payload generator will only generate an executable for a " \
                   "reverse shell connection and the executable can only be run on a windows machine."
DIR_TRAV_IDOR_DESC = "This attack vector uses a kali Linux machine to scan the web servers of a network environment " \
                     "for open directories which may contain potentially confidential information. The user may " \
                     "select a homepage of choice in order to execute the scan from and then subsequently " \
                     "automatically or manually scan for open directories. The user is given options to traverse " \
                     "through the web directories as they uncover open directories and download any files or pages " \
                     "containing sensitive information. Any passwords or other highly sensitive information " \
                     "uncovered from the fuzzer may be used in conjunction with other attack vectors or tools should " \
                     "it be deemed necessary as part of an attack. "
UNPATCH_VULN_EXP_DESC = "This attack vector accesses Metasploit to search for exploits, and provide " \
                        "information about an exploit (description, required fields that the user will have to enter " \
                        "and the payloads that work with that exploit), execute an exploit and open a session " \
                        "created if the exploit was successful. "
DDOS_ATTACK_DESC = "DDoS Attack Tool is a python-based tool that can be used to curate packets that can be bombarded " \
                   "on a network. These packets can have different ports and source IP addresses making it anonymous " \
                   "and extremely hard for target network defences to block. \n\nEssentially crashing the defences " \
                   "of the target network or overwhelming the firewall IDS system of the target network. This allows " \
                   "a pathway for attackers to perpetuate into the network and drop malicious code or back door " \
                   "shell that can then allows further foothold of the network.  "
WEB_APP_XSS_SQLI_DESC = "The kali machine (attacker) uses the pfsense to reach the webserver and exploit its " \
                        "vulnerabilities.\n\nSQLi injection are one of the most severe threats for web-based " \
                        "applications. The vulnerability allows an attacker to interfere between an application and " \
                        "its database by manipulating the queries that the application sends through; thus, " \
                        "compromising the security of the whole system. This attack is more common with PHP and ASP " \
                        "applications due to it being developed using C language, where there is a lack of data " \
                        "sanitisation. This attack affects all areas of security including – confidentiality, " \
                        "authentication, authorisation and integrity. \n\nXSS attacks is a commonly used web-based " \
                        "attack which demonstrates the failure of correctly handling program output and input. This " \
                        "leads to the exploitation of access control, confidentiality, availability and integrity. " \
                        "The attacker uses a legitimate web application as tool to conduct their attack. Where " \
                        "malicious script is entered into the web application to generate dynamic web pages which " \
                        "contain malicious data. Every time an end user comes to this web page, their browser will " \
                        "execute the malicious script because it assumes that the script has come from a trusted " \
                        "source. The script can also attempt to steal cookies, sensitive information within the " \
                        "browser and session tokens. This attack may also damage the webpage by altering the " \
                        "content of the HTML page.  "
NFS_PRIV_ESC_DESC = ""
APACHE_DESC = "Making use of CVE-2021-41773/42013, this attack vector demonstrates the use of Path Traversal and Remote Code Execution" \
              " on a vulnerable configuration of Apache Webserver 2.4.49 or 2.4.50."
AUTH_BYPASS_DESC = "Privilege escalation attack will be applied to demonstrate Authentication Bypass attack. Before " \
                   "exploiting the target machine, we need to know an overview of privilege escalation. \n\nPrivilege " \
                   "escalation attack is known as a child of Authentication Bypass attack. In this experiment, " \
                   "Metasploist will be used for testing, which consists of Meterpreter script and getsystem, " \
                   "that will utilize several alternative methods to attempt to acquire system level privilege on the target machine. "
PHPMYADMIN_RCE_DESC = ""
