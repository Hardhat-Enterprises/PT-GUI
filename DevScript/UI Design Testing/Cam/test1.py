#!/usr/bin/python3
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
import os

sg.LOOK_AND_FEEL_TABLE['DarkMode'] = {  'BACKGROUND': '#121212',
                                        'TEXT': '#FFFFFF',
                                        'INPUT': '#333333',
                                        'TEXT_INPUT': '#FFFFFF',
                                        'SCROLL': '#F18AA0',
                                        'BUTTON': ('#FFFFFF', '#F18AA0'),
                                        'PROGRESS': ('#F18AA0', '#333333'),
                                        'BORDER': 0,
                                        'SLIDER_DEPTH': 0,
                                        'PROGRESS_DEPTH': 0 
                                    }

sg.theme("DarkMode")
sg.SetOptions(element_padding=(8,4))

T1 = "#E0E0E0"
T2 = "#A0A0A0"
T3 = "#6C6C6C"

navbar = [  ['&SCAN', ['Example 1', 'Example 2']],
            ['&ENUMERATE', ['Example 1', 'Example 2']],
            ['&ATTACK', ['Example 1', 'Example 2']],
            ['&HELP', ['Example 1', 'Example 2']] ]

welcome_para = "Welcome to Deakin Detonator Toolkit.\n\nHere, you will be able to utilise several penetration testing tools that we have developed a user-friendly interface for.\n\nThis includes enumeration/scanning and specific attacking tools. DDT's main purpose is to simplify the penetration testing learning experience and to minimise the amount of repetition in certain attacks.\n\nPlease choose an option from the navigation menu above to get started."

home_layout = [  [sg.Menu(navbar, tearoff=False)],
            [sg.Text("WELCOME!", font='Any 112', text_color=T1, size=(64,1), justification='center')],
            [sg.Text(welcome_para, size=(64, 10), font='Any 24', text_color=T2, justification='center')] ]

scan_layout = [ [sg.Menu(navbar, tearoff=False)],
                [sg.Text("Target: ", font='Any 24', text_color=T2)]]

window = sg.Window("Deakin Detonator Toolkit", home_layout, size=(1280,720))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break

window.close()