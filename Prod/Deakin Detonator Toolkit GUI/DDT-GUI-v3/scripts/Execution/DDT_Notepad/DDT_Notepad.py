import PySimpleGUI as sg
import os
import tkinter
from tkinter import filedialog # Module for opening file browse dialog
from pathlib import Path # Module to create directory

# DDT Theme
sg.LOOK_AND_FEEL_TABLE['DarkMode'] = {  'BACKGROUND': '#121212',
                                        'TEXT': '#E0E0E0',
                                        'INPUT': '#1C1C1E',
                                        'TEXT_INPUT': '#FFFFFF',
                                        'SCROLL': '#32D74B',
                                        'BUTTON': ('#E0E0E0', '#32D74B'),
                                        'PROGRESS': ('#32D74B', '#333333'),
                                        'BORDER': 0,
                                        'SLIDER_DEPTH': 0,
                                        'PROGRESS_DEPTH': 0
                                    }

sg.theme('DarkMode')
sg.SetOptions(element_padding=(8,8))

notes_v = True # Variable that manages the notes section visibility

filename = 'New File' # The text to put above the notes section

# Create prompt window for clear
def create_window_clear():
    prompt =  [[sg.Text('Are you sure you want to clear?', font='Any 14')], # Creates the layout
                [sg.Button('Yes', font='Any 14'), sg.Button('No', font='Any 14')]]
    return prompt # Returns the layout

# Performs save file as
def save_as(values):
    p = Path('notes') # Set the directory name to notes
    p.mkdir(exist_ok=True) # Create directory if not exist
    root = tkinter.Tk() # Create the tkinter root object
    root.wm_withdraw() # Hide the tkinter window
    # Create the dialog window
    file = filedialog.asksaveasfilename(initialdir = "notes/", title = "Save file as", defaultextension='.txt', filetypes = (("TXT files","*.txt"), ("All Files","*.*")))
    root.destroy() # Destroy the tkinter object
    if (file): # If file is not None
        try:
            f = open(file, 'w') # Open/create the file in write mode
            f.write(values['-NOTES-']) # Dump all the values inside the Multiline to the file
        finally:
            f.close() # Close the file
            return os.path.split(file)[1] # Return the file's name
    else:
        return None # Return None if no file is chosen

# Performs save on current file
def save(values):
    p = Path('notes') # Set the directory name to notes
    p.mkdir(exist_ok=True) # Create directory if not exist
    try:
        f = open("notes/" + filename, 'w') # Open file in write mode
        f.write(values['-NOTES-']) # Dump all the values inside the Multiline to the file
    finally:
        f.close() # Close the file

# Performs load file
def load(window):
    p = Path('notes') # Set the directory name to notes
    p.mkdir(exist_ok=True) # Create directory if not exist
    root = tkinter.Tk() # Create the tkinter root object
    root.wm_withdraw() # Hide the tkinter window
    # Create the dialog window
    file = filedialog.askopenfilename(initialdir = "notes/", title = "Select file", defaultextension='.txt', filetypes = (("TXT files","*.txt"), ("All Files","*.*")))
    root.destroy() # Destroy the tkinter object
    if (file): # If file is not None
        try:
            f = open(file, 'r') # Open file in read mode
            window['-NOTES-'].update(f.read()) # Copy the file's content to the Multiline
            f.close() # Close the file
        except FileNotFoundError: # If file is not found, raise exception
            raise
        except: # If file is opened but an error occurs, close the file and raise the exception
            f.close()
            raise
        finally:
            return os.path.split(file)[1] # Return the file's name
    else:
        return None # Return None if no file is chosen

def MAKE_DDT_Notepad():
    global filename

    # Notes section layout
    notes = [
                [sg.Text(filename, key='-FILENAME-', font='Any 18', text_color='#E0E0E0', size=(200,1))],
                [sg.Multiline(autoscroll=True, size=(800, 22), key='-NOTES-', font='Any 14')],
                [sg.Button('Save', font='Any 18'), sg.Button('Load', font='Any 18'), sg.Button('Clear', font='Any 18')]
            ]

    # Main layout
    layout =   [
                #### Notes ####
                [sg.Column(notes, key='-COLUMN-')],
                #### Buttons at bottom ####
                [sg.Button('Close', font='Any 18', button_color=('#E0E0E0','#9F9FA5'))]
            ]

    return sg.Window('DDT Notepad', layout, size=(1280,720), finalize=True) # Create window

def CHECK_DDT_Notepad(window, event, values):
    global filename

    # Route working directory to the python file
    main_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(main_path)

    if event == sg.WIN_CLOSED or event == 'Close': # Breaks the loop if exit is triggered
        window.close() # Closes the main window in the end

    if event == 'Save':
        window.disable() # Disables interaction in the main window
        if (filename == 'New File' or filename == None): # If the note is a new file, do save as instead of save
            _fn = save_as(values) # Perform load function and store the returned filename
            if (_fn != None): # If _fn is not None change filename to _fn
                filename = _fn
                window['-FILENAME-'].update(filename) # Update the filename placeholder text accordingly
        else: # Perform save on current file
            save(values)
        window.enable() # Enables back interaction in the main window
    
    if event == 'Load':
        window.disable() # Disables interaction in the main window
        _fn = load(window) # Perform load function and store the returned filename
        if (_fn != None): # If _fn is not None change filename to _fn
            filename = _fn
            window['-FILENAME-'].update(filename) # Update the filename placeholder text accordingly
        window.enable() # Enables back interaction in the main window
        
    if event == 'Clear':
        prompt = sg.Window('Clear', create_window_clear()) # Create prompt window for clear
        window.disable() # Disables interaction in the main window
        while True: # Event loop in clear window
            p_event, p_values = prompt.read() # Read events in clear window
            if p_event == sg.WIN_CLOSED or p_event == 'No': # Breaks the loop and closes window on exit
                prompt.close() # Closes the prompt window
                break
            if p_event == 'Yes':
                window['-NOTES-'].update('') # Clears the Multiline
                prompt.close() # closes the prompt window
                break
        window.enable() # Enables back interaction in the main window
        window.BringToFront() # Brings the window back into focus

    os.chdir("../../..") # Reset the Working Directory back to main.py's folder

#if __name__ == '__main__':
    #DDT_Notepad()