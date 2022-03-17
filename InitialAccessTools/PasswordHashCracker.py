# Hash Analyzer
# By Willem Tranku
# GUI by Ryan Harris

import hashlib
# import Tkinter as tk     # python 2
# import tkFont as tkfont  # python 2
from tkinter import font as tkfont

from nav_bar import *

# Global var for list of hashes
wordlist = open("InitialAccessTools/wordlist4PHC.txt", "r")
wordlistString = wordlist.read()
global word_list
word_list = wordlistString.split("\n")


class PHCracker(tk.Frame):

    # ============================= Initializer Function

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        abtframefont = tkfont.Font(family='Calibri', size=33, weight="bold")
        display_nav_bar(self, controller)
        aboutframe = tk.Label(self, text="    Password Hash Cracker", bg='#3B5262', fg='white', anchor="c",
                              font=abtframefont)
        aboutframe.place(rely=0.08, relheight=0.12, relwidth=1)

        allscreenframe = tk.Label(self, bg='white')
        allscreenframe.place(rely=0.2, relheight=1, relwidth=1)

        # LABELS / TEXT ON SCREEN
        labelHomepage = Label(self, text="Enter password hash to crack",
                              font=('Calibri', 16), bg='#4D6C84', fg='white', anchor='c').place(rely=0.26, relx=0.12,
                                                                                                relheight=0.06,
                                                                                                relwidth=0.20)

        #  BUTTONS
        Button(self, text="CHECK HASH", font=('Calibri', 16), bg='#4D6C84', fg='white', anchor='c',
               command=lambda: self.check_hash()).place(rely=0.35, relx=0.33, relheight=0.06, relwidth=0.38)

        # INPUT TEXT BOXES
        self.HashTB = Entry(self, font=('Calibri', 16))
        self.HashTB.place(rely=0.26, relx=0.33, relheight=0.06, relwidth=0.38)

        # OUTPUT TEXT BOX
        resultsBox = tk.Label(self, bg='#E3E4E5', font=('Calibri', 16))
        resultsBox.place(rely=0.45, relx=0.33, relheight=0.52, relwidth=0.38)
        resultsBoxSB = Scrollbar(resultsBox)
        resultsBoxSB.pack(side=RIGHT, fill=Y)
        hashResults = Listbox(resultsBox, yscrollcommand=resultsBoxSB.set)

    # Check the hash function ===============
    def check_hash(self):
        resultsBox = tk.Label(self, bg='#E3E4E5', font=('Calibri', 16))
        resultsBox.place(rely=0.45, relx=0.35, relheight=0.52, relwidth=0.30)
        resultsBoxSB = Scrollbar(resultsBox)
        resultsBoxSB.pack(side=RIGHT, fill=Y)
        hashResults = Listbox(resultsBox, yscrollcommand=resultsBoxSB.set)
        flag = 0
        global word_list
        pass_hash = self.HashTB.get()

        # check md5 hashes
        for word in word_list:
            enc_wrd = word.encode('utf-8')
            digest = hashlib.md5(enc_wrd.strip()).hexdigest()

            if (digest == pass_hash):
                hashResults.insert(END, ("!! PASSWORD FOUND !!"))
                hashResults.insert(END, ("Password is:     " + word))
                flag = 1
                break

        # check sha1 hashes
        if (flag == 0):
            for word in word_list:
                enc_wrd = word.encode('utf-8')
                digest = hashlib.sha1(enc_wrd.strip()).hexdigest()

                if (digest == pass_hash):
                    hashResults.insert(END, ("!! PASSWORD FOUND !!"))
                    hashResults.insert(END, ("Password is :     " + word))
                    flag = 1
                    break

        if (flag == 0):
            hashResults.insert(END, ("Password not found."))

        hashResults.pack(fill="both", expand=True)
        resultsBoxSB.config(command=hashResults.yview)

# =======================================
