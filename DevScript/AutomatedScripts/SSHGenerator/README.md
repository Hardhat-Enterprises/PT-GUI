# SSH Generator Guide
![alt text](https://i.imgur.com/grzBZFy.png "Logo Title Text 1")

<img src="https://img.shields.io/badge/Bash-Bash%20Script-green"/>

---
## Overview

#### SSH Generator
```
This bash script provides a GUI overlay to the creation of an SSH public / private key pair. The GUI prompts the user for the name of the public key file as well as a password for authentication purposes. Additionally, there is functionality to upload the public key to a web server which can be downloaded from a remote machine (using wget etc.)
```

---
## How To Use

####
```
Run via ssh_webserver.sh or through the toolkit. Follow the GUI prompts to make the public / private key pair.
```

---
## Basic Command Usage

#### Command 1
```
Zenity is used to spawn the GUI interfaces that are used.
```

#### Command 2
```
Tmux is a terminal multiplexer that is used to run CeWL during multiple instances.
```

#### Command 3
```
$ipaddress is set to the first ip address listed in ifconfig.
```

#### Command 4
```
ssh-keygen is used to create the ssh key pair.
```
---

## Variables

#### Variable 1
```
$ipaddress gets the first ifconfig ip address and prints it to the screen
```

#### Variable 1
```
$? is used to access the boolean variable of the zenity prompts. Such as the answer to yes / no or okay buttons.
```

---

## Open Issues

#### Issue 1
```
The usage of Python as an overlay would have been more effective in associating the script with the PySimpleGUI based toolkit.
```
