#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
This simple GUI app allows the user to enter an IP and ping it.

It was created using the example code in PySimpleGUI's documentation page (Jump-Start section):
- https://pysimplegui.readthedocs.io/en/latest/
'''

import PySimpleGUI as sg
import sys, os

sg.theme("DarkGrey6")

layout = [  [sg.Text('Target IP: '), sg.InputText()],
            [sg.Button('Ping IP'), sg.Button('Exit')] ]

window = sg.Window('Ping 4 Packets', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Ping IP':
    	try:
    		os.system("ping " + values[0] + " -c 4")
    	except:
    		print("Something went wrong. Please check the IP address is formatted correctly (x.x.x.x).")

window.close()