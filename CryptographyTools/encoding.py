from subprocess import Popen, PIPE

import tkinter as tk
from tkinter import font as tkfont
from base64 import b64decode, b64encode

from tkinter import font as tkfont
from tkinter import *
from tkinter import font, messagebox
from nav_bar import *
from utils.console import Console


class Encoding(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        framefont = tkfont.Font(family='Arial Rounded MT Bold', size=28, weight='bold')

        main_frame = tk.Frame(self)

        highlightFont = tkfont.Font(family='Arial Rounded MT Bold', size=28, weight='bold')
        
        # creates blue bar as canvas below nav bar housing label containing title of page
        title_label = tk.Label(self, text="Encoding", bg='white', fg='#92CEFF',
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

        sidescreenframe = tk.Label(main_frame, text="UTF8 Encoding/Decoding:", 
        font=('OpenSans', 18, 'italic'),anchor='nw')

        sidescreenframe.place(rely=0.2, relheight=1, relwidth=0.3)
        
        labelIn = Label(main_frame, text = "Plaintext").place(rely=0.25, relx=0.23, relheight=0.05, relwidth=0.2)                             
        TextIn = Text(main_frame)
        TextIn.place(rely = 0.3, relx= 0.19, relheight = 0.5, relwidth = 0.28)

        #creates and displays elements
        labelOut = Label(main_frame, text = "MD5")
        labelOut.place(rely=0.25, relx=0.57, relheight=0.05, relwidth=0.2)
        TextOut = Text(main_frame)
        TextOut.place(rely = 0.3, relx=0.53, relheight= 0.5, relwidth=0.28)
        encodeButton = ttk.Button(main_frame, text="Encode", style="Accent.TButton")
        decodeButton = ttk.Button(main_frame, text="Decode", style="Accent.TButton")

        #button commands and placement
        binaryButton = ttk.Button(main_frame, text="UTF-8:Binary",
                        command=lambda: self.changetoBinary(labelOut, TextIn, TextOut,
                                                            encodeButton, decodeButton,
                                                            binaryButton, base64Button), style='Rocket.TButton')
        binaryButton.place(rely=0.3, relx=0.03, relheight=0.05, relwidth=0.1)

        base64Button = ttk.Button(main_frame, text="UTF-8:Base64",
                        command=lambda: self.changetoB64(labelOut, TextIn, TextOut, encodeButton,
                                                         decodeButton, binaryButton, base64Button), style='Accent.TButton')
        base64Button.place(rely=0.4, relx=0.03, relheight=0.05, relwidth=0.1)

        #defaults to binary
        self.changetoBinary(labelOut, TextIn, TextOut, encodeButton,
                            decodeButton, binaryButton, base64Button)

    def changetoBinary(self, labelOut, TextIn, TextOut, encodeButton,
                       decodeButton, binaryButton, base64Button):
        TextOut.delete("1.0",END)#clears the out field and switches current label to binary
        labelOut.configure(text="Binary")
        binaryButton.configure(style="Rocket.TButton")
        base64Button.configure(style="Accent.TButton")

        def encodeBinary(TextIn, TextOut):#constructs a binary string from an input string
            inputtext = TextIn.get("1.0",END) #from line 1, character 0 until end
            inputtext = inputtext[0:len(inputtext)-1]

            if(inputtext != ""):
                TextOut.delete("1.0",END)
                outputstring = ''.join(format(ord(i),'08b') for i in inputtext) 
                TextOut.insert(END, outputstring)
                
        def decodeBinary(TextIn, TextOut):#converts binary to characters
            inputtext = TextOut.get("1.0",END)
            inputtext = inputtext[0:len(inputtext)-1]

            if(inputtext != ""):
                TextIn.delete("1.0",END)
                outputstring = ''
                for i in range (0, len(inputtext), 8):
                    charbyte = inputtext[i:i+8]
                    outputstring = outputstring + chr(int(charbyte,2))
                TextIn.insert(END, outputstring)

        encodeButton.config(command=lambda: encodeBinary(TextIn, TextOut))
        encodeButton.place(rely=0.49, relx=0.47, relheight=0.06, relwidth=0.06)

        decodeButton.config(command=lambda: decodeBinary(TextIn, TextOut))
        decodeButton.place(rely=0.55, relx=0.47, relheight=0.06, relwidth=0.06)

    def changetoB64(self, labelOut, TextIn, TextOut, encodeButton, 
                    decodeButton, binaryButton, base64Button):
        TextOut.delete("1.0",END)#clears the out field and switches current label to base64
        labelOut.configure(text="Base64")
        binaryButton.configure(style="Accent.TButton")
        base64Button.configure(style="Rocket.TButton")

        def encodeB64(TextIn, TextOut):#constructs a base64 string from an input string
            inputtext = TextIn.get("1.0",END)
            inputtext = inputtext[0:len(inputtext)-1]

            if(inputtext != ""):
                TextOut.delete("1.0",END)
                output = b64encode(bytes(inputtext,'utf-8'))
                TextOut.insert(END, output)
        def decodeB64(TextIn, TextOut):#converts base64 to characters
            inputtext = TextOut.get("1.0",END)
            inputtext = inputtext[0:len(inputtext)-1]

            if(inputtext != ""):
                TextIn.delete("1.0",END)
                output = b64decode(bytes(inputtext,'utf-8'))
                TextIn.insert(END, output)

        encodeButton.config(command=lambda: encodeB64(TextIn, TextOut))
        encodeButton.place(rely=0.49, relx=0.47, relheight=0.06, relwidth=0.06)

        decodeButton.config(command=lambda: decodeB64(TextIn, TextOut))
        decodeButton.place(rely=0.55, relx=0.47, relheight=0.06, relwidth=0.06)

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
