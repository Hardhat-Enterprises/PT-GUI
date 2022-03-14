# Toolkit

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://bitbucket-students.deakin.edu.au/projects/DDCDEF-UG/repos/network-recovery-tools---red-team/browse)

## Toolkit Installation, Usage and Development
Deakin Detonator Toolkit (DDT) is a toolkit that aims to simplify the penetration testing experience and workflow. The toolkit was initially started as a Command Line Interface (CLI) toolkit with a few minor tools. This Trimester, DDT has been further developed to now have a Graphical User Interface (GUI) with several new attack vectors and tools added.

This README will cover the following with regards to DDT:
1. Istalling the toolkit;
2. Using the toolkit; and
2. Developing the toolkit further.

**Important notes:**
* This document assumes you have a basic understanding of Git terminologies and working with Git repostories.
* DDT-GUI-v3 is the previous version of the toolkit 
* The most up-to-date version of the toolkit is DDT-GUI-v4.

---
## 1. INSTALLING THE TOOLKIT
### 1.1 Dependencies
The following tools/technologies must be installed in order to use DDT (linked guides included):
* [Kali Linux](https://phoenixnap.com/kb/how-to-install-kali-linux-on-virtualbox)
* [Python 3.0+](https://docs.python-guide.org/starting/install3/linux/)
* [PySimpleGUI](https://pypi.org/project/PySimpleGUI/)
* [SourceTree](https://www.sourcetreeapp.com/)

### 1.2 Cloning the repository
If you are only planning on using the toolkit, simply clone the repository with your Git client of choice.
if you are Red Team member, follow 3.2 to clone the repository by sourcetree.


---
## 3. CLONE THE TOOLKIT
### 3.1 Git client
Please ensure that you have configured Git on your computer with your Deakin credentials with the following commands:
* `git config --global user.email user@deakin.edu.au`; and
* `git config --global user.name Name`

### 3.2 Working with the repository
First, fork the repository:
1. Navigate to the repository on Bitbucket.
2. On the left-hand toolbar; click the **Create fork** button.
3. Change the repository name if you wish, otherwise leave everything at default and hit the **Fork repository** button.
4. You will now have a personal copy of the repository using 'sourcetree'. Use this to make changes (either additions, modifications or deletions) to the repository.

Secondly, clone your fork using the steps from section 1.2.

---
## 4. Using TOOLKIT
 To run the toolkit, navigate to your cloned repository in a terminal, and move to the folder where `main.py` is (`Network Recovery Tools/Dev/Deakin Detonator Toolkit GUI/DDT-GUI-v4`).

 Before you run the toolkit, Please run the conmmand: `sudo python3 AppDependencies.py` to install the library we used.
 Then, run the toolkit using `python3 main.py`. You will see the toolkit open with a welcome/home screen. From here, you can see About, Attack Vector, Attack Tools, References button. Select any tool you want inside the Attack vector or attack tools
---
## 5. Development Toolkit
Red Team's members can study attack vectors or attack tools that can be done by themselves or a group. Use [Tkinter](https://docs.python.org/3/library/tkinter.html) to implement GUI and add to toolkit

### 5.1 Proposal Document
Before you start to develop your attack vector or attack tool, remember write a proposal document to your senior checking whether it is suitable for the toolkit.
The proposal document template:
* [Proposal Template](https://deakin365.sharepoint.com/sites/DeakinDetonatorCyberDefence-UG/_layouts/15/Doc.aspx?OR=teams&action=edit&sourcedoc={C40D2D95-4412-4A67-B694-2F283BBE858C})

### 5.2 Follow The Project Rule
When your proposal document is passed, start to create your attack vector or attack tool. There are a few points to note and follow:

* create your task for your work in [Trello Board](https://trello.com/b/U3eCuM0S/network-recovery-tools-red-trello)
* Honestly record the work to the [worklog](https://deakin365.sharepoint.com/:x:/r/sites/DeakinDetonatorCyberDefence-UG/Shared%20Documents/Network%20Recovery%20Tools/Archives/Red%20Team%20(T1%202021)/Worklog%202021%20T1.xlsx?d=w6ee7aa64d73e4643a2dc881f56cc52a5&csf=1&web=1&e=HnBKwd)
* upload your work to bitbucket using [sourcetree](https://www.sourcetreeapp.com/)

**notes:**
* To see the tutorials of how to use above listed please see xxtutorialxx(have not create yet)

