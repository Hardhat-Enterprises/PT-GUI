#Use this script prior to launching the 'MsfconsoleListener.py' tool
#to check all libraries are installed and up to date. This script only
#needs to be run once on each machine the 'MsfconsoleListener.py'
#script will be run on.

import os
import time

os.system('sudo apt install python3-pip')
time.sleep(5)
os.system('Y')
time.sleep(35)

os.system('pip3 install pymetasploit3')
time.sleep(10)

os.system('pip3 install -U msgpack')
time.sleep(10)