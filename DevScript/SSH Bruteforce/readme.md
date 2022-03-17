# SSHBrute Guide


---
## Overview


```
SSHBrute is a password bruteforce for an SSH server. It runs a wordlist against the targeted SSH server and attempts to find the users password to gain access to their system.
```

---
## How To Use


```
SSHBrute is a tool developed in Python3 and can run from the terminal in linux. It will need the installation of the python package paramiko to run.
```

---
## Basic Command Usage

#### python3 sshbrute.py
```
This command will run the program as intended. It will then ask for the user to input the target IP address, the SSH username and then the file location of the wordlist.
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
This tool requires knowing the target IP address and the SSH username to run.
```

#### Open Issues
```
As this program needs the SSH username to run, it requires other knowledge to function properly. This tool can be modified to allow for a username wordlist to run every password in the password wordlist against in the future.
```
