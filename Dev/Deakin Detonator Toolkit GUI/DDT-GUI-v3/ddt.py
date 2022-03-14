#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys

sys.dont_write_bytecode = True

main_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(main_path)
script_file = open("scripts/Imports.py", "w") # Open the file to store the script entries into
os.system('python3 install_dep.py') # Install all dependencies

import PySimpleGUI as sg

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

def scan(toscan, toappend):
    os.chdir("scripts")
    for file in os.listdir(toscan):
        if os.path.isdir(os.path.join(toscan, file)): # Checks if file is a directory
            for subdir_file in os.listdir(os.path.join(toscan, file)): # Searches that Directory
                if subdir_file.endswith(".py"): # If a '.py' file is found
                    file_wo_ext = os.path.splitext(subdir_file)[0] # Get the filename without the extension
                    # Writes the import of each script into 'Imports.py' to be used in main
                    script_file.write("from scripts." + toscan + "." +  file + "." + file_wo_ext + " import *" + "\n")
                    toappend.append(file_wo_ext) #Creates a list of tool names

        elif file.endswith(".py"):
            file_wo_ext = os.path.splitext(file)[0]
            # Make sure 'Template.py' and 'Imports.py' files are not read as a tool
            if file_wo_ext != 'Template' and file_wo_ext != 'Imports':
                # Writes the import of each script into 'Imports.py' to be used in main
                script_file.write("from scripts." + toscan + "." + file_wo_ext + " import *" + "\n")
                toappend.append(file_wo_ext) #Creates a list of tool names
    os.chdir(main_path)

recon_tools = []
scan("Recon", recon_tools)
resourcedev_tools = []
scan("ResDev", resourcedev_tools)
access_tools = []
scan("InitialAccess", access_tools)
execution_tools = []
scan("Execution", execution_tools)
payload_tools = []
scan("Payloads", payload_tools)
help_tools = []
scan("Help", help_tools)
script_file.close() #Closes the file after adding all scripts

# Imports all scripts and their functions from each tool's file in /scripts/
from scripts.Imports import *

# common_scripts_file = open("common/Imports/py")

navbar = [  ["Recon", [recon_tools]],
            ["Resource Development", [resourcedev_tools]],
            ["Initial Access", [access_tools]],
            ["Execution", [execution_tools]],
            ["Payloads", [payload_tools]],
            ["Help", [help_tools]]]

welcome_msg = "\n\nWelcome to Deakin Detonator Toolkit.\n\nChoose a tool from the navigation menu above to get started.\nAlternatively, visit HELP > About to learn more about this toolkit."
legal_msg = 'Please note: This toolkit is intended for educational and research purposes only.\nThe developers, owners and business correspondents are not responsible for any malicious use of the tools provided.'

def Homescreen():
    layout = [  [sg.Menu(navbar, font='Any 9', background_color='#F5F5F5', tearoff=False)],
                [sg.Text('\n', font='Any 26')],
                [sg.Text('WELCOME!', font='Any 64', text_color='#FFFFFF', justification='c', size=(64, 1))],
                [sg.Text(welcome_msg, font='Any 26', text_color='#E0E0E0', justification='c', size=(64,8))],
                [sg.Text(legal_msg, font='Any 14', text_color='#E0E0E0', justification='c', size=(128, 4))] ]

    return sg.Window('Deakin Detonator Toolkit', layout, size=(1280,720), finalize=True)

event_check = []
windows = []

def main():
    window1 = Homescreen()
    while True:
        window, event, values = sg.read_all_windows()

        if window == window1 and event == sg.WIN_CLOSED:
            break

        for name in recon_tools:
            if event == name:
                n = globals()["MAKE_" + name]()
                windows.append(n)
                event_check.append(name)

        for name in resourcedev_tools:
            if event == name:
                n = globals()["MAKE_" + name]()
                windows.append(n)
                event_check.append(name)

        for name in access_tools:
            if event == name:
                n = globals()["MAKE_" + name]()
                windows.append(n)
                event_check.append(name)

        for name in execution_tools:
            if event == name:
                n = globals()["MAKE_" + name]()
                windows.append(n)
                event_check.append(name)

        for name in payload_tools:
            if event == name:
                n = globals()["MAKE_" + name]()
                windows.append(n)
                event_check.append(name)

        for name in help_tools:
            if event == name:
                n = globals()["MAKE_" + name]()
                windows.append(n)
                event_check.append(name)

        i = 0
        for win in windows:
            if window == win:
                globals()["CHECK_" + event_check[i]](window, event, values)
            i += 1

if __name__ == '__main__':
    main()
