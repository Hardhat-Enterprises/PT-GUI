import PySimpleGUI as sg
from hash_analyzer import *
import os

SHOW = 'Show output'
HIDE = 'Hide output'

HASH = "Hash     : "
FILE = "Filename: "

main_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(main_path)

def collapse(layout, key):
    return sg.pin(sg.Column(layout, key=key))

section1 = [
            [sg.Multiline(disabled=True, write_only=True, autoscroll=True, size=(67, 30), key="-OUTPUT-"+sg.WRITE_ONLY_KEY)]
        ]

layout =   [[sg.Text('Hash Analyzer Return String')],
            [sg.T(HASH, key='-IN1 TEXT-'),
            sg.Input(focus=True, key='-IN1-'),
            sg.Combo(["Hash","File"], default_value='Hash', size=(10,10), enable_events=True, key="-COMBO-", readonly=True)],
            [sg.Button('Enter', key="-ENTER-", bind_return_key=True)],
            #### Section 1 part ####
            [sg.Button(HIDE, enable_events=True, k='-OPEN SEC1-')],
            [collapse(section1, '-SEC1-')],
            #### Buttons at bottom ####
            [sg.Button('Exit')]]

window = sg.Window('Hash Analyzer Return String', layout)

opened1 = True

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event.startswith('-OPEN SEC1-'):
        opened1 = not opened1
        window['-OPEN SEC1-'].update(HIDE if opened1 else SHOW)
        window['-SEC1-'].update(visible=opened1)
    if event.startswith('-COMBO-'):
        combo = values['-COMBO-']
        window['-IN1 TEXT-'].update(HASH if combo=='Hash' else FILE)
    if event.startswith('-ENTER-'):
        inp = values['-IN1-']
        combo = values['-COMBO-']
        window['-OUTPUT-'+sg.WRITE_ONLY_KEY].print(hash_analyze(inp, combo))

window.close()