# pylint: disable=line-too-long

from tkinter import font as tkfont
from tkinter import ttk

from nav_bar import *


class ReferencesPage(tk.Frame):
    """
    References page.
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # displays navbar at top of app screen
        display_nav_bar(self, controller)
        # sets font for frame
        framefont = tkfont.Font(family='Calibri', size=33, weight="bold")
        # sets font for buttons
        tkfont.Font(family='Calibri', size=14)

        # creates blue bar as canvas below nav bar housing label containing title of page
        title_canvas = tk.Canvas(self, bg='#3A4C5E', highlightthickness=0)
        title_canvas.place(rely=0.08, relheight=0.12, relwidth=1)
        title_label = tk.Label(self, text="References", bg='#3A4C5E', fg='white', anchor="c",
                               font=framefont)
        title_label.place(rely=0.08, relheight=0.12, relwidth=1)

        # extra frame for spacing, pushes all subsequent content
        # below nav bar and title label using the pady field
        frameextra = Label(self, bg='#3A4C5E')
        frameextra.pack(pady=120)

        # new frame for tools list
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
        # create scrollbar x
        scrollbar_x = ttk.Scrollbar(container,
                                orient=HORIZONTAL,
                                command=canvas.xview)
        scrollbar_x.pack(side=BOTTOM, fill=X)
        scrollbar_x.config(command=canvas.xview)
        # create new canvas that will be scrolled
        scrollable_frame = Frame(canvas)
        # binds scroll canvas to execute function that gets scrollable region of canvas on event e
        scrollable_frame.bind("<Configure>",
                              lambda _: canvas.configure(scrollregion=canvas.bbox("all")))

        # creates new window using scrollable frame as a base
        canvas.create_window((565, 3), window=scrollable_frame, anchor="nw")

        # sets scrollcommand to the existing scrollbar, linking the widgets
        canvas.config(
            xscrollcommand=scrollbar_x.set,
            yscrollcommand=scrollbar_y.set
        )
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # packs passed widget to the left of screen, used for creating a reference entry
        def pack_widget_left(widget):
            widget.pack(fill='x', padx=280, pady=(1, 1), side=tk.TOP)

        # creates a reference entry using passed strings
        def create_reference(title, explanation, link):
            # creates new canvas to hold reference information
            reference_canvas = tk.Canvas(scrollable_frame, height=200)
            # if the title is empty, use a smaller label (lower font size)
            if title == "":
                tool_title_label = ttk.Label(reference_canvas, text="", font="calibri 4 bold",
                                            anchor="c")
            else:
                tool_title_label = ttk.Label(reference_canvas, text=title, font="calibri 20 bold",
                                            anchor="c")
            pack_widget_left(tool_title_label)

            explanation_label = ttk.Label(reference_canvas, text=explanation, font="calibri 12",
                                         anchor="c")
            pack_widget_left(explanation_label)

            # the reason the link is in a text widget is so it can be copied directly,
            # labels dont let you copy the text
            widget = Text(reference_canvas, height=1, borderwidth=0)
            widget.insert(1.0, link)
            pack_widget_left(widget)
            # sets the text box to disabled so it cannot be edited
            widget.configure(state="disabled")

            reference_canvas.pack(expand=TRUE, fill='x', padx=90, pady=20)

        # creates reference entries
        # if you want to add a new reference entry,
        # 1. invoke create_reference
        # 2. enter the title of the tool the reference pertains to, the explanation of how
        # the reference is used and...
        #    ...the URL link to the resource
        # 4. You're done, run the app and see your new reference entry
        # --------------------------------------------------------------------------------------
        # NOTE: if you have multiple entries for a single tool, create separate invocations of
        # create_reference for...
        # ...each link, however make sure they are all together in the code, then only include
        # the title of the tool...
        # ...in the first entry, and use "" (essentially blank) for the title in the other entries
        # --------------------------------------------------------------------------------------

        # GUI DEVELOPMENT REFERENCES
        create_reference("GUI Development",
                         "Used this video to help learn the basics of tkinter and how to add functionality to the "
                         "application",
                         "https://www.youtube.com/watch?v=YXPyB4XeYLA")
        create_reference("",
                         "Used this site to learn the basics of tkinter and using the place command",
                         "https://www.youtube.com/watch?v=D8-snVfekto&ab_channel=KeithGalli")
        create_reference("", "Used this site to learn how to implement navigation between screens",
                         "https://www.youtube.com/watch?v=39P4BMvvLdM&ab_channel=IntrotoComputerScience")
        create_reference("", "Used this site to learn how to add scrollbars to a frame in tkinter",
                         "https://www.youtube.com/watch?v=0WafQCaok6g&ab_channel=Codemy.com")
        create_reference("", "Used this site to learn how to create dynamically resizing labels",
                         "https://stackoverflow.com/questions/49037051/when-using-the-pack-layout-of-tkinter-how-can-i-have-a-labels-wraplength-be-eq")
        create_reference("", "Used this site to learn how to add horizontal scrollbars to toolkit",
                         "https://pythonguides.com/python-tkinter-scrollbar/")
        # ATTACK VECTOR 1 REFERENCES
        create_reference("Attack Vector One",
                         "Repository where 'pymetasploit3.msfrpc' module is imported from. Used as"
                         " guide for communication with MSFRPC framework",
                         "https://github.com/DanMcInerney/pymetasploit3")
        create_reference("", "Used to help define 'kill_PID()' function.",
                         "https://stackoverflow.com/questions/26688936/how-to-get-pid-by-process-name")
        create_reference("", "Used to help define 'find_session()' function.",
                         "https://infosecaddicts.com/python-and-metasploit/")
        create_reference("", "Used to help define 'set_IP()' function.",
                         "https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib")

        # ATTACK VECTOR 2 REFERENCES
        create_reference("Attack Vector Two",
                         "Mutillidae is a deliberately broken web application which I installed to"
                         " guide me in the creation and testing of my tool since the blue teams "
                         "network was not operational.",
                         "https://github.com/webpwnized/mutillidae")
        create_reference("",
                         "Succinct, easy to read site regarding directory traversal attacks – ideal for beginner/"
                         "intermediate ethical hackers to help understand key concepts and aid in creation of a "
                         "tool to compromise a vulnerability  \n as such. ",
                         "https://portswigger.net/web-security/file-path-traversal ")
        create_reference("",
                         "Same site as above except focussing on IDOR (Insecure direct object reference) attacks."
                         " Once again easy readability for novice hackers and to help understand concepts to guide \n"
                         "user to create a tool or conduct an attack for a vulnerability of this nature. ",
                         "https://portswigger.net/web-security/access-control/idor ")

        # ATTACK VECTOR 3 REFERENCES
        create_reference("Attack Vector Three",
                         "Used in session function to help find session and read console "
                         "function",
                         "https://infosec.smashedpixels.pro/metasploit-automatization-using-python/")
        create_reference("", "Used to help define close_msfrpc()' function.",
                         "https://stackoverflow.com/questions/26688936/how-to-get-pid-by-process-name")
        create_reference("", "Used as a guide to using pymetasploit3 to create an exploit",
                         "https://www.coalfire.com/the-coalfire-blog/may-2019/pymetasploit3-metasploit-automation-library")
        create_reference("",
                         "Repository where 'pymetasploit3.msfrpc' module is imported from. Used as a guide for "
                         "communication with MSFRPC framework.",
                         "https://github.com/DanMcInerney/pymetasploit3")

        # FTP brute force
        create_reference("FTP Brute Force Tool",
                         "This guided me through installing a FTP server on my kali virtual "
                         "machine for testing purposes",
                         "https://allabouttesting.org/install-ftp-server-on-kali-linux/")
        create_reference("",
                         "Helped me understand how to login to FTP using code what parameters to pass to the "
                         "login function",
                         "https://pythontic.com/ftplib/ftp/login")

        # HTTP Header analyzer tool
        create_reference("HTTP Header Analyzer Tool",
                         "This helped me understand how HTTP headers worked and what "
                         "bits of them were important",
                         "https://www.youtube.com/watch?v=Oz902cJcCUg&ab_channel=JohnWatsonRooney")
        create_reference("",
                         "Helped me understand how to code the functionality behind the tool and how to connect "
                         "to a URL via code",
                         "http://www.learningaboutelectronics.com/Articles/How-to-retrieve-the-HTTP-headers-of-a-web-page-Python-http-client.php")

        # WALKTHROUGH REFERENCES
        create_reference("Buffer Overflow", "Sources used to create overflow walkthrough",
                         "https://princerohit8800.medium.com/buffer-overflow-exploiting-slmail-email-server-f90b27459911")
        # Wordlist Generator References
        create_reference("Wordlist Generator", "Sources used to create Wordlist Generator",
                         "https://github.com/Mebus/cupp")

        create_reference("Video Player", "Sources used to create video player function",
                         "https://www.geeksforgeeks.org/pyglet-media-player/")

        create_reference("Authentication Bypass",
                         "Sources used to conduct Privilege Escalation to demonstrate Authentication Bypass attack",
                         "https://www.youtube.com/watch?v=pRcenfXjf9A")

        create_reference("TCP SYN Flooder", "Sources used to create this attack ",
                         "https://github.com/Malam-X/TCP-Flood/blob/main/flood.py")
        
        #ATTACK VECTOR 11 REFERENCES
        create_reference("phpMyAdmin 4.8.1 RCE Attack", "Sources used to perform the attack",
                         "https://www.youtube.com/watch?v=ftYwX5hn7dY&t")
        
        create_reference("", "Used to better understand the attack",
                         "https://www.vulnspy.com/phpmyadmin-4.8.1/")
        
        create_reference("", "Used to get image for the attack vector",
                         "https://www.wallarm.com/what/the-concept-of-rce-remote-code-execution-attack")
