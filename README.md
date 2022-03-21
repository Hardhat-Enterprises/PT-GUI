# Deakin Detonator Toolkit

Deakin Detonator Toolkit (DDT) is a toolkit that aims to simplify the penetration testing experience and workflow. The toolkit was initially started as a Command Line Interface (CLI) toolkit with a few minor tools. This Trimester, DDT has been further developed to now have a Graphical User Interface (GUI) with several new attack vectors and tools added.

## Installation

### Requirements
* [Kali](https://www.kali.org/)

### Steps

1. Clone the repo
```bash
$ git clone https://github.com/taysmith99/PT-GUI.git
```

2. Install requirements

```bash
$ sudo apt update
$ sudo apt install -y python3 python3-pip python3-tk git
$ cd PT-GUI fff
$ pip3 install -r requirements.txt
```

3. Start the application

```bash
$ cd PT-GUI (this step is not needed if you are already in the directory)
$ python3 main.py
```

## Usage

After launching the tool, the GUI will open the homepage of toolkit. From there, we can see five main pages show up: About, Attack vectors, Tools, Walkthroughs, and References.

![Main page](https://gyazo.com/0c511c5fd1e5c8ce65247fb8e6b6b9e3.png)

- **About:** Provides basic information about the tool and its purpose.
- **Attack Vectors:** Contains a step by step demonstration of different exploitations.
- **Tools:** The tools page provides an easy access to many tools of different purposes, like reconnaissance and enummeration tools.
- **Walkthroughs:** This page will have video walkthroughs to different exploits and tools.

![Attack vectors](https://gyazo.com/1541331284ea3c948c54dbf1dc356b9a.png)
![Tools](https://gyazo.com/8278a773d58cbc0332104ab4fba69c27.png)

# Development

The GUI of the toolkit is developed using [Tkinter](https://docs.python.org/3/library/tkinter.html).
