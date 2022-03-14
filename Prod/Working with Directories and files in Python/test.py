import os

os.chdir(os.path.abspath(os.path.dirname(__file__))) # This will get current directory of test.py
os.chdir("new") # This will change the current working directory
check = os.getcwd() # This will get the current working directory
print(check)

stream = os.popen("runme.bat") # This will run the program
# stream = os.popen("ping") # This will run a command
output = stream.read() # Read the terminal window
print(output) # This will output a command run through os.popen() using read()

os.chdir("..") # This will go up a folder (../..) = up 2, (../../..) = 3 and so on