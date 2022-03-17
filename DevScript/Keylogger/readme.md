# Keylogger Guide


---
## Overview


```
Keylogger is a payload developed in Python to use the keyboard package and collect keystrokes entered on the system and log them to the programs file location or to relay them back to an email account.
```

---
## How To Use


```
Keylogger is a tool developed in Python3 and can run from the terminal in linux. It will need the installation of the python package keyboard to run.
```

---
## Basic Command Usage

#### python3 keyscript.py
```
This command will run the program as intended. It will then begin to log keystrokes in a file location or relay them back to an email if the email function has been selected instead.
```

---

## Variables

```
EMAIL_ADDRESS is the selected email address to relay the keylogs to.
```

```
EMAIL_PASSWORD is the password to the email address to relay the keylogs to.
```

```
The Main part of the program will be where you select whether or not you want to relay to email or store on the target system. This can be changed my commenting and uncommenting the necessary lines. 
```

---
## Limitations and Open Issues

#### Limitations
```
The target will be required to have the python package "keyboard" to run.
```

#### Open Issues
```
This program has issues with understanding the .start function coded into the program. This may need to be bugfixed in the future. A fix suggested might be to change the filename, however this has not been confirmed. Check the proposal documentation for source.
```
