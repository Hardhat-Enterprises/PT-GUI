import os
import requests
from requests.exceptions import MissingSchema

import tkinter.messagebox
from socket import *
from threading import Thread, Lock
import sys, re, random, requests, os

import tkinter as tk  # python 3
from tkinter import font as tkfont  # python 3
# import Tkinter as tk     # python 2
# import tkFont as tkfont  # python 2
from tkinter import font as tkfont
from tkinter import font, messagebox
import PySimpleGUI as sg
from nav_bar import *

# ------------------------------------

# READ IN DIRECTORY LIBRARY FILE & SAVE AS LIST
data = open("Fuzzers/DirectoryLibrary.txt", "r")
dataString = data.read()
global dirList
dirList = dataString.split("\n")

# --- GLOBAL VARS ---
global homepageURL
homepageURL = ""


# ------------------------------------


class DTFuzz(tk.Frame):

    # ============================= Initializer Function ========================================================================

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        abtframefont = tkfont.Font(family='Calibri', size=33, weight="bold")
        display_nav_bar(self, controller)
        aboutframe = tk.Label(self, text="    Directory Traversal Fuzzer", bg='#3B5262', fg='white', anchor="c",
                              font=abtframefont)
        aboutframe.place(rely=0.08, relheight=0.12, relwidth=1)

        allscreenframe = tk.Label(self, bg='white')
        allscreenframe.place(rely=0.2, relheight=1, relwidth=1)

        # ---------------------------------------------------------------------------------------------------

        # LABELS / TEXT ON SCREEN
        # Label for "enter homepage"
        labelHomepage = Label(self, text="Enter homepage of target site:",
                              font=('Calibri', 13), bg="white", anchor='w').place(rely=0.24, relx=0.03, relheight=0.04,
                                                                                  relwidth=0.30)
        # Label for "VULNERABLE DIRECTORY SCANNER"
        label2 = Label(self, text="-- Vulnerable Directory Scanners --",
                       font=('Calibri', 13), anchor='c').place(rely=0.36, relx=0.03, relheight=0.04, relwidth=0.62)
        # Label "automatically scan for directories using library"
        label3 = Label(self, text="Scan for custom directory",
                       font=('Calibri', 13), bg="white", anchor='c').place(rely=0.43, relx=0.03, relheight=0.04,
                                                                           relwidth=0.30)
        # Label "Enter CUSTOM directory to scan for"
        label4 = Label(self, text="Enter custom directory to scan for:",
                       font=('Calibri', 13), bg="white", anchor='w').place(rely=0.48, relx=0.03, relheight=0.04,
                                                                           relwidth=0.18)
        # Label "OR"
        label5 = Label(self, text="OR",
                       font=('Calibri', 13), bg="white", anchor='c').place(rely=0.64, relx=0.03, relheight=0.04,
                                                                           relwidth=0.30)
        # Label "automatically scan for directories using library"
        label6 = Label(self, text="Automatically scan for directories using library",
                       font=('Calibri', 13), bg="white", anchor='c').place(rely=0.69, relx=0.03, relheight=0.04,
                                                                           relwidth=0.30)
        # Label "Enter parent directory to scan from - LIBRARY"
        label7 = Label(self, text="Enter parent directory to scan from:",
                       font=('Calibri', 13), bg="white", anchor='w').place(rely=0.74, relx=0.03, relheight=0.04,
                                                                           relwidth=0.30)
        # Label "FILE DOWNLOADER"
        label8 = Label(self, text="File Downloader",
                       font=('Calibri', 13), anchor='c').place(rely=0.71, relx=0.68, relheight=0.04, relwidth=0.28)
        # Label "ENTER file to DOWNLOAD"
        label9 = Label(self, text="Enter path of file to download:",
                       font=('Calibri', 13), bg="white", anchor='w').place(rely=0.75, relx=0.68, relheight=0.04,
                                                                           relwidth=0.28)
        # Label "Visit Page"
        label9 = Label(self, text="Visit A Directory",
                       font=('Calibri', 13), anchor='c').place(rely=0.45, relx=0.68, relheight=0.04, relwidth=0.28)
        # Label "Visit Page2"
        label9 = Label(self, text="Enter URL of page to visit:",
                       font=('Calibri', 13), bg="white", anchor='w').place(rely=0.49, relx=0.68, relheight=0.04,
                                                                           relwidth=0.28)

        # ---------------------------------------------------------------------------------------------------

        # BIG SCAN OUTPUT TEXT BOX
        dsrBox = tk.Label(self, bg='#E3E4E5')
        dsrBox.place(rely=0.45, relx=0.35, relheight=0.52, relwidth=0.30)
        dsrBoxSB = Scrollbar(dsrBox)
        dsrBoxSB.pack(side=RIGHT, fill=Y)

        # ---------------------------------------------------------------------------------------------------

        # INPUT TEXT BOXES
        # input text box for setting the homepage of victim site
        self.HomepageTB = Entry(self, font=('Calibri', 13))
        self.HomepageTB.place(rely=0.24, relx=0.18, relheight=0.04, relwidth=0.30)
        # input box for CUSTOM directory scan
        self.CustomDirScanTB = Entry(self, font=('Calibri', 13), )
        self.CustomDirScanTB.place(rely=0.52, relx=0.03, relheight=0.04, relwidth=0.30)
        # input box for LIBRARY directory scan
        self.LibraryDirScanTB = Entry(self, font=('Calibri', 13), )
        self.LibraryDirScanTB.place(rely=0.78, relx=0.03, relheight=0.04, relwidth=0.30)
        # input box for VISIT
        self.VisitPageTB = Entry(self, font=('Calibri', 13), )
        self.VisitPageTB.place(rely=0.53, relx=0.68, relheight=0.04, relwidth=0.28)
        # input box for DOWNLOAD
        self.DownloadFileTB = Entry(self, font=('Calibri', 13), )
        self.DownloadFileTB.place(rely=0.79, relx=0.68, relheight=0.04, relwidth=0.28)

        # ---------------------------------------------------------------------------------------------------

        #  BUTTONS
        # set homepage button
        Button(self, text="Set Homepage", font=('Calibri', 13), anchor='c',
               command=lambda: self.homepage_set()).place(rely=0.24, relx=0.49, relheight=0.04, relwidth=0.13)
        # visit homepage button
        Button(self, text="Visit Homepage", font=('Calibri', 13), anchor='c',
               command=lambda: self.visit_homepage()).place(rely=0.24, relx=0.63, relheight=0.04, relwidth=0.13)
        # button to start CUSTOM directory scan
        Button(self, text="Start Custom Directory Scan", font=('Calibri', 13), anchor='c',
               command=lambda: self.custom_scan()).place(rely=0.57, relx=0.03, relheight=0.04, relwidth=0.30)
        # button to start LIBRARY directory scan
        Button(self, text="Start Library Scan", font=('Calibri', 13), anchor='c',
               command=lambda: self.library_scan()).place(rely=0.83, relx=0.03, relheight=0.04, relwidth=0.30)
        # button to insert homepage URL into text box CUSTOM
        Button(self, text="Insert homepage", font=('Calibri', 13), anchor='c',
               command=lambda: self.insert_homepage_custom()).place(rely=0.485, relx=0.24, relheight=0.03,
                                                                    relwidth=0.09)
        # button to insert homepage URL into text box LIBRARY
        Button(self, text="Insert homepage", font=('Calibri', 13), anchor='c',
               command=lambda: self.insert_homepage_library()).place(rely=0.745, relx=0.24, relheight=0.03,
                                                                     relwidth=0.09)
        # button to DOWNLOAD page
        Button(self, text="Download File", font=('Calibri', 13), anchor='c',
               command=lambda: self.download_page()).place(rely=0.84, relx=0.68, relheight=0.04, relwidth=0.28)
        # button to VISIT a page
        Button(self, text="Visit Page", font=('Calibri', 13), anchor='c',
               command=lambda: self.visit_page()).place(rely=0.58, relx=0.68, relheight=0.04, relwidth=0.28)

    # ============================== Other Functions ==========================================================================

    def insert_homepage_custom(self):
        global homepageURL
        if (homepageURL.endswith("/") == False):
            homepageURL = homepageURL + "/"
        textToInsert = homepageURL
        self.CustomDirScanTB.insert(0, homepageURL)

    def insert_homepage_library(self):
        global homepageURL
        if (homepageURL.endswith("/") == False):
            homepageURL = homepageURL + "/"
        textToInsert = homepageURL
        self.LibraryDirScanTB.insert(0, homepageURL)

    def homepage_set(self):
        global homepageURL
        homepageURL = self.HomepageTB.get()
        if (homepageURL.endswith("/") == False):
            homepageURL = homepageURL + "/"
        homepage_set = Label(self, text="Homepage set", font=('Calibri', 13))
        homepage_set.place(rely=0.285, relx=0.27, relwidth=0.08)

    def visit_homepage(self):
        os.system("xdg-open " + homepageURL)

    def visit_page(self):
        command = self.VisitPageTB.get()
        os.system("xdg-open " + command)

    def custom_scan(self):
        directoryToSearch = ""
        # Text box for showing results from a directory scan
        dsrBox = tk.Label(self, bg='#E3E4E5')
        dsrBox.place(rely=0.45, relx=0.35, relheight=0.52, relwidth=0.30)
        # Init & Pack Scrollbar
        dsrBoxSB = Scrollbar(dsrBox)
        dsrBoxSB.pack(side=RIGHT, fill=Y)
        # Init Textbox
        myList = Listbox(dsrBox, yscrollcommand=dsrBoxSB.set)

        myList.insert(END, ("Custom Directory Scanner"))
        myList.insert(END, (""))

        # Get directory to search for from textbox input
        directoryToSearch = self.CustomDirScanTB.get()
        try:
            request = requests.get(directoryToSearch)
            if (request.status_code == 200):
                myList.insert(END, ("FOUND: " + directoryToSearch))
            else:
                myList.insert(END, ("ERROR: Requested directory not found."))
        except MissingSchema:
            myList.insert(END, ("Error: Please specify http:// or https:// in input."))

        myList.pack(fill="both", expand=True)
        dsrBoxSB.config(command=myList.yview)

    def library_scan(self):
        global homepageURL
        global dirList

        # Text box for showing results from a directory scan
        dsrBox = tk.Label(self, bg='#E3E4E5')
        dsrBox.place(rely=0.45, relx=0.35, relheight=0.52, relwidth=0.30)
        # Init & Pack Scrollbar
        dsrBoxSB = Scrollbar(dsrBox)
        dsrBoxSB.pack(side=RIGHT, fill=Y)

        # Init textbox/list
        myList = Listbox(dsrBox, yscrollcommand=dsrBoxSB.set)
        # Fill textbox/list
        myList.insert(END, ("==== Automated Library Directory Scan ===="))
        myList.insert(END, (" "))
        myList.insert(END, ("Scanning with pathway set as '" + homepageURL + "'"))
        myList.insert(END, (" "))
        myList.insert(END, ("Open directories found include..."))
        myList.insert(END, (" "))
        # Pack list on screen
        myList.pack(fill="both", expand=True)

        command = self.LibraryDirScanTB.get()

        for directory in dirList:
            request = requests.get(command + directory)
            if (request.status_code != 404):
                myList.insert(END, (command + directory))

        myList.pack(fill="both", expand=True)
        dsrBoxSB.config(command=myList.yview)

    def download_page(self):
        command = self.DownloadFileTB.get()
        os.system("curl -O " + command)
        # display msg saying "file downloaded"?


# OLD CODE FROM COMMAND LINE VERSION OF DIRECTORY TRAVERSAL FUZZER v1 ============================================          

"""
# READ IN DIRECTORY LIBRARY FILE & SAVE AS LIST
data = open("DirectoryLibrary.txt", "r")
datastring = data.read()
dirlist = datastring.split("\n")

# --- VARS ---

indexref = "index.php?page="
currentdir = ""
menuoptions = 8 #including exit

# ---- FUNCTIONS ----

def visitpage(command):
	os.system("xdg-open " + command)

def download(url):
	os.system("curl -O " + url)

def pageexists(url):
	request = requests.get(url)
	if (request.status_code != 404):
		return "true"
	else:
		return "false"

def appendslash(url):
	if (url.endswith("/") == False):
		url = url + "/"
	return url

# ---- MENU ----

print("\n\n====== Deakin Detonator Directory Traversal Fuzzer Tool ======\n")

homepage = input("Enter homepage of targeted webpage >> ")
homepage = appendslash(homepage)
currentdir = homepage

selection = 0
while (selection != 8):
	print("\n----------------------------\n")
	print("What would you like to do?\n")
	print("1: Access homepage")
	print("2: Change targeted site homepage")
	print("3: Scan for open directories on webserver using library")
	print("4: Scan for custom directory")
	print("5: Access custom directory")
	print("6: Access directory within webserver index via object reference manipulation (IDOR)")
	print("7: Download file")
	print("8: Exit Tool\n")
	
	isint = False
	while (isint == False):
		try:
			selection = int(input("Select an option >> "))
			if (selection >= 1 and selection <= menuoptions):
				isint = True
			else:
				print("Please enter valid selection between 1 and " + str(menuoptions) + " ...\n")
		except ValueError:
			print("Please enter valid selection between 1 and " + str(menuoptions) + " ...\n")



	if (selection == 1):
		visitpage(homepage)

	elif (selection == 2):
		homepage = input("Enter homepage of targeted webpage >> ")
		currentdir = homepage

	elif (selection == 3):
		print("\n**** Scanning for open directories using directory library ****\n\nSearching ...")
		truepages = 0		
		falsepages = 0
		for directory in dirlist:
			if (pageexists(homepage + directory) == "true"):
				print("FOUND: " + homepage + directory)
				truepages += 1
			else:
				falsepages += 1
		print("\n" + str(truepages) + " directories FOUND on "
			 + homepage + " and listed above")
		print(str(falsepages) + " directories NOT FOUND on " 
			+ homepage + " from library\n")

	elif (selection == 4):
		print("\nEnter directory to scan for...")
		directory = input("http://homepage/ >> ")
		if (pageexists(homepage + directory) == "true"):
			print("\nDirectory exists on webserver! \n\t" 
					+ homepage + directory + "\n")
		else:
			print("\nError: Could not find directory. \n\t"
					+ homepage + directory + "\n")
		
	elif (selection == 5):
		print("\nWhich directory would you like to access?")
		directory = input("http://homepage/ >> ")
		visitpage(homepage + directory)
		print()

	elif (selection == 6):
		print("\nEnter directory within the site's index to visit...")
		print("!! HINT: 'robots' text file and /etc/passwd often contain confidential informaiton!!")
		filepath = input("http://homepage/index.php?page= >> ")
		visitpage(homepage + indexref + filepath)

	elif (selection == 7):
		print("\nEnter file (including path) to download...")
		filepath = input("http://homepage/ >> ")
		download(homepage + indexref + filepath)
		print()

	elif (selection == 8):
		break

	else:
		print("Please enter a valid option...")


	input("Press enter to continue...")

"""
