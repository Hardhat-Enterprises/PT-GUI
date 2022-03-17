#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
This tool was created as a "proof of concept" to show the structure of this GUI implementation for DDT.
'''

import PySimpleGUI as sg
import sys, os

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

'''
The below enumeration_menu() function creates a PySimpleGUI window that allows the user to:
- load the windows enumeration batch files
- run the windows enumeration batch files
- read the output text files
'''

os.chdir(os.path.abspath(os.path.dirname(__file__))) # This will get current directory of menu.py
sg.theme('DarkMode')
sg.SetOptions(element_padding=(8,8))


# Defining the layout for the window to use
layout = [  [sg.Text('Netstat', font='Any 26', text_color='#E0E0E0')],
            [sg.Button('Run Netstat', font='Any 24'), sg.Button('Show Netstat Results', font='Any 24')],

            [sg.Text('Ping', font='Any 26', text_color='#E0E0E0')], #[sg.InputText(font='Any 24', text_color='#E0E0E0')] #Commented out incase we decide to add IP entry through python
            [sg.Button('Run Ping', font='Any 24'), sg.Button('Show Ping Results', font='Any 24')],

            [sg.Button('Exit', font='Any 24', button_color=('#E0E0E0','#9F9FA5'))],
            [sg.Multiline(key="output", size=(1240, 20), text_color='#E0E0E0', font='Any 12')]
            ]


# Defining the window with it's name and layout
window = sg.Window('Windows Enumeration', layout, size=(1280,720))

'''
The below while loop runs as long as the window is active and checks to see if the Tool buttons or Exit button has been pressed:
- Exit - break the loop causing the window to close
- Netstat - runs the Netstat batch file
- Ping - runs the Ping batch file
'''
while True:
    event, values = window.read()
    print(values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Run Netstat':
        try:
            os.popen("enumeration_netstat.bat")
        
        except:
            print("Something went wrong.")
            
    if event == 'Show Netstat Results':
        try:
            open_file = open("netstat_output.txt")
            for line in open_file:
                window['output'].print(line)
                window.refresh()

        except:
            print("Something went wrong.")

    if event == 'Run Ping':
        try:
            os.popen("enumeration_ping.bat")
        except:
            print("Something went wrong.")

    if event == 'Show Ping Results':
        try:
            open_file = open("results.log")
            for line in open_file:
                window['output'].print(line)
                window.refresh()
        
        except:
            print("Something went wrong.")        

window.close()
# os.chdir(../../..)