# FTPBrute Guide


---
## Overview


```
FTPBrute is a password bruteforce for an open FTP server. It runs a wordlist against the targeted FTP server and attempts to find the users password to gain access to their system.
```

---
## How To Use


```
FTPBrute is a tool developed in Python3 and can run from the terminal in linux. It will need the installation of the python package ftplib to run.
```

---
## Basic Command Usage

#### python3 ftpbrute.py
```
This command will run the program as intended. It will then ask for the user to input the target IP address, the FTP username and then the file location of the wordlist.
```

---

## Variables

```
There are no variables to change, however, this program can be integrated into a GUI to have user inputs in a form and a file open command to open the wordlist.
```

---
## Limitations and Open Issues

#### Limitations
```
This tool requires knowing the target IP address and the FTP username to run.
```

#### Open Issues
```
As this program needs the FTP username to run, it requires other knowledge to function properly. This tool can be modified to allow for a username wordlist to run every password in the password wordlist against in the future.
```
