import tkinter as tk  # python 3
from tkinter import font as tkfont, ttk  # python 3
import os
from tkinter import font as tkfont
from tkinter import *
from tkinter import font, messagebox
from nav_bar import *
from subprocess import call, Popen, PIPE


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


class AttackVectorEleven(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        framefont = tkfont.Font(family='Calibri', size=33, weight="bold")

        main_frame = tk.Frame(self)

        highlightFont = font.Font(family='Calibri', name='appHighlightFont8', size=18)

        def load_exploit():
            os.chdir("./Tools")
            cmd = 'exo-open --launch TerminalEmulator'
            p1 = Popen([cmd + ' python3 av8_exploit.py'], stdout=PIPE, shell=True)
            os.chdir("../../")

        def load_listener():
            cmd = 'exo-open --launch TerminalEmulator'
            p1 = Popen([cmd + ' nc -lvnp 4444'], stdout=PIPE, shell=True)

        def run_listener_button(frame):
            tk.Button(frame, text="Launch Listener", bg="#E7E7E7", fg="black", font=highlightFont,
                      command=load_listener,
                      relief='flat').place(rely=0.47, relx=0.02, relheight=0.05, relwidth=0.18)

        def run_exploit_button(frame):
            tk.Button(frame, text="Launch Exploit", bg="#E7E7E7", fg="black", font=highlightFont,
                      command=load_exploit,
                      relief='flat').place(rely=0.68, relx=0.02, relheight=0.05, relwidth=0.1)

        global apacheexploit
        apacheexploit = tk.PhotoImage(file='resources/apacheexploit.png')

        def change_to_Step1():
            text = (
                "\nStep 1: Understanding the exploit\n\n"
                "o   The exploit works through a path traversal attack.\n\n"
                "o   Attackers could map a URL to files outside of the local document root\n\n"
                "o   If these files are not protected with incorrect configuration, these files can be leaked.\n\n"
                "o   This addtionally lead to the exploitation of the Apache CGI scripts.\n\n"
                "o   Before heading to the next step, click the button to launch a terminal and launch a listening post on port 4444.\n"
                "o   Note: You can launch your own listening post on another port manually and proceed to the next step.\n"

            )
            step1frame = tk.Message(main_frame, text=text, fg='black', bg='white', font=('Calibri', 20), anchor='nw',
                                    aspect=300)
            step1frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)
            run_listener_button(step1frame)

        def change_to_Step2():
            text = (
                "\nStep 2: Using the Exploit\n\n"
                "o   Clicking the Launch Exploit button will open the python script containing the code.\n\n"
                "o   Set the IP your listening post is on (find this with 'ip a' in terminal).\n\n"
                "o   Set the port number you're listening on (4444, if not changed).\n\n"
                "o   Set your victim details, IP, Apache Webserver port and version (localhost, 8080, 2.4.49 when using provided docker)\n\n"
                "o   The tool will then build and run the exploit automatically.\n\n"
                "o   Your listening post should now have a reverse shell to the Apache Webserver,\n"
                "     swap windows to the previous terminal to verify this.\n\n"

            )
            step2frame = tk.Message(main_frame, text=text, fg='black', bg='white', font=('Calibri', 20), anchor='nw',
                                    aspect=300)
            step2frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)
            run_exploit_button(step2frame)

        def create_step_button(step_num, command):
            button = tk.Button(main_frame, text="Step " + str(step_num), bg="#E7E7E7", fg="black", font=highlightFont,
                               command=command, relief='flat').place(rely=0.3 + 0.1 * step_num, relx=0.02,
                                                                     relheight=0.05, relwidth=0.1)

        # creates blue bar as canvas below nav bar housing label containing title of page
        title_canvas = tk.Canvas(self, bg='#64C1DA', highlightthickness=0)
        title_canvas.place(rely=0.08, relheight=0.12, relwidth=1)
        title_label = tk.Label(self, text="Apache Webserver Exploit", bg='#4D6C84', fg='white', anchor="c",
                               font=framefont)
        title_label.place(rely=0.08, relheight=0.12, relwidth=1)

        allscreenframe = tk.Label(main_frame, bg='white')
        allscreenframe.place(rely=0.2, relheight=1, relwidth=1)

        side_label = tk.Label(main_frame, text="", bg='#E7E7E7', font='calibri 20 bold', anchor='nw')
        side_label.place(rely=0.2, relheight=1, relwidth=0.2) \

        sidescreenframe = tk.Label(main_frame, text="\n         Steps", bg='#E7E7E7', font='calibri 20 bold',
                                   anchor='nw')
        sidescreenframe.place(rely=0.25, relheight=1, relwidth=0.2)

        apacheexploit_label = tk.Label(main_frame, image=apacheexploit)
        apacheexploit_label.place(rely=0.36, relx=0.4)

        create_step_button(1, change_to_Step1)
        create_step_button(2, change_to_Step2)

        display_nav_bar(self, controller)
        main_frame.pack(fill='both', expand=1)
