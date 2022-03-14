#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PySimpleGUI as sg # Main framework
from copy import deepcopy # Function to make a deepcopy of an object
import json # Module to process JSON file
from pathlib import Path # Module to create directory
import os # OS based command

current_path = os.getcwd() # Save the current path before changing the working directory
main_path = os.path.dirname(os.path.realpath(__file__)) # Get the path of the python file
os.chdir(main_path)  # Route working directory to the python file

config = {} # Create the config placeholder

def create_json():
    global config
    if not(os.path.exists("config.json")):
        config['theme'] = {} # Create the theme placeholder

        config['theme']['DarkMode'] = {  'BACKGROUND': '#121212',
                                    'TEXT': '#E0E0E0',
                                    'INPUT': '#1C1C1E',
                                    'TEXT_INPUT': '#FFFFFF',
                                    'SCROLL': '#32D74B',
                                    'BUTTON': ('#E0E0E0', '#32D74B'),
                                    'PROGRESS': ('#32D74B', '#333333'),
                                    'BORDER': 0,
                                    'SLIDER_DEPTH': 0,
                                    'PROGRESS_DEPTH': 0 }
        config['text'] = {'font':'Any 26'}
        config['button'] = {'font':'Any 24'}
        config['inputtext'] = {'font':'Any 24'}
        config['close_button'] = {'button_text':'Close', 'font':'Any 24', 'button_color':('#E0E0E0','#9F9FA5')}
        config['window'] = {'size':(1280, 720)}

        with open('config.json', 'w') as outf: # Open the file in write mode (create if not exist)
            json.dump(config, outf, indent=4) # Dump the config dictionary in json format to the output file

    else:
        with open('config.json', 'r') as inf: # Open the file in read mode
            config = json.load(inf) # Load the json file into the config dictionary

create_json() # Create a new json file based on the default settings or load an existing one

theme = list(config['theme'])[0] # Get the theme name from the config file
sg.LOOK_AND_FEEL_TABLE[theme] = config['theme'][theme] # Add the theme to the PySimpleGUI's theme collection
sg.theme(theme) # Set the theme accordingly
sg.SetOptions(element_padding=(8,8)) # Set extra options

class WindowCreator:
    def __init__(self): # Initialize the __layout and __window field
        self.__layout = []
        self.__window = None

    def set_layout(self, layout):
        self.__layout = layout # Replace the layout based on the inserted parameter

    def _duplicate_layout(self):
        return deepcopy(self.__layout) # Clone the layout objects because PySimpleGUI doesn't support duplicate layout usage
    
    def add_closebutton(self, index=None): # Create the close button element
        c = config['close_button'] 
        self.insert_element(sg.Button(c['button_text'], font=c['font'], button_color=c['button_color']), index=index)

    def show_layout(self, title='Example Window', create_close=True): # Show the layout of the window before creating it

        layout = self._duplicate_layout() # Duplicate the layout

        if create_close:
            self.add_closebutton() # Append the close button element if parameter is true

        window = sg.Window(title, layout, size=config['window']['size'], finalize=True) # Create the example window

        while True: # Simple event to close the window
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == config['close_button']['button_text']:
                break

        window.close() # Close the window

    def make_window(self, title, create_close=True): # Create the finalised window and return it
        if self.__window == None:

            if create_close:
                self.add_closebutton()

            c = config['window']
            self.__window = sg.Window(title, self.__layout, size=c['size'], finalize=True)
            return self.__window

        else:
            print("Window has already been generated!")

    def get_window(self): # Get the window
        if self.__window == None:
            print("Window has not yet been generated!")
        else:
            return self.__window

    def add_text(self, text="", index=None): # Add a text element to the layout
        c = config['text']
        self.insert_element(sg.Text(text, font=c['font']), index=index)
    
    def add_button(self, text="", key=None, index=None): # Add a button element to the layout
        c = config['button']
        self.insert_element(sg.Button(text, font=c['font'], key=key), index=index)
    
    def add_input_text(self, text="", index=None): # Add an input text element to the layout
        c = config['inputtext']
        self.insert_element(sg.InputText(text, font=c['font']), index=index)

    def insert_element(self, elem, index=None): # Insert an element to the layout
        if index != None:
            try:
                self.__layout[index].append(elem)
                return
            except IndexError:
                pass
        self.__layout.append([elem])

if __name__ == "__main__":
    w1 = WindowCreator() # Create the WindowCreator object
    w1.add_text("Hello World") # Add a text element
    w1.add_button("Enter") # Add a button
    # w1.ShowLayout() # Show the current layout

    window = w1.make_window("Window Creator") # Create the PySimpleGUI window object
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == config['close_button']['button_text']:
            break

        if event == 'Enter':
            print("Hello World!")

    window.close() # Close the window