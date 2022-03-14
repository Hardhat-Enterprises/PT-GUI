#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
This script is to act as a template to standardise the tools developed for this GUI toolkit. Please note the following:
- Don't change this file directly. Copy it to a new file then make changes
- The file's name will act as the tool's name in the toolkit. E.g. a SYN scanner would be SYN_Scanner.py
- The program should have two functions; MAKE_*FUNC_NAME* and CHECK_*FUNC_NAME*. E.g. SYN_Scanner.py would have MAKE_SYN_Scanner() and CHECK_SYN_Scanner()
    - MAKE_*FUNC_NAME* should contain the layout of your window and returns a created window object (see below)
    - CHECK_*FUNC_NAME* should contain the contents of your window's while loop, WITHOUT the while loop (see below)
    - Do note that you should change *FUNC_NAME* to your program's name
- Once you have made your changes, delete any comments you wish and add your own
'''

''' ===== **TEMPLATE STARTS BELOW** ===== '''

import PySimpleGUI as sg

'''
Please note the following:
- Remember to put this outside your functions (e.g. directly above your MAKE_FUNC_NAME() function)
- Don't change the theme and padding for the program.
'''
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

# Change FUNC_NAME to your file's name without .py; E.g. SYN_Scanner.py would have MAKE_SYN_Scanner()
def MAKE_FUNC_NAME():

    '''
    The layout is how you want elements on the window to appear.
    - The layout's elements are contained in a set of square brackets ([])
    - Each row in the program is defined with another set of square brackets
    - Each row can have multiple elements, as shown in the example layout below
    See the PySimpleGUI documentation and cookbook for more information about window elements
    Note: Make sure "sg.Button('Close')" as the final element in the last row
    '''
    layout = [  [sg.Text('Example text: ', font='Any 26', text_color='#E0E0E0'), sg.InputText('Example default input text', font='Any 24', text_color='#E0E0E0')],
                [sg.Button('Example Button', font='Any 24', key='-EXAMPLE_BUTTON-'), sg.Button('Close', font='Any 24', button_color=('#E0E0E0','#9F9FA5'))] ]

    '''
	The sg.Window() function creates the PySimpleGUI window object, which takes four parameters:
	- A string to be used as the window title, such as 'Google Chrome', 'Microsoft Teams', 'XYZ Tool' etc.
	- A layout for the window to use; this was defined above
    - A size; should be left at 1280x720
    - The statement "finalize=True"
    The newly created window object should directly be returned (notice the return keyword).
    '''
    return sg.Window('WINDOW TITLE', layout, size=(1280,720), finalize=True)


'''
Please note the following:
- The CHECK_FUNC_NAME function needs to accept three parameters:
    - window; your program's window where you can directly change its elements' values
    - event; the event that just happened in your program's window
    - values; all values from elements in your window where the elements allow events to happen (e.g. Input, Combo, any elements with enable_events=True)
'''
# Change FUNC_NAME to your file's name without .py; E.g. SYN_Scanner.py would have CHECK_SYN_Scanner(window, event, values)
def CHECK_FUNC_NAME(window, event, values):

    '''
    These are the changes made to the previous template's while loop:
    - The while loop is removed as it is no longer used
    - The event, values = window.read() is no longer used as the main DDT.py will do the read
    - Note that the break statement when event == 'Close' can no longer be used and is replaced by window.close()
    '''
    if event == sg.WIN_CLOSED or event == 'Close': # LEAVE THIS - checks if the event is the window being closed
        window.close() # LEAVE THIS - closes the window if the user has exited the program and stops memory leaks

    #Below is an example of the layout's 'Example Button' event on being pressed
    if event == 'Example Button':
        print('The example button was pressed!')

    #Below is an example of detecting an event happening using its key value
    #Please note that if you want to refer to the element's key value you need to use an elif (else if) statement then event.startswith(*KEY_VALUE*)
    elif event.startswith('-EXAMPLE_BUTTON-'):
        print('The example button was pressed!')