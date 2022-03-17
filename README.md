# Deakin Detonator Toolkit

Deakin Detonator Toolkit (DDT) is a toolkit that aims to simplify the penetration testing experience and workflow. The toolkit was initially started as a Command Line Interface (CLI) toolkit with a few minor tools. This Trimester, DDT has been further developed to now have a Graphical User Interface (GUI) with several new attack vectors and tools added.

## Installation

### Requirements
* [Kali](https://www.kali.org/)

### Steps

1. Clone the repo
```bash
$ git clone https://github.com/taysmith99/PT-GUI.git
$ cd PT-GUI
```

2. Install requirements

```bash
$ sudo apt update
$ sudo apt install -y python3 python3-pip python3-tk git
$ cd DDT-GUI/
$ pip3 install -r requirements.txt
```

3. Start the application

```bash
$ python3 main.py
```
