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
            tk.Button(frame, text="Directory Traversal Fuzzer", bg="#E7E7E7", fg="black", font=highlightFont,
                      command=lambda: controller.show_frame("DTFuzz"),
                      relief='flat').place(rely=0.47, relx=0.02, relheight=0.05, relwidth=0.18)

        def change_to_Step1():
            text = (
                "\n\nStep 1:\n\n"
                "o   Open Directory Traversal Fuzzer tool by clicking on the button below.\n\n"
                "o   Enter the homepage of the targeted site.\n\n"

            )
            step1frame = tk.Message(main_frame, text=text, fg='black', bg='white', font=('Calibri', 20), anchor='nw',
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
            step2frame = tk.Message(main_frame, text=text, fg='black', bg='white', font=('Calibri', 20), anchor='nw',
                                    aspect=350)
            step2frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)
            run_dtfuzz_button(step2frame)

        # creates blue bar as canvas below nav bar housing label containing title of page
        title_canvas = tk.Canvas(self, bg='#64C1DA', highlightthickness=0)
        title_canvas.place(rely=0.08, relheight=0.12, relwidth=1)
        title_label = tk.Label(self, text="Directory Triversal & IDOR", bg='#4D6C84', fg='white', anchor="c",
                               font=framefont)
        title_label.place(rely=0.08, relheight=0.12, relwidth=1)

        allscreenframe = tk.Label(main_frame, bg='white')
        allscreenframe.place(rely=0.2, relheight=1, relwidth=1)

        sidescreenframe = tk.Label(main_frame, text="\n          Steps\n\n", bg='#E7E7E7', font=('Calibri', 20, 'bold'),
                                   anchor='nw')
        sidescreenframe.place(rely=0.2, relheight=1, relwidth=0.2)

        revtcp_label = tk.Label(main_frame, image=dirtraverse)
        revtcp_label.place(rely=0.36, relx=0.4)

        step1btn = tk.Button(main_frame, text="Step 1", bg="#E7E7E7", fg="black", font=highlightFont,
                             command=change_to_Step1, relief='flat').place(rely=0.3, relx=0.02, relheight=0.05,
                                                                           relwidth=0.1)
        step2btn = tk.Button(main_frame, text="Step 2", bg="#E7E7E7", fg="black", font=highlightFont,
                             command=change_to_Step2, relief='flat').place(rely=0.4, relx=0.02, relheight=0.05,
                                                                           relwidth=0.1)
        # step3btn = tk.Button(main_frame, text="Step 3", bg="#E7E7E7", fg="black", font=highlightFont, command=change_to_Step3, relief='flat').place(rely=0.5, relx=0.02, relheight=0.05, relwidth=0.1)

        display_nav_bar(self, controller)
        main_frame.pack(fill='both', expand=1)
