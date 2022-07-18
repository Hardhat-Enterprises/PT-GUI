## ATTACK VECTOR 3 PAGE ##

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


class AttackVectorThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        framefont = tkfont.Font(family='Calibri', size=33, weight="bold")

        main_frame = tk.Frame(self)

        highlightFont = font.Font(family='Calibri', name='appHighlightFont', size=18)

        global unpatchedvul
        unpatchedvul = tk.PhotoImage(file='resources/unpatched.png')

        def load_nmap_tool():
            os.chdir("./Tools/Nmap_Gui")
            cmd = "python3 nmapGUI.py"
            p1 = Popen(cmd, stdout=PIPE, universal_newlines=True, shell=True)
            os.chdir("../../")

        def load_vulnexploit_tool():
            os.chdir("./Tools")
            cmd = 'exo-open --launch TerminalEmulator'
            p1 = Popen([cmd + ' python3 VulnExploit.py'], stdout=PIPE, shell=True)
            os.chdir("../../")

        def load_terminal():
            p1 = Popen("exo-open --launch TerminalEmulator", stdout=PIPE, universal_newlines=True, shell=True).stdout

        def change_to_Step1():
            text = (
                "\n\nStep 1: \n\n"
                "o   Recon the target system for Vulnerabilities\n\n"
                "o   Using Nmap tool below, Enter the IP Address of the target system and select Vulscan from the scan type.\n\n"
                "o   Press Scan           Or\n\n"
                "o   Open a new terminal and enter the script below - changing IP to the IP of the target system.\n\n"
                "               nmap -sV --script=Tools/Nmap_Gui/scipag_vulscan/vulscan.nse IP\n"
            )
            step1frame = tk.Message(main_frame, text=text, font=('OpenSans', 14), anchor='nw',
                                    aspect=350)
            step1frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)
            nmapButton = ttk.Button(step1frame, text="Nmap Tool", style='Accent.TButton',
                                   command=load_nmap_tool).place(rely=0.4, relx=0.02, relheight=0.05,
                                                                                relwidth=0.1)
            terminalButton = ttk.Button(step1frame, text="Terminal", style='Accent.TButton',
                                       command=load_terminal).place(rely=0.4, relx=0.14, relheight=0.05,
                                                                                   relwidth=0.1)

        def change_to_Step2():
            text = (
                "\n\nStep 2:  \n\n"
                "o   Use ‘UpdateScript.py’from Attack Vector 1 if you have not used it\n\n"
                "o   Press VulnExploit Tool button\n\n"
                "o   Select 1 to search Metasploit for vulnerability found in step 1\n\n"
                "o   Copy the exploit found\n\n"
                "o   Select 2 to find information about required fields of an exploit and paste a copied exploit from select 1.\n\n"

            )
            step1frame = tk.Message(main_frame, text=text, font=('OpenSans', 14), anchor='nw',
                                    aspect=300)
            step1frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)
            vulnButton = ttk.Button(step1frame, text="VulnExploit", style='Accent.TButton',
                                   command=load_vulnexploit_tool).place(rely=0.4, relx=0.02,
                                                                                       relheight=0.05, relwidth=0.1)
            terminalButton = ttk.Button(step1frame, text="Terminal", style='Accent.TButton',
                                       command=load_terminal).place(rely=0.4, relx=0.14, relheight=0.05,
                                                                                   relwidth=0.1)

        def change_to_Step3():
            text = (
                "\n\nStep 3:  \n\n"
                "o   Select 3 to use exploit, enter exploit that you searched information about and enter requested information about the exploit and payload.\n\n"
                "o   Press Enter to launch exploit\n\n"
                "o   Select 4 open session created by exploit\n\n"
                "o   Select 5 to exit program\n\n"
            )
            step1frame = tk.Message(main_frame, text=text, font=('OpenSans', 14), anchor='nw',
                                    aspect=300)
            step1frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)
            vulnButton = ttk.Button(step1frame, text="VulnExploit", style='Accent.TButton',
                                   command=load_vulnexploit_tool).place(rely=0.4, relx=0.02,
                                                                                       relheight=0.05, relwidth=0.1)
            terminalButton = ttk.Button(step1frame, text="Terminal", style='Accent.TButton',
                                       command=load_terminal).place(rely=0.4, relx=0.14, relheight=0.05,
                                                                                   relwidth=0.1)
        
        def create_step_button(step_num, command):
            button = ttk.Button(main_frame, text="Step " + str(step_num),
                               command=command, style='Accent.TButton').place(rely=0.20 + 0.1 * step_num, relx=0.04,
                                                                     relheight=0.05, relwidth=0.1)
        
        tkfont.Font(family='OpenSans', size=13)
        framefont = tkfont.Font(family='Arial Rounded MT Bold', size=28, weight='bold')

        title_label = tk.Label(self, text="Unpatched Vulnerabilities and Exploits", bg='white', fg='#92CEFF', anchor="c", font=framefont)
        title_label.place(rely=0.06, relheight=0.12, relwidth=1)
        
        # creates blue bar as canvas below nav bar
        title_canvas = tk.Canvas(self, bg='#c8e6ff', highlightthickness=0)
        title_canvas.place(rely=0.08, relheight=0.004, relwidth=1)

        # creates blue bar as canvas below title
        title_canvas = tk.Canvas(self, bg='#c8e6ff', highlightthickness=0)
        title_canvas.place(rely=0.155, relheight=0.004, relwidth=1)

        allscreenframe = tk.Label(main_frame, bg='white')
        allscreenframe.place(rely=0.2, relheight=1, relwidth=1)

        sidescreenframe = tk.Label(main_frame, text="\n           Steps:", bg='white', fg='#92CEFF', font=('Calibri', 20, 'bold'),
                                   anchor='nw')
        sidescreenframe.place(rely=0.2, relheight=1, relwidth=0.2)

        unpatched_label = tk.Label(main_frame, image=unpatchedvul)
        unpatched_label.place(rely=0.36, relx=0.4)

        create_step_button(1, change_to_Step1)
        create_step_button(2, change_to_Step2)
        create_step_button(3, change_to_Step3)
        
        # step4btn = tk.Button(main_frame, text="Step 4", bg="#E7E7E7", fg="black", font=highlightFont, command=change_to_Step4, relief='flat').place(rely=0.6, relx=0.02, relheight=0.05, relwidth=0.1)

        display_nav_bar(self, controller)
        main_frame.pack(fill='both', expand=1)
