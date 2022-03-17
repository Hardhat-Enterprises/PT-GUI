import PySimpleGUI as sg
import os
import time
from subprocess import call, Popen, PIPE

# Set theme
sg.LOOK_AND_FEEL_TABLE['DarkMode'] = {'BACKGROUND': '#232536',
                                      'TEXT': 'white',
                                      'INPUT': '#E3E4E5',
                                      'TEXT_INPUT': 'black',
                                      'SCROLL': 'black',
                                      'BUTTON': ('black', '#c4c4c4'),
                                      'PROGRESS': ('white', 'black'),
                                      'BORDER': 0.5,
                                      'SLIDER_DEPTH': 0.5,
                                      'PROGRESS_DEPTH': 0.5}
sg.theme('DarkMode')
sg.SetOptions(element_padding=(8, 8))


# Creating program function
def MAKE_nmapGUI():
    main_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(main_path)
    # Obtains the current working directory

    layout = [
        [sg.Text('Enter The NMAP Scan Information Below', justification='center', size=(60, 1), key='-bold-',
                 font='Celebri 26', background_color='#3B5262')],
        [sg.Text('Enter sudo password: ', size=(17, 1), font='Celebri 18'),
         sg.InputText(font='Celebri 18', key='-PASS-', size=(22, 1), password_char='*')],
        [sg.Text('Enter IP to scan:', size=(17, 1), font='Celebri 18'),
         sg.InputText(font='Celebri 18', key='-IP1-', size=(22, 1))],
        [sg.Text('Port (optional):', size=(17, 1), font='Celebri 18'), sg.InputText(font='Celebri 18', key='-PORT1-',
                                                                                    size=(22, 1)),
         sg.CBox('Top 20 ports', font='Celebri 18', key='-PORT2-')],
        [sg.Text('Scan Type:', size=(17, 1), font='Celebri 18'), sg.Combo(('All', 'Operating System', 'Firewall Status',
                                                                           'Services', 'Stealth', 'Device discovery',
                                                                           'Vulscan(CVE finder)'), size=(21, 1),
                                                                          default_value='All', font='Celebri 18',
                                                                          key='-SCAN1-')],
        [sg.Text('Speed:', size=(17, 1), font='Celebri 18'),
         sg.Combo(('T1', 'T2', 'T3', 'T4', 'T5'), size=(21, 1), default_value='T3', font='Celebri 18', key='-SCAN2-'),
         sg.CBox('Save results', font='Celebri 18', key='-LOG1-')],
        # [sg.CBox('Vulscan (service scan type only): returns CVEs for detected services', key='-VULSCAN-')],
        [sg.Button('Scan', enable_events=True, font='Celebri 18', key="-SUBMIT-"),
         sg.Button('Close', font='Celebri 18', button_color=('black', '#c4c4c4'))],
        [sg.MLine(default_text='Results: ', disabled=True, write_only=True, autoscroll=True, size=(120, 16),
                  font='Celebri 16', key='multi1')]]

    window = sg.Window('Scan with NMAP', layout, size=(1380, 820), finalize=True)
    while True:
        event, values = window.Read()
        if event in (None, 'Close'):
            CHECK_nmapGUI(window, event, values)
            break
        if event == '-SUBMIT-':
            CHECK_nmapGUI(window, event, values)


def runCommand(window, cmd):
    p1 = Popen(cmd, stdout=PIPE, universal_newlines=True, shell=True)
    for line in p1.stdout:
        window['multi1'].print(line, end="")
        window.refresh()


def CHECK_nmapGUI(window, event, values):
    if event == sg.WIN_CLOSED or event == 'Close':
        os.chdir('../..')
        window.close()

    if event == '-SUBMIT-':  # Appends nmap commands based on options selected
        main_path = os.path.dirname(os.path.realpath(__file__))
        # get_pass = sg.popup_get_text('Nmap requires root privileges to run, please enter root password: ', 'Sudo permission', password_char='*')
        # Creates a popup window that takes in the root password
        # This will be revised in the next iteration so we won't have to store the root password
        output_command = "echo " + values['-PASS-'] + " | sudo -S "
        output_command += "nmap"  # Initialising the final nmap command

        if values['-SCAN1-'] == 'All':
            output_command += ' -A'
        if values['-SCAN1-'] == 'Operating System':
            output_command += ' -O'
        if values['-SCAN1-'] == 'Firewall Status':
            output_command += ' -sA'
        if values['-SCAN1-'] == 'Services':
            output_command += ' -sV'
        if values['-SCAN1-'] == 'Stealth':
            output_command += ' -sS'
        if values['-SCAN1-'] == 'Device Discovery':
            output_command += ' -sn'
        if values['-SCAN1-'] == 'Vulscan(CVE finder)':
            output_command += ' -sV --script ' + "'" + main_path + "'" + '/scipag_vulscan/vulscan.nse'
        if values['-PORT2-'] == True:
            output_command += ' --top-ports 20'
        if values['-LOG1-'] == True:
            output_command += ' -oN results.txt'
        if values['-PORT2-'] == False:
            if values['-PORT1-'] != "":
                output_command += ' -p ' + values['-PORT1-']
        # elif values['-PORT1-'] != "":
        # 	output_command += ' -p ' + values['-PORT1-']
        output_command += ' ' + values['-IP1-'] + ' -' + values['-SCAN2-'] + ' --stats-every 5s'
        # window['multi1'].update('')
        print(output_command)
        runCommand(window, output_command)


MAKE_nmapGUI()
