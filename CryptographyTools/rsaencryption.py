from subprocess import Popen, PIPE

import tkinter as tk
from tkinter import font as tkfont

import rsa
import base64

from tkinter import font as tkfont
from tkinter import *
from tkinter import font, messagebox
from nav_bar import *
from utils.console import Console


class RSAEncryption(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        framefont = tkfont.Font(family='Arial Rounded MT Bold', size=28, weight='bold')

        main_frame = tk.Frame(self)

        highlightFont = tkfont.Font(family='Arial Rounded MT Bold', size=28, weight='bold')
        # creates blue bar as canvas below nav bar housing label containing title of page
        title_label = tk.Label(self, text="Encryption", bg='white', fg='#92CEFF',
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

        sidescreenframe = tk.Label(main_frame, text="\n  RSA Encryption Algorithm", 
        font=('OpenSans', 18, 'italic'),anchor='nw')

        sidescreenframe.place(rely=0.2, relheight=1, relwidth=0.2)
        
        # input box
        labelIn = Label(main_frame, text = "Plaintext").place(rely=0.25,
        relx=0.23, relheight=0.05, relwidth=0.2)                             
        TextIn = Text(main_frame)
        TextIn.place(rely = 0.3, relx= 0.19, relheight = 0.5, relwidth = 0.28)

	# output box
        labelOut = Label(main_frame, text = "RSA")
        labelOut.place(rely=0.25, relx=0.57, relheight=0.05, relwidth=0.2)                             
        TextOut = Text(main_frame)
        TextOut.place(rely = 0.3, relx=0.53, relheight= 0.5, relwidth=0.28)
        
        # buttons to encrypt/decrypt/generate keys
        encryptButton = ttk.Button(main_frame, text="Encrypt", style="Rocket.TButton")
        decryptButton = ttk.Button(main_frame, text="Decrypt", style="Rocket.TButton")
        generateKeysButton = ttk.Button(main_frame, text="Key Pair", style="Rocket.TButton")
        
        RSAbutton = ttk.Button(main_frame, text="RSA", 
                        command=lambda: self.changetoRSA(labelOut, TextIn, TextOut,
                        encryptButton, RSAbutton, decryptButton, generateKeysButton), style='Accent.TButton')
        RSAbutton.place(rely=0.3, relx=0.03, relheight=0.05, relwidth=0.1)

        self.changetoRSA(labelOut, TextIn, TextOut, encryptButton, RSAbutton,
        decryptButton, generateKeysButton)

	# function for RSA algorithm
    def changetoRSA(self, labelOut, TextIn, TextOut, encryptButton, RSAbutton,
    decryptButton, generateKeysButton):
        TextOut.delete("1.0",END)
        labelOut.configure(text="RSA Enryption")
        RSAbutton.configure(style="Accent.TButton")

	# generates a key pair and stores it in the same folder
        def generateKeys():
            (publicKey, privateKey) = rsa.newkeys(2048)
            with open('CryptographyTools/publicKey.pem', 'wb') as p:
                p.write(publicKey.save_pkcs1('PEM'))
            with open('CryptographyTools/privateKey.pem', 'wb') as p:
                p.write(privateKey.save_pkcs1('PEM'))
        
        # applies keys to software
        def loadKeys():
            with open('CryptographyTools/publicKey.pem', 'rb') as p:
                publicKey = rsa.PublicKey.load_pkcs1(p.read())
            with open('CryptographyTools/privateKey.pem', 'rb') as p:
                privateKey = rsa.PrivateKey.load_pkcs1(p.read())
            return privateKey, publicKey
        privateKey, publicKey =loadKeys()

	# run the encryption algorithm
        def encrypt(TextIn, TextOut, publicKey):
            privateKey, publicKey =loadKeys()
            inputmessage = TextIn.get("1.0", END)
            if(inputmessage != " "):
                TextOut.delete("1.0", END)
                message_cipher = rsa.encrypt(inputmessage.encode('ascii'), publicKey)
                base64_message = base64.b64encode(message_cipher)
                outputcipher = base64_message.decode()
                TextOut.insert(END, outputcipher)
        
        encryptButton.config(command=lambda: encrypt(TextIn, TextOut, publicKey))
        encryptButton.place(rely=0.49, relx=0.47, relheight=0.06, relwidth=0.06)

	# runs the decryption algorithm
        def decrypt(TextIn, TextOut, privateKey):
            privateKey, publicKey =loadKeys()            
            inputmessage = TextOut.get("1.0", END)
            if(inputmessage != " "):
                TextIn.delete("1.0", END)
                base64_cipher = inputmessage.encode('ascii')
                base64_message = base64.b64decode(base64_cipher)
                message = rsa.decrypt(base64_message, privateKey).decode('ascii')
                TextIn.insert(END, message)
        
        # button configurations and placements
        decryptButton.config(command=lambda: decrypt(TextIn, TextOut, privateKey))
        decryptButton.place(rely=0.59, relx=0.47, relheight=0.06, relwidth=0.06)
        
        generateKeysButton.config(command=lambda: generateKeys())
        generateKeysButton.place(rely=0.39, relx=0.47, relheight=0.06, relwidth=0.06)

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
