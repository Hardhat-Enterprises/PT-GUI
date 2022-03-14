import PySimpleGUI as sg
from subprocess import Popen, PIPE
import subprocess
import os

SYMBOL_UP = 'Show terminal'
SYMBOL_DOWN = 'Hide terminal'

main_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(main_path)

def runCommand(window, cmd):
    p1 = Popen(cmd, stdout=PIPE, universal_newlines=True)
    for line in p1.stdout:
        window['-OUTPUT-'+sg.WRITE_ONLY_KEY].print(line, end="")
        window.refresh()

def collapse(layout, key):
    return sg.pin(sg.Column(layout, key=key))

section1 = [[sg.Multiline(disabled=True, write_only=True, autoscroll=True, size=(88, 20), key="-OUTPUT-"+sg.WRITE_ONLY_KEY)],
            [sg.Input(focus=True, key='-IN1-'), sg.Button('Run', key="-EXECUTE-", bind_return_key=True)]]

layout =   [[sg.Text('Integrated Terminal')],
            #### Section 1 part ####
            [sg.Button(SYMBOL_DOWN, enable_events=True, k='-OPEN SEC1-')],
            [collapse(section1, '-SEC1-')],
            #### Buttons at bottom ####
            [sg.Button('Exit')]]

window = sg.Window('Integrated Terminal', layout)

opened1 = True

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event.startswith('-OPEN SEC1-'):
        opened1 = not opened1
        window['-OPEN SEC1-'].update(SYMBOL_DOWN if opened1 else SYMBOL_UP)
        window['-SEC1-'].update(visible=opened1)

    if event.startswith('-EXECUTE-'):
        runCommand(window, values["-IN1-"])

window.close()