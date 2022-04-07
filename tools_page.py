# pylint: disable=unnecessary-lambda
# pylint: disable=consider-using-with
# pylint: disable=global-variable-undefined
# pylint: disable=invalid-name
# pylint: disable=no-self-use
# pylint: disable=unused-variable

import os
from subprocess import Popen, PIPE
from tkinter import font as tkfont
from tkinter import ttk

from nav_bar import *
from tool_descriptions import *


class ToolsPage(tk.Frame):
    """
    Class for the Tools Page.
    """

    def __init__(self, parent, controller):
        """
        Initialisation of the tools page.
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # displays navbar at top of app screen
        display_nav_bar(self, controller)
        # sets font for frame
        framefont = tkfont.Font(family='Calibri', size=33, weight="bold")
        # sets font for buttons
        tkfont.Font(family='Calibri', size=13)

        # creates blue bar as canvas below nav bar housing label containing title of page
        title_canvas = tk.Canvas(self, bg='#3A4C5E', highlightthickness=0)
        title_canvas.place(rely=0.08, relheight=0.12, relwidth=1)
        title_label = tk.Label(self, text="Network Tools List", bg='#3A4C5E', fg='white',
                               anchor="c", font=framefont)
        title_label.place(rely=0.08, relheight=0.12, relwidth=1)

        def notepadopen():
            """
            Open notepad.
            """
            os.chdir("./Tools")
            cmd = "python3 Notepad.py"
            _ = Popen(cmd, stdout=PIPE, universal_newlines=True, shell=True)
            os.chdir("../")

        # extra frame for spacing, pushes all subsequent content below nav bar and
        # title label using the pady field
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
        # creates new image variable from start_button.png, used for launch button on tools
        global button_image
        button_image = tk.PhotoImage(file='resources/start_button.png')
        global info_image
        info_image = tk.PhotoImage(file='resources/Info_button.png')

        def open_wordlistgen():
            os.chdir("./Tools")
            cmd = "python3 WordlistGen.py"
            _ = Popen(cmd, stdout=PIPE, universal_newlines=True, shell=True)
            os.chdir("../")

        def open_notepad():
            os.chdir("./Tools")
            cmd = "python3 Notepad.py"
            _ = Popen(cmd, stdout=PIPE, universal_newlines=True, shell=True)
            os.chdir("../")

        def load_nmap_tool():
            os.chdir("./Tools/Nmap_Gui")
            cmd = "python3 nmapGUI.py"
            _ = Popen(cmd, stdout=PIPE, universal_newlines=True, shell=True)
            os.chdir("../../")

        def open_synfloodGUI():
            os.chdir("./Tools")
            cmd = "python3 synfloodGUI.py"
            _ = Popen(cmd, stdout=PIPE, universal_newlines=True, shell=True)
            os.chdir("../")

        def load_vulnexploit_tool():
            os.chdir("./Tools")
            cmd = 'exo-open --launch TerminalEmulator'
            _ = Popen([cmd + ' python3 VulnExploit.py'], stdout=PIPE, shell=True)
            os.chdir("../")

        def load_terminal():
            _ = Popen("exo-open --launch TerminalEmulator", stdout=PIPE, universal_newlines=True,
                       shell=True).stdout

        # packs passed widget to the left of screen, used for creating a tool entry
        def pack_widget_left(button):
            button.pack(fill='x', padx=80, pady=(5, 5), side=LEFT)

        # same as above but to right of screen
        def pack_widget_right(button):
            button.pack(fill='x', padx=180, pady=(5, 5), side=RIGHT)

        # creates section title from passed string
        def create_title(title):
            title = ttk.Label(scrollable_frame, text=title,
                             font='controller.btn_font2 20 bold', anchor="c")
            title.pack(expand=TRUE, fill='x', padx=100, pady=20)

        # creates navigation button that executes passed command, allows for variety
        # of functionality of tool click
        def nav_button(canvas, command):
            nav_button = ttk.Button(canvas, compound=LEFT, text="LAUNCH", command=command)
            pack_widget_right(nav_button)

        # creates a tool using passed strings and command function
        def create_tool(name, author, version, command, desc):
            # creates new canvas to hold tool information/execute widgets
            tool_canvas = tk.Canvas(scrollable_frame, height=10)

            toolname_label = ttk.Label(tool_canvas, text=name,
                                      font='controller.btn_font2 14')
            pack_widget_left(toolname_label)

            author_label = ttk.Label(tool_canvas, text=author,
                                    font='controller.btn_font2 12')

            nav_button(tool_canvas, command)
            info_button = ttk.Button(tool_canvas, image=info_image, compound=LEFT,
                                    command=lambda: self.show_hint(desc))
            pack_widget_right(info_button)

            version_label = ttk.Label(tool_canvas, text=version, font='controller.btn_font2 12')
            pack_widget_right(version_label)
            pack_widget_right(author_label)

            tool_canvas.pack(expand=TRUE, fill='x', padx=190, pady=8)

        # creates tools and section titles by invoking previous functions
        # if you want to add a new tool,
        # 1. invoke create_tool under a relevant section heading (e.g "Reconnaissence Tools")
        # 2. enter the name, author, version and command you want to execute between the brackets
        # 3. if you want the button to navigate to a page, use:
        #                                   lambda: controller.show_frame("PAGE_NAME")
        #    and replace PAGE_NAME with the name of the page defined in main.py at line 35
        # 4. You're done, run the app and see your new tool
        create_title(
            "                                                                Reconnaissance Tools"
            "                                                                ")
        create_tool("Port Scanner", "Laiba Samar", "1.01",
                    lambda: controller.show_frame("PortScan"), PORT_SCANNER_DESC)
        create_tool("Nmap", "Malik Ayub", "1.01", lambda: load_nmap_tool(), NMAP_SCANNER_DESC)
        create_tool("Banner Grabber", "Laiba Samar", "1.01",
                    lambda: controller.show_frame("BannerGrab"),
                    BANNER_GRABBER_DESC)
        create_tool("Shodan Reconnaissance", "A.S. Jaeger / K. Gray", "1.01", 
                    lambda: controller.show_frame("ShodanScript"), 
                    SHODAN_DESC)

        create_title("Enumeration Tools")
        create_tool("Sniffer", "Laiba Samar", "1.01", lambda: controller.show_frame("TestSniff"),
                    SNIFFER_DESC)
        create_tool("Mac Changer", "Laiba Samar", "1.01",
                    lambda: controller.show_frame("MacChange"), MAC_CHANGER_DESC)
        create_tool("Image Metadata Extractor", "Laiba Samar", "1.01",
                    lambda: controller.show_frame("IMDExtractor"),
                    IMG_META_EXT_DESC)
        create_tool("Hash Analyzer", "W. Tranku / R. Harris", "1.01",
                    lambda: controller.show_frame("HashAn"),
                    HASH_ANALYZER_DESC)
        create_tool("HTTP Header Analyzer", "James Martin", "1.01",
                    lambda: controller.show_frame("HTTPheaders"),
                    HTTP_ANALYZER_DESC)

        create_title("Execution Tools")
        create_tool("VulnExploit", "Adrian Nadalin", "1.01", lambda: load_vulnexploit_tool(),
                    VULN_EXPLOIT_DESC)
        create_tool("Msfconsole Listener", "Daniel Sacchetta", "1.01",
                    lambda: controller.show_frame("MsfListener"),
                    MSFCON_LISTENER_DESC)
        create_tool("Mimt + Dns Spoof", "Laiba Samar", "1.01",
                    lambda: controller.show_frame("MimtDnsSpoof"),
                    MITM_AND_DNS_DESC)
        create_tool("FTP Brute Forcer", "James Martin", "1.01",
                    lambda: controller.show_frame("FTPBruteForce"),
                    FTP_BRUTE_DESC)
        create_tool("Wordlist generator", "Steve Tee", "1.01", lambda: open_wordlistgen(),
                    WORDLIST_GEN_DESC)
        create_tool("ICMP Ping Flooder", "Ryan Harris", "1.01",
                    lambda: controller.show_frame("ICMP"),
                    PHCRACKER_DESC)
        create_tool("TCP SYN Flooder", "Warren Bartholomeusz", "1.01", lambda: open_synfloodGUI(),
                    TCP_SYN_FLOOD_DESC)

        create_title("Fuzzers")
        create_tool("Directory Traversal Fuzzer", "Ryan Harris", "1.01",
                    lambda: controller.show_frame("DTFuzz"),
                    DIREC_TRAV_DESC)

        create_title("Initial Access Tools")
        create_tool("SSH Bruteforce", "Laiba Samar", "1.01",
                    lambda: controller.show_frame("SshBrute"), SSH_BRUTE_DESC)
        create_tool("Password Hash Cracker", "Ryan Harris", "1.01",
                    lambda: controller.show_frame("PHCracker"),
                    PHCRACKER_DESC)
        create_tool("ZIP File Brute Forcer", "Ryan Harris", "1.01",
                    lambda: controller.show_frame("ZipBF"),
                    PHCRACKER_DESC)

        create_title("Payloads")
        create_tool("Msfvenom Payload Generator", "Daniel Sacchetta", "1.1",
                    lambda: controller.show_frame("MsfPayloadGen"), MSFVENOM_PAY_GEN_DESC)

        create_title("Resource Development Tools")
        create_tool("Notepad", "Laiba Samar", "1.01", lambda: open_synfloodGUI(), NOTEPAD_DESC)

        create_title("Help")
        create_tool("Command Prompt", "", "1.01", lambda: load_terminal(), CMD_DESC)

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
