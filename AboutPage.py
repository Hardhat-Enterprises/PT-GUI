## ABOUT PAGE ##

import tkinter as tk  # python 3
from tkinter import font as tkfont  # python 3
# import Tkinter as tk     # python 2
# import tkFont as tkfont  # python 2
from tkinter import font as tkfont
import PIL
from tkinter import *
from tkinter import font, messagebox
import random, requests, os, sys
import PySimpleGUI as sg
from nav_bar import *


class AboutPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        display_nav_bar(self, controller)
        framefont = tkfont.Font(family='Calibri', size=33, weight="bold")

        # creates blue bar as canvas below nav bar housing label containing title of page
        title_canvas = tk.Canvas(self, bg='white', highlightthickness=0)
        title_canvas.place(rely=0.08, relheight=0.12, relwidth=1)

        title_label = tk.Label(self, text="About The Toolkit", bg='#3A4C5E', fg='white', anchor="c", font=framefont)
        title_label.place(rely=0.08, relheight=0.12, relwidth=1)

        # allscreenframe = tk.Label(mycanvas)
        # allscreenframe.place(rely=0.2, relheight=1, relwidth=1)
        # extra frame for spacing, pushes all subsequent content below nav bar and title label using the pady field
        frameextra = Label(self, bg='#3B5262')
        frameextra.pack(pady=120)

        # new frame for tools list
        container = Frame(self)
        container.pack(fill='both', expand=True)
        # create a canvas on the new frame
        canvas = Canvas(container)

        # create scrollbar on new frame
        # scrollbar y
        scrollbar_y = Scrollbar(container,
                                orient=VERTICAL,
                                command=canvas.yview)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        scrollbar_y.config(command=canvas.yview)
        # create scrollbar x
        scrollbar_x = Scrollbar(container,
                                orient=HORIZONTAL,
                                command=canvas.xview)
        scrollbar_x.pack(side=BOTTOM, fill=X)
        scrollbar_x.config(command=canvas.xview)
        # create new canvas that will be scrolled
        scrollable_frame = Frame(canvas)
        # binds scroll canvas to execute function that gets scrollable region of canvas on event e
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # creates new window using scrollable frame as a base
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # sets scrollcommand to the existing scrollbar, linking the widgets
        canvas.config(
            xscrollcommand=scrollbar_x.set,
            yscrollcommand=scrollbar_y.set
        )
        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        frame1 = Canvas(scrollable_frame)
        frame1.pack()
        # creates new image variable from teamwork.png, used for background on title screen
        global teamwork
        teamwork = tk.PhotoImage(file='resources/teamwork.png')
        teamwork_label = tk.Label(frame1, image=teamwork)

        frame2 = Canvas(scrollable_frame)
        frame2.pack()
        # creates new image variable from using_computer.png, used for background on title screen
        global using_computer
        using_computer = tk.PhotoImage(file='resources/using_computer.png')
        computer_label = tk.Label(frame2, image=using_computer)

        paragraph_one = Label(frame1,
                              text="In it's simplest definition, Deakin Detonator Toolkit (DDT) is a penetration testing toolkit. "
                                   "\n\nMade by university students, DDT is our capstone project, completed over successive trimesters."
                                   "\n\nThe toolkit allows you to make use of a variety of tools, without needing the \"know-how\" of each command.",
                              bg="#E7E7E7", fg="black", font=('Calibri', 14), justify=LEFT, width=100)

        paragraph_two = Label(frame2,
                              text="We have simplified the penetration testing experience for both newcomers who are still learning, and those who have been hacking for years."
                                   "\n\nTo get started, choose a categoery of Tools from the sub-menu's. Then chose a specific tool from the Category."
                                   "\n\nAlternatively, you can choose an attack vector from the attack vectors sub-menu and follow the steps.",
                              bg="#E7E7E7", fg="black", font=('Calibri', 14), justify=LEFT, width=120)

        # places labels on the screen
        # paragraph_one.place(rely=0.22, relx=0.085, relheight=0.24, relwidth=0.4)
        # paragraph_two.place(rely=0.71, relx=0.48, relheight=0.24, relwidth=0.4)
        # teamwork_label.place(rely=0.22, relx=0.54, relheight=0.4, relwidth=0.31)
        # computer_label.place(rely=0.5, relx=0.13, relheight=0.45, relwidth=0.31)
        paragraph_one.pack(side=LEFT, padx=40, pady=50)
        teamwork_label.pack(side=LEFT, padx=40, pady=50)

        computer_label.pack(side=LEFT, padx=40, pady=50)
        paragraph_two.pack(side=LEFT, padx=40, pady=50)
        # binds the labels configure action to execute the set_label_wrap function
        # This will run when the screen is resized
        # paragraph_one.bind("<Configure>", self.set_label_wrap)
        # paragraph_two.bind("<Configure>", self.set_label_wrap)

    # dynamically updates the wraplength of the labels so that the text fits to the width properly
    def set_label_wrap(self, event):
        wraplength = event.width - 20  # the 8 is for padding (makes it look nicer)
        event.widget.configure(wraplength=wraplength)
