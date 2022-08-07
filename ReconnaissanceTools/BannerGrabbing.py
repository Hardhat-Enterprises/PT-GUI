#!/usr/bin/env/ python

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


class BannerGrab(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #created title
        tkfont.Font(family='OpenSans', size=13)
        framefont = tkfont.Font(family='Arial Rounded MT Bold', size=28, weight='bold')
        title_label = tk.Label(self, text="Banner Grabber", bg='white', fg='#92CEFF',
                               anchor="c", font=framefont)
        title_label.place(rely=0.06, relheight=0.12, relwidth=1)

        #creates blue bar as canvas below nav bar
        title_canvas = tk.Canvas(self, bg='#c8e6ff', highlightthickness=0)
        title_canvas.place(rely=0.08, relheight=0.004, relwidth=1)
        display_nav_bar(self, controller)

        #creates blue bar as canvas below title
        title_canvas = tk.Canvas(self, bg='#c8e6ff', highlightthickness=0)
        title_canvas.place(rely=0.155, relheight=0.004, relwidth=1)

        label = ttk.Label(self, text=" Enter Target IP Address:", font=('Calibri', 14), style='Dropdown.TButton').place(rely=0.38, relx=0.16, relheight=0.08, relwidth=0.22)
        label = ttk.Label(self, text=" Enter Port Number:", font=('Calibri', 14), style='Dropdown.TButton').place(rely=0.48, relx=0.16, relheight=0.08, relwidth=0.22)

        # Set input box for interface Entry
        self.entry = Entry(self, font=('Calibri', 13), )
        self.entry.place(rely=0.38, relx=0.36, relheight=0.08, relwidth=0.3)

        # Set input box for New Mac Address Entry
        self.entry2 = Entry(self, font=('Calibri', 13), )
        self.entry2.place(rely=0.48, relx=0.36, relheight=0.08, relwidth=0.3)

        # Start button
        ttk.Button(self, text="Start", style='Accent.TButton',
               command=self.mainprog).place(rely=0.43, relx=0.7, relheight=0.08, relwidth=0.08)

    def mainprog(self):
        import socket
        ip = self.entry.get()
        port = str(self.entry2.get())
        banner(self, ip, port)
        result = Label(self, text=self.storevar, font=('Calibri', 13))
        result.place(rely=0.68, relx=0.36, relwidth=0.3)


def banner(self, ip, port):
    import socket
    s = socket.socket()
    s.connect((ip, int(port)))
    self.storevar = s.recv(1024)
