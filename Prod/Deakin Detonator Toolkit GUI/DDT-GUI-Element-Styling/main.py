'''
    In this file, you will find the likely PySimpleGUI elements that you will use in your tools.
    Each element in this example has been styled so you can simply copy each element you need and whatever other parameters you see necessary.

    The "Output" section includes more in-depth examples about presenting program output using buttons as inputs.

    For a list of parameters for a given element, see the call reference on PySimpleGUI's readthedocs page:
    https://pysimplegui.readthedocs.io/en/latest/call%20reference/#slider-element
'''

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

navbar = [  ['COMMON', ['Tool 1']],
            ['ENUMERATION', ['2', '3']],
            ['ATTACK', ['4', '5']],
            ['HELP', ['6', '7']] ]

def main():
    basics = [  [sg.Text('This is a heading!', font='Any 64', text_color='#FFFFFF')],
                    [sg.Text('This is the standard text.', font='Any 26', text_color='#E0E0E0')],
                    [sg.Text('This is the standard disabled text.', font='Any 26', text_color='#6C6C6C')] ]

    inputs = [  [sg.Checkbox('Checkbox value 1', font='Any 24', text_color='#E0E0E0'), sg.Checkbox('Checkbox value 2', font='Any 24', text_color='#E0E0E0')],
                        [sg.Text('Combobox:', font='Any 26', text_color='#E0E0E0'), sg.InputCombo(('Value 1', 'Value 2'), font='Any 24', text_color='#E0E0E0')],
                        [sg.Text('Input text:', font='Any 26', text_color='#E0E0E0'), sg.InputText('Default text', font='Any 24', text_color='#E0E0E0')],
                        [sg.Multiline(default_text='This is some default text in a multiline element.', size=(1240, 4), text_color='#E0E0E0', font='Any 24')],
                        [sg.Radio('Radio option 1', 'GROUP_RADIO', font='Any 24', text_color='#E0E0E0')],
                        [sg.Radio('Radio option 2', 'GROUP_RADIO', font='Any 24', text_color='#E0E0E0')],
                        [sg.Text('0', font='Any 26', text_color='#E0E0E0'), sg.Slider(range=(0, 100), orientation='h', default_value=50, font='Any 24', text_color='#E0E0E0'), sg.Text('100', font='Any 26', text_color='#E0E0E0')],
                        [sg.Button('Submit', font='Any 24'), sg.Button('Cancel', font='Any 24', button_color=('#E0E0E0','#9F9FA5'))] ]

    outputs = [  [sg.Multiline(default_text='This multiline will reroute stdout.\n', reroute_stdout=True, autoscroll=True, size=(1240, 8), text_color='#E0E0E0', font='Any 24')],
                    [sg.Button('Test', font='Any 24', tooltip='Press me to see rerouted output!')],
                    [sg.ProgressBar(10, orientation='h', key='-PBAR-', size=(1240, 8))],
                    [sg.Button('Add Progress', font='Any 24', tooltip='Press me to add progress to the progress bar!')] ] 

    layout = [  [sg.Menu(navbar, background_color='#F5F5F5', tearoff=False)],
                [sg.TabGroup([[sg.Tab('Basics', basics), sg.Tab('Input', inputs), sg.Tab('Output', outputs)]], font='Any 24', title_color='#6C6C6C', tab_background_color='#1C1C1E', selected_title_color='#E0E0E0', selected_background_color='#2C2C2E')] ]

    window = sg.Window('Deakin Detonator Toolkit - Styled Elements', layout, size=(1280,720))

    progress = 0

    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Submit':
            print('Submit button pressed!')
        if event == 'Cancel':
            print('Cancel button pressed!')
        if event == 'Test':
            print('See? STDOUT rerouted!')
        if event == 'Add Progress':
            if progress < 10:
                progress += 1
                window['-PBAR-'].update_bar(progress)
            else:
                print("Progress bar is already at 100%")

    window.close()

main()