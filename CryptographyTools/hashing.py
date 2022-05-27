from subprocess import Popen, PIPE

import tkinter as tk
import hashlib
from tkinter import font as tkfont

from tkinter import font as tkfont
from tkinter import *
from tkinter import font, messagebox
from nav_bar import *
from utils.console import Console


class Hashing(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        framefont = tkfont.Font(family='Arial Rounded MT Bold', size=28, weight='bold')

        main_frame = tk.Frame(self)

        highlightFont = tkfont.Font(family='Arial Rounded MT Bold', size=28, weight='bold')
        
        # creates blue bar as canvas below nav bar housing label containing title of page
        title_label = tk.Label(self, text="Hashing", bg='white', fg='#92CEFF',
                               anchor="c", font=framefont)
        title_label.place(rely=0.06, relheight=0.12, relwidth=1)
        
        # creates blue bar as canvas below nav bar
        title_canvas = tk.Canvas(self, bg='#c8e6ff', highlightthickness=0)
        title_canvas.place(rely=0.08, relheight=0.004, relwidth=1)

        # creates blue bar as canvas below title
        title_canvas = tk.Canvas(self, bg='#c8e6ff', highlightthickness=0)
        title_canvas.place(rely=0.155, relheight=0.004, relwidth=1)
        
        display_nav_bar(self, controller)
        main_frame.pack(fill='both', expand=1)
        
        allscreenframe = tk.Label(main_frame)
        allscreenframe.place(rely=0.2, relheight=1, relwidth=1)

        sidescreenframe = tk.Label(main_frame, text="\n       Hashing options:",
        font=('OpenSans', 18, 'italic'),anchor='nw')

        sidescreenframe.place(rely=0.2, relheight=1, relwidth=0.2)
        
        labelIn = Label(main_frame, text = "Plaintext").place(rely=0.25, relx=0.23,
                                                              relheight=0.05, relwidth=0.2)
        TextIn = Text(main_frame)
        TextIn.place(rely = 0.3, relx= 0.19, relheight = 0.5, relwidth = 0.28)

        #creates and displays elements
        labelOut = Label(main_frame, text = "MD5")
        labelOut.place(rely=0.25, relx=0.57, relheight=0.05, relwidth=0.2)
        TextOut = Text(main_frame)
        TextOut.place(rely = 0.3, relx=0.53, relheight= 0.5, relwidth=0.28)

        #button commands and placement
        MD5button = ttk.Button(main_frame, text="MD5 Hashing",
                        command=lambda: self.changetoMD5(labelOut, TextIn,
                                                         TextOut, hashButton,
                                                         MD5button, SHA1button), style='Rocket.TButton')
        MD5button.place(rely=0.3, relx=0.03, relheight=0.05, relwidth=0.1)

        SHA1button = ttk.Button(main_frame, text="SHA1 Hashing",
                        command=lambda: self.changetoSHA1(labelOut, TextIn,
                                                          TextOut, hashButton,
                                                          MD5button, SHA1button), style='Accent.TButton')
        SHA1button.place(rely=0.4, relx=0.03, relheight=0.05, relwidth=0.1)

        hashButton = ttk.Button(main_frame, text="Hash", style="Accent.TButton")
        #defaults to MD5
        self.changetoMD5(labelOut, TextIn, TextOut, hashButton, MD5button, SHA1button)

    def changetoMD5(self, labelOut, TextIn, TextOut, hashButton, MD5button, SHA1button):
        TextOut.delete("1.0",END)#clears the out field and switches current label to MD5
        labelOut.configure(text="MD5")
        MD5button.configure(style="Rocket.TButton")
        SHA1button.configure(style="Accent.TButton")

        def doMD5(TextIn, TextOut):#MD5 hashes text
            inputtext = TextIn.get("1.0",END)#from line 1, character 0, until end
            inputtext = inputtext[0:len(inputtext)-1]

            if(inputtext != ""):
                TextOut.delete("1.0",END)
                output = hashlib.md5(inputtext.encode('utf-8')).hexdigest()
                TextOut.insert(END, output)

        hashButton.config(command=lambda: doMD5(TextIn, TextOut))
        hashButton.place(rely=0.52, relx=0.47, relheight=0.06, relwidth=0.06)


    def changetoSHA1(self, labelOut, TextIn, TextOut, hashButton, MD5button, SHA1button):
        TextOut.delete("1.0",END)#clears out field and switches current label to SHA1
        labelOut.configure(text="SHA1")
        SHA1button.configure(style="Rocket.TButton")
        MD5button.configure(style="Accent.TButton")

        def doSHA1(TextIn, TextOut):#SHA1 hashes text
            inputtext = TextIn.get("1.0",END)
            inputtext = inputtext[0:len(inputtext)-1]

            if(inputtext != ""):
                TextOut.delete("1.0",END)
                output = hashlib.SHA1(inputtext.encode('utf-8')).hexdigest()
                TextOut.insert(END, output)

        hashButton.config(command=lambda: doSHA1(TextIn, TextOut))
        hashButton.place(rely=0.52, relx=0.47, relheight=0.06, relwidth=0.06)

    def place_widget_center(self, widget: Widget):
        """
        Helper function to place a widget center. Each subsequent call will place each widget BELOW the previous.
        :param widget: Widget to place.
        """
        widget.place(anchor=CENTER, relx=self.screen_base_x, rely=self.screen_base_y)

        # Bump base y coordinate value by increment to ensure the next element is below the previously placed one.
        self.screen_base_y += self.incremental_y

    def place_widget_center_beside(self, widget: Widget, x_offset=0.1):
        """
          Helper function to place a widget center but beside another on the X axis.
          :param widget: Widget to place.
          :param x_offset: Offset on the X axis at which to place the widget. Defaults to 0.1.
          """
        widget.place(anchor=CENTER, relx=self.screen_base_x + x_offset, rely=self.screen_base_y - self.incremental_y)
