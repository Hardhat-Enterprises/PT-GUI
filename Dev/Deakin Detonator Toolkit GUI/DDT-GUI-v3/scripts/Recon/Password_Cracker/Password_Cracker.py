# This program will allow you to Crack Unix DES hashes
# The current wordlist is only 3 characters as the file
# size of the wordlist outside of this gets vastly larger.
# Hash: Q1Qf.FFnF7dgo is = to Password: L0n + salt: Q1
# You can use functions-online.com/crypt.html to validate this.

import PySimpleGUI as sg
import sys, os

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

def MAKE_Password_Cracker():

    Password_Cracker = os.path.dirname(os.path.realpath(__file__)) # Get the current directory the python file is running from
    os.chdir(Password_Cracker) # Set the working Directory to Password_Cracker

    wordlists = [] # Keeps a list of available wordlists
    for file in os.listdir(): # Looks at all files in the current directory
            if file.endswith(".txt"): # If it ends with .txt
                wordlists.append(file) # Appends it to our list

    layout = [  [sg.Text('Encrypt Password: ', font='Any 36', text_color='#FFFFFF')],
                [sg.Text('Password: ', font='Any 26', text_color='#E0E0E0'), sg.InputText(font='Any 24', text_color='#E0E0E0', key='pass_input', size=(30, 1)),
                sg.Text('Salt: ', font='Any 26', text_color='#E0E0E0'), sg.InputText(font='Any 24', text_color='#E0E0E0', key='salt_input')],
                [sg.Button('Encrypt Password', font='Any 24')],
                [sg.Text(size=(50, 2), key='encrypted_output', font='Any 26', text_color='#E0E0E0')],
                
                [sg.Text('Decrypt Unix Hash: ', font='Any 36', text_color='#FFFFFF')],
                [sg.Text('Choose a Wordlist: ', font='Any 26', text_color='#E0E0E0'), sg.Combo(wordlists, key='wordlist_dropdown', font='Any 14', text_color='#E0E0E0')],
                [sg.Text('Input a Hash (13 Characters): ', font='Any 26', text_color='#E0E0E0'), sg.InputText(font='Any 24', text_color='#E0E0E0', key='hash_input')],
                [sg.Button('Crack Hash', font='Any 24'), sg.Button('Close', font='Any 24', button_color=('#E0E0E0','#9F9FA5'))],
                [sg.Text(size=(50, 2), key='decrypted_output', font='Any 26', text_color='#E0E0E0')] ]

    return sg.Window('Unix DES Password Tools', layout, size=(1280,720), finalize=True)

def CHECK_Password_Cracker(window, event, values):
        if event == sg.WIN_CLOSED or event == 'Close':
            os.chdir("../../..") # Reset the Working Directory back to main.py's folder
            window.close() # Exit
        if event == 'Crack Hash': # If Button Crack Hash is clicked
            try:
                window['hash_input'].update('') # Clear the input
                os.popen('chmod u+x crypto_decrypt') # Make the file executable
                stream = os.popen('./crypto_decrypt ' + values['hash_input'] + ' ' + values['wordlist_dropdown']) # Run the password cracker with the selected wordlist
                output = stream.read() # Read the terminal window
                window['decrypted_output'].update(output) # Read the output
            except:
                print("Password Not found")
        if event == 'Encrypt Password': # If Button Encrypt Password is clicked
            try:
                window['pass_input'].update('') # Clear the input
                window['salt_input'].update('') # Clear the input
                os.popen('chmod u+x crypto_encrypt') # Make the file executable
                stream = os.popen('./crypto_encrypt ' + values['pass_input'] + " " + values['salt_input']) # Run the password cracker
                output = stream.read() # Read the terminal window
                window['encrypted_output'].update(output) # Read the output
            except:
                print("Please input a salt")
