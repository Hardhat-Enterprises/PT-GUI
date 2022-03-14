import tkinter as tk
from tkinter import *
from nav_bar import *


# function that takes the passed frame and controller variable and adds the navigation bar to the top of the frame
def display_nav_bar(frame, controller):
    # defines nav_bar a new canvas on the passed frame
    nav_bar = Canvas(frame, bg='#232536')   ##FDFDFD
    # places nav bar at the top of the frame
    nav_bar.place(relx=0, relheight=0.08, relwidth=1)

    # these variables influence the placement and appearance of the menu option buttons
    # they've been centralised into variables for ease of modification
    border = 0          # used for the border-width of the menu buttons
    style = "flat"     # used for the border style of the menu buttons
    btn_width = 0.11     # used for the width of the buttons
    btn_num = 1         # used to track the button num (used for spacing on the right side of the nav_bar equally)

    # defines the buttons that will appear in the navigation bar
    button_home = tk.Button(frame, text="Home", bg ='#6f8396', fg='white', borderwidth=border, relief=style, font=controller.btn_font2,
                            command=lambda: controller.show_frame("StartPage"))
    button_vectors = tk.Button(frame, text="Attack Vectors", bg='#4D6C84', fg='white', borderwidth=border, relief=style, font=controller.btn_font2,
                               command=lambda: controller.show_frame("VectorsPage"))
    button_about = tk.Button(frame, text="About", bg='#3A4C5E', fg='white', borderwidth=border, relief=style, font=controller.btn_font2,
                             command=lambda: controller.show_frame("AboutPage"))
    button_tools = tk.Button(frame, text="Tools", bg='#3B5262', fg='white', borderwidth=border, relief=style, font=controller.btn_font2,
                             command=lambda: controller.show_frame("ToolsPage"))
    button_walkthroughs = tk.Button(frame, text="Walkthroughs", bg='#375973', fg='white', borderwidth=border, relief=style, font=controller.btn_font2,
                             command=lambda: controller.show_frame("WalkthroughClass"))     
    button_references = tk.Button(frame, text="References", bg='#2E414F', fg='white', borderwidth=border, relief=style, font=controller.btn_font2,
                                  command=lambda: controller.show_frame("ReferencesPage"))

    # this code block places all the buttons in the correct order
    # btn_num is used to correctly space out the buttons on the right side of the nav_bar and must be incremented...
    # ...every time a button is added to the right side of the nav bar
    button_home.place(rely=0.01, relx=0.02, relheight=0.06, relwidth=btn_width)
    button_references.place(rely=0.01, relx=1 - btn_width * btn_num - btn_num * 0.01, relheight=0.06, relwidth=btn_width)
    btn_num = 2
    button_walkthroughs.place(rely=0.01, relx=1 - btn_width * btn_num - btn_num * 0.01, relheight=0.06, relwidth=btn_width)
    btn_num = 3
    button_tools.place(rely=0.01, relx=1 - btn_width * btn_num - btn_num * 0.01, relheight=0.06, relwidth=btn_width)
    btn_num = 4
    button_vectors.place(rely=0.01, relx=1 - btn_width * btn_num - btn_num * 0.01, relheight=0.06, relwidth=btn_width)
    btn_num = 5
    button_about.place(rely=0.01, relx=1 - btn_width * btn_num - btn_num * 0.01, relheight=0.06, relwidth=btn_width)
    btn_num = 6
