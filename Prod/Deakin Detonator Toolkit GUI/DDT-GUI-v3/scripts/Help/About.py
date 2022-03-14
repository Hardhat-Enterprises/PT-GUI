#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PySimpleGUI as sg

def MAKE_About():
	# Don't change the theme and padding for the program.
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

    msg = "In it's simplest definition, Deakin Detonator Toolkit (DDT) is a penetration testing toolkit.\n\nThe toolkit allows you to make use of a variety of tools, without needing the \"know-how\" of each command. We have simplified the penetration testing experience for both newcomers who are still learning, and those who have been hacking for years. To get started, choose a tool from the navigation menu, found at the top of the homescreen.\n\nHappy hacking!"

    layout = [  [sg.Text('\n', font='Any 14')],
                [sg.Text('What is DDT?', font='Any 64', text_color='#FFFFFF', justification='c', size=(64, 1))],
                [sg.Text('\n', font='Any 14')],
                [sg.Multiline(default_text=msg, size=(1240, 9), text_color='#E0E0E0', font='Any 24', disabled=True)],
                [sg.Text('\n', font='Any 14')],
                [sg.Button('Back to homescreen', font='Any 24', button_color=('#E0E0E0','#9F9FA5'))] ]

    return sg.Window('Deakin Detonator Toolkit - About', layout, size=(1280,720), finalize=True)

def CHECK_About(window, event, values):
    if event == sg.WIN_CLOSED or event == 'Back to homescreen': 
        window.close()