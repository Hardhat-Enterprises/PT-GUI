import http.client

try:
    import os
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import filedialog
except ImportError:
    import Tkinter as tk
    import ttk
    import tkFileDialog as filedialog

from tkinter import font as tkfont
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from nav_bar import *
import socket
from tkinter.filedialog import asksaveasfile


class HTTPheaders(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # displays navbar at top of app screen
        display_nav_bar(self, controller)
        # sets font for frame
        framefont = tkfont.Font(family='Calibri', size=33, weight="bold")
        # sets font for buttons
        btnfont = tkfont.Font(family='Calibri', size=13)

        self.temp_var = ""

        # extra frame for spacing, pushes all subsequent content below nav bar and title label using the pady field
        frameextra = tk.Label(self, bg='#64C1DA')
        frameextra.pack(pady=78)

        white_canvas = tk.Canvas(self, bg="white")
        white_canvas.place(rely=0.1, relx=0, relheight=0.9, relwidth=1)

        # creates blue bar as canvas below nav bar housing label containing title of page
        title_canvas = tk.Canvas(self, bg='#64C1DA', highlightthickness=0)
        title_canvas.place(rely=0.08, relheight=0.12, relwidth=1)
        title_label = tk.Label(self, text="HTTP Header Analyzer", bg='#3B5262', fg='white', anchor="c", font=framefont)
        title_label.place(rely=0.08, relheight=0.12, relwidth=1)

        target_title_label = tk.Label(self, text="Target", justify=LEFT, bg="white", anchor='nw',
                                      font=("Calibri", 20, "bold"))

        target_desc = tk.Label(self, text="Enter URL: ", justify=LEFT, bg="white", anchor='nw',
                               font=("Calibri", 14))
        target_input = Text(self, bg="#E4E4E4", font=("Calibri", 10), state="normal")

        target_input.place(rely=0.284, relx=0.11, relheight=0.035, relwidth=0.28)
        target_title_label.place(rely=0.23, relx=0.04)
        target_desc.place(rely=0.286, relx=0.04)

        launch_button = tk.Button(self, compound=LEFT, text="LAUNCH", bg='#4D6C84', fg='white',
                                  font=("Calibri", 20, "bold"), command=lambda: launch_tool())
        launch_button.place(rely=0.246, relx=0.4, relheight=0.075, relwidth=0.12)

        results_title = tk.Label(self, text="Results", justify=LEFT, bg="white", anchor='nw',
                                 font=("Calibri", 20, "bold"))
        results_title.place(rely=0.37, relx=0.04)

        # packs widget to left of screen
        def pack_widget_left(button):
            button.pack(fill='x', padx=40, pady=(5, 5), side=tk.LEFT)

        # same as above but to right of screen
        def pack_widget_right(button):
            button.pack(fill='x', padx=40, pady=(5, 5), side=tk.RIGHT)

        global delete_image
        delete_image = tk.PhotoImage(file='resources/delete_icon.png')
        global input_image
        input_image = tk.PhotoImage(file='resources/input_icon.png')

        # creates a tool using passed strings and command function
        def create_header_item(header):
            # creates new canvas to hold tool information/execute widgets
            header_canvas = tk.Canvas(scrollable_frame, height=10, bg="#E3E4E5")

            delete_button = tk.Button(header_canvas, image=delete_image, compound=LEFT,
                                      command=lambda: delete_header(header), relief=FLAT, bg="#E3E4E5", borderwidth=0)
            pack_widget_left(delete_button)

            header_info = tk.Label(header_canvas, text=header, font='controller.btn_font2 14 ',
                                   bg="#E3E4E5", wraplength=500)
            pack_widget_left(header_info)

            info_button = tk.Button(header_canvas, image=input_image, compound=LEFT,
                                    command=lambda: input_header(header), relief=FLAT, bg="#E3E4E5", borderwidth=0)
            pack_widget_right(info_button)

            header_canvas.pack(expand=True, fill='x', pady=8)

        # new frame for tools list
        container = ttk.Frame(self)
        # create a canvas on the new frame
        canvas = tk.Canvas(container)

        # create scrollbar on new frame
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)

        # create new canvas that will be scrolled
        scrollable_frame = ttk.Frame(canvas)
        # binds scroll canvas to execute function that gets scrollable region of canvas on event e
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # creates new window using scrollable frame as a base
        canvas.create_window((565, 3), window=scrollable_frame, anchor="n")
        # sets scrollcommand to the existing scrollbar, linking the widgets
        canvas.configure(yscrollcommand=scrollbar.set)

        container.place(rely=0.44, relx=0.042, relheight=0.5, relwidth=0.478)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        saved_headers = tk.Text(self, bg="#E7E7E7", borderwidth=2, relief="solid")
        saved_headers.place(rely=0.24, relx=0.55, relheight=0.615, relwidth=0.43)

        clear_button = tk.Button(self, compound=LEFT, text="CLEAR", bg='#4D6C84', fg='white',
                                 font=("Calibri", 16, "bold"), command=lambda: clear_text())
        clear_button.place(rely=0.865, relx=0.55, relheight=0.075, relwidth=0.12)

        save_button = tk.Button(self, compound=LEFT, text="SAVE", bg='#4D6C84', fg='white',
                                font=("Calibri", 16, "bold"), command=lambda: save_file())
        save_button.place(rely=0.865, relx=0.86, relheight=0.075, relwidth=0.12)

        select_all = tk.Button(self, compound=LEFT, text="SELECT ALL", bg='#4D6C84', fg='white',
                               font=("Calibri", 13, "bold"), command=lambda: select_all())
        select_all.place(rely=0.38, relx=0.4, relheight=0.05, relwidth=0.12)

        # deletes the header given to it by searching the string contained within the tkinter Text widget and
        # splitting that string into two, one that ends just before the header that is being deleted,
        # and the second string starts just after that header.
        def delete_header(header):
            find_this = header
            search_this = saved_headers.get("1.0", 'end-1c')
            if search_this.find(find_this) != -1:
                beg_index = search_this.find(find_this)
                end_index = beg_index + len(find_this)
                edited_string = search_this[0: beg_index:] + search_this[end_index::]
                clear_text()
                saved_headers.insert("1.0", edited_string)

        # adds the header in the parameter to the text in the Text widget
        def input_header(header):
            saved_headers.insert("end", "\n")
            saved_headers.insert("end", header)

        # saves the text as a new file
        def save_file():
            text = saved_headers.get("1.0", 'end-1c')
            file = asksaveasfile(defaultextension=".txt")
            file.write(text)

        # adds the global variable used to hold the headers string to the Text widget
        def select_all():
            input_header(self.temp_var)

        # clears all the text contained in the Text widget
        def clear_text():
            saved_headers.delete("1.0", "end")

        # converts a tuple to a text string. for the first element in the tuple it adds a colon : after the text
        def convert_tuple(tup):
            string = ""
            flag = 1
            for val in tup:
                if flag == 1:
                    val = val + ": "
                    flag = 0
                string = string + val
            return string

        # visits website and populates headers list
        def launch_tool():
            url = target_input.get("1.0", "end-1c")
            write_string = "HTTP Header information from URL: ", url
            saved_headers.insert("end", write_string)

            try:
                connection = http.client.HTTPConnection(url)
                connection.request("GET", "/")
                data = connection.getresponse()
                headers = data.getheaders()
            except socket.gaierror:
                messagebox.showerror('Error', 'Something went wrong, please double check the website URL.')

            # populates the variable temp_var with all of the headers returned from the website
            for header in headers:
                temp_header = convert_tuple(header)
                create_header_item(temp_header)
                self.temp_var = self.temp_var + temp_header + "\n"
