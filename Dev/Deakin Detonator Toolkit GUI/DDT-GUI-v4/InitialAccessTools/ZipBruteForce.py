import zipfile
from tqdm import tqdm
from sys import exit
import base64
import re
import os
import requests
from requests.exceptions import MissingSchema
import tkinter.messagebox
from socket import *
from threading import Thread,Lock
import sys,re,random, requests, os
import tkinter as tk  # python 3
from tkinter import font  as tkfont  # python 3
# import Tkinter as tk     # python 2
# import tkFont as tkfont  # python 2
from tkinter import font as tkfont
from tkinter import font, messagebox
import PySimpleGUI as sg
from nav_bar import *
from tkinter import filedialog

global zip_file
zip_file = ""

global obj

global password_list
password_list = "wordlist4zip.txt"


class ZipBF(tk.Frame):
  
# ============================= Initializer Function 

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        abtframefont = tkfont.Font(family='Calibri', size=33, weight="bold")
        display_nav_bar(self, controller)
        aboutframe = tk.Label(self, text="    ZIP Password Brute Forcer", bg='#3B5262', fg='white', anchor="w", font=abtframefont)
        aboutframe.place(rely=0.08, relheight=0.12, relwidth=1)

        allscreenframe = tk.Label(self, bg='white')
        allscreenframe.place(rely=0.2, relheight=1, relwidth=1)

        # LABELS
        labelFilepath = Label(self,text = "Filepath: ",
          font=('Calibri', 9), bg='white', anchor='w').place(rely=0.27, relx=0.35, relheight=0.06, relwidth=0.45)


        #  BUTTONS
        Button(self,text="Select Zip File",font=('Calibri', 16),bg='#4D6C84', fg='white', anchor='c',
          command= lambda: self.get_file()).place(rely=0.27, relx=0.14, relheight=0.06, relwidth=0.20)
        Button(self,text="GO",font=('Calibri', 16), bg='#4D6C84', fg='white', anchor='c',
          command= lambda: self.execute()).place(rely=0.35, relx=0.35, relheight=0.06, relwidth=0.30)

        # OUTPUT TEXT BOX
        resultsBox = tk.Label(self, bg='#E3E4E5')
        resultsBox.place(rely=0.45, relx=0.35, relheight=0.52, relwidth=0.30)
        resultsBoxSB = Scrollbar(resultsBox)  
        resultsBoxSB.pack(side = RIGHT, fill = Y)
        bfResults = Listbox(resultsBox, yscrollcommand = resultsBoxSB.set)



    # Get file function ===============
    def get_file(self):
        global zip_file
        zip_file = filedialog.askopenfilename(filetypes=[("ZIP files", ".zip")])
        labelFilepath = Label(self,text = "Filepath: " + zip_file,
          font=('Calibri', 9), anchor='w').place(rely=0.27, relx=0.35, relheight=0.06, relwidth=0.45)



    def execute(self):

        resultsBox = tk.Label(self, bg='#E3E4E5', font=('Calibri', 16))
        resultsBox.place(rely=0.45, relx=0.35, relheight=0.52, relwidth=0.30)
        resultsBoxSB = Scrollbar(resultsBox)  
        resultsBoxSB.pack(side = RIGHT, fill = Y)
        bfResults = Listbox(resultsBox, yscrollcommand = resultsBoxSB.set)

        global zip_file
        global obj
        global password_list
        obj = zipfile.ZipFile(zip_file)
        flag = 0
        foo = ""

   
        with open(password_list, "rb") as file:
            for line in file:
                for word in line.split():
                    try:
                        obj.extractall(pwd=word)
                        foo = word.decode()
                        flag = 1
                        break

                    except:
                        continue
        if (flag == 1):
            bfResults.insert(END, ("!! Password Found !!"))
            bfResults.insert(END, ("Password for ZIP file is:    " + foo))
            bfResults.pack(fill = "both", expand=True)
            resultsBoxSB.config(command = bfResults.yview)
        else:
            bfResults.insert(END, ("Error: No password found, try another wordlist."))
            bfResults.pack(fill = "both", expand=True)
            resultsBoxSB.config(command = bfResults.yview)


"""

Command line version code

wordlist = "wordlist4zip.txt"
zip_file = "zippy.zip"

zip_file = zipfile.ZipFile(zip_file)

n_words = len(list(open(wordlist, "rb")))

print("Total passwords to test: ", n_words)


with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("[+] Password found:", word.decode().strip())
            exit(0)
print("[!] Password not found, try other wordlist.")




# --- references ---
# https://www.thepythoncode.com/article/crack-zip-file-password-in-python
"""
