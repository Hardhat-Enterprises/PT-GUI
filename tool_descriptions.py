PORT_SCANNER_DESC = " Ports on a computer are the place where information is sent to and received from." \
                    " Port scanning is used to determine which ports on a network are open. A port" \
                    " scanner sends a network request to connect to a specific TCP or UDP port on a" \
                    " computer and records the response. So what is does is send a packet of network" \
                    " data to a port to check the current status. If you wanted to check to see if your" \
                    " web server was operating correctly, you would check the status of port 80 on that" \
                    " server to make sure it was open and listening. The status helps network engineers" \
                    " diagnose network issues or application connectivity issues, or helps attackers " \
                    " find possible ports to use for infiltration into your network." \
                    " This tool checks for open ports among the top 20 most used ports and displays the" \
                    " list of ports that are open. You can check for other ports of your choice by " \
                    " editing the tools code. To operate it, you have to specify the IP address of your" \
                    "  target."

NMAP_SCANNER_DESC = "Nmap (short for network mapper) is used for scanning networks and hosts, it can determine what" \
                    " hosts are available on a network, what services (application name and version) those hosts are " \
                    "offering, what operating systems (and OS versions) they are running, what type of packet " \
                    "filters/firewalls are in use, and dozens of other characteristics. It is used to recon and map " \
                    "out a network to inform further attacks."

BANNER_GRABBER_DESC = "Banner Grabbing is a technique that helps in gaining information about some system that" \
                      " is available on a certain network. This technique can also be used to grab all the services" \
                      " running on the open ports of that particular system. Banner Grabbing attacks are performed" \
                      " when users/attackers want to send a request to the system they are attempting to hack to " \
                      "gain more information and this can cause exploitation of the service. Few examples of service" \
                      " ports that are used for the Banner Grabbing technique are HyperText Transfer Protocol (HTTP)," \
                      " File Transfer Protocol (FTP), and Service Mail Transfer Protocol (SMTP). \n" \
                      "This tool can be used against systems that are running these specific services, to get more" \
                      " information about these services and if a service is running on a vulnerable version, attackers" \
                      " can exploit it. The tool here takes the victim IP address and the port number from the user" \
                      " to perform banner grabbing."

SNIFFER_DESC = "A packet sniffer is essentially a tool that helps monitor network traffic and troubleshoot a network." \
               " It captures and analyzes data packets flowing through a specific network. Using a sniffer, it's " \
               "possible to capture almost any information — for example, which websites that a user visits, what is" \
               " viewed on the site, the contents and destination of any email along with details about any " \
               "downloaded files. Attackers can use packet sniffers for purposes such as spying on network user " \
               "traffic and collecting passwords. This tool is intended for the same purpose! It will capture the " \
               "traffic of victim machines and alert the attackers if any unencrypted passwords or credentials are " \
               "found!"

MAC_CHANGER_DESC = "MAC addresses are distinct hardware addresses that identify network interface controllers (NIC)" \
                   " such as LAN cards or WLAN adapters, and are used to identify devices in local networks. Every " \
                   "MAC address includes 48 bits, or 6 bytes, and is arranged in the following pattern: 00:81:41:fe:ad:7e." \
                   " Hackers use spoofing attacks to conceal their own identity and imitate another. \n" \
                   "This Mac Changer tool is used to change the Mac address of the attacker’s machine for the purpose" \
                   " of a Mac Spoofing attack. It takes the interface the attacker is on and the mac address he wants" \
                   " to impersonate. Hackers use the strategy of MAC spoofing to bypass access controls and security " \
                   "checks or for illegal activities, and obtain data that is not intended for their machines."

IMG_META_EXT_DESC = "Meta-data contained in images, videos and other files can sometimes expose highly sensitive" \
                    " and potentially damaging information such as owner details, Comments, Track Changes, " \
                    "device names and versions, causing a data breach that is punishable under global regulations." \
                    " This tool can be used either in reconnaissance phase or after gaining initial access. " \
                    "The tool takes the image path or name as user input and extracts all the metadata contained " \
                    "in the file. This can show if the files have properly been stripped out of important meta " \
                    "data or not and if attackers can use some of the information to perform further attacks " \
                    "against the devices used within the victim organization or damage the reputation of the " \
                    "organization."

HASH_ANALYZER_DESC = "The hash analyzer tool is used primarly for determining the types of possible hashes which may " \
                     "correspond to a user entered hash. This can help users to uncover information about the nature " \
                     "of any unknown hashes they may be dealing with and includes identification of common hashes" \
                     " such MD5, the SHA series, tiger, NTLM, and many more."

VULN_EXPLOIT_DESC = "A python script-based tool that accesses Metasploit to search for exploits, provide information " \
                    "about an exploit (description, required fields that the user will have to enter and the " \
                    "payloads that work with that exploit), execute an exploit and open a session created if the " \
                    "exploit was successful. "

MSFCON_LISTENER_DESC = "The purpose of this tool is to simplify the process of launching a reverse shell connection " \
                       "with a victim machine, allowing the user to execute commands on that machine. This is " \
                       "possible provided an executable payload is opened on the victim machine (can be generated " \
                       "using the \"Msfvenom Payload Generator Tool\"), and the attack is successful overall. Happy " \
                       "Hacking!"

MITM_AND_DNS_DESC = "Man-in-the-middle attacks (MITM) is a common category of cyber attacks that allows attackers to " \
                    "eavesdrop on the communication between two targets. The attack takes place in between two legitimately" \
                    " communicating hosts, allowing the attacker to “listen” to a conversation they should normally not" \
                    " be able to listen to. \n" \
                    "DNS resolves domain names to IP addresses. When using a DNS spoofing attack, the attacker attempts" \
                    " to introduce corrupt DNS cache information to a host in an attempt to access another host using their" \
                    " domain name, such as www.bigfishgames.com. Once a hacker successfully spoofs the DNS server he/she" \
                    " is able to hear to the data that was being transferred somewhere else and was not meant to read by " \
                    "somebody else. \n This tool can be used to perform a man-in-the-middle attack alone or use the DNS " \
                    "spoof along with it as a full attack vector. Just enter the victim and the attacker details and get started!"

FTP_BRUTE_DESC = "This tool will take an IP address, a username or username list, and a password list and will use " \
                 "this input to guess the credentials of existing FTP users on the target machine.\n\nThis tool " \
                 "will work making FTP logon requests to the target IP with all the combinations of usernames and " \
                 "passwords. If there is a successful login, the credentials will be displayed onscreen, otherwise " \
                 "a failure message will appear."

DIREC_TRAV_DESC = "This tool aims to expose any insecure directories within a web server by searching a library " \
                  "containing common web pathways which are known to potentially contain confidential information. " \
                  "The user is prompted to enter the homepage of the website they wish to fuzz and then is given " \
                  "options to access the page, scan manually or automatically for open directories and subsequently " \
                  "re-set the default parent directory in aims of uncovering and traversal deeper insecure webpages. "

SSH_BRUTE_DESC = "SSH or Secure Shell is a network protocol that allows encrypted communication across insecure " \
                 "networks. SSH is used for remote logins, command execution, file transfer, and more. SSH brute" \
                 " force attacks are often carried out by attackers trying a common username and password across " \
                 "thousands of servers until they find a match. This tool takes the victim IP address running an " \
                 "SSH server, and a wordlist (or dictionary), and the username against with the attacker wants to " \
                 "perform the password bruteforce. Once these 3 pieces of data are given by the user, the tool starts" \
                 " brute-forcing the SSH server, if a match if found, the tool displays the username and correct " \
                 "password and the program terminates. "

PHCRACKER_DESC = "The password hash cracker tool serves as a simple tool to crosscheck the hash of a user entered " \
                 "password with the hashes from a library containing thousands of the most common passwords. The " \
                 "tool can be used in the “intitial access” phase of a cyber attack as a means of uncovering any " \
                 "simple and insecure passwords set by the targeted party should the attacker come across any hashes. "

MSFVENOM_PAY_GEN_DESC = "This tool uses the Msfvenom framework to generate an executable file which connects a victim" \
                        " machine to the attack machine (this computer) and, in this case, will launch a command " \
                        "shell to run in the background allowing the attack machine to execute commands remotely on " \
                        "the victim. #PLEASE NOTE: This tool will only generate an executable for a reverse shell " \
                        "connection and the executable can only be run on a windows machine."

NOTEPAD_DESC = " It is a simple text editing tool that enables users to create plain text documents. If you don’t" \
               " have a text viewing & editing tool installed on your machine, you can use this to open text files" \
               " you stole from victim machines and analyze the information contained in them. Moreover, you can " \
               " use this tool while carrying out your penetration tests and attacks to note down important" \
               " information, copy paste commands and outputs for your ease and save these files for later use."

CMD_DESC = "This terminal is just like the command prompt of Windows OS. Linux/Unix commands are case-sensitive. The " \
           "terminal can be used to accomplish all Administrative tasks. This includes package installation, file " \
           "manipulation, and user management. Linux terminal is user-interactive. The terminal outputs the results " \
           "of commands which are specified by the user itself."

WORDLIST_GEN_DESC = "The wordlist generator is a tool which can generate wordlist using lowercase, uppercase, symbols, number and etc." \
                    "It can work with any platform. Wordlist Generator has two mode which is random mode and user profile mode. " \
                    "you can randomly generate a wordlist using random mode or using victim's information such name, birthday,or common words(money,bird,etc)." \
                    "Wordlist Generator is used for educational purposes, please use it with caution, "

HTTP_ANALYZER_DESC = "This tool is used to view the HTTP headers that are sent during the loading of a website. It " \
                     "allows the user to save these headers into a new text file, and add edit the text to write " \
                     "whatever they want before saving. This is used as an enumeration technique, as technical i" \
                     "nformation and vulnerabilties are often evidenced through the HTTP headers."

TCP_SYN_FLOOD_DESC = "This tool is used to attack web servers by continuously sending spoofed SYN packets to opened TCP ports. " \
                     "It allows users to set the target destination and packet data, with the option of stopping, restarting or redirecting the attack. " \
                     "The program also randomizes the user's host IP address, anonymizing each attack. " \
                     "This application can be used in conjunction with other tools, such as NMap to scan the web server for open ports, " \
                     "or Wireshark to monitor the packet transfer activity."
