#installing library 
pip3 install paramiko
import paramiko

#define as per your local Linux box
#user will need to edit there variables
hostname = "192.168.1.100"
username = "test"
password = "abc123"

#list of commands to execute on the remote machine:

commands = [
    "pwd",
    "id",
    "uname -a",
    "df -h"
]


#Initiating the SSH client and connecting to the server:

# initialize the SSH client
client = paramiko.SSHClient()
# add to known hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=hostname, username=username, password=password)
except:
    print("[!] Cannot connect to the SSH Server")
    exit()

    
# # execute the commands
#    print("="*50, command, "="*50)
#     stdin, stdout, stderr = client.exec_command(command)
#     print(stdout.read().decode())
#     err = stderr.read().decode()
#     if err:
#         print(err)#



#Executing Scripts
cd Desktop
mkdir test_folder
cd test_folder
echo "$PATH" > path.txt

#After the SSH connection, instead of iterating for commands, now we read the content of this script and execute it:
# read the BASH script content from the file
bash_script = open("script.sh").read()
# execute the BASH script
stdin, stdout, stderr = client.exec_command(bash_script)
# read the standard output and print it
print(stdout.read().decode())
# print errors if there are any
err = stderr.read().decode()
if err:
    print(err)

#close the connection
client.close()


# Reference
# https://www.thepythoncode.com/code/executing-bash-commands-remotely-in-python