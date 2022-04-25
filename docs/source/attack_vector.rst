*************************************
Attack Vectors and walkthroughs
*************************************


Reverse TCP Shell
*************************************

1.	**What software/OS/Protocol it targets ?** 

This attack targets Windows OS and the TCP protocol.

2.	**What it does ?**

It will create a reverse connection from a machine you are attempting to attack, for example if you’re on a Windows 10 computer and I send you this file, if you run it this will create a live session for the attacker, giving them access to your computer through the listening which is run via the app but is a command line tool from Metasploit.

3. **How it works ?**

It creates a payload and saves it into a Windows Executable Format which will send a connection request to a specified IP address, if on that IP address there is something expecting this request it can allow it to connect and therefore give an attacker access to the machine where the payload was ran. 

4.	**How to use it ?**

Fill the input field with required data, there is auto IP detection if the current machine is the one you will be using to connect to the victim, and default port configuration unless you’d prefer to use another. Save the file and send it to the victim machine. Open the listening from step 2 and run the file on the victim windows computer. 



Directory Traversal & IDOR
*************************************
1.	**What software/OS/Protocol it targets ?**

This attacks webpages which mostly use the HTTP and HTTPS protocols and can be ran on most operating systems, generally on Linux webservers like Apache2.

2.	**What it does ?**

The Directory Traversal Fuzzer takes a websites URL as input and will search that website using keywords for other paths which may not be publicly known. It will automate the manual typing of a URL with a common path name at the end to try and fuzz for hidden directories. Once found it will give a list of the successfully found pages.

3.	**How it works ?**

This works by making requests to a webpage via curl or some other means at a specified URL, then iterates over a dictionary of words that are likely to be in a webpage. If the response code is 200 meaning the path returned a webpage you will see it in the list of valid directories. 

4.	**How to use it ?**

Input the URL and you can save it as a target to quickly enter in other fields, then run the fuzzer.



Unpatched Vulnerabilities and Exploits
**************************************************************************
1)	**What software/OS/Protocol it targets ?**

All operating systems and can detect most port information

2)	**What it does ?**

Provides a graphical interface for NMAP which has a few options in terms of the scan types, however you can’t combine them. After identifying potential vulnerable ports or protocols on a target you can move on to the VulnExploit tool which lets you search for Metasploit exploits and use them. Following through each option given a vulnerable system you will be able to open a remote session on a victim machine. 

3)	**How it works ?**

It works by scanning a target IP using NMAP and is searching for vulnerabilities. The identified vulnerable services or ports on a machine are then used by the attacker and input into the second tool which is essentially using Metasploit in more simplistic terms to make the process easier and more systematic. Once you have discovered an exploit for a vulnerability you just need to like in Metasploit use the module and set the parameters, in remote access cases this could be a combination of a local and remote ip address/port. 

4)	**How to use it ?**

Run the NMAP tool and select the option under Scan Type that best suits your situation, you can also adjust the speed which in summary will either be more thorough or less depending on your choice, T5 being the fastest and least thorough. More information can be found here https://nmap.org/book/performance-timing-templates.html. Once the scan is complete and you have some useful results, searching for these in the next step by selecting the first option, and following through until you execute the exploit, if one doesn’t work you can try other potential vulnerabilities discovered by NMAP.



Web Application Attacks: Automated XSS and SQL Injection Attack
**************************************************************************
Coming Soon


NFS privilege Escalation
*************************************
1)	**What software/OS/Protocol it targets ?**

This exploit targets the Linux Operating System.

2)	**What it does ?**

NFS Privilege Escalation can grant a user who has access to a Network File Share (NFS) root privileges. 

3)	**How it works ?**

This works by exploiting a misconfiguration in the implementation of NFS, you can place a binary on the NFS share location. Specifically, we’re looking for a share that has no_root_squash option enabled and using an enumeration tool like LinPEAS makes this process easier although you can manually identify this information looking through /etc/exports. Copying /bin/bash into the /tmp location of the share and then executing it to gain root access

4)	**How to use it ?**

Following the guide, you need to access the NFS location and search for some SSH keys, then access the machine create a folder in /tmp for example /tmp/test then copy in the /bin/bash file to this location and mounting it to the NFS share. Go back to your attack machine with root privileges copy the file to your local machine, edit the permissions and put it back to the share, log in to it again via SSH and run “./bash -p” in the shared location providing root privileges. 



Apache Web Server Exploit
*************************************
1)	**What software/OS/Protocol it targets ?**

Any operating system running Apache2.4.49 or Apache2.4.50

2)	**What it does ?**

This is a path traversal attack that gives access to the remote machine without the requirement of user input, simply having this version of Apache2 and having it running makes you vulnerable to this attack.

3)	**How it works ?**

It works by exploiting a URL encoding vulnerability that allows accessing files outside of the Apache2 webservers home directory, this also allows the execution of commands also, in our case we are running a reverse shell giving remote root privilege access

4)	**How to use it ?**

Simply determine the version of Apache2 using NMAP or navigating to the website location and identifying the version if its easily found. Once determined launch a listener in advance on a port you will be using to connect back to then run the script and input the required fields such as IP, port, version. This will automatically run and provide a shell.



Authentication Bypass Attack
*************************************
1)	**What software/OS/Protocol it targets ?**

Most Windows versions, in our example we’re using Windows XP

2)	**What it does ?**

This exploit is a privilege escalation and remote access type that attempts to become System on the Windows OS after gaining initial access. This does not work on all machines, it is recommended to test for it when exploiting a Windows machine. 

3)	**How it works ?**

The Metasploit module exploit/windows/browser/ms10_002_aurora works by exploiting a flaw in Internet Explorers memory. Only Internet Explorer 6 can currently be exploited according to rapid7. The next stop is gaining privilege access which Metasploit has a built-in module that will try various methods to gain System Authority on a Windows machine. 

4)	**How to use it ?**

After a NMAP scan find an appropriate method to gain initial access and select the module filling in required fields, once access has been obtained you can either move the session to meterpreter or make this your initial connection by selecting it as your listener, then typing the command “getsystem” in a meterpreter session will attempt to elevate privileges. 

