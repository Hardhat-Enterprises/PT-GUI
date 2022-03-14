# TCP SYN Flood Guide


---
## Overview

```
A TCP Syn Flood is a Denial-of-Service attack vector where a user continuously sends SYN data packets to a targeted web server without finalizing or establishing a handshake connection. This renders the target machine to slow down and eventually become unusable.
```

---
## How To Use

```
synfloodGUI is developed in Python3 using the TKinter library. It can be accessed from the Deakin Detonator Toolkit (v4) or by using the command 'python3 synfloodGUI.py' from a command line Terminal.
```

---
## Basic Command Usage
```
The user inputs entry fields of the target destination and packet data (some entry fields being provided for easier usability). The user has the option of; attacking the target machine, stopping the attack, clearing the entry fields and attack window, or quitting the application. While the attack is running, the program will randomize the user's host IP address adding anonimity. 
If the IP Address is not accepting incoming requests or the port is closed, the program will state that the server is down (this may take some time).
```

---
## Variables

```
IP_entry opts user to enter the IP address of the destination.
```

```
port_entry opts user to enter the target port number of the web server. It is recommended to use a network scanning tool such as NMap to see which ports are Open. (The Default setting is port 80 (HTTP), the most common open port of a web server).
```

```
packet_entry opts user to enter the number of packets to be sent. (Default setting: 100)
```

```
thread_entry opts user to enter the number of threads. The sequential control flow of packets being sent. (Default setting: 200)
```

---
#### Limitations
```
The program is limited to only one target destination per attack.
The program will only send packets to IP addresses accepting incoming requests and open ports.
```

#### Open Issues
```
Larger packet and thread numbers than the default settings may result in the program to lag, hang, or crash.
Attempting to quit the application whilst an attack is in progress may result in the program to lag, or hang. It is recommended to stop the program before exiting.
```