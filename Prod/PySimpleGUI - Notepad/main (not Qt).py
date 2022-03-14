import PySimpleGUI as sg
import os
from tkinter import filedialog
from pathlib import Path

main_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(main_path)

notes_v = True

filename = 'New File'

def create_window_clear():
    prompt =  [[sg.Text('Are you sure you want to clear?')],
                [sg.Button('Yes'), sg.Button('No')]]
    return prompt

def save_as(values):
    p = Path('notes')
    p.mkdir(exist_ok=True)
    file = filedialog.asksaveasfilename(initialdir = "notes/", title = "Save file as", defaultextension='.txt', filetypes = (("TXT files","*.txt"), ("All Files","*.*")))
    if (file):
        try:
            f = open(file, 'w')
            f.write(values['-NOTES-'])
        finally:
            f.close()
            return os.path.split(file)[1]

def load(window):
    p = Path('notes')
    p.mkdir(exist_ok=True)
    file = filedialog.askopenfilename(initialdir = "notes/", title = "Select file", defaultextension='.txt', filetypes = (("TXT files","*.txt"), ("All Files","*.*")))
    if (file):
        try:
            f = open(file, 'r')
            window['-NOTES-'].update(f.read())
            f.close()
        except FileNotFoundError:
            raise
        except:
            f.close()
            raise
        finally:
            return os.path.split(file)[1]

notes = [
            [sg.Text(filename, key='-FILENAME-')],
            [sg.Multiline(autoscroll=True, size=(67, 30), key='-NOTES-')],
            [sg.Button('Save'), sg.Button('Load'), sg.Button('Clear')]
        ]

layout =   [[sg.Text('Notes')],
            [sg.Button('Test')],
            #### Notes ####
            [sg.pin(sg.Column(notes, key='-COLUMN-', visible=notes_v))],
            #### Buttons at bottom ####
            [sg.Button('Exit')]]

window = sg.Window('Notes', layout)

while True: # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Test':
        notes_v = not notes_v
        window['-COLUMN-'].update(visible = notes_v)

    if event == 'Save':
        window.disable()
        filename = save_as(values)
        window['-FILENAME-'].update(filename)
        window.enable()
    
    if event == 'Load':
        window.disable()
        filename = load(window)
        window['-FILENAME-'].update(filename)
        window.enable()
        
    if event == 'Clear':
        prompt = sg.Window('Clear', create_window_clear())
        window.disable()
        while True:
            p_event, p_values = prompt.read()
            if p_event == sg.WIN_CLOSED:
                prompt.close()
                break
            if p_event == 'Yes':
                window['-NOTES-'].update('')
                prompt.close()
                break
            if p_event == 'No':
                prompt.close()
                break
        window.enable()

window.close()