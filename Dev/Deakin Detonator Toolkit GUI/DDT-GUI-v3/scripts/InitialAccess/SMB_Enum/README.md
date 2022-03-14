# SMB Enumeration Tool Guide

<img src="https://img.shields.io/badge/language-Python-brightgreen?logo=Python&style=for-the-badge"/>

---
## Overview

### SMB
Server Message Block (SMB) is a protocol for sharing various elements over a network, such as files, printers and serial ports.

In penetration testing, SMB can be seen most-commonly on port 445, and is usually accompanied by port 139. This is because port 139 relates to NetBIOS, which allows devices on a LAN to talk to network hardware.

Note that in modern systems, SMB is sometimes referred to as Common Internet File System, or CIFS.

### Execution
Execution is discussed further under the "Commands" section, but in short:
* The subprocess Python module is used to execute a command using smbclient.
* It's stdout is piped to the tool.
* The tool uses conditional statements to determine whether the credentials worked or not.
* Once all credentials have been checked, they are printed to a multiline box.

---
## How To Use

### Inputs
Once the tool has been selected from the toolkit's navigation menu (ENUMERATION > SMB_Enum), it has three inputs:
1. A target IP address, defaults to local loopback (127.0.0.1).
2. A list of usernames. This should be passed as a username on each line, such as:
```
cam
joel
julian
etc.
```
3. A list of passwords. This should follow the same formatting as the usernames.

Note there is also two buttons, one to start the tool and one to exit the tool.

### Outputs
Once finished, the tool will print its results in a multiline as follows:
```
[-] username%password : Indicates that the credentials did not work
[+] username%password : Indicates that the credentials did work
[+] username%password - NOTE: Credentials must be changed : Indicates that the password needs to be updated for the credentials to allow access
```

---
## Basic Command Usage

### smbclient
`smbclient` is a tool pre-baked into Kali Linux that allows its user to execute various tasks relating to an SMB share. To simply access and view the share, the command `smbclient -L [host] -U user%pass` is used. 

For example, to login to an SMB share on 192.168.1.1 as user john with password 1234, the command would be: `smbclient -L 192.168.1.1 -U john%1234`.

In this tool, the following line is used to test user credentials:
```python
test = subprocess.Popen(['smbclient', '-L', target, '-U', creds], stdout=subprocess.PIPE)
```
The `test` variable is then checked against conditional statements to determine whether the credentials worked or not.

---
## Limitations and Open Issues

### Limitations
The following limitations are present within the tool:
1. The username and password lists will only work properly if each username is separated by a new line.

### Open Issues
The following issues are present within the tool:
1. The tool does not print the credentials as it tests them. As such, if a long username and password list are used, it can take a while before anything is shown to the user and looks as if the tool has frozen.
2. The tool sometimes returns false positives, i.e. says credentials work when they don't. Note however, that it doesn't return working credentials as "not working" (from what I have tested).