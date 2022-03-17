# Wordlist Generator Guide
![alt text](https://i.imgur.com/grzBZFy.png "Logo Title Text 1")

<img src="https://img.shields.io/badge/Bash-Bash%20Script-green"/>

---
## Overview

#### Sherlock and CeWL
```bash
This bash script overlays on top of Sherlock and CeWL to create custom Wordlists. To use / update, clone the Sherlock github repository. https://github.com/sherlock-project/sherlock Install via requirements.txt and add into the toolkit folder. Move generator.sh to sherlock/sherlock.
```

---
## How To Use

####
```
Run via generator.sh or through the toolkit. Insert a username and wordlists will appear in the same folder as well as the master word list.
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
---

## Variables

#### Variable 1
```
There are multiple boolean variables set to 0 that are used as conditional flags. These can be edited / used elsewhere in other logic based statements.
```

## Open Issues

#### Issue 1
```
All CeWL instasnces run at the same time, this can cause a potential spike in CPU usage however the CeWL is quite light weight. This can be fixed by running CeWL instances one at a time and checking for completion before running the next one. This will take longer than the current method.
```
