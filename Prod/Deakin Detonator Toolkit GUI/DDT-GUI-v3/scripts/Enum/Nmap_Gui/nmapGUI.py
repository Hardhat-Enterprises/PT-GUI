import PySimpleGUI as sg
import os
from subprocess import call, Popen, PIPE

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
def MAKE_nmapGUI():
	main_path = os.path.dirname(os.path.realpath(__file__))
	os.chdir(main_path)
	#Obtains the current working directory


	layout = [
		[sg.Text('Enter Scan Information Below', font='Any 36')],
		[sg.Text('Enter IP to scan:', size =(14, 1), font='Any 26'), sg.InputText(font='Any 24', key='-IP1-')],
        [sg.Text('Port (optional):', size =(12, 1), font='Any 26'), sg.InputText(font='Any 24', key='-PORT1-',
		size=(5,1)), sg.CBox('Top 20 ports', font='Any 26', key='-PORT2-')],
		[sg.Text('Scan Type:', size =(12, 1), font='Any 26'), sg.Combo(('All', 'Operating System', 'Firewall Status', 'Services', 'Stealth', 'Device discovery', 'Vulscan(CVE finder)'), default_value='All', font='Any 24',
		key='-SCAN1-')],
		[sg.Text('Speed:', size =(12, 1), font='Any 26'), sg.Combo(('T1', 'T2', 'T3', 'T4', 'T5'), default_value='T3', font='Any 24', key='-SCAN2-'), sg.CBox('Save results', font='Any 26', key='-LOG1-')],
		#[sg.CBox('Vulscan (service scan type only): returns CVEs for detected services', key='-VULSCAN-')],
		[sg.Button('Submit', enable_events=True, font='Any 24', key="-SUBMIT-"), sg.Button('Close', font='Any 24', button_color=('#E0E0E0','#9F9FA5'))],
	    [sg.MLine(default_text='Results: ', disabled=True, write_only=True, autoscroll=True, size=(140, 16), font='Any 18', key='multi1')]]

	return sg.Window('Network Scan', layout, size=(1280, 720), finalize=True)

def runCommand(window, cmd):
    p1 = Popen(cmd, stdout=PIPE, universal_newlines=True, shell = True)
    for line in p1.stdout:
        window['multi1'].print(line, end="")
        window.refresh()

def CHECK_nmapGUI(window, event, values):
    if event == sg.WIN_CLOSED or event == 'Close':
    	os.chdir('../..')
    	window.close()

    if event == '-SUBMIT-':	#Appends nmap commands based on options selected
        main_path = os.path.dirname(os.path.realpath(__file__))
        #get_pass = sg.popup_get_text('Nmap requires root privileges to run, please enter root password: ', 'Sudo permission', password_char='*')
        #Creates a popup window that takes in the root password
        #This will be revised in the next iteration so we won't have to store the root password
        output_command = "nmap" #Initialising the final nmap command

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
        elif values['-PORT1-'] != "":
        	output_command += ' -p ' + values['-PORT1-']
        output_command += ' ' + values['-IP1-'] + ' -' + values['-SCAN2-'] + ' --stats-every 5s'
        #window['multi1'].update('')
        runCommand(window, output_command)
