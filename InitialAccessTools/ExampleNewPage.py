from tkinter import font as tkfont

from nav_bar import *


class ExampleNewPage(tk.Frame):
    """
    Class that houses the ExampleNewPage GUI.
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

        # Heading for page
        heading_frame = tk.Label(self, text="Example new page", bg="#3B5262", fg="white",
                                 anchor="center", font=heading_font)
        heading_frame.place(rely=0.08, relheight=0.12, relwidth=1)

        # Create a screen frame to house our components.
        screen_frame = tk.Frame(self, bg="white")
        screen_frame.place(rely=0.2, relheight=1, relwidth=1)

        # Example label.
        label = ttk.Label(
            screen_frame,
            text="My awesome label here",
            justify="center",
            font=("-size", 15, "-weight", "bold"),
        )
        self.place_widget_center(label)

        # Text entry field.
        hash_to_crack_entry = ttk.Entry(screen_frame, width=34)
        hash_to_crack_entry.insert(0, "Please enter something here.")
        self.place_widget_center(hash_to_crack_entry)

        # Crack hash button.
        crack_button = ttk.Button(screen_frame, text="Do something!", style="Accent.TButton")
        self.place_widget_center(crack_button)

        # These are variables that hold the value of the radiobutton.
        radio_1_value = tk.IntVar(value=1)
        radio_2_value = tk.IntVar(value=2)
        radio_3_value = tk.IntVar(value=0)

        # Example radio buttons.
        radio_1 = ttk.Radiobutton(screen_frame, text="Unselected", variable=radio_1_value)
        radio_2 = ttk.Radiobutton(screen_frame, text="Selected", variable=radio_2_value)
        radio_3 = ttk.Radiobutton(screen_frame, text="Disabled", state="disabled", variable=radio_3_value)

        # Place the first widget center.
        self.place_widget_center(radio_1)
        # Place the next widget to the left.
        self.place_widget_center_beside(radio_2, -0.1)
        # Place the final widget to the right.
        self.place_widget_center_beside(radio_3, 0.1)

        # Example switch.
        switch_value = tk.IntVar(value=0)
        switch = ttk.Checkbutton(screen_frame, text="Switch", style="Switch.TCheckbutton", variable=switch_value)
        self.place_widget_center(switch)

        # Example option menu.
        option_menu_list = ["", "OptionMenu", "Option 1", "Option 2"]
        option_menu_selection = tk.StringVar(value=option_menu_list[1])
        optionmenu = ttk.OptionMenu(screen_frame, option_menu_selection, *option_menu_list)
        self.place_widget_center(optionmenu)

        # Will store the value of the scale and progress bar.
        progress_bar_value = tk.DoubleVar(value=50.0)

        # Example slider, will control the progress bar.
        scale = ttk.Scale(
            screen_frame,
            from_=0,
            to=100,
            variable=progress_bar_value,
            command=lambda event: progress_bar_value.set(scale.get()),
        )

        # Example progress bar using the value of progress_bar_value to demonstrate progress.
        progress_bar = ttk.Progressbar(screen_frame, value=0, variable=progress_bar_value, mode="determinate")
        self.place_widget_center(progress_bar)
        self.place_widget_center_beside(scale, -0.1)

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
