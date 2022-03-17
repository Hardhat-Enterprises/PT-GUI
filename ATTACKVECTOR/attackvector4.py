## ATTACK VECTOR 4 PAGE ##

import tkinter as tk  # python 3
from tkinter import font as tkfont  # python 3
# import Tkinter as tk     # python 2
# import tkFont as tkfont  # python 2

from tkinter import font as tkfont
from tkinter import *
from tkinter import font, messagebox
import random, requests, os, sys
import PySimpleGUI as sg
from nav_bar import *
from subprocess import call, Popen, PIPE
import os


class AttackVectorFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        framefont = tkfont.Font(family='Calibri', size=33, weight="bold")

        main_frame = tk.Frame(self)

        highlightFont = font.Font(family='Calibri', name='appHighlightFont4', size=18)

        global unpatchedvul
        unpatchedvul = tk.PhotoImage(file='resources/unpatched.png')

        def load_sqli():
            os.chdir("./Tools")
            cmd = "python3 SQLi_tool.py"
            p1 = Popen(cmd, stdout=PIPE, universal_newlines=True, shell=True)
            os.chdir("../../")

        # def load_vulnexploit_tool():
        #    os.chdir("./Tools")
        #    cmd = 'exo-open --launch TerminalEmulator'
        #    p1 = Popen([cmd + ' python3 VulnExploit.py'], stdout=PIPE, shell = True)
        #    os.chdir("../../")

        def load_terminal():
            p1 = Popen("exo-open --launch TerminalEmulator", stdout=PIPE, universal_newlines=True, shell=True).stdout

        def change_to_Step1():
            text = (
                "\n\nStep 1: \n\n"
                "Attack Vector 4 being maintaining"
            )
            step1frame = tk.Message(main_frame, text=text, fg='black', bg='white', font=('Calibri', 20), anchor='nw',
                                    aspect=350)
            step1frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)
            XSSButton = tk.Button(step1frame, text="SQL injection Tool", bg="#E7E7E7", fg="black", font=highlightFont,
                                  command=load_sqli, relief='flat').place(rely=0.5, relx=0.02, relheight=0.05,
                                                                          relwidth=0.1)
            terminalButton = tk.Button(step1frame, text="Terminal", bg="#E7E7E7",
                                       fg="black", font=highlightFont, command=load_terminal,
                                       relief='flat').place(rely=0.5, relx=0.14,
                                                            relheight=0.05, relwidth=0.1)

        # def change_to_Step2():
        #    text = (
        #    "\n\nStep 2:  \n\n"
        #    "Attack Vector 4 being maintaining"
        #    )
        #    step1frame = tk.Message(main_frame, text=text, fg='black', bg='white',  font=('Calibri', 20), anchor= 'nw', aspect=300)
        #    step1frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)
        #    SQLiButton = tk.Button(step1frame, text="SQL Injection", bg="#E7E7E7", fg="black", 
        #                            font=highlightFont, command=load_sqli, 
        #                            relief='flat').place(rely=0.6, relx=0.02, relheight=0.05, relwidth=0.1)
        #    terminalButton = tk.Button(step1frame, text="Terminal", bg="#E7E7E7", fg="black", font=highlightFont,
        #                                 command=load_terminal, relief='flat').place(rely=0.6, relx=0.14, relheight=0.05, relwidth=0.1)
        #
        # creates blue bar as canvas below nav bar housing label containing title of page
        title_canvas = tk.Canvas(self, bg='#64C1DA', highlightthickness=0)
        title_canvas.place(rely=0.08, relheight=0.12, relwidth=1)
        title_label = tk.Label(self, text="Web Application Attacks: Automated XSS and SQLiInjection attack",
                               bg='#64C1DA', anchor="w", font=framefont)
        title_label.place(rely=0.08, relx=0.03, relheight=0.12, relwidth=1)

        allscreenframe = tk.Label(main_frame, bg='white')
        allscreenframe.place(rely=0.2, relheight=1, relwidth=1)

        sidescreenframe = tk.Label(main_frame, text="\n            Steps", bg='#E7E7E7',
                                   font=('Calibri', 20), anchor='nw')
        sidescreenframe.place(rely=0.2, relheight=1, relwidth=0.2)
        # delete it when you done the content.
        maintainnotice = tk.Label(self, text="ATTACK VECTOR 4 being maintaining", bg='#6f8396', fg='white',
                                  borderwidth=8, relief=RAISED,
                                  font=("Calibri", 30)).pack(side=LEFT, fill=BOTH, expand=True)

        # step1btn = tk.Button(main_frame, text="Step 1",
        #                     bg="#E7E7E7", fg="black",
        #                     font=highlightFont,
        #                     command=change_to_Step1,
        #                     relief='flat').place(rely=0.3, relx=0.02,
        #                                             relheight=0.05, relwidth=0.1)
        # step2btn = tk.Button(main_frame, text="Step 2",
        #                    bg="#E7E7E7", fg="black",
        #                    font=highlightFont, command=change_to_Step2,
        #                    relief='flat').place(rely=0.4, relx=0.02, relheight=0.05, relwidth=0.1)
        # step3btn = tk.Button(main_frame, text="Step 3", bg="#E7E7E7", fg="black", font=highlightFont, command=change_to_Step3, relief='flat').place(rely=0.5, relx=0.02, relheight=0.05, relwidth=0.1)
        # step4btn = tk.Button(main_frame, text="Step 4", bg="#E7E7E7", fg="black", font=highlightFont, command=change_to_Step4, relief='flat').place(rely=0.6, relx=0.02, relheight=0.05, relwidth=0.1)
        #
        display_nav_bar(self, controller)
        main_frame.pack(fill='both', expand=1)
