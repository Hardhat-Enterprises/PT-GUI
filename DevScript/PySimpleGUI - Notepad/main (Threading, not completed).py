import PySimpleGUIQt as sg
import os
import tkinter
import threading
from sys import exit
from tkinter import filedialog # Module for opening file browse dialog
from pathlib import Path # Module to create directory

"""
TO DO:
- If main window closed while second window is still active, the program still runs the function once last time (crash if no timeout)
- Append * to the filename on file edit to detect changes
- On toolkit open, the last note can be opened (store filename in a file)

UPDATE:
- Started working on threading to close program if main window is closed
    - Threading works for save_as
    - Threading doesn't work for load because Multiline elements are unable to be accessed from another thread
"""

# Route working directory to the python file
main_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(main_path)

notes_v = True # Variable that manages the notes section visibility
contents = '' # Variable to store the loaded file's contents
filename = 'New File' # The text to put above the notes section

# Create prompt window for clear
def create_window_clear():
    prompt =  [[sg.Text('Are you sure you want to clear?')], # Creates the layout
                [sg.Button('Yes'), sg.Button('No')]]
    return prompt # Returns the layout

# Performs save file as
def save_as(window, values):
    window.disable() # Disables interaction in the main window
    p = Path('notes') # Set the directory name to notes
    p.mkdir(exist_ok=True) # Create directory if not exist
    root = tkinter.Tk() # Create the tkinter root object
    root.wm_withdraw() # Hide the tkinter window
    # Create the dialog window
    file = filedialog.asksaveasfilename(initialdir = "notes/", title = "Save file as", defaultextension='.txt', filetypes = (("TXT files","*.txt"), ("All Files","*.*")))
    root.destroy() # Destroy the tkinter object
    _fn = '' # Variable to store the file name
    if (file): # If file is not None
        try:
            f = open(file, 'w') # Open/create the file in write mode
            f.write(values['-NOTES-']) # Dump all the values inside the Multiline to the file
        finally:
            f.close() # Close the file
            _fn = os.path.split(file)[1] # Return the file's name
    else:
        _fn = None # Return None if no file is chosen
    if (_fn != None): # If _fn is not None change filename to _fn
        filename = _fn
        window['-FILENAME-'].update(filename) # Update the filename placeholder text accordingly
    window.enable() # Enables back interaction in the main window

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
    window.disable() # Disables interaction in the main window
    p = Path('notes') # Set the directory name to notes
    p.mkdir(exist_ok=True) # Create directory if not exist
    root = tkinter.Tk() # Create the tkinter root object
    root.wm_withdraw() # Hide the tkinter window
    # Create the dialog window
    file = filedialog.askopenfilename(initialdir = "notes/", title = "Select file", defaultextension='.txt', filetypes = (("TXT files","*.txt"), ("All Files","*.*")))
    root.destroy() # Destroy the tkinter object
    _fn = '' # Variable to store the file name
    if (file): # If file is not None
        try:
            f = open(file, 'r') # Open file in read mode
            print(f.read())
            f.close() # Close the file
        except FileNotFoundError: # If file is not found, raise exception
            raise
        except: # If file is opened but an error occurs, close the file and raise the exception
            f.close()
            raise
        finally:
            _fn = os.path.split(file)[1] # Return the file's name
    else:
        _fn = None # Return None if no file is chosen
    if (_fn != None): # If _fn is not None change filename to _fn
        filename = _fn
        window['-FILENAME-'].update(filename) # Update the filename placeholder text accordingly
    window.enable() # Enables back interaction in the main window

# Threading test
def start_thread(type):
    if type == 'Save':
        threading.Thread(target=save_as, args=(window, values,), daemon=True).start()
    elif type == 'Load':
        threading.Thread(target=load, args=(window,), daemon=True).start()

# Notes section layout
notes = [
            [sg.Text(filename, key='-FILENAME-')],
            [sg.Multiline(autoscroll=True, size_px=(400, 500), key='-NOTES-')],
            [sg.Button('Save', size=(6, 1)), sg.Button('Load', size=(6, 1)), sg.Button('Clear', size=(6, 1))]
        ]

# Main layout
layout =   [[sg.Button('Hide', key='-COL_BUTTON-', size=(6, 1))],
            [sg.T(key='-PLACEHOLDER-', visible=True)],
            #### Notes ####
            [sg.Column(notes, key='-COLUMN-', visible=notes_v)],
            #### Buttons at bottom ####
            [sg.Button('Exit', size=(6, 1))]]

window = sg.Window('Notes', layout) # Create window

while True: # Event Loop
    event, values = window.read() # Read events
    print(event, values) # Print events (can be removed on debug completion)

    if event == sg.WIN_CLOSED or event == 'Exit': # Breaks the loop if exit is triggered
        break

    if event.startswith('-COL_BUTTON-'): # Collapse button pressed event
        notes_v = not notes_v # Show/Hide the notes section
        window['-COLUMN-'].update(visible = notes_v) # Update the visibility of the notes section accordingly
        window['-COL_BUTTON-'].update("Hide" if notes_v else "Show") # Updates the collapse button text accordingly
        window.VisibilityChanged() # Added in PySimpleGUIQt to shrink window after changing visibility (use sg.pin in normal PSG)

    if event == 'Save':
        if (filename == 'New File' or filename != None): # If the note is a new file, do save as instead of save
            start_thread('Save') # Start thread on save_as function
        else: # Perform save on current file
            save(values)
    
    if event == 'Load':
        print(contents)
        window['-NOTES-'].update(contents) # Copy the file's content to the Multiline
        start_thread('Load') # Start thread on load function
        
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
    
    if event.startswith('-PLACEHOLDER-'):
        window['-NOTES-'].update()

window.close() # Closes the main window in the end
exit()