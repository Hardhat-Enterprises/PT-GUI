import tkinter as tk  # python 3
from tkinter import font  as tkfont, ttk  # python 3

from tkinter import font as tkfont
from tkinter import *
from tkinter import font, messagebox
from nav_bar import *

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

class AttackVectorOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        framefont = tkfont.Font(family='Calibri', size=33, weight="bold")

        main_frame = tk.Frame(self)

        highlightFont = font.Font(family='Calibri', name='appHighlightFont1', size=18)

        def run_generator_button(frame):
            tk.Button(frame, text="Payload Generator Tool", bg="#E7E7E7", fg="black", font=highlightFont,
                                 command=lambda: controller.show_frame("MsfPayloadGen"),
                                 relief='flat').place(rely=0.47, relx=0.02, relheight=0.05, relwidth=0.18)

        def run_listener_button(frame):
            tk.Button(frame, text="Listener Tool", bg="#E7E7E7", fg="black", font=highlightFont,
                                 command=lambda: controller.show_frame("MsfListener"),
                                 relief='flat').place(rely=0.68, relx=0.02, relheight=0.05, relwidth=0.1)

        global revtcp
        revtcp = tk.PhotoImage(file='resources/reversetcp1.png')

        def change_to_Step1():
            text = (
                "\nStep 1: Msfvenom Payload Generator\n\n"
                "o   Navigate to ‘Msfvenom Payload Generator’ tool by clicking button below\n"
                "     and click 'Launch Tool'.\n\n"
                "o   Set IP address of localhost (attack machine).\n\n"
                "o   Set port number to be used for connection.\n\n"
                "o   Click 'Save Payload As' and enter desired name for executable file.\n\n"
                "o   Click 'Generate Payload' button to generate payload.\n"

            )
            step1frame = tk.Message(main_frame, text=text, fg='black', bg='white', font=('Calibri', 20), anchor='nw', aspect=300)
            step1frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)
            run_generator_button(step1frame)
            
        def change_to_Step2():
            text = (
                "\nStep 2: Msfconsole Listener Tool\n\n"
                "o   Navigate to ‘Msfconsole Listener’ tool by clicking button below and click 'Launch Tool'.\n\n"
                "o   Set IP address of localhost (attack machine).\n\n"
                "o   Set port number for connection (same as port number declared in the payload generator).\n\n"
                "o   Click 'Start Listening' button to lauch the listener. (Note: GUI will freeze until\n"
                "     connection from victim is received. Please read remaining steps before doing this.)\n\n"
                "o   Run generated payload on the victim machine.\n\n"
                "o   Once 'Connection Successful' message appears, click 'Shell' button to interact\n"
                "     with active reverse shell on victim machine.\n\n"
                "o   Commands can now be typed within the entry box and communicated by clicking 'Enter'\n"
                "     button. Once finished, click ‘Terminate’ button to close the connection.\n\n"

            )
            step2frame = tk.Message(main_frame, text=text, fg='black', bg='white', font=('Calibri', 20), anchor='nw', aspect=300)
            step2frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)
            run_listener_button(step2frame)
        
        def create_step_button(step_num, command):
            button = tk.Button(main_frame, text="Step " + str(step_num), bg="#E7E7E7", fg="black", font=highlightFont,
                               command=command, relief='flat').place(rely=0.3 + 0.1 * step_num, relx=0.02,
                                                                     relheight=0.05, relwidth=0.1)

        # creates blue bar as canvas below nav bar housing label containing title of page
        title_canvas = tk.Canvas(self, bg='#64C1DA', highlightthickness=0)
        title_canvas.place(rely=0.08, relheight=0.12, relwidth=1)
        title_label = tk.Label(self, text="Reverse TCP Shell", bg='#4D6C84', fg='white', anchor="c", font=framefont)
        title_label.place(rely=0.08, relheight=0.12, relwidth=1)

        allscreenframe = tk.Label(main_frame, bg='white')
        allscreenframe.place(rely=0.2, relheight=1, relwidth=1)

        side_label = tk.Label(main_frame, text="", bg='#E7E7E7', font='calibri 20 bold', anchor='nw')
        side_label.place(rely=0.2, relheight=1, relwidth=0.2)\

        sidescreenframe = tk.Label(main_frame, text="\n         Steps", bg='#E7E7E7', font='calibri 20 bold', anchor='nw')
        sidescreenframe.place(rely=0.25, relheight=1, relwidth=0.2)

        revtcp_label = tk.Label(main_frame, image=revtcp)
        revtcp_label.place(rely=0.36, relx=0.4)

        create_step_button(1, change_to_Step1)
        create_step_button(2, change_to_Step2)

        display_nav_bar(self, controller)
        main_frame.pack(fill='both', expand=1)