## ATTACK VECTORS PAGE ##

import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2


from tkinter import font as tkfont
from tkinter import *
from tkinter import font, messagebox
import random, requests, os, sys
import PySimpleGUI as sg


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        framefont = tkfont.Font(family='Calibri', size=33, weight="bold")


        nav_bar = Canvas(self, bg='#FDFDFD')
        nav_bar.place(rely=0, relheight=0.08, relwidth=1)

        aboutframe = tk.Label(self, text="    Attack Vectors List", bg='#64C1DA', anchor="w", font=framefont)
        aboutframe.place(rely=0.08, relheight=0.12, relwidth=1)
        
        allscreenframe = tk.Label(self, bg='white')
        allscreenframe.place(rely=0.2, relheight=1, relwidth=1)

        button_home = tk.Button(self, text="← Home", borderwidth=6, font=controller.btn_font2 , command=lambda: controller.show_frame("StartPage"))
        button_vectors = tk.Button(self, text="Attack Vectors", borderwidth=6, bg="#9A9A9A", font=controller.btn_font2 , command=lambda: controller.show_frame("PageTwo"))
        button_about = tk.Button(self, text="About", borderwidth=6, font=controller.btn_font2 , command=lambda: controller.show_frame("PageOne"))
        button_tools = tk.Button(self, text="Tools",borderwidth=6, font=controller.btn_font2 ,  command=lambda: controller.show_frame("PageThree"))
        button_references = tk.Button(self, text="References", borderwidth=6, font=controller.btn_font2 , command=lambda: controller.show_frame("PageFour"))


        button_home.place(rely=0.01, relx=0.02, relheight=0.06, relwidth=0.1)
        button_about.place(rely=0.01, relx=0.6, relheight=0.06, relwidth=0.09)
        button_tools.place(rely=0.01, relx=0.8, relheight=0.06, relwidth=0.09)
        button_references.place(rely=0.01, relx=0.9, relheight=0.06, relwidth=0.09)
        button_vectors.place(rely=0.01, relx=0.7, relheight=0.06, relwidth=0.09)


        button1 = tk.Button(self, text="₪          Attack Vector 1 Name", bg="#E7E7E7", fg="black", font=controller.btn_font , 
		command=lambda: controller.show_frame("AttackVectorOne"), anchor="w").place(rely=0.3, relx=0.02, relheight=0.08, relwidth=0.96)
        button2 = tk.Button(self, text="₪          Attack Vector 2 Name", bg="#E7E7E7", fg="black",  font=controller.btn_font , 
		 anchor="w").place(rely=0.4, relx=0.02, relheight=0.08, relwidth=0.96)
        button3 = tk.Button(self, text="₪          Attack Vector 3 Name", bg="#E7E7E7", fg="black",  font=controller.btn_font , 
		 anchor="w").place(rely=0.5, relx=0.02, relheight=0.08, relwidth=0.96)
        button4 = tk.Button(self, text="₪          Attack Vector 4 Name",  bg="#E7E7E7", fg="black", font=controller.btn_font , 
		 anchor="w").place(rely=0.6, relx=0.02, relheight=0.08, relwidth=0.96)
        button4 = tk.Button(self, text="₪          Attack Vector 5 Name",  bg="#E7E7E7", fg="black", font=controller.btn_font , 
		anchor="w").place(rely=0.7, relx=0.02, relheight=0.08, relwidth=0.96)

