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

class AttackVectorSeven(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        framefont = tkfont.Font(family='Calibri', size=33, weight="bold")


        main_frame = tk.Frame(self)


        highlightFont = font.Font(family='Calibri', name='appHighlightFont7', size=18)


        def load_terminal():
            p1 = Popen("exo-open --launch TerminalEmulator", stdout=PIPE, universal_newlines=True, shell = True).stdout

        def change_to_Step1():
            text = (
            "\nStep 1: NFS enumeration\n\n"
                "o   Find what port nfs is running on (usually on port 2049) by using 'nmap target IP'.\n\n"
                "o   Check if there are share directories open by using the command 'showmount -e IP'.\n\n"
                "o   Create a directory using the command 'mkdir /path/NameOfDirectory' to mount the share to.\n\n"
                "o   Mount your new directory to the share using the command 'mount -t nfs targetIP:share /PathToYourNewDirectory -nolock'.\n\n"
                "o   Check the directory or files you mounted, if you can't see it, exit the directory and access it again.\n\n"
            )
            step1frame = tk.Message(main_frame, text=text, fg='black', bg='white',  font=('Calibri', 20), anchor= 'nw', aspect = 300)
            step1frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)
            terminalButton = tk.Button(step1frame, text="Terminal", bg="#E7E7E7", fg="black", font=highlightFont, command=load_terminal, relief='flat').place(rely=0.5, relx=0.02, relheight=0.05, relwidth=0.1)


        def change_to_Step2():
            text = (
            "\nStep 2: Exploiting NFS\n\n"
                "o   Access the mounted directory, and search for the ssh directory inside it(or .ssh).\n\n"
                "o   If you find files containing private ssh keys, look for the 'id_rsa' file and copy it to your local machine.\n\n"
                "o   After copying the id_rsa file, use ssh to connect to that server with the key you obtained. the command will look like this ' ssh -i [Key file(id_rsa)] username@serverIP '.\n\n"
                "o   You should now have access to the server, but with limited permissions..\n\n"
            )
            step1frame = tk.Message(main_frame, text=text, fg='black', bg='white',  font=('Calibri', 20), anchor= 'nw', aspect = 300)
            step1frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)


        def change_to_Step3():
            text = (
            "\Step 3: Privilege escalation\n\n"
                "o   As you now have access to the NFS server, make a copy of the /bin/bash to the mounted path. This command will copy it to your current path[cp /bin/bash .]\n\n"
                "o   In your attack machine, log as root, and copy that bash file from the mounted to your local machine. Remove the copy in the mount, then place move the copy in your local machine back to the mount file.\n\n"
                "o   This basically creates the bash from the server as a root user. Once you put the bash file back to mounted path, use this command as root [chmod +sx bash].\n\n"
		"o   Now log back to the server using the ssh command from step two, run the bash file in the mounted path using the command [./bash -p].\n\n"
		"o   You now have root permissions, use id or whoami commands to confirm"
            )
            step3frame = tk.Message(main_frame, text=text, fg='black', bg='white',  font=('Calibri', 20), anchor= 'nw', aspect = 300)
            step3frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)

        # creates blue bar as canvas below nav bar housing label containing title of page
        title_canvas = tk.Canvas(self, bg='#64C1DA', highlightthickness=0)
        title_canvas.place(rely=0.08, relheight=0.12, relwidth=1)
        title_label = tk.Label(self, text="NFS Privilege Escalation", bg='#4D6C84', fg='white', anchor="c", font=framefont)
        title_label.place(rely=0.08, relheight=0.12, relwidth=1)

        allscreenframe = tk.Label(main_frame, bg='white')
        allscreenframe.place(rely=0.2, relheight=1, relwidth=1)

        sidescreenframe = tk.Label(main_frame, text="\n            Steps", bg='#E7E7E7',  font=('Calibri', 20), anchor= 'nw')
        sidescreenframe.place(rely=0.2, relheight=1, relwidth=0.2)

        step1btn = tk.Button(main_frame, text="Step 1", bg="#E7E7E7", fg="black", font=highlightFont, command=change_to_Step1, relief='flat').place(rely=0.3, relx=0.02, relheight=0.05, relwidth=0.1)
        step2btn = tk.Button(main_frame, text="Step 2", bg="#E7E7E7", fg="black", font=highlightFont, command=change_to_Step2, relief='flat').place(rely=0.4, relx=0.02, relheight=0.05, relwidth=0.1)
        step3btn = tk.Button(main_frame, text="Step 3", bg="#E7E7E7", fg="black", font=highlightFont, command=change_to_Step3, relief='flat').place(rely=0.5, relx=0.02, relheight=0.05, relwidth=0.1)


        display_nav_bar(self, controller)
        main_frame.pack(fill='both', expand=1) 
