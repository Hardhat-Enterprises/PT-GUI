# pylint: disable=unnecessary-lambda
# pylint: disable=consider-using-with
# pylint: disable=global-variable-undefined
# pylint: disable=invalid-name
# pylint: disable=no-self-use
# pylint: disable=unused-variable

import webbrowser
import os
from subprocess import Popen, PIPE
from tkinter import font as tkfont

from nav_bar import *
from references_descriptions import *


class ReferencesPage(tk.Frame):
    """
    Class for the References Page.
    """

    def __init__(self, parent, controller):
        """
        Initialisation of the references page.
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # sets font for buttons and title
        tkfont.Font(family='OpenSans', size=13)
        framefont = tkfont.Font(family='Arial Rounded MT Bold', size=28, weight='bold')

        title_label = tk.Label(self, text="References", bg='white', fg='#92CEFF',
                               anchor="c", font=framefont)
        title_label.place(rely=0.06, relheight=0.12, relwidth=1)

        # extra frame for spacing, pushes all subsequent content below nav bar and
        # title label using the pady field
        frameextra = Label(self, anchor='c')
        frameextra.pack(pady=54.49)
        # displays navbar at top of app screen
        display_nav_bar(self, controller)

	# creates blue bar as canvas below nav bar
        title_canvas = tk.Canvas(self, bg='#c8e6ff', highlightthickness=0)
        title_canvas.place(rely=0.08, relheight=0.004, relwidth=1)

        # creates blue bar as canvas below title
        title_canvas = tk.Canvas(self, bg='#c8e6ff', highlightthickness=0)
        title_canvas.place(rely=0.155, relheight=0.004, relwidth=1)

        # new frame for references list
        container = Frame(self)
        container.pack(fill='both', expand=True)
        # create a canvas on the new frame
        canvas = Canvas(container)

        # create scrollbar on new frame
        # scrollbar y
        scrollbar_y = ttk.Scrollbar(container,
                                    orient=VERTICAL,
                                    command=canvas.yview)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        scrollbar_y.config(command=canvas.yview)
        # create new canvas that will be scrolled
        scrollable_frame = Frame(canvas)
        # binds scroll canvas to execute function that gets scrollable region of canvas on event e
        scrollable_frame.bind("<Configure>",
                              lambda _: canvas.configure(scrollregion=canvas.bbox("all")))

        # creates new window using scrollable frame as a base
        canvas.create_window((10, 3), window=scrollable_frame, anchor="nw")

        # sets scrollcommand to the existing scrollbar, linking the widgets
        canvas.config(
           yscrollcommand=scrollbar_y.set
        )
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        ##for toggling visibility of references under a title
        self.titleChildrenNumber = []#number of elements below a title (reference's labels and buttons)
        self.referencesList = []#a list of each of these elements to hide
        self.hideButtons=[]#a list of the title buttons
        # creates new image variable from start_button.png, used for launch button on references
        global button_image
        button_image = tk.PhotoImage(file='resources/start_button.png')
        global info_image
        info_image = tk.PhotoImage(file='resources/Info_button.png')
        global launch_image
        launch_image = tk.PhotoImage(file='resources/internetsymbol.png')

        # packs passed widget to the left of screen, used for creating a reference entry
        def pack_widget_left(button):
            button.pack(fill='x', padx=10, pady=(5, 5), side=LEFT)

        # same as above but to right of screen
        def pack_widget_right(button):
            button.pack(fill='x', padx=10, pady=(5, 5), side=RIGHT)

        # creates section title from passed string
        def create_title(title):
            self.titleChildrenNumber.append(0)

            titleidx = len(self.titleChildrenNumber)-1
            self.hideButtons.append(ttk.Button(scrollable_frame,
            		text=title, style='Dropdown.TButton',
            		command=lambda : hide_on_title(titleidx, self.hideButtons[titleidx])))
            self.hideButtons[len(self.hideButtons)-1].pack(expand=TRUE, fill='x', padx=5)

        ## toggles visibility of references under a title
        def toggle_references(titleidx, namebutton, hidden):
            ## using namebutton.configure, visual indicators for hidden/not hidden can be added here

            ## calculates target indexes for all components under given title
            idxFrom = idxTo = 0
            for idx, val in enumerate(self.titleChildrenNumber):
                if idx < titleidx:
                    idxFrom += (val)
                    idxTo += (val)
                else:
                    idxTo += (val)
                    break

            ## referencestype%4: 0=references_canvas, 1=referencesname_label, 2=navbutton, 3=infobutton
            referencestype = 0

            ## in the range of items below the target title at titleidx: hide or unhide
            for n in range(idxFrom, idxTo):
                if ((referencestype%4 == 0) and not hidden):
                    self.referencesList[n].pack_forget()
                    namebutton.configure(command=lambda : show_on_title(titleidx,namebutton))

                elif (referencestype%4 == 0 and hidden):
                    pack_widget_left(self.referencesList[n+1])
                    pack_widget_right(self.referencesList[n+2])
                    pack_widget_right(self.referencesList[n+3])
                    self.referencesList[n].pack(after=namebutton, expand=TRUE, fill='x', padx=90, pady=8)
                    namebutton.configure(command=lambda : hide_on_title(titleidx,namebutton))

                referencestype += 1
        ##shows references under a title
        def show_on_title(titleidx, namebutton):
            toggle_references(titleidx, namebutton, True)

        ##hides references under a title
        def hide_on_title(titleidx, namebutton):
            toggle_references(titleidx, namebutton, False)

        # creates navigation button that executes passed command, allows for variety
        # of functionality of reference click
        def nav_button(canvas, command):
            nav_button = ttk.Button(canvas, image=launch_image,
            command=command, style='Rocket.TButton')
            pack_widget_right(nav_button)
            Tk.update(self)
            return nav_button

        # creates a reference using passed strings and command function
        def create_references(name, command, desc):
            # creates new canvas to hold reference information/execute widgets
            references_canvas = tk.Canvas(scrollable_frame, height=0)

            referencesname_label = ttk.Label(references_canvas, text=name,
                                       font='controller.btn_font2 12 italic')
            pack_widget_left(referencesname_label)

            navbutton = nav_button(references_canvas, command)
            info_button = ttk.Button(references_canvas, image=info_image,
                                     command=lambda: self.show_hint(desc), style='Accent.TButton')
            pack_widget_right(info_button)
            references_canvas.pack(expand=TRUE, fill='x', padx=90, pady=8)
            self.referencesList.append(references_canvas)
            self.referencesList.append(referencesname_label)
            self.referencesList.append(navbutton)
            self.referencesList.append(info_button)
            self.titleChildrenNumber[len(self.titleChildrenNumber)-1] += 4

        # creates references and section titles by invoking previous functions
        # if you want to add a new reference,
        # 1. invoke create_references under a relevant section heading 
        # 2. enter the name and command you want to execute between the brackets
        # 3. if you want the button to navigate to a page, use:
        #                                   lambda: controller.show_frame("PAGE_NAME")
        #    and replace PAGE_NAME with the name of the page defined in main.py at line 35
        # 4. You're done, run the app and see your new reference
        
        
        
        create_title("GUI Development")
        create_references("Basics of tkinter - Adding functionality to the application",
                lambda: webbrowser.open_new_tab('https://www.youtube.com/watch?v=YXPyB4XeYLA'), ADDING_FUNCTIONALITY_TO_THE_APPLICATION)
        create_references("Basics of tkinter - Using the place command", 
        	lambda: webbrowser.open_new_tab('https://www.youtube.com/watch?v=D8-snVfekto&ab_channel=KeithGalli'), USING_THE_PLACE_COMMAND)
        create_references("Basics of tkinter - Adding a scrollbar to a frame", 
        	lambda: webbrowser.open_new_tab('https://www.youtube.com/watch?v=0WafQCaok6g&ab_channel=Codemy.com'), ADDING_A_SCROLLBAR_TO_A_FRAME)
        create_references("Implementing navigation between screens", 
        	lambda: webbrowser.open_new_tab('https://www.youtube.com/watch?v=39P4BMvvLdM&ab_channel=IntrotoComputerScience'), IMPLEMENTING_NAVIGATION_BETWEEN_SCREENS)
        create_references("Creating dynamically resizing labels",
                lambda: webbrowser.open_new_tab('https://stackoverflow.com/questions/49037051/when-using-the-pack-layout-of-tkinter-how-can-i-have-a-labels-wraplength-be-eq'), CREATING_DYNAMICALLY_RESIZING_LABELS)
        create_references("Adding horizontal scrollbars to toolkit",
                lambda: webbrowser.open_new_tab('https://pythonguides.com/python-tkinter-scrollbar/'), ADDING_HORIZONTAL_SCROLLBARS_TO_TOOLKIT) 
                  
        create_title("Attack Vector One")
        create_references("Communication with the MSFRPC framework", 
        	lambda: webbrowser.open_new_tab('https://github.com/DanMcInerney/pymetasploit3'), COMMUNICATION_WITH_THE_MSFRPC_FRAMEWORK)
        create_references("Defining the 'kill_PID()' function",
                lambda: webbrowser.open_new_tab('https://stackoverflow.com/questions/26688936/how-to-get-pid-by-process-name'), DEFINING_THE_KILL_PID_FUNCTION)
        create_references("Defining the 'find_session()' function",
                lambda: webbrowser.open_new_tab('https://infosecaddicts.com/python-and-metasploit/'), DEFINING_THE_FIND_SESSION_FUNCTION)
        create_references("Defining the 'set_IP()' function",
                lambda: webbrowser.open_new_tab('https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib'), DEFINING_THE_SET_IP_FUNCTION)

        create_title("Attack Vector Two")
        create_references("Mutillidae installation", 
        	lambda: webbrowser.open_new_tab('https://github.com/webpwnized/mutillidae'), MUTILLIDAE_INSTALLATION)
        create_references("Understanding directory traversal attacks",
                lambda: webbrowser.open_new_tab('https://portswigger.net/web-security/file-path-traversal'), UNDERSTANDING_DIRECTORY_TRAVERSAL_ATTACKS)
        create_references("Understanding IDOR attacks",
                lambda: webbrowser.open_new_tab('https://portswigger.net/web-security/access-control/idor'), UNDERSTANDING_IDOR_ATTACKS)

        create_title("Attack Vector Three")
        create_references("Finding a session and reading a console functions",
                lambda: webbrowser.open_new_tab('https://infosec.smashedpixels.pro/metasploit-automatization-using-python/'), FINDING_A_SESSION_AND_READING_A_CONSOLE_FUNCTIONS)
        create_references("Defining the 'close_msfrpc()' function",
                lambda: webbrowser.open_new_tab('https://stackoverflow.com/questions/26688936/how-to-get-pid-by-process-name'), DEFINING_THE_CLOSE_MSFRPC_FUNCTION)
        create_references("Creating an exploit using pymetasploit3",
                lambda: webbrowser.open_new_tab('URL: https://www.coalfire.com/the-coalfire-blog/may-2019/pymetasploit3-metasploit-automation-library'), CREATING_AN_EXPLOIT_USING_PYMETASPLOIT3)
        create_references("Communication with the MSFRPC framework",
                lambda: webbrowser.open_new_tab('https://github.com/DanMcInerney/pymetasploit3'), COMMUNICATION_WITH_THE_MSFRPC_FRAMEWORK)

        create_title("FTP Brute Force Tool")
        create_references("Installing a FTP server on Kali virtual machine",
                lambda: webbrowser.open_new_tab('https://allabouttesting.org/install-ftp-server-on-kali-linux/'), INSTALLING_A_FTP_SERVER_ON_KALI_VIRTUAL_MACHINE)
        create_references("Understanding how to login to FTP",
                lambda: webbrowser.open_new_tab('https://pythontic.com/ftplib/ftp/login'), UNDERSTANDING_HOW_TO_LOGIN_TO_FTP)

        create_title("HTTP Header Analyzer Tool")
        create_references("Understanding HTTP headers",
                lambda: webbrowser.open_new_tab('https://www.youtube.com/watch?v=Oz902cJcCUg&ab_channel=JohnWatsonRooney'), UNDERSTANDING_HTTP_HEADERS)
        create_references("Coding functions and connecting a URL",
                lambda: webbrowser.open_new_tab('ttp://www.learningaboutelectronics.com/Articles/How-to-retrieve-the-HTTP-headers-of-a-web-page-Python-http-client.php'), CODING_FUNCTIONS_AND_CONNECTING_A_URL)

        create_title("Buffer Overflow")
        create_references("Creating overflow walkthrough", 
        	lambda: webbrowser.open_new_tab('https://princerohit8800.medium.com/buffer-overflow-exploiting-slmail-email-server-f90b27459911'), CREATING_OVERFLOW_WALKTHROUGH)

        create_title("Wordlist Generator")
        create_references("Creating the Wordlist generator", 
        	lambda: webbrowser.open_new_tab('https://github.com/Mebus/cupp'), CREATING_THE_WORDLIST_GENERATOR)
        
        create_title("Video Player")
        create_references("Creating a video player function", 
        	lambda: webbrowser.open_new_tab('https://www.geeksforgeeks.org/pyglet-media-player/'), CREATING_A_VIDEO_PLAYER_FUNCTION)
        
        create_title("Authentication Bypass")
        create_references("Conducting privilege escalation", 
        	lambda: webbrowser.open_new_tab('https://www.youtube.com/watch?v=pRcenfXjf9A'), CONDUCTING_PRIVILEGE_ESCALATION)
        
        create_title("TCP SYN Flooder")
        create_references("Creating the attack", 
        	lambda: webbrowser.open_new_tab('https://github.com/Malam-X/TCP-Flood/blob/main/flood.py'), CREATING_THE_ATTACK)
        
        
    def show_hint(self, desc):
        """
        Show hint function.
        """
        desc_label = ttk.Label(self, text=desc + "\n\n\n\nClick to dismiss", borderwidth=8,
                               relief=RAISED, font=("Calibri", 15))
        desc_label.place(rely=0.125, relx=0.25, relheight=0.75, relwidth=0.5)
        desc_label.bind("<Button-1>", lambda _: desc_label.place_forget())

        # binds the labels configure action to execute the set_label_wrap function
        # This will run when the screen is resized
        desc_label.bind("<Configure>", self.set_label_wrap)

    def set_label_wrap(self, event):
        """
        Dynamically updates the wraplength of the labels so that the text fits to the width properly
        """
        wraplength = event.width - 100  # the 8 is for padding (makes it look nicer)
        event.widget.configure(wraplength=wraplength)
