import PySimpleGUI as sg
import sys, os
import time
from subprocess import call, Popen, PIPE

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

def MAKE_Wordlist_Gen():

    layout = [  [sg.Text('Wordlist Generator ', font='Any 36', text_color='#FFFFFF')],
                [sg.Text('This will make a wordlist: ', font='Any 26', text_color='#E0E0E0')],
                [sg.Multiline(autoscroll=True, size=(780, 22), key='output', font='Any 14', reroute_stdout=True)],
                [sg.Button('Run', font='Any 24'), sg.Button('Close', font='Any 24')] ]

    return sg.Window('Wordlist Generator', layout, size=(1280,720), finalize=True)

def CHECK_Wordlist_Gen(window, event, values):
        if event == sg.WIN_CLOSED or event == 'Close':
            Wordlist_Gen = os.path.dirname(os.path.realpath(__file__)) # Set the working Directory to where python file is
            os.chdir(Wordlist_Gen)
            os.chdir("../../") # Reset the Working Directory back to main.py's folder
            window.close()

        if event == 'Run': # If Button Run is clicked
            try:
                Wordlist_Gen = os.path.dirname(os.path.realpath(__file__)) # Set the working Directory to where python file is
                os.chdir(Wordlist_Gen) # ddt.py/scripts/Wordlist_Gen/sherlock/sherlock
                print(os.getcwd())
                os.chdir("sherlock/sherlock/") # Move into sherlock/sherlock
                os.popen('dos2unix generator.sh')
                os.popen('chmod 755 generator.sh')
                os.popen('chmod 755 sherlock.py')
                os.popen('tmux new -s Wordlist')
                call("tmux a -t Wordlist \; detach", shell=True)
                # to avoid conflict, remove existing named pipe and then create named pipe
                call("rm -f /tmp/mypipe && mkfifo /tmp/mypipe && tmux pipe-pane -t Wordlist -o 'cat > /tmp/mypipe'", shell=True)
                # feed the pipe to the stdout and stderr
                proc = Popen(['cat', '/tmp/mypipe'], stdout=PIPE, stderr=PIPE, universal_newlines=True)
                # finally execute the command in tmux session
                Popen(['tmux', 'send-keys', '-t', 'Wordlist.0', '"./generator.sh"', 'C-m'])
                Popen(['tmux', 'send-keys', '-t', 'Wordlist.0', '"Enter"', 'C-m'])
                for line in proc.stdout:
                    window['output'].print(line, end="")
                    window.refresh()
                
            except:
                raise
                print("Something Went Wrong")

