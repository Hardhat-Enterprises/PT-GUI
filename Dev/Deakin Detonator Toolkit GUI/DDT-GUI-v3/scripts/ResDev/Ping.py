import subprocess
import sys
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

def MAKE_Ping():

    sg.theme('DarkMode')
    sg.SetOptions(element_padding=(8,8))
    layout = [  [sg.Text('Target IP: ', font='Any 26', text_color='#E0E0E0'),sg.Input(key='ip',font='Any 24', text_color='#E0E0E0')],
                [sg.Text('Number Of Packets: ', font='Any 26', text_color='#E0E0E0'),sg.Input(key='count',font='Any 24', text_color='#E0E0E0')],
                [sg.Button('Ping', font='Any 24'), sg.Button('Exit', font='Any 24', button_color=('#E0E0E0','#9F9FA5'))],
                [sg.Output(font = 'Any 24', size=(60,15))]]


    window = sg.Window('Ping Tool', layout, size=(1280,720),finalize=True)

    while True:             # Event Loop
        event, values = window.Read()
        # print(event, values)
        if event in (None, 'Exit'):
            break
        elif event == 'Ping':
            cmd=("ping " + values['ip'] + " -c" + values['count'])
            runCommand(cmd, window=window)
    window.Close()


def runCommand(cmd, timeout=None, window=None):

    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ''
    for line in p.stdout:
        line = line.decode(errors='replace' if (sys.version_info) < (3, 5) else 'backslashreplace').rstrip()
        output += line
        print(line)
        window.Refresh() if window else None

    retval = p.wait(timeout)
    return (retval, output)
