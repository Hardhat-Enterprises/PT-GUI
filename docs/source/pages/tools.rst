*************************************************
Tool Descriptions and Walkthroughs
*************************************************

***************
Recon Tools
***************

Port Scanner
**********************
1)	**What software/OS/Protocol it targets ?**

All devices with an IP address including websites and devices on a network.

2)	**What it does ?**

Provides the user with the top 20 most used ports and displays the list of ports that are open.

3)	**How it works ?**

It works by sending a TCP or UDP request to the commonly used ports, it then will record and display this information to the user after completion of the scan. 

4)	**How to use it ?**

You simply input the IP address in the field after opening the tool and wait for it to finish. You can edit the code for this program to do custom scanning if you'd like. 

Nmap
**********************
1)	**What software/OS/Protocol it targets ?**

All devices with an IP address including websites and devices on a network.

2)	**What it does ?**

It scans the IP address for open and vulnerable ports on a device and displays the results.

3)	**How it works ?**

It works similarly to the Port Scanner, sending TCP and UDP requests to ports on the specified IP Address and can determine the potential service running on the port using banner grabbing it can also tell you if the port is open, it also when specified can use the gathered data and compare it to its database of known vulnerabilities providing the user with potential vulnerabilities to exploit. 

4)	**How to use it ?**

Just type the IP address and specify ports and Scan Type then wait for it to finish running.


Banner Grabber
**********************
1)	**What software/OS/Protocol it targets ?**

All devices with an IP address including websites and devices on a network.

2)	**What it does ?**

It provides useful information which can help in identifying the service running on a specific protocol

3)	**How it works ?**

This sends out requests to different protocols that can provide information such as HTTP, SMTP and FTP then if it receives information back it will display the information of the protocol scanned to the user.

4)	**How to use it ?**

Type and IP and port into the fields as this banner grabber doesn't attempt to do all common ports and only the specified one.


Shodan Reconnaissance:
*****************************
1)	**What software/OS/Protocol it targets ?**

All devices with an IP address including websites and devices on a network.

2)	**What it does ?**


Scans an IP address for login details stored in plain text or default credentials of services running on the device.

3)	**How it works ?**

It attempts to connect to commonly used ports for which security cameras and other services such as routers are hosted on that use default credentials, and if it can access the service will provide this information to you.

4)	**How to use it ?**

Enter in an IP address and wait for the scan to complete.


********************
Enumeration Tools
********************

Sniffer
**********************
1)	**What software/OS/Protocol it targets ?**

This tool targets network interfaces.

2)	**What it does ?**

Provides the network traffic of a selected interface in real time.

3)	**How it works ?**

It works by connecting to the interface as an intermediary and listens in on any traffic passing through an interface. This can intercept plain text information on a networks interface and provide passwords if the user is not careful.

4)	**How to use it ?**

Type the interface name into the field and start the sniffer. 


MAC Changer
**********************
1)	**What software/OS/Protocol it targets ?**

This tool targets hardware.

2)	**What it does ?**

Once connected to a network the MAC changer can identify MAC addresses of other devices on the network and change the attackers to imitate another on that network.

3)	**How it works ?**

It works by spoofing the MAC address of the attacker machine and when asked by the network what its MAC address is it will provide the one it is pretending to be and can receive information that was destined for the other device if you were able to remove it from the network (SYN Flood attack might work here).

4)	**How to use it ?**

Select a computer vendor from the list and network interface you want to spoof to a new MAC address, you can also change back to the original MAC by clicking the “Original MAC” button.


Image Metadata Extractor
***************************
1)	**What software/OS/Protocol it targets ?**

This tool targets files.

2)	**What it does ?**

It provides metadata information that might be hidden in an image.

3)	**How it works ?**

It works by using a metadata extracting tool in the background that once you put in the path location of the image/video or other file will inspect it and could expose sensitive data or hidden information. 

4)	**How to use it ?**

Provide the path of the file for the tool to analyse and run it.


Hash Analyzer
**********************
1)	**What software/OS/Protocol it targets ?**

This tool works on Linux and targets hashes.

2)	**What it does ?**

Can help determine the type of hashing algorithm used on text.

3)	**How it works ?**

It works by analysing patterns of other hashing algorithms and will determine if the provided hash has the same formatting patterns. It can with decent accuracy provide the correct hash used.

4)	**How to use it ?**

Enter a hash value and run the tool.


HTTP Header Analyzer
**********************
1)	**What software/OS/Protocol it targets ?**

This tool targets websites and most the HTTP/S protocol

2)	**What it does ?**

This tool will provide header information of a HTTP response which can help in identifying useful information for exploiting.

3)	**How it works ?**

This tool takes the URL provided and forwards a GET request from a URL, once receiving the RESPONSE from this URL it takes the header packet data and displays it to the user.

4)	**How to use it ?**

Enter in a website address into the tool and select Launch.


SNMP Check
**********************
1)	**What software/OS/Protocol it targets ?**

This tool works on Linux

2)	**What it does ?**

It provides enumeration of SNMP device on a network and displays the output in an easily understandable format

3)	**How it works ?**

It scans the IP address specified and will return useful information of that device such as the uptime, hostname, system date, location, description and more. 

4)	**How to use it ?**

Enter the IP address and port of the device you would like to scan


*************************
Execution Tools
*************************

VulnExploit
**********************
1)	**What software/OS/Protocol it targets ?**

This exploit targets most operating systems

2)	**What it does ?**

It allows the access of Metasploit through an easy 5 step interface allowing a new user to search for, set up and exploit a machine with the Metasploit module.

3)	**How it works ?**

It’s a python-based script that accesses Metasploit to search for and provide information about exploits, then select the exploit found and fill in the required fields, this works well with the NMAP tool as you will usually need to identify vulnerable ports in order to start using Metasploit.  

4)	**How to use it ?**

Run the program and follow the prompts, its very straight forward. 


Msfconsole Listener
**********************
1)	**What software/OS/Protocol it targets ?**

This does not specifically target anything

2)	**What it does ?**

Opens a listening on a specified port or the default one awaiting an incoming connection.

3)	**How to use it ?**

Open the tool and select the automatically generate IP address or input a different one, select the port and then the listener will be awaiting a connection.


Mimt + Dns Spoof
**********************
1)	**What software/OS/Protocol it targets ?**

Targets all Operating Systems

2)	**What it does ?**

This tool can listen in on two devices communication simply imitating a man in the middle (MITM) who can hear a conversation between two people, it also has the ability to spoof DNS which could direct a user on a network to go to the MITM’s websites that aren’t encrypted giving sensitive information up.

3)	**How it works ?**

It works by convincing both devices that this MITM is the other device, then forwards the information on usually requiring multiple interfaces on the device to make the MITM attack hidden. The DNS spoofing will attempt to poison the DNS cache of the device which resolves IP addresses to domain names. 

4)	**How to use it ?**

Launch the tool and fill in the input fields with the correct information. 


FTP Brute Forcer
**********************
1)	**What software/OS/Protocol it targets ?**

This exploit targets FTP

2)	**What it does ?**

Attacks an open FTP server and can give the attacker access to the data stored on the FTP server

3)	**How it works ?**

This works by providing the IP address of the FTP server, username list and password list to the tool. It will iterate over each password per username or if one username is provided just doing this once until it gets access to the FTP server. 

4)	**How to use it ?**

Launch the tool and follow the prompts then you can come back once its done, hopefully brute forcing a logon.


Wordlist generator
**********************
1)	**What software/OS/Protocol it targets ?**

This does not attack anything

2)	**What it does ?**

Will generate a list of words either randomly within specific parameters such as maximum/minimum length, upper/lower case or with specified information of a person such as their name, surname, nicknames, birth date and any other keywords you might know about the person. 

3)	**How it works ?**

It works by iterating over the information provided and creating a large array of words that contain the parameters specified. 

4)	**How to use it ?**

Launch the tool and select the desired mode, then fill in the required fields and start the tool.


ICMP Ping Flooder
**********************
1)	**What software/OS/Protocol it targets ?**

This tool targets the ICMP protocol

2)	**What it does ?**

It floods the ICMP (ping) connection of a device and can disable communications for the device on the network.

3)	**How it works ?**

It works by sending ICMP packets to a device that is specified, it will continue sending packets at a high rate depending on the provided number of packets to send.

4)	**How to use it ?**

Launch the tool and provide the IP address of the device you want to ICMP flood, the port for ICMP and the number of packets to be sent, then click “Start Flood”


TCP SYN Flooder
**********************
1)	**What software/OS/Protocol it targets ?**

This tool targets the TCP protocol

2)	**What it does ?**

Denies service to TCP protocol activity for a device and can even disable a network that has no protection from this.

3)	**How it works ?**

The tool sends large amount of synchronize (SYN) packets to a specified device and drops the connection, by repeating this action the network or device is overloaded and cannot handle the receiving of this information anymore as each time it also replies with a synchronize acknowledge (SYN-ACK) slowing down the network heavily. 

4)	**How to use it ?**

Launch the tool and fill in the required fields, increasing the number of threads makes it run faster, the number of packets is to ensure that enough packets are being sent. 


Email Bomber
**********************
1)	**What software/OS/Protocol it targets ?**

This tool targets peoples email box

2)	**What it does ?**

The Email Bomber overloads a victim’s email by sending large amounts of spoofed email messages preventing them from viewing important messages or even flood the webserver of the recipient. 

3)	**How it works ?**

It works by automating a person sending an email and instead sending many emails to a email address in quick succession in the hopes of flooding their mailbox or disabled the email server. By specifying the number of emails to send you can leave this running indefinitely. 

4)	**How to use it ?**

Launch the tool and fill in the fields.



**********************
Initial Access Tools
**********************

SSH Bruteforce
**********************
1)	**What software/OS/Protocol it targets ?**

This tool attacks SSH 

2)	**What it does ?**

Similar to the FTP brute forcer tool this brute forces SSH logins until it runs out of attempts or successfully gets the correct password and username.

3)	**How it works ?**

Providing a username and password list to the tool it will recursively input the username and each password in order and will provide output if the password was successful. 

4)	**How to use it ?**

Launch the tool and fill in the required field, providing a password list to use for the brute forcing.


Password Hash Cracker
**********************
1)	**What software/OS/Protocol it targets ?**

This tool attacks hashed passwords

2)	**What it does ?**

This will take a password that is hashed or any hashed value and provide the password as output in plain text format if the hashing algorithm was detected.

3)	**How it works ?**

It works by comparing the hash with various others in its database and attempting to apply the algorithm to decode the password. 

4)	**How to use it ?**

Launch the tool and enter the hash into the field, then click the “Check Hash” button.

ZIP File Brute Forcer
**********************
1)	**What software/OS/Protocol it targets ?**

This tool attacks zipped files

2)	**What it does ?**

This tool will unlock password protected zip files if the password is found.

3)	**How it works ?**

It works by using a script to enumerate over a list of passwords and input them to the zip file over and over until it either cracks the zip files password or runs out of attempts.

4)	**How to use it ?**

Launch the tool and provide a zip file you wish to crack, then hit the “Go” button.


************
Payloads
************
Msfvenom Payload Generator
*******************************
1)	**What software/OS/Protocol it targets ?**

This tool targets the Windows Operating System

2)	**What it does ?**

The Msfvenom Payload Generator will provide a reverse shell from a victim’s Windows machine once they have run the executable file generated by it.

3)	**How it works ?**

It generates an executable file which can be run on Windows, the executable is compiled with a reverse shell as the payload and will execute once it has been opened. 

4)	**How to use it ?**

Provide the IP address you would like this reverse shell to connect to and a port, then it will generate the executable to which you can send to a victim.



********************************
Resource Development Tools
********************************
Notepad
**********************
Coming Soon

********
Help
********
Command Prompt
**********************
Coming Soon

Example New Page
**********************
Coming Soon

API Key Management
**********************
Coming Soon
