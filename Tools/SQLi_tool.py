## SQLi scanner ##
# Author: Nancy
## have not implemented GUI , steve.
from tkinter import font as tkfont

from nav_bar import *


# !/usr/bin/env/ python

# Creating a python script to help sumbit forms and analyse the response using mechanise

# getting mechanise module


class SQLi(Frame):

    # tk.Frame.__init__(self, parent,controller)
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        abtframefont = tkfont.Font(family='Calibri', size=33, weight="bold")
        display_nav_bar(self, controller)
        aboutframe = Label(self, text="   SQLi Tool", bg='#64C1DA', anchor="w", font=abtframefont)
        aboutframe.place(rely=0.08, relheight=0.12, relwidth=1)

        allscreenframe = Label(self, bg='white')
        allscreenframe.place(rely=0.2, relheight=1, relwidth=1)
        # instructions label to avoid confusion
        label = Label(self, text=" Note: Please fill both field correctly.                                   \n" +
                                 "For Example: interface: eth0, New Mac: 08:00:27:1b:a9:50\nThe Format for MAC address should be 00:00:00:00:00:00  ",
                      font=('Calibri', 13), anchor='c').place(rely=0.28, relx=0.36, relheight=0.08, relwidth=0.3)

        # docstring for SQLi"tk.Framef __init__(self, arg):
        # super(SQLi,Frame.__init__()
        # self.arg = arg

        # providing URL from where we will obtain the response after submitting form
        # Set input box
        label = Label(self, text=" Enter URL", font=('Calibri', 13), anchor='c').place(rely=0.48, relx=0.08,
                                                                                       relheight=0.08, relwidth=0.24)
        # Set input box for interface Entry
        self.entry = Entry(self, font=('Calibri', 13), )
        self.entry.place(rely=0.38, relx=0.36, relheight=0.08, relwidth=0.3)
        # Start button
        Button(self, text="Click to Change Mac", font=('Calibri', 13), anchor='c', command=self.myMac).place(rely=0.44,
                                                                                                             relx=0.7,
                                                                                                             relheight=0.08,
                                                                                                             relwidth=0.12)

        # extra frame for spacing, pushes all subsequent content below nav bar and title label using the pady field
        frameextra = Label(self, bg='#64C1DA')
        frameextra.pack(pady=78)

        white_canvas = Canvas(self, bg="white")
        white_canvas.place(rely=0.1, relx=0, relheight=0.9, relwidth=1)

        open_button_username = Button(self, image=openfile_image, bg="#E3E4E5", command=c_open_file_old)
        open_button_password = Button(self, image=openfile_image, bg="#E3E4E5", command=c_open_file_old)

    # function to start the actual program for SQLi
    def mySQLi(self):
        # getting entries from user in the entry boxes and binding it to the variables used in functions.
        interface = self.entry.get()
        new_mac = self.entry.get()

    # read the attack vecotrs from the file
    with open('attack_vectors.txt') as v:
        # sending request with each attack vector
        For
        line in v:
        browser.open(url)
        browser.select_form(nr=0)
        browser["id"] = line
        res = browser.submit()
        content = res.read()

        # The following line of code will write the response to the output file.
        output = open('response/' + str(attack_no) + '.txt', 'w')
        output.write(content)
        output.close()
        print
        attack_no
        attack_no += 1

# Reference
# https://www.tutorialspoint.com/python_penetration_testing/python_penetration_testing_sqli_web_attack.htm#:~:text=The%20SQL%20injection%20is%20a,connected%20with%20the%20web%20applications.
