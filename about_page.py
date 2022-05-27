# pylint: disable=invalid-name
# pylint: disable=global-variable-undefined


from tkinter import font as tkfont
from tkinter import ttk
from nav_bar import *


class AboutPage(tk.Frame):
    """
    About page.
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        display_nav_bar(self, controller)
        framefont = tkfont.Font(family='Calibri', size=30, weight="bold")

        title_label = tk.Label(self, text="Tools", bg='white', fg='#92CEFF',
                               anchor="c", font=framefont)
        # creates blue bar as canvas below nav bar housing label containing
        # title of page
        title_label = tk.Label(
            self,
            text="Welcome to Toolkit",
            bg='white',
            fg='#92CEFF',
            anchor="c",
            font=framefont)
        title_label.place(rely=0.08, relheight=0.1, relwidth=1)

        # creates blue bar as canvas below nav bar
        title_canvas = tk.Canvas(self, bg='#c8e6ff', highlightthickness=0)
        title_canvas.place(rely=0.08, relheight=0.004, relwidth=1)

        # creates blue bar as canvas below title
        title_canvas = tk.Canvas(self, bg='#c8e6ff', highlightthickness=0)
        title_canvas.place(rely=0.17, relheight=0.004, relwidth=1)

        # content below nav bar and title label using the pady field
        frameextra = Label(self, anchor="w")
        frameextra.pack(pady=73)

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
        # binds scroll canvas to execute function that gets scrollable region
        # of canvas on event
        scrollable_frame.bind(
            "<Configure>", lambda _: canvas.configure(
                scrollregion=canvas.bbox("all")))

        # creates new window using scrollable frame as a base
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # sets scrollcommand to the existing scrollbar, linking the widgets
        canvas.config(yscrollcommand=scrollbar_y.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        frame1 = Canvas(scrollable_frame)
        frame1.pack()
        # creates new image variable from teamwork.png, used for background on
        # title screen
        global teamwork
        teamwork = tk.PhotoImage(file='resources/DDT_Logo.png')
        teamwork_label = ttk.Label(frame1, image=teamwork)

        frame2 = Canvas(scrollable_frame)
        frame2.pack()

        frame3 = Canvas(scrollable_frame)
        frame3.pack()

        frame4 = Canvas(scrollable_frame)
        frame4.pack()
        global using_computer
        using_computer = tk.PhotoImage(file='resources/DeakinLogo.png')
        computer_label = ttk.Label(frame4, image=using_computer)

        paragraph_one = ttk.Label(
            frame1, text="	About The Deakin Detonator Toolkit: "
            "\n \n     In the simplest definition, Deakin Detonator Toolkit (DDT) is a"
            " penetration testing "
            "\n environment developed by Deakin "
            "University Capstone students under the Hardhat "
            "\n Project. Originally designed as a Command Line Interface with limited"
            "testing abilities, "
            "\n the toolkit has evolved in recent years"
            "to become the established Graphical  User "
            "\n Interface capable of hosting and deploying Attack Vectors and various tools to "
            "\n combat todays exploits and vulnerabilities.", font=(
                'Helvetica', 15), justify=LEFT, width=150)

        paragraph_two = ttk.Label(
            frame2,
            text="About Attack Vectors:		"
            "\n        The DTT features several student-developed Attack Vector scenarios that "
            "allow users of the toolkit to become"
            "\n        familiar with various cyber-attacks. Featuring scenarios such as Web "
            "application vulnerabilities and user"
            "\n        privilege bypass attacks, the DTT allows a stable and secure environment"
            " to perform ethical hacking, while the"
            "\n        continued expansion of the toolkit’s software capabilities will allow for "
            "more intricate cyber-attacks to be investigated.",
            font=('Calibri', 14), justify=LEFT, width=150)

        paragraph_three = ttk.Label(
            frame3,
            text="About DTT Vectors:		   "
            "\n        The DTT Tools database features an extensive range of exploitation, "
            "execution, access, and software tools to "
            "\n        allow DTT users the necessary support in performing ethical hacking tasks."
           " The tools included show an insight"
            "\n        into various cybersecurity prevention and detection techniques to allow "
            "users to perform penetration-testing "
            "\n        tasks and become well equipped against cyber-attacks.",
            font=('Calibri', 14), justify=LEFT, width=150)

        paragraph_four = Label(
            frame4,
            text="									 	"
            "\n		Contact: \nCompany: Hardhat Enterprises - "
            "Mail:Keshav Sood: keshav.sood@deakin.edu.au"
            "\nProject: Taylor Smith - Mail:smithtaylor@deakin.edu.au",
            font=(
                'Calibri',
                14),
            justify=LEFT,
            width=100)

        # places labels on the screen
        #paragraph_two.place(rely=0.22, relx=0.085, relheight=0.24, relwidth=0.4)
        #paragraph_three.place(rely=0.71, relx=0.48, relheight=0.24, relwidth=0.4)
        #teamwork_label.place(rely=0.22, relx=0.54, relheight=0.4, relwidth=0.31)
        #computer_label.place(rely=0.5, relx=0.13, relheight=0.45, relwidth=0.31)

        paragraph_one.pack(side=RIGHT, padx=40, pady=30)
        teamwork_label.pack(side=LEFT, padx=40, pady=33)

        paragraph_two.pack(side=LEFT, padx=40, pady=30)
        paragraph_three.pack(side=LEFT, padx=40, pady=30)

        computer_label.pack(side=LEFT, padx=40, pady=50)
        paragraph_four.pack(side=RIGHT, padx=40, pady=50)
        # binds the labels configure action to execute the set_label_wrap function
        # This will run when the screen is resized
        # paragraph_one.bind("<Configure>", self.set_label_wrap)
        # paragraph_two.bind("<Configure>", self.set_label_wrap)

    @staticmethod
    def set_label_wrap(event):
        """
        dynamically updates the wraplength of the labels
        so that the text fits to the width properly.
        """
        wraplength = event.width - \
            20  # the 8 is for padding (makes it look nicer)
        event.widget.configure(wraplength=wraplength)
