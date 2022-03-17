import PySimpleGUI as sg
import os

#Set theme
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


#Creating program function
def MAKE_LazGUI():
    main_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(main_path)
    #Obtains the current working directory


    layout = [
        [sg.Text('Select Scan Options', font='Any 36'), sg.Combo(('All', 'Chats', 'System Admin', 'Databases', 'Mail', 'Memory', 'Wi-fi', 'Browsers', 'Crypto Wallets'), default_value='All',
        key='-Option1-', font='Any 24'), sg.CBox('Verbose (optional)', font='Any 26', key='-Verbose1-')],
        [sg.Button('Submit', enable_events=True, key="-SUBMIT-", font='Any 24'), sg.Cancel(font='Any 24')],
        [sg.MLine(default_text='Results: ', disabled=True, write_only=True, autoscroll=True, size=(140, 16), font='Any 18', key='multi1')]]

    return sg.Window('Password Scan', layout, size=(1280, 720), finalize=True)

def runCommand(window, cmd):
    p1 = Popen(cmd, stdout=PIPE, universal_newlines=True, shell = True)
    for line in p1.stdout:
        window['multi1'].print(line, end="")
        window.refresh()

def CHECK_LazGUI(window, event, values):
    #Creates a popup window that takes in the root password
    #This will be revised in the next iteration so we won't have to store the root password
    output_command = "python3 tool/laZagne.py" #Initialising the final nmap command

    if event == sg.WIN_CLOSED or event == 'Cancel':
        os.chdir(main_path)
        os.chdir("../../") # Reset the Working Directory back to main.py's folder
        window.close()

    if event == '-SUBMIT-':    #Appends nmap commands based on options selected
        if values['-Option1-'] == 'All':
            output_command += ' all'
        if values['-Option1-'] == 'Chats':
            output_command += ' chats'
        if values['-Option1-'] == 'System Admin':
            output_command += ' sysadmin'
        if values['-Option1-'] == 'Databases':
            output_command += ' databases'
        if values['-Option1-'] == 'Mail':
            output_command += ' mails'
        if values['-Option1-'] == 'Memory':
            output_command += ' memory'
        if values['-Option1-'] == 'Wi-fi':
            output_command += ' wifi'
        if values['-Option1-'] == 'Browsers':
            output_command += ' browsers'
        if values['-Option1-'] == 'Crypto Wallets':
            output_command += ' wallet'
        if values['-Verbose1-'] == True:
            output_command += ' -v'
        window['multi1'].update('')
        print(output_command)
        window['multi1'].update(output_command)
        output = os.popen(output_command)
        window['multi1'].update(output)
