# Network Recovery Tools - Red Team T3 2020
## Toolkit Installation, Usage and Development
---
Deakin Detonator Toolkit (DDT) is a toolkit that aims to simplify the penetration testing experience and workflow. The toolkit was initially started as a Command Line Interface (CLI) toolkit with a few minor tools. This Trimester, DDT has been further developed to now have a Graphical User Interface (GUI) with several new tools added.

This README will cover the following with regards to DDT:
1. Istalling the toolkit;
2. Using the toolkit; and
2. Developing the toolkit further.

**Important notes:**
* This document assumes you have a basic understanding of Git terminologies and working with Git repostories.
* The most up-to-date version of the toolkit is DDT-GUI-v3.

---
## 1. INSTALLING THE TOOLKIT
### 1.1 Dependencies
The following tools/technologies must be installed in order to use DDT (linked guides included):
* [Kali Linux](https://phoenixnap.com/kb/how-to-install-kali-linux-on-virtualbox)
* [Python 3.0+](https://docs.python-guide.org/starting/install3/linux/)
* [PySimpleGUI](https://pypi.org/project/PySimpleGUI/)
* [Sherlock](https://github.com/sherlock-project/sherlock#installation)

### 1.2 Cloning the repository
If you are only planning on using the toolkit, simply clone the repository with your Git client of choice.

---
## 2. USING THE TOOLKIT
### 2.1 Launch the toolkit
To run the toolkit, navigate to your cloned repository in a terminal, and move to the folder where `ddt.py` is (`.../Tri 2/Deakin Detonator Toolkit GUI/DDT-GUI-v3/`).

Then, run the toolkit using `python3 ddt.py`. You will see the toolkit open with a welcome/home screen. From here, you can use the navigation bar at the top of the home screen to use the various tools.

---
## 3. DEVELOPING THE TOOLKIT
### 3.1 Git client
Please ensure that you have configured Git on your computer with your Deakin credentials with the following commands:
* `git config --global user.email user@deakin.edu.au`; and
* `git config --global user.name Name`

### 3.2 Working with the repository
First, fork the repository:
1. Navigate to the repository on Bitbucket.
2. On the left-hand toolbar; click the **Create fork** button.
3. Change the repository name if you wish, otherwise leave everything at default and hit the **Fork repository** button.
4. You will now have a personal copy of the repository. Use this to make changes (either additions, modifications or deletions) to the repository.

Secondly, clone your fork using the steps from section 1.2.

### 3.3 Adding new tools
To preface this section, we are assuming that your tool has been developed with our guidelines set in place on Bitbucket:
* [Tool template](https://bitbucket-students.deakin.edu.au/projects/DDCDEF-UG/repos/network-recovery-tools---red-team_2020t3/browse/Tri2/Deakin%20Detonator%20Toolkit%20GUI/DDT-GUI-v3/scripts/Template.py)
* [Styling elements](https://bitbucket-students.deakin.edu.au/projects/DDCDEF-UG/repos/network-recovery-tools---red-team_2020t3/browse/Tri2/Deakin%20Detonator%20Toolkit%20GUI/DDT-GUI-Element-Styling/main.py)

The toolkit has been developed such that integrating new tools should be straight forward for future developers. To add new tools to the toolkit:
1. Fork the Bitbucket repository and clone your fork.
2. Add your tool to one of the five folders (categories) – “Attack”, “Common”, “Enum”, “Help”or “Misc” – found [here](https://bitbucket-students.deakin.edu.au/projects/DDCDEF-UG/repos/network-recovery-tools---red-team_2020t3/browse/Tri2/Deakin%20Detonator%20Toolkit%20GUI/DDT-GUI-v3/scripts).
3. Commit and push the changes from your clone to your fork.
4. Create a pull request from your fork to the origin.
5. Assuming the pull request is approved, your tool will now be available in the toolkit.

---
## 4. USING SHERLOCK
### 4.1 Installing Sherlock

Please ensure that an up to date version of Sherlock is installed. The two Sherlock folders that are installed via the requirements.txt file should match the current folder structure uploaded to this repository. Sherlock can be installed from the following repository with included instructions:

https://github.com/sherlock-project/sherlock


### 4.2 Working with Sherlock
After Sherlock has been successfully installed in the correct location (outlined by the current folder structure). Please ensure that the generator.sh script is located in sherlock/sherlock (with the sherlock.py file)

After this, please ensure the correct privileges are set for these files. Executable privileges are needed for generator.sh and sherlock.py. This can be done by navigating to the directory in the terminal and writing chmod +x filenamehere.

For more information on Linux permissions, please visit the following online resources:
https://github.com/sherlock-project/sherlock
https://github.com/sherlock-project/sherlock
