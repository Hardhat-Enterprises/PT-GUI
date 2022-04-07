from tkinter import font as tkfont
import os
from nav_bar import *


class API_Keys(tk.Frame):

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

        # Heading for page
        heading_frame = tk.Label(self, text="Set API Keys", bg="#3B5262", fg="white",
                                 anchor="center", font=heading_font)
        heading_frame.place(rely=0.08, relheight=0.12, relwidth=1)

        # Create a screen frame to house our components.
        screen_frame = tk.Frame(self, bg="white")
        screen_frame.place(rely=0.2, relheight=1, relwidth=1)
        
        #SHODAN API KEY
        label = ttk.Label(
            screen_frame,
            text="Shodan API Key",
            justify="center",
            font=("-size", 15, "-weight", "bold"),
        )
        self.place_widget_center(label)

        shodan_entry = ttk.Entry(screen_frame, width=34)
        shodan_entry.insert(0, "Please enter key here")
        self.place_widget_center(shodan_entry)

        #Set environ variable of Shodan API key
        def shodanClick():
            key = shodan_entry.get()
            os.environ["SHODAN_API_KEY"] = key

        shodan_button = ttk.Button(screen_frame, text="Set", style="Accent.TButton", command=lambda:shodanClick())
        self.place_widget_center(shodan_button)


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

