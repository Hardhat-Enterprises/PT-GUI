#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
import sys, os
import glob
from crontab import CronTab
import getpass

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

def MAKE_Cron():

    # Layout of the window

    layout = [  [sg.Button('How to use', font='Any 26')], # Give user info on program
                [sg.Button('Easy mode', font='Any 26'), sg.Button('Custom mode', font='Any 26')], # Buttons to choose learner friendly mode or a more advanced mode

                # Learner friendly elements
                [sg.Combo(tools_list_new, size=(20,1), font='Any 26', key='ez1')], # Drop down box to choose script
                [sg.Text('Run job every', font='Any 26', text_color='#E0E0E0', key='ez2'), sg.InputText('*', size=(3,1), font='Any 26', key='ez3'), sg.Text(' minutes', font='Any 26', text_color='#E0E0E0', key='ez4')], # Choose cron minutes
                [sg.Button('Add job', font='Any 26', key='ez5')],

                # Advanced user elements
                [sg.Text('Custom command:', font='Any 26', text_color='#E0E0E0', key='pro1'), sg.InputText('', size=(30,1), font='Any 26', key='pro2', disabled=True), sg.Button('Run', font='Any 26', key='pro3', disabled=True)], 

                [sg.Button('See current jobs', font='Any 26')], # Reads the crontab (crontab -l)
                [sg.Button('Clear all jobs', font='Any 26')], # Clears all jobs from the crontab
                [sg.Button('View cron log', font='Any 26'), sg.Button('Clear the cron log', font='Any 26')], # Reads, clears the cronlog
                [sg.Button('Close', font='Any 26', button_color=('#E0E0E0','#9F9FA5'))]
                ]
 
    return sg.Window('Cron Jobber', layout, size=(1280,720), finalize=True)


def CHECK_Cron(window, event, values):

    # Change file path to Cron folder
    main_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(main_path)

    # Set crontab user automatically
    username = getpass.getuser()
    cron = CronTab(user=username) 

    # Get path of "cronlog" and "how_to" txt files
    fileslist = glob.glob(os.getcwd() + '/*.txt')
    fileslist_new = []
    # Remove spaces, otherwise errors will be thrown
    for i in fileslist: 
        x = i.replace(' ', '\ ')
        fileslist_new.append(x)
    cronlog = ''
    cron_how_to = ''
    for i in fileslist_new:
        if 'cronlog' in i:
            cronlog = i
        elif 'how_to' in i:
            cron_how_to = i

    if event == sg.WIN_CLOSED or event == 'Close': # Checks for user exit
        window.close() # Closes the window if the user has exited the program and stops memory leaks
        os.chdir('../..')
    
    if event == 'How to use': # Show user contents of how_to file
        os.system('cat ' + cron_how_to)

    if event == 'Easy mode': # Enable and disable easy/advanced elements based on event
        window['ez1'].update(disabled=False)
        window['ez3'].update(disabled=False)
        window['ez5'].update(disabled=False)
        window['pro2'].update(disabled=True)
        window['pro3'].update(disabled=True)

    if event == 'Custom mode': # Enable and disable easy/advanced elements based on event
        window['pro2'].update(disabled=False)
        window['pro3'].update(disabled=False)
        window['ez1'].update(disabled=True)
        window['ez3'].update(disabled=True)
        window['ez5'].update(disabled=True)

    if event == 'ez5': # Adding a job via easy mode

        # Get the path of selected script from drop down
        substring = ''
        for i in tools_list2:
            if substring in i:
                select = i

        # Set the command for cron job
        job_str = 'python ' + select + ' >> ' + cronlog
        job = cron.new(command=job_str)

        # Add the recurring minute
        if values['ez3'] == '*':
            job.minute.every(1)
        else:
            minvalue = int(values['ez3'])
            job.minute.every(minvalue)

        cron.write()
        print('\n Job successfully added. \n')

    if event == 'pro3': # Add different values from custom cmd using crontab module

        mins, h, dom, mon, dow, cmd = cmd_strings(values['pro2'])
        job = cron.new(command=cmd)
        job.minute.every(mins)
        job.hour.every(h)
        job.day.every(dom)
        job.month.every(mon)
        job.dow.every(dow)
        cron.write()
        print('\n Job successfully added. \n')

    if event == 'See current jobs': # Show user current jobs up
        os.system('crontab -l')

    if event == 'Clear all jobs': # Clear all jobs in the crontab
        cron.remove_all()
        cron.write()
        print('\n All jobs cleared. \n')

    if event == 'View cron log': # Show user log file
        os.system('cat ' + cronlog)

    if event == 'Clear the cron log': # Clear the log file
        os.system('> ' + cronlog)
        print('\n All logs cleared. \n')

# Change file path to Cron folder
main_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(main_path)

# Create a list of all scripts in folder
os.chdir('scripts')
tools_list = glob.glob(os.getcwd() + '/*.py')
# Remove spaces, otherwise errors will be thrown
tools_list2 = []
for i in tools_list: 
    x = i.replace(' ', '\ ')
    tools_list2.append(x)
# List of shortened script names for drop down
tools_list_new = []
for i in tools_list:
    head, sep, tail = i.partition('Cron/scripts/')
    tools_list_new.append(tail)
os.chdir(main_path)

# Function that receives an input string and returns seperate values for crontab module
def cmd_strings(cmd): 

    cmd_split = cmd.split(' ') # Split the custom command wherever there is a space
    list1 = cmd_split[:5] # Create a list of first 5 elements (minute, hour, etc...)

    # Remove symbols from list1 so that crontab module can use the returned values
    for i, s in enumerate(list1):
        if list1[i] == '*':
            list1[i] = 1
        elif '/' in list1[i]:
            value = list1[i].split('/')
            list1[i] = value[1]

    # Assign values to return later
    m = list1[0]
    h = list1[1]
    dom = list1[2]
    mon = list1[3]
    dow = list1[4]
    
    # Join the remaining values from cmd_split to return a single string as the command
    x = cmd_split[5:]
    custom_cmd = ' '.join(x)

    return m, h, dom, mon, dow, custom_cmd
