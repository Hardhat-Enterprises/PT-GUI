## ABOUT PAGE ##


import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2
from tkinter import font as tkfont
from tkinter import *
from tkinter import font, messagebox
import random, requests, os, sys
import PySimpleGUI as sg

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        abtframefont = tkfont.Font(family='Calibri', size=33, weight="bold")


        nav_bar = Canvas(self, bg='#FDFDFD')
        nav_bar.place(rely=0, relheight=0.08, relwidth=1)



        button_home = tk.Button(self, text="← Home", borderwidth=6, font=controller.btn_font2 , command=lambda: controller.show_frame("StartPage"))
        button_vectors = tk.Button(self, text="Attack Vectors", borderwidth=6, font=controller.btn_font2 , command=lambda: controller.show_frame("PageTwo"))
        button_about = tk.Button(self, text="About", borderwidth=6, bg="#9A9A9A" , font=controller.btn_font2 , command=lambda: controller.show_frame("PageOne"))
        button_tools = tk.Button(self, text="Tools",borderwidth=6, font=controller.btn_font2 ,  command=lambda: controller.show_frame("PageThree"))
        button_references = tk.Button(self, text="References", borderwidth=6, font=controller.btn_font2 , command=lambda: controller.show_frame("PageFour"))


        button_home.place(rely=0.01, relx=0.02, relheight=0.06, relwidth=0.1)
        button_about.place(rely=0.01, relx=0.6, relheight=0.06, relwidth=0.09)
        button_tools.place(rely=0.01, relx=0.8, relheight=0.06, relwidth=0.09)
        button_references.place(rely=0.01, relx=0.9, relheight=0.06, relwidth=0.09)
        button_vectors.place(rely=0.01, relx=0.7, relheight=0.06, relwidth=0.09)


        aboutframe = tk.Label(self, text="    About", bg='#64C1DA', anchor="w", font=abtframefont)
        aboutframe.place(rely=0.08, relheight=0.12, relwidth=1)
        
        allscreenframe = tk.Label(self, bg='white')
        allscreenframe.place(rely=0.2, relheight=1, relwidth=1)


        heading1 = tk.Label(self, text='WHAT IS DDT?', bg="#E7E7E7" , fg="black", font=('Calibri', 32))
        heading2 = tk.Label(self, text="\n\n In it's simplest definition, Deakin Detonator Toolkit (DDT) is \na penetration testing toolkit."
				"\n\nThe toolkit allows you to make use of a variety of tools, without needing\n the \"know-how\" of each command."
				"\n\n\n We have simplified the penetration testing experience for both newcomers who\n are still learning, and those who have been hacking for years." 
				"\n\nTo get started, choose a categoery of Tools from the SubMenus\n Then chose a specific tool from the Category."
				"\n\n Alternatively, you can choose an attack vector from the attack \nvectors sub-menu and follow the steps."
				"\n\n\n\nHappy hacking!\n\n",
				bg="#E7E7E7" , fg="black", font=('Calibri', 13))

       
        heading1.place(rely=0.28, relx=0.3, relheight=0.08, relwidth=0.4)
        heading2.place(rely=0.4, relx=0.3, relheight=0.54, relwidth=0.4)

