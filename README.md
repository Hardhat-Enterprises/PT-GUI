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
If you are a member of the Red Team , follow section 2.2 to clone the repository by sourcetree.


---
## 2. CLONE THE TOOLKIT
### 2.1 Git client
Please ensure that you have configured Git on your computer with your Deakin credentials with the following commands:
* `git config --global user.email user@deakin.edu.au`; and
* `git config --global user.name Name`

### 2.2 Working with the repository
First, fork the repository:
1. Navigate to the repository on Bitbucket.
2. On the left-hand toolbar; click the **Create fork** button as shown below.

![Forking a repository](https://gyazo.com/b4133ae2549f51d3d6d15de82462b094.png)

3. Change the repository name if you wish, otherwise leave everything at default and hit the **Fork repository** button.
4. You will now have a personal copy of the repository, you can clone it to a Git client of your choice. Use this copy to make changes (either additions, modifications or deletions) to the repository.

**To clone the repository to your linux machine. Navigate to an empty folder in the terminal, then write the following command `$ git clone [clone link here]`. You will be asked for your username and password, make sure you provide your bitbucket credentials**

---
## 3. Using the TOOLKIT
 **The tool should be used in a linux machine for the best results.**
 
### 3.1 Before using the tool
 - Before you run the toolkit, navigate to the following path: `Network Recovery Tools/Dev/Deakin Detonator Toolkit GUI/DDT-GUI-v4`. This should be inside the folder of the cloned repository.
 - Then run the following command: `$ sudo python3 AppDependencies.py`. This command will install the libraries and depandencies needed to run the tool.
- To run the toolkit, use the following command:  `$ python3 main.py`. A window will open with the homepage of the toolkit, navigate through the different pages to learn about the different tools and attack vectors.

### 3.2 Usage
**Make sure you go through section 3.1 before running the toolkit**

After laucnhing the tool in the terminal, the GUI will open the homepage of toolkit. From there, we can see five main pages show up: About, Attack vectors, Tools, Walkthroughs, and References.
![Main page](https://gyazo.com/0c511c5fd1e5c8ce65247fb8e6b6b9e3.png)




- **About:** Provides basic information about the tool and its purpose.
- **Attack Vectors:** Contains a step by step demonstration of different exploitations.
- **Tools:** The tools page provides an easy access to many tools of different purposes, like reconnaissance and enummeration tools.
- **Walkthroughs:** This page will have video walkthroughs to different exploits and tools.

![Attack vectors](https://gyazo.com/1541331284ea3c948c54dbf1dc356b9a.png)
![Tools](https://gyazo.com/8278a773d58cbc0332104ab4fba69c27.png)

---

## 4. Development Toolkit
The Red Teams' members are to study/research attack vectors or attack tools to implement in the toolkit. The GUI of the toolkit is developed using [Tkinter](https://docs.python.org/3/library/tkinter.html).

### 4.1 Proposal Document
Before you (as a member of the Red Team) start to develop your attack vector or attack tool, remember to write a proposal document to your seniors to check whether it is suitable for the toolkit or not.

**A template for the proposal document:**
* [Proposal Template](https://deakin365.sharepoint.com/sites/DeakinDetonatorCyberDefence-UG/_layouts/15/Doc.aspx?OR=teams&action=edit&sourcedoc={C40D2D95-4412-4A67-B694-2F283BBE858C})

### 4.2 Follow The Project Rule
When your proposal document is reviewed and approved by a senior, start working on your attack vector or attack tool. There are a few points to note and follow:

* create a task for your work (attack vector or tool) in the [Trello Board](https://trello.com/b/U3eCuM0S/network-recovery-tools-red-trello)
* Honestly record the work to the [worklog](https://deakin365.sharepoint.com/:x:/r/sites/DeakinDetonatorCyberDefence-UG/Shared%20Documents/Network%20Recovery%20Tools/Archives/Red%20Team%20(T1%202021)/Worklog%202021%20T1.xlsx?d=w6ee7aa64d73e4643a2dc881f56cc52a5&csf=1&web=1&e=HnBKwd)
* upload your work to bitbucket using [sourcetree](https://www.sourcetreeapp.com/)



