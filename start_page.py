import tkinter as tk
from tkinter import *
from tkinter import font as tkfont
from nav_bar import * #DarkNight Mode


class StartPage(tk.Frame):
    """
    Start page.
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # sets font for titles
        tkfont.Font(family='Calibri', size=40, weight="bold")
        display_nav_bar(self, controller) #DarkNight Mode

        # creates new image variable from bkg.png, used for background on title screen
        self.image = tk.PhotoImage(file="resources/landingpagebkgBLUE.png")
        image_canvas = tk.Canvas(self, bg='#232536')
        image_canvas.place(rely=0, relx=0, relwidth=1, relheight=0.4)
        image_canvas.place(rely=0.048, relx=0, relwidth=1, relheight=0.4) #DarkNight Mode

        title = tk.Label(self, text="Deakin Detonator Toolkit", bg='#232536', fg='white',
                         font=('Calibri', 42, 'bold'))
        subtitle = tk.Label(self, text="Network Recovery Tools Red Team", bg='#232536', fg='white',
                            font=('Calibri', 17, 'bold'))

        title.pack(side=TOP, anchor=CENTER, pady=50)
        subtitle.pack(side=TOP, anchor=CENTER, pady=10)

        # image_canvas.create_image(0, 0, image=self.image, anchor="nw")

        # creates and places new white canvas on which the menu buttons are placed
        options_canvas = tk.Canvas(self, bg="white")
        options_canvas.place(rely=0.4, relx=0, relwidth=1, relheight=0.6)
        bgcolours = ['#3A4C5E', '#4D6C84', '#3B5262', '#2E414F', '#375973']

        # function that creates a menu button, takes a title, menu option number and
        # page to navigate to on click
        def create_option(title, menu_num, onclick_page):
            option_button = tk.Button(options_canvas, text=title, bg=bgcolours[menu_num],
                                      fg="white",
                                      font=('Calibri', 20, 'bold'),
                                      command=lambda: controller.show_frame(onclick_page),
                                      borderwidth=2, relief="flat", width=10)
            option_button.pack(anchor=CENTER, side=BOTTOM, fill=BOTH, expand=True) #Change side=LEFT to side=BOTTOM

        # option_button.grid(sticky="nsew")

        # creates the 4 menu options
        # if you want to add a new menu option,
        # 1. invoke create_option
        # 2. enter the button text, menu option number and p6ageName you want to navigate
        # to on button click
        # 3. make sure you enter the name of the page defined in main.py at line 35
        # 4. You're done, run the app and see your new menu option
        create_option("About", 0, "AboutPage")
        create_option("Attack Vectors", 1, "VectorsPage")
        create_option("Tools", 2, "ToolsPage")
        create_option("Walkthroughs", 3, "WalkthroughClass")
        create_option("References", 4, "ReferencesPage")
