#!/usr/bin/env/ python

import tkinter as tk  # python 3
# import Tkinter as tk     # python 2
# import tkFont as tkfont  # python 2
from tkinter import font as tkfont

from nav_bar import *


class BannerGrab(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        abtframefont = tkfont.Font(family='Calibri', size=33, weight="bold")
        display_nav_bar(self, controller)
        aboutframe = tk.Label(self, text="    Banner Grabber", bg='#3B5262', fg='white', anchor="c", font=abtframefont)
        aboutframe.place(rely=0.08, relheight=0.12, relwidth=1)

        allscreenframe = tk.Label(self, bg='white')
        allscreenframe.place(rely=0.2, relheight=1, relwidth=1)

        label = Label(self, text=" Enter Target IP Address:", font=('Calibri', 14), bg='#4D6C84', fg='white',
                      anchor='c').place(rely=0.38, relx=0.16, relheight=0.08, relwidth=0.22)
        label = Label(self, text=" Enter Port Number:", font=('Calibri', 14), bg='#4D6C84', fg='white',
                      anchor='c').place(rely=0.48, relx=0.16, relheight=0.08, relwidth=0.22)

        # Set input box for interface Entry
        self.entry = Entry(self, font=('Calibri', 13), )
        self.entry.place(rely=0.38, relx=0.36, relheight=0.08, relwidth=0.3)

        # Set input box for New Mac Address Entry
        self.entry2 = Entry(self, font=('Calibri', 13), )
        self.entry2.place(rely=0.48, relx=0.36, relheight=0.08, relwidth=0.3)

        # Start button
        Button(self, text="Start", font=('Calibri', 14), bg='#4D6C84', fg='white', anchor='c',
               command=self.mainprog).place(rely=0.43, relx=0.7, relheight=0.08, relwidth=0.08)

    def mainprog(self):
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
