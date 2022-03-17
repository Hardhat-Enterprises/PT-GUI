# Hash Analyzer
# By Willem Tranku
# GUI by Ryan Harris

from sys import exit
import base64
import re
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

# Global var for list of hashes
global hashes
hashes = []


class HashAn(tk.Frame):

    # ============================= Initializer Function

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        abtframefont = tkfont.Font(family='Calibri', size=33, weight="bold")
        display_nav_bar(self, controller)
        aboutframe = tk.Label(self, text="    Hash Analyzer", bg='#3B5262', fg='white', anchor="c", font=abtframefont)
        aboutframe.place(rely=0.08, relheight=0.12, relwidth=1)

        allscreenframe = tk.Label(self, bg='white')
        allscreenframe.place(rely=0.2, relheight=1, relwidth=1)

        # LABELS / TEXT ON SCREEN
        labelHomepage = Label(self, text="Enter hash value to check",
                              font=('Calibri', 16), bg='#4D6C84', fg='white', anchor='c').place(rely=0.26, relx=0.12,
                                                                                                relheight=0.06,
                                                                                                relwidth=0.20)

        #  BUTTONS
        Button(self, text="CHECK HASH", font=('Calibri', 16), anchor='c', bg='#4D6C84', fg='white',
               command=lambda: self.check_hash()).place(rely=0.35, relx=0.33, relheight=0.06, relwidth=0.38)

        # INPUT TEXT BOXES
        self.HashTB = Entry(self, font=('Calibri', 16))
        self.HashTB.place(rely=0.26, relx=0.33, relheight=0.06, relwidth=0.38)

        # OUTPUT TEXT BOX
        resultsBox = tk.Label(self, bg='#E3E4E5')
        resultsBox.place(rely=0.45, relx=0.33, relheight=0.52, relwidth=0.38)
        resultsBoxSB = Scrollbar(resultsBox)
        resultsBoxSB.pack(side=RIGHT, fill=Y)
        hashResults = Listbox(resultsBox, yscrollcommand=resultsBoxSB.set)

    # Check the hash function ===============
    def check_hash(self):
        resultsBox = tk.Label(self, bg='#E3E4E5')
        resultsBox.place(rely=0.45, relx=0.35, relheight=0.52, relwidth=0.30)
        resultsBoxSB = Scrollbar(resultsBox)
        resultsBoxSB.pack(side=RIGHT, fill=Y)
        hashResults = Listbox(resultsBox, yscrollcommand=resultsBoxSB.set)

        global hashes
        hashes.clear()
        h = self.HashTB.get()

        # check all the hashes to see if input is matches
        self.md5(h);
        self.md2(h);
        self.md4(h);
        self.sha1(h)
        self.sha224(h);
        self.sha3224(h);
        self.sha256(h);
        self.sha3256(h)
        self.sha384(h);
        self.sha3384(h);
        self.sha512(h);
        self.sha3512(h)
        self.ripemd160(h);
        self.ripemd256(h);
        self.ripemd320(h);
        self.tiger128(h)
        self.tiger160(h);
        self.tiger192(h);
        self.whirlpool(h);
        self.adler32(h)
        self.ntlm(h);
        self.crc16(h);
        self.crc32(h);
        self.desunix(h)
        self.haval128(h);
        self.haval160(h);
        self.haval192(h);
        self.haval224(h)
        self.haval256(h)

        if (bool(hashes) == True):
            hashResults.insert(END, ("Potential Hash format(s) include:"))
            hashResults.insert(END, (" "))
            for x in hashes:
                hashResults.insert(END, (x + ("\n")))
        else:
            hashResults.insert(END, ("No recognizable hash formats found..."))

        hashResults.pack(fill="both", expand=True)
        resultsBoxSB.config(command=hashResults.yview)

    # ========== ALL THE HASH DETAILS / FUNCTIONS TO MATCH TO USER INPUT ===================

    def md5(self, hash):
        global hashes
        if (re.search(r'([a-fA-F0-9]{32})', hash) != None and len(hash) == 32):
            hashes.append("MD5")

    def md4(self, hash):
        global hashes
        if (re.search(r'([a-fA-F0-9]{32})', hash) != None and len(hash) == 32):
            hashes.append("MD4")

    def md2(self, hash):
        global hashes
        if (re.search(r'([a-fA-F0-9]{32})', hash) != None and len(hash) == 32):
            hashes.append("MD2")

    def sha1(self, hash):
        global hashes
        if (re.search(r'([a-fA-F0-9]{40})', hash) != None and len(hash) == 40):
            hashes.append("SHA1")

    def sha224(self, hash):
        global hashes
        if (re.search(r'([a-fA-F0-9]{56})', hash) != None and len(hash) == 56):
            hashes.append("SHA224")

    def sha3224(self, hash):
        global hashes
        if (re.search(r'([a-fA-F0-9]{56})', hash) != None and len(hash) == 56):
            hashes.append("SHA3224")

    def sha256(self, hash):
        global hashes
        if (re.search(r'([a-fA-F0-9]{64})', hash) != None and len(hash) == 64):
            hashes.append("SHA256")

    def sha3256(self, hash):
        global hashes
        if (re.search(r'([a-fA-F0-9]{64})', hash) != None and len(hash) == 64):
            hashes.append("SHA3256")

    def sha384(self, hash):
        global hashes
        if (re.search(r'([a-fA-F0-9]{96})', hash) != None and len(hash) == 96):
            hashes.append("SHA384")

    def sha3384(self, hash):
        global hashes
        if (re.search(r'([a-fA-F0-9]{96})', hash) != None and len(hash) == 96):
            hashes.append("SHA3384")

    def sha512(self, hash):
        global hashes
        if (re.search(r'([a-fA-F0-9]{128})', hash) != None and len(hash) == 128):
            hashes.append("SHA512")

    def sha3512(self, hash):
        global hashes
        if (re.search(r'([a-fA-F0-9]{128})', hash) != None and len(hash) == 128):
            hashes.append("SHA3512")

    def ripemd160(self, hash):
        global hashes
        if (re.search(r'([a-fA-F0-9]{40})', hash) != None and len(hash) == 40):
            hashes.append("RIPE MD160")

    def ripemd256(self, hash):
        global hashes
        if (re.search(r'([a-fA-F0-9]{64})', hash) != None and len(hash) == 64):
            hashes.append("RIPE MD256")

    def ripemd320(self, hash):
        global hashes
        if (re.search(r'([a-fA-F0-9]{80})', hash) != None and len(hash) == 80):
            hashes.append("RIPE MD320")

    def tiger128(self, hash):
        global hashes
        if (re.search(r'([a-fA-F0-9]{32})', hash) != None and len(hash) == 32):
            hashes.append("TIGER 128")

    def tiger160(self, hash):
        global hashes
        if (re.search(r'([a-fA-F0-9]{40})', hash) != None and len(hash) == 40):
            hashes.append("TIGER 160")

    def tiger192(self, hash):
        global hashes
        if (re.search(r'([a-fA-F0-9]{48})', hash) != None and len(hash) == 48):
            hashes.append("TIGER 192")

    def whirlpool(self, hash):
        global hashes
        if (re.search(r'([a-fA-F0-9]{128})', hash) != None and len(hash) == 128):
            hashes.append("Whirlpool")

    def adler32(self, hash):
        global hashes
        if (re.search(r'([a-fA-F0-9]{8})', hash) != None and len(hash) == 8):
            hashes.append("adler32")

    def ntlm(self, hash):
        global hashes
        if (re.search(r'([a-fA-F0-9]{32})', hash) != None and len(hash) == 32):
            hashes.append("NTLM")

    def crc16(self, hash):
        global hashes
        if (re.search(r'([a-fA-F0-9]{4})', hash) != None and len(hash) == 4):
            hashes.append("crc16")

    def crc32(self, hash):
        global hashes
        if (re.search(r'([a-fA-F0-9]{8})', hash) != None and len(hash) == 8):
            hashes.append("crc32")

    def desunix(self, hash):
        global hashes
        if (re.search(r'([./0-9A-Za-z]{13})', hash) != None and len(hash) == 13):
            hashes.append("desunix")

    def haval128(self, hash):
        global hashes
        if (re.search(r'([a-fA-F0-9]{32})', hash) != None and len(hash) == 32):
            hashes.append("haval128")

    def haval160(self, hash):
        global hashes
        if (re.search(r'([a-fA-F0-9]{40})', hash) != None and len(hash) == 40):
            hashes.append("haval160")

    def haval192(self, hash):
        global hashes
        if (re.search(r'([a-fA-F0-9]{48})', hash) != None and len(hash) == 48):
            hashes.append("haval192")

    def haval224(self, hash):
        global hashes
        if (re.search(r'([a-fA-F0-9]{56})', hash) != None and len(hash) == 56):
            hashes.append("haval224")

    def haval256(self, hash):
        global hashes
        if (re.search(r'([a-fA-F0-9]{64})', hash) != None and len(hash) == 64):
            hashes.append("haval256")

# =======================================
