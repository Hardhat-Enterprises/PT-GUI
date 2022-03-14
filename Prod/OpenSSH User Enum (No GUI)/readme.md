# OpenSSH User Enumeration Guide


---
## Overview


```
OpenSSH User Enumeration is a tool developed to utilise a vulnerability in OpenSSH servers version 7.7 or lower to test if a user in a wordlist is a user on the system.
```

---
## How To Use


```
sshuser is a tool developed in Python. It will require a wordlist full of usernames and the required arguments given below
```

---
## Basic Command Usage

#### python3 sshuser.py --userList [user.txt]
```
This command will run the program with the given username wordlist. This is required.
```

#### python3 sshuser.py --outputFile [output.txt]
```
This command will set the output file for the programs functionality. This is required.
```

#### python3 sshuser.py [targetIP]
```
This command will give the program a target IP for the program to function against. This is required.
```

#### python3 sshuser.py --port [port]
```
This command will tell the program what port to target. This is not required and will default to port 21 for SSH.
```

#### python3 sshuser.py --threads [thread value]
```
This command will tell the program how fast to run. This is not required to run the program.
```

---

## Variables

```
There are no other variables needed.
```


---
## Limitations and Open Issues

#### Limitations
```
The target OpenSSH server needs to be version 7.7 or lower as this vulnerability was subsequently patched out.
```

#### Open Issues
```
This program requires the --userList, --outputFile and target IP arguments to run. This can be changed to a user input in the future or automated within the GUI.
```
