# pylint: disable=unnecessary-lambda
# pylint: disable=consider-using-with
# pylint: disable=global-variable-undefined
# pylint: disable=invalid-name
# pylint: disable=no-self-use
# pylint: disable=unused-variable

import os
from subprocess import Popen, PIPE
from tkinter import font as tkfont

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
        # sets font for buttons and title
        tkfont.Font(family='OpenSans', size=13)
        framefont = tkfont.Font(family='Arial Rounded MT Bold', size=28, weight='bold')

        title_label = tk.Label(self, text="Tools", bg='white', fg='#92CEFF',
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

        ##for toggling visibility of tools under a title
        self.titleChildrenNumber = []#number of elements below a title (tool's labels and buttons)
        self.toolsList = []#a list of each of these elements to hide
        self.hideButtons=[]#a list of the title buttons
        # creates new image variable from start_button.png, used for launch button on tools
        global button_image
        button_image = tk.PhotoImage(file='resources/start_button.png')
        global info_image
        info_image = tk.PhotoImage(file='resources/Info_button.png')
        global launch_image
        launch_image = tk.PhotoImage(file='resources/rocketsmall.png')

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

        ## toggles visibility of tools under a title
        def toggle_tools(titleidx, namebutton, hidden):
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

            ## tooltype%4: 0=tool_canvas, 1=toolname_label, 2=navbutton, 3=infobutton
            tooltype = 0

            ## in the range of items below the target title at titleidx: hide or unhide
            for n in range(idxFrom, idxTo):
                if ((tooltype%4 == 0) and not hidden):
                    self.toolsList[n].pack_forget()
                    namebutton.configure(command=lambda : show_on_title(titleidx,namebutton))

                elif (tooltype%4 == 0 and hidden):
                    pack_widget_left(self.toolsList[n+1])
                    pack_widget_right(self.toolsList[n+2])
                    pack_widget_right(self.toolsList[n+3])
                    self.toolsList[n].pack(after=namebutton, expand=TRUE, fill='x', padx=90, pady=8)
                    namebutton.configure(command=lambda : hide_on_title(titleidx,namebutton))

                tooltype += 1
        ##shows tools under a title
        def show_on_title(titleidx, namebutton):
            toggle_tools(titleidx, namebutton, True)

        ##hides tools under a title
        def hide_on_title(titleidx, namebutton):
            toggle_tools(titleidx, namebutton, False)

        # creates navigation button that executes passed command, allows for variety
        # of functionality of tool click
        def nav_button(canvas, command):
            nav_button = ttk.Button(canvas, image=launch_image,
            command=command, style='Rocket.TButton')
            pack_widget_right(nav_button)
            Tk.update(self)
            return nav_button

        # creates a tool using passed strings and command function
        def create_tool(name, command, desc):
            # creates new canvas to hold tool information/execute widgets
            tool_canvas = tk.Canvas(scrollable_frame, height=0)

            toolname_label = ttk.Label(tool_canvas, text=name,
                                       font='controller.btn_font2 12 italic')
            pack_widget_left(toolname_label)

            navbutton = nav_button(tool_canvas, command)
            info_button = ttk.Button(tool_canvas, image=info_image,
                                     command=lambda: self.show_hint(desc), style='Accent.TButton')
            pack_widget_right(info_button)
            tool_canvas.pack(expand=TRUE, fill='x', padx=90, pady=8)
            self.toolsList.append(tool_canvas)
            self.toolsList.append(toolname_label)
            self.toolsList.append(navbutton)
            self.toolsList.append(info_button)
            self.titleChildrenNumber[len(self.titleChildrenNumber)-1] += 4

        # creates tools and section titles by invoking previous functions
        # if you want to add a new tool,
        # 1. invoke create_tool under a relevant section heading (e.g "Reconnaissence Tools")
        # 2. enter the name and command you want to execute between the brackets
        # 3. if you want the button to navigate to a page, use:
        #                                   lambda: controller.show_frame("PAGE_NAME")
        #    and replace PAGE_NAME with the name of the page defined in main.py at line 35
        # 4. You're done, run the app and see your new tool
        create_title("Reconnaissance Tools")
        create_tool("Port Scanner",
                    lambda: controller.show_frame("PortScan"), PORT_SCANNER_DESC)
        create_tool("Nmap", lambda: load_nmap_tool(), NMAP_SCANNER_DESC)
        create_tool("Banner Grabber",
                    lambda: controller.show_frame("BannerGrab"),
                    BANNER_GRABBER_DESC)

        create_title("Enumeration Tools")

        create_tool("Sniffer", lambda: controller.show_frame("TestSniff"),
                    SNIFFER_DESC)
        create_tool("Mac Changer",
                    lambda: controller.show_frame("MacChange"), MAC_CHANGER_DESC)
        create_tool("Image Metadata Extractor",
                    lambda: controller.show_frame("IMDExtractor"),
                    IMG_META_EXT_DESC)
        create_tool("Hash Analyzer",
                    lambda: controller.show_frame("HashAn"),
                    HASH_ANALYZER_DESC)
        create_tool("HTTP Header Analyzer",
                    lambda: controller.show_frame("HTTPheaders"),
                    HTTP_ANALYZER_DESC)

        create_title("Execution Tools")
        create_tool("VulnExploit", lambda: load_vulnexploit_tool(),
                    VULN_EXPLOIT_DESC)
        create_tool("Msfconsole Listener",
                    lambda: controller.show_frame("MsfListener"),
                    MSFCON_LISTENER_DESC)
        create_tool("Mimt + Dns Spoof",
                    lambda: controller.show_frame("MimtDnsSpoof"),
                    MITM_AND_DNS_DESC)
        create_tool("FTP Brute Forcer",
                    lambda: controller.show_frame("FTPBruteForce"),
                    FTP_BRUTE_DESC)
        create_tool("Wordlist generator", lambda: open_wordlistgen(),
                    WORDLIST_GEN_DESC)
        create_tool("ICMP Ping Flooder",
                    lambda: controller.show_frame("ICMP"),
                    PHCRACKER_DESC)
        create_tool("TCP SYN Flooder", lambda: open_synfloodGUI(),
                    TCP_SYN_FLOOD_DESC)

        create_title("Fuzzers")
        create_tool("Directory Traversal Fuzzer",
                    lambda: controller.show_frame("DTFuzz"),
                    DIREC_TRAV_DESC)

        create_title("Initial Access Tools")
        create_tool("SSH Bruteforce",
                    lambda: controller.show_frame("SshBrute"), SSH_BRUTE_DESC)
        create_tool("Password Hash Cracker",
                    lambda: controller.show_frame("PHCracker"),
                    PHCRACKER_DESC)
        create_tool("ZIP File Brute Forcer",
                    lambda: controller.show_frame("ZipBF"),
                    PHCRACKER_DESC)

        create_title("Payloads")
        create_tool("Msfvenom Payload Generator",
                    lambda: controller.show_frame("MsfPayloadGen"), MSFVENOM_PAY_GEN_DESC)

        create_title("Resource Development Tools")
        create_tool("Notepad", lambda: open_notepad(), NOTEPAD_DESC)

        create_title("Help")
        create_tool("Command Prompt", lambda: load_terminal(), CMD_DESC)
        create_tool("Example New Page",
                    lambda: controller.show_frame("ExampleNewPage"), "Example new page")

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
