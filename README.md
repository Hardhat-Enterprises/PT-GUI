# Toolkit
{todo}


## Toolkit Installation, Usage and Development
Deakin Detonator Toolkit (DDT) is a toolkit that aims to simplify the penetration testing experience and workflow. The toolkit was initially started as a Command Line Interface (CLI) toolkit with a few minor tools. This Trimester, DDT has been further developed to now have a Graphical User Interface (GUI) with several new attack vectors and tools added.
{todo}

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
{todo}


---
## 2. CLONE THE TOOLKIT
### 2.1 Git client
{todo}

### 2.2 Working with the repository
{todo}

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

