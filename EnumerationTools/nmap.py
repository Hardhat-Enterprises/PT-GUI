from subprocess import Popen, PIPE
from tkinter import font as tkfont

from nav_bar import *
from utils.console import Console


class NMAP(tk.Frame):
    """
    Class that houses the nmap GUI.
    """

    # Below are some basic class variables that are used for controlling positioning of elements.
    screen_base_x = .5
    screen_base_y = .2
    incremental_y = .05

    def __init__(self, parent, controller):
        """
        Function called upon class instantiation.
        """
        tk.Frame.__init__(self, parent)
        display_nav_bar(self, controller)

        heading_font = tkfont.Font(family="Calibri", size=32, weight="bold")

        heading_frame = tk.Label(self, text="NMAP Scan", bg="#3B5262", fg="white",
                                 anchor="center", font=heading_font)
        heading_frame.place(rely=0.08, relheight=0.12, relwidth=1)

        screen_frame = tk.Frame(self, bg="white")
        screen_frame.place(rely=0.2, relheight=1, relwidth=1)

        label = ttk.Label(
            screen_frame,
            text="Scan options",
            justify="center",
            font=("-size", 15, "-weight", "bold"),
        )
        self.place_widget_center(label)

        # IP entry field.
        sudo_password_field = ttk.Entry(screen_frame, width=34)
        sudo_password_field.insert(0, "Please enter sudo password here.")
        self.place_widget_center(sudo_password_field)

        # IP entry field.
        ip_entry_field = ttk.Entry(screen_frame, width=34)
        ip_entry_field.insert(0, "Please enter target ip or hostname here.")
        self.place_widget_center(ip_entry_field)

        # Port entry field.
        port_entry_field = ttk.Entry(screen_frame, width=34)
        port_entry_field.insert(0, "Please enter number of top ports to scan.")
        self.place_widget_center(port_entry_field)

        console = Console(screen_frame, width="200")

        # Button to start snmp-check.
        start_button = ttk.Button(screen_frame, text="Start", style="Accent.TButton",
                                  command=lambda: self.start_button_action(ip_entry_field.get(), port_entry_field.get(),
                                                                           sudo_password_field.get(),
                                                                           console))
        self.place_widget_center(start_button)

        console_output_label = ttk.Label(
            screen_frame,
            text="Scan Output",
            justify="center",
            font=("-size", 15, "-weight", "bold"),
        )
        self.place_widget_center(console_output_label)

        self.screen_base_y *= 1.3

        self.place_widget_center(console)

    def start_button_action(self, ip: str, port: str, sudo_password: str, console: Console):
        command = f"printf '{sudo_password}\n' | sudo -S nmap -O -P0 -sTUV -top-ports {port} -oA target {ip} --stats-every 5s"

        # Start process
        process = Popen(command, stdout=PIPE, universal_newlines=True, shell=True)

        # Print all output from stdout to tkinter.
        for line in process.stdout:
            console.write(line)

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
