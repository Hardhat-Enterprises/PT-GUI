import tkinter as tk  # python 3
from tkinter import font as tkfont, ttk  # python 3
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
        framefont = tkfont.Font(family='OpenSans', size=13)

        main_frame = tk.Frame(self)

        highlightFont = font.Font(family='Calibri', name='appHighlightFont1', size=18)

        def run_generator_button(frame):
            ttk.Button(frame, text="Payload Generator Tool", style='Accent.TButton',
                      command=lambda: controller.show_frame("MsfPayloadGen")).place(rely=0.35, relx=0.02, relheight=0.05, relwidth=0.18)

        def run_listener_button(frame):
            ttk.Button(frame, text="Listener Tool", style='Accent.TButton',
                      command=lambda: controller.show_frame("MsfListener")).place(rely=0.50, relx=0.02, relheight=0.05, relwidth=0.1)

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
            step1frame = tk.Message(main_frame, text=text, font=('OpenSans', 14), anchor='nw',
                                    aspect=300)
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
            step2frame = tk.Message(main_frame, text=text, font=('OpenSans', 14), anchor='nw',
                                    aspect=300)
            step2frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)
            run_listener_button(step2frame)

        def create_step_button(step_num, command):
            button = ttk.Button(main_frame, text="Step " + str(step_num),
                               command=command, style='Accent.TButton').place(rely=0.25 + 0.1 * step_num, relx=0.04,
                                                                     relheight=0.05, relwidth=0.1)

        
        tkfont.Font(family='OpenSans', size=13)
        framefont = tkfont.Font(family='Arial Rounded MT Bold', size=28, weight='bold')

        title_label = tk.Label(self, text="Reverse TCP Shell", bg='white', fg='#92CEFF', anchor="c", font=framefont)
        title_label.place(rely=0.06, relheight=0.12, relwidth=1)
        
        # creates blue bar as canvas below nav bar
        title_canvas = tk.Canvas(self, bg='#c8e6ff', highlightthickness=0)
        title_canvas.place(rely=0.08, relheight=0.004, relwidth=1)

        # creates blue bar as canvas below title
        title_canvas = tk.Canvas(self, bg='#c8e6ff', highlightthickness=0)
        title_canvas.place(rely=0.155, relheight=0.004, relwidth=1)

        allscreenframe = tk.Label(main_frame, bg='white')
        allscreenframe.place(rely=0.2, relheight=1, relwidth=1)

        side_label = tk.Label(main_frame, text="", bg='white', font='calibri 20 bold', anchor='nw')
        side_label.place(rely=0.2, relheight=1, relwidth=0.2)
        sidescreenframe = tk.Label(main_frame, text="\n         Steps:", bg='white', fg='#92CEFF', font='calibri 20 bold',
                                   anchor='nw')
        sidescreenframe.place(rely=0.25, relheight=1, relwidth=0.2)

        revtcp_label = tk.Label(main_frame, image=revtcp)
        revtcp_label.place(rely=0.36, relx=0.4)

        create_step_button(1, change_to_Step1)
        create_step_button(2, change_to_Step2)

        display_nav_bar(self, controller)
        main_frame.pack(fill='both', expand=1)
