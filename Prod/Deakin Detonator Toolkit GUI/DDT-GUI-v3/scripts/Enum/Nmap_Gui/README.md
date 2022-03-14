# Nmap GUI Guide
![alt text](https://i.imgur.com/grzBZFy.png "Logo Title Text 1")

<img src="https://img.shields.io/badge/language-python-brightgreen?logo=python&style=for-the-badge"/>

---
## Overview

#### Nmap GUI
```codinglanguagehere
This module provides a GUI for the open-source network scanner 'Nmap'.

The GUI works by having each menu option map to a corresponding nmap tag. (eg. Scan Type: All = -A) when the user clicks Submit, the tool takes all the selected options and appends them to the given IP address. From here it sends the generated Nmap command to a bash script which creates a Tmux session which runs the Nmap command. All output from the Tmux session is then displayed in the multiline text-box at the bottom of the window.
```

---
## How To Use

```
This tool only requires an IP address to run, however users may choose to use additional options to suit their needs.
```

---
## Limitations and Open Issues

#### Limitations
```
Most of the current limitations come from PySimpleGUI, due to the way the module works, it's not possible to add many dynamic features due to the static nature in which PySimpleGUI creates each window.
```

#### Open Issues
```
Currently there are known issues with Tmux which result in the Tmux session sometimes returning '☎1;2c' which breaks the script and causes the tool to freeze.

Currently the only work around we have is to re-open the terminal that's running the toolkit and terminate the Tmux session by entering the command: 'tmux kill-server'.
```
