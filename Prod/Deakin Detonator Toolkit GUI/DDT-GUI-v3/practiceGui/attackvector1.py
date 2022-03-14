## ATTACK VECTOR 1 PAGE ##

import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

from tkinter import font as tkfont
from tkinter import *
from tkinter import font, messagebox
import random, requests, os, sys
import PySimpleGUI as sg

class AttackVectorOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        framefont = tkfont.Font(family='Calibri', size=33, weight="bold")

        main_frame = tk.Frame(self)


        highlightFont = font.Font(family='Calibri', name='appHighlightFont', size=18)



        def change_to_Step1():
                step1frame = tk.Label(main_frame, text="\n    Step 1  \n\n       Explanation for step 1 here", fg='black', bg='white',  font=('Calibri', 20), anchor= 'nw')
                step1frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)

        def change_to_Step2():
                step1frame = tk.Label(main_frame, text="\n    Step 2  \n\n       Explanation for Step 2 here", fg='black', bg='white',  font=('Calibri', 20), anchor= 'nw')
                step1frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)

        def change_to_Step3():
                step1frame = tk.Label(main_frame, text="\n    Step 3  \n\n       Explanation for Step 3 Here", fg='black', bg='white',  font=('Calibri', 20), anchor= 'nw')
                step1frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)

        def change_to_Step4():
                step1frame = tk.Label(main_frame, text="\n    Step 4  \n\n      Explanation for Step 4 here", fg='black', bg='white',  font=('Calibri', 20), anchor= 'nw')
                step1frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)



        nav_bar = Canvas(main_frame, bg='#FDFDFD')
        nav_bar.place(rely=0, relheight=0.08, relwidth=1)

        aboutframe = tk.Label(main_frame, text="   Attack Vector Name", bg='#64C1DA', anchor="w", font=framefont)
        aboutframe.place(rely=0.08, relheight=0.12, relwidth=1)
        
        allscreenframe = tk.Label(main_frame, bg='white')
        allscreenframe.place(rely=0.2, relheight=1, relwidth=1)

        sidescreenframe = tk.Label(main_frame, text="\n            Steps", bg='#E7E7E7',  font=('Calibri', 20), anchor= 'nw')
        sidescreenframe.place(rely=0.2, relheight=1, relwidth=0.2)


        button_home = tk.Button(main_frame, text="← Home", borderwidth=6, font=controller.btn_font2 , command=lambda: controller.show_frame("StartPage"))
        button_vectors = tk.Button(main_frame, text="Attack Vectors", borderwidth=6, font=controller.btn_font2 , command=lambda: controller.show_frame("PageTwo"))
        button_about = tk.Button(main_frame, text="About", borderwidth=6, font=controller.btn_font2 , command=lambda: controller.show_frame("PageOne"))
        button_tools = tk.Button(main_frame, text="Tools",borderwidth=6, font=controller.btn_font2 ,  command=lambda: controller.show_frame("PageThree"))
        button_references = tk.Button(main_frame, text="References", borderwidth=6, font=controller.btn_font2 , command=lambda: controller.show_frame("PageFour"))


        button_home.place(rely=0.01, relx=0.02, relheight=0.06, relwidth=0.1)
        button_about.place(rely=0.01, relx=0.6, relheight=0.06, relwidth=0.09)
        button_tools.place(rely=0.01, relx=0.8, relheight=0.06, relwidth=0.09)
        button_references.place(rely=0.01, relx=0.9, relheight=0.06, relwidth=0.09)
        button_vectors.place(rely=0.01, relx=0.7, relheight=0.06, relwidth=0.09)
        
        step1btn = tk.Button(main_frame, text="Step 1", bg="#E7E7E7", fg="black", font=highlightFont, command=change_to_Step1, relief='flat').place(rely=0.3, relx=0.02, relheight=0.05, relwidth=0.1)
        step2btn = tk.Button(main_frame, text="Step 2", bg="#E7E7E7", fg="black", font=highlightFont, command=change_to_Step2, relief='flat').place(rely=0.4, relx=0.02, relheight=0.05, relwidth=0.1)
        step3btn = tk.Button(main_frame, text="Step 3", bg="#E7E7E7", fg="black", font=highlightFont, command=change_to_Step3, relief='flat').place(rely=0.5, relx=0.02, relheight=0.05, relwidth=0.1)
        step4btn = tk.Button(main_frame, text="Step 4", bg="#E7E7E7", fg="black", font=highlightFont, command=change_to_Step4, relief='flat').place(rely=0.6, relx=0.02, relheight=0.05, relwidth=0.1)



        main_frame.pack(fill='both', expand=1)
