# installing libraries
from tkinter import font as tkfont

from UpdateScriptAV1 import UpdateScript

from nav_bar import *


# !/usr/bin/env/ python


class ResizingCanvas(Canvas):
    def __init__(self, parent, **kwargs):
        Canvas.__init__(self, parent, **kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self, event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width) / self.width
        hscale = float(event.height) / self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all", 0, 0, wscale, hscale)


class XXS_scanner(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        framefont = tkfont.Font(family='Calibri', size=33, weight="bold")

        main_frame = tk.Frame(self)

        highlightFont = font.Font(family='Calibri', name='appHighlightFont1', size=18)

        def load_terminal():
            p1 = Popen("exo-open --launch TerminalEmulator", stdout=PIPE, universal_newlines=True, shell=True).stdout

        def create_terminal_button(frame):
            terminal = tk.Button(frame, text="Terminal", bg="#E7E7E7", fg="black", font=highlightFont,
                                 command=load_terminal,
                                 relief='flat').place(rely=0.54, relx=0.15, relheight=0.05, relwidth=0.1)

        def update_script_button(frame):
            tk.Button(frame, text="Run Script", bg="#E7E7E7", fg="black", font=highlightFont,
                      command=lambda: UpdateScript.Run_Script(),
                      relief='flat').place(rely=0.23, relx=0.02, relheight=0.05, relwidth=0.1)

        def run_generator_button(frame):
            tk.Button(frame, text="Payload Generator Tool", bg="#E7E7E7", fg="black", font=highlightFont,
                      command=lambda: controller.show_frame("MsfPayloadGen"),
                      relief='flat').place(rely=0.47, relx=0.02, relheight=0.05, relwidth=0.18)


side_label = tk.Label(main_frame, text="", bg='#E7E7E7', font='calibri 20 bold', anchor='nw')
side_label.place(rely=0.2, relheight=1, relwidth=0.2)
sidescreenframe = tk.Label(main_frame, text="Steps", bg='#E7E7E7', font='calibri 20 bold', anchor='nw')
sidescreenframe.place(rely=0.2, relx=0.02, relheight=1, relwidth=0.2)

create_step_button(1, change_to_Step1)
create_step_button(2, change_to_Step2)
create_step_button(3, change_to_Step3)

display_nav_bar(self, controller)
main_frame.pack(fill='both', expand=1)
