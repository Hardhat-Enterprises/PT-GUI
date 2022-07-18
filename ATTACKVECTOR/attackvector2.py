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

from Fuzzers.DirectoryTraversalFuzzer import DTFuzz


class AttackVectorTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        framefont = tkfont.Font(family='Calibri', size=33, weight="bold")

        main_frame = tk.Frame(self)

        highlightFont = font.Font(family='Calibri', name='appHighlightFont2', size=18)

        global dirtraverse
        dirtraverse = tk.PhotoImage(file='resources/dirtraversal.png')

        def run_dtfuzz_button(frame):
            ttk.Button(frame, text="Directory Traversal Fuzzer", style='Accent.TButton',
                      command=lambda: controller.show_frame("DTFuzz")).place(rely=0.3, relx=0.02, relheight=0.05, relwidth=0.18)

        def change_to_Step1():
            text = (
                "\n\nStep 1:\n\n"
                "o   Open Directory Traversal Fuzzer tool by clicking on the button below.\n\n"
                "o   Enter the homepage of the targeted site.\n\n"

            )
            step1frame = tk.Message(main_frame, text=text, font=('OpenSans', 14), anchor='nw',
                                    aspect=350)
            step1frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)
            run_dtfuzz_button(step1frame)

        def change_to_Step2():
            text = (
                "\n\nStep 2:\n\n"
                "o  Choose from the menu presented what you wish to do.\n\n"
                "o  Some options include:scan for commonly insecure/open directories using a library supplied in the same"
                "folder as the python script, open the homepage or custom directory within the homepage, or download a file.\n"

            )
            step2frame = tk.Message(main_frame, text=text, font=('OpenSans', 14), anchor='nw',
                                    aspect=350)
            step2frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)
            run_dtfuzz_button(step2frame)
            
        def create_step_button(step_num, command):
            button = ttk.Button(main_frame, text="Step " + str(step_num),
                               command=command, style='Accent.TButton').place(rely=0.25 + 0.1 * step_num, relx=0.04,
                                                                     relheight=0.05, relwidth=0.1)
        
        tkfont.Font(family='OpenSans', size=13)
        framefont = tkfont.Font(family='Arial Rounded MT Bold', size=28, weight='bold')

        title_label = tk.Label(self, text="Directory Triversal & IDOR", bg='white', fg='#92CEFF', anchor="c", font=framefont)
        title_label.place(rely=0.06, relheight=0.12, relwidth=1)

	# creates blue bar as canvas below nav bar
        title_canvas = tk.Canvas(self, bg='#c8e6ff', highlightthickness=0)
        title_canvas.place(rely=0.08, relheight=0.004, relwidth=1)

        # creates blue bar as canvas below title
        title_canvas = tk.Canvas(self, bg='#c8e6ff', highlightthickness=0)
        title_canvas.place(rely=0.155, relheight=0.004, relwidth=1)

        allscreenframe = tk.Label(main_frame)
        allscreenframe.place(rely=0.2, relheight=1, relwidth=1)

        sidescreenframe = tk.Label(main_frame, text="\n          Steps:\n\n", bg='white', fg='#92CEFF', font=('Calibri', 20, 'bold'),
                                   anchor='nw')
        sidescreenframe.place(rely=0.25, relheight=1, relwidth=0.2)

        revtcp_label = tk.Label(main_frame, image=dirtraverse)
        revtcp_label.place(rely=0.36, relx=0.4)

        create_step_button(1, change_to_Step1)
        create_step_button(2, change_to_Step2)
        
        # step3btn = tk.Button(main_frame, text="Step 3", bg="#E7E7E7", fg="black", font=highlightFont, command=change_to_Step3, relief='flat').place(rely=0.5, relx=0.02, relheight=0.05, relwidth=0.1)

        display_nav_bar(self, controller)
        main_frame.pack(fill='both', expand=1)
