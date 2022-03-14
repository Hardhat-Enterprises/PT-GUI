import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2
from pgone import PageOne
from pgtwo import PageTwo
from pgthree import PageThree
from pgfour import PageFour
from attackvector1 import AttackVectorOne
                
from tkinter import *
from tkinter import messagebox
import random, requests, os, sys
import PySimpleGUI as sg 


class GUIApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Calibri', size=18, weight="bold")
        self.btn_font = tkfont.Font(family='Calibri', size=18)
        self.btn_font2 = tkfont.Font(family='Calibri', size=15)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, AttackVectorOne):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        global background_image1
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_image1 = tk.PhotoImage(file='bkg.PNG')
        background_label1 = tk.Label(self, image=background_image1).place(relwidth=1, relheight=1)
        

        button1 = tk.Button(self, text="₪          About", bg="#E7E7E7", fg="black", font=controller.btn_font , 
		command=lambda: controller.show_frame("PageOne"), anchor="w", borderwidth=6).place( x = 250, y = 355+90, width=300, height=75)
        button2 = tk.Button(self, text="₪    Attack Vectors",bg="#E7E7E7", fg="black",  font=controller.btn_font , 
		command=lambda: controller.show_frame("PageTwo"), anchor="w", borderwidth=6).place( x = 250, y = 445 + 90, width=300, height=75)
        button3 = tk.Button(self, text="₪          Tools", bg="#E7E7E7", fg="black",  font=controller.btn_font , 
		command=lambda: controller.show_frame("PageThree"), anchor="w", borderwidth=6).place( x = 250, y = 535 + 90, width=300, height=75)
        button4 = tk.Button(self, text="₪       References",  bg="#E7E7E7", fg="black", font=controller.btn_font , 
		command=lambda: controller.show_frame("PageFour"), anchor="w", borderwidth=6).place( x = 250, y = 625 + 90, width=300, height=75)



if __name__ == "__main__":
    app = GUIApp()

    app.title("Deakin Detonator Toolkit")
#getting the width & height of display sscreen
    screenwidth= app.winfo_screenwidth() 
    screenheight= app.winfo_screenheight()
#setting the size of window
    app.geometry("%dx%d" % (screenwidth, screenheight))

    app.mainloop()