# DDT GUI v3
---
This document covers the following with regards to DDT GUI v1:
1. Overview - a brief overview of this implementation
2. Development - how others can develop in this implementation
3. Drawbacks - issues and/or limitations of this implementation

<br>

## 1 Overview
---
This first implementation of the toolkit uses a file structure similar to the CLI one created in Trimester 1.

The `main.py` file is executed and takes functions from tool specific scripts; in this case `Ping.py` is used as a proof of concept. 

Each of the tool specific scripts must adhere to the following in this version:
* It must be located in the "*scripts*" folder;
* It must have the tool's name as the file name (E.g. a SYN flood tool would be called `SYN_Flood.py`);
* The tool's code must be contained in a single function with the same name as the filename (E.g. `SYN_Flood.py` would use `SYN_Flood()`);

<br>

## 2 Development
---
To develop for this version of the toolkit, there is a `Template.py` file which contains more information about developing a tool for this structure of toolkit. In short:
1. Copy `Template.py`.
2. Read the comments within the template and understand the code. If there are aspects you don't understand contact Cam Boyd or PySimpleGUI's documentation.
3. Make your changes and assure they comply with what's noted in `Template.py` and in section 1 of this document.

<br>

## 3 Drawbacks
---
This implementation of the toolkit has the following drawbacks:
* Development is not as simple as we want it to be - this is caused by the limitations of Python regarding importing other files/functions;
* PySimpleGUI does not allow a window to change it's layout - a new window has to be created when a layout changes.