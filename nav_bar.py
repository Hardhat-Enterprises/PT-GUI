# pylint: disable=global-statement
# pylint: disable=unused-import

from tkinter import *
from tkinter import ttk
import tkinter as tk

# Global variable for dark mode toggle status.
DARK_MODE_TOGGLE = 0

# function that takes the passed frame and controller variable and adds the navigation bar
# to the top of the frame
def display_nav_bar(frame, controller):
    """
    Helper function to display the nav bar.
    """
    # defines nav_bar a new canvas on the passed frame
    nav_bar = Canvas(frame)  ##FDFDFD
    # places nav bar at the top of the frame
    nav_bar.place(relx=0, relheight=0.08, relwidth=1)

    # these variables influence the placement and appearance of the menu option buttons
    # they've been centralised into variables for ease of modification
    # used for the width of the buttons
    btn_width = 0.11
    # used to track the button num (used for spacing on the right side of the nav_bar equally)
    btn_num = 1
    # defines the buttons that will appear in the navigation bar
    button_home = ttk.Button(frame, text="Home", style="Accent.TButton",
                             command=lambda: controller.show_frame("StartPage"))
    button_vectors = ttk.Button(frame, text="Attack Vectors", style="Accent.TButton",
                                command=lambda: controller.show_frame("VectorsPage"))
    button_about = ttk.Button(frame, text="About", style="Accent.TButton",
                              command=lambda: controller.show_frame("AboutPage"))
    button_tools = ttk.Button(frame, text="Tools", style="Accent.TButton",
                              command=lambda: controller.show_frame("ToolsPage"))
    button_walkthroughs = ttk.Button(frame, text="Walkthroughs", style="Accent.TButton",
                                     command=lambda: controller.show_frame("WalkthroughClass"))
    button_references = ttk.Button(frame, text="References", style="Accent.TButton",
                                   command=lambda: controller.show_frame("ReferencesPage"))
    # Dark mode switch global to ensure state is retained.
    global DARK_MODE_TOGGLE
    DARK_MODE_TOGGLE = 0
    dark_mode_switch = ttk.Checkbutton(frame, text="Dark mode", style="Switch.TCheckbutton",
                                       command=lambda: change_theme(controller),
                                       variable=DARK_MODE_TOGGLE)

    # this code block places all the buttons in the correct order
    # btn_num is used to correctly space out the buttons on the right side of the nav_bar
    # and must be incremented every time a button is added to the right side of the nav bar
    button_home.place(rely=0.01, relx=0.01, relheight=0.06, relwidth=0.055)
    button_references.place(rely=0.01, relx=1 - btn_width * btn_num - btn_num * 0.01,
     relheight=0.06,
                            relwidth=btn_width)

    btn_num += 1
    button_walkthroughs.place(rely=0.01, relx=1 - btn_width * btn_num - btn_num * 0.01,
     relheight=0.06,
                              relwidth=btn_width)

    btn_num += 1
    button_tools.place(rely=0.01, relx=1 - btn_width * btn_num - btn_num * 0.01, relheight=0.06,
     relwidth=btn_width)

    btn_num += 1
    button_vectors.place(rely=0.01, relx=1 - btn_width * btn_num - btn_num * 0.01, relheight=0.06,
     relwidth=btn_width)

    btn_num += 1
    button_about.place(rely=0.01, relx=1 - btn_width * btn_num - btn_num * 0.01, relheight=0.06,
     relwidth=btn_width)
    btn_num += 1

    dark_mode_switch.place(rely=0.01, relx=1 - btn_width * btn_num - btn_num * 0.01, relheight=0.06,
                            relwidth=btn_width)
    btn_num += 1


def change_theme(controller):
    """
    Helper function to change the theme of the application.
    """
    # NOTE: The theme's real name is azure-<mode>
    if controller.tk.call("ttk::style", "theme", "use") == "azure-dark":
        # Set light theme
        controller.tk.call("set_theme", "light")
    else:
        # Set dark theme
        controller.tk.call("set_theme", "dark")
