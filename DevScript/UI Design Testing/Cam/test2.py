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

HIGH_EMPHASIS_TEXT = "#E0E0E0"
LOW_EMPHASIS_TEXT = "#A0A0A0"
DISABLED_TEXT = "#6C6C6C"

navbar = [  ['&SCAN', ['Scan Tool']],
            ['&ENUMERATE', ['Example 1', 'Example 2']],
            ['&ATTACK', ['Example 1', 'Example 2']],
            ['&HELP', ['Example 1', 'Example 2']] ]

def main():
    welcome_para = "Welcome to Deakin Detonator Toolkit.\n\nHere, you will be able to utilise several penetration testing tools that we have developed a user-friendly interface for.\n\nThis includes enumeration/scanning and specific attacking tools. DDT's main purpose is to simplify the penetration testing learning experience and to minimise the amount of repetition in certain attacks.\n\nPlease choose an option from the navigation menu above to get started."

    home_layout = [ [sg.Menu(navbar, tearoff=False)],
                    [sg.Text("WELCOME!", font='Any 112', text_color=HIGH_EMPHASIS_TEXT, size=(64,1), justification='center', background_color='#1E1E1E')],
                    [sg.Text(welcome_para, size=(64, 10), font='Any 24', text_color=LOW_EMPHASIS_TEXT, justification='center', background_color='#1E1E1E')] ]

    window = sg.Window("Deakin Detonator Toolkit", home_layout, size=(1280,720))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        if event == "Scan Tool":
            Scan()

    window.close()

def Scan():
    speed_keys = ['T1', 'T2', 'T3', 'T4', 'T5']

    options_tab = [ [sg.Text("Target Address*:", font='Any 18', text_color=HIGH_EMPHASIS_TEXT), sg.InputText(default_text='www.example.com', key='-TARGET_IP-', font='Any 18', text_color=LOW_EMPHASIS_TEXT)],
                    [sg.Text("Target Port(s):", font='Any 18', text_color=HIGH_EMPHASIS_TEXT), sg.InputText(default_text='0', key='-PORT1-', font='Any 18', text_color=LOW_EMPHASIS_TEXT), sg.Text('to', font='Any 18', text_color=HIGH_EMPHASIS_TEXT), sg.InputText(default_text='1023', key='-PORT2-', font='Any 18', text_color=LOW_EMPHASIS_TEXT)],
                    [sg.Text("Scan Speed:", font='Any 18', text_color=HIGH_EMPHASIS_TEXT)],
                    [sg.Radio("Very slow", "speed_radio", key=speed_keys[0], font='Any 18', text_color=HIGH_EMPHASIS_TEXT)],
                    [sg.Radio("Slow", "speed_radio", key=speed_keys[1], font='Any 18', text_color=HIGH_EMPHASIS_TEXT)],
                    [sg.Radio("Moderate", "speed_radio", key=speed_keys[2], font='Any 18', text_color=HIGH_EMPHASIS_TEXT)],
                    [sg.Radio("Fast", "speed_radio", key=speed_keys[3], font='Any 18', text_color=HIGH_EMPHASIS_TEXT)],
                    [sg.Radio("Very fast", "speed_radio", key=speed_keys[4], font='Any 18', text_color=HIGH_EMPHASIS_TEXT)],
                    [sg.Button("Start Scan"), sg.Button("Cancel")]]

    output_tab = [  [sg.Text("This is the output tab", font='Any 18', text_color=HIGH_EMPHASIS_TEXT)]]

    scan_layout = [ [sg.Menu(navbar, tearoff=False)],
                    [sg.TabGroup([[sg.Tab('Options', options_tab), sg.Tab('Output', output_tab)]], font='Any 24', title_color=HIGH_EMPHASIS_TEXT)] ]

    scan_window = sg.Window("Deakin Detonator Toolkit: Scan Tool", scan_layout, size=(1280, 720))

    while True:
        event, values = scan_window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        if event == "Start Scan":
            for key in speed_keys:
                if values[key] == True:
                    print("Command to execute: nmap -{} -p {}-{} {}".format(key, values['-PORT1-'], values['-PORT2-'], values['-TARGET_IP-']))

    scan_window.close()

main()