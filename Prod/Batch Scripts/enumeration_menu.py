# Imports

import os

os.chdir(os.path.abspath(os.path.dirname(__file__))) # This will get current directory of menu.py
#os.chdir("scripts/foldername") # Set the working directory to Enumeration folder

print('Select an Enumeration Tool: (1-2)') # This is just a basic text selection menu
print('1. Netstat')
print('2. Ping')

x = input()

if x == "1":
    stream = os.popen("enumeration_netstat.bat") # This will run the batch file using import os    


elif x == "2":
    stream = os.popen("enumeration_ping.bat")


else:
    print('Invalid Selection')