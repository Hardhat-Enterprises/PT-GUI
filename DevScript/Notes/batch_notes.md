# Batch Scripting
## What is Batch Scripting?

Batch scripting is done within a text file containing a series of commands to be executed by Command Prompt, also known as CMD. When the batch file is run, CMD reads the file and executes its commands in order of where they are placed.

## Creating a .bat file

In order to create a .bat file all we need to do is open notepad on our desktop. Once we have notepad opened we can put in a variety of different commands. In order for the file to execute in the command line promt we must save the file with a .bat extension rather then .txt. Now we have a new batch script. 

# Basic Commands
These basic commands will allow you to get comfortable with batch scripting and ensuring its used properly. 

### PAUSE
> *pause* 

We use 'pause' at the end of our script. This will allow the script to stop once its executed all the previous commands in the file so we can see the output. If you try to execute following commands without puase down the bottom cmd will close in a short time span and you wont see anything. 

### ECHO
> *echo This is text*

We use 'Echo' to display messages in the command line prompt. This wont do anything but show plain text. 


### ECHO OFF
> *@echo off* 

We use '@echo off' at the start of our script to turn off the file path in the command line. You wouldve seen by now that when we run our .bat file that the file paths are shown. These can get annoying and look messy when our script becomes larger, we can get rid of this by simply entering this command at the start of our script. 

### GOTO
>*@echo off* 

>*:Hello*

>*echo Welcome to batch scripting;*

>*goto Hello*

The 'GOTO'command will jump to a certain part of your script. So for instance if you type "goto Hello"
then it will goto the place that you have typed in ":Hello". Reminder if you want to go to a particular word you must always have a colon (:).

### START
> *start https://www.deakin.edu.au/students*

> *start Visual Studio Code*

> *start Desktop/PythonScripts/python.py*


The start command is straight forward it means you're starting a particular application. You can start a website, you can also add this to file paths and programs installed on your pc.

### SET

> *SET name=Claudia*

> *echo %name%*

When we create a variable creating something that we can use later on in a program, that is stored against a value. In order to derive the variable we must put % before and after. 

### COUNTING

> *@echo off*

> *set /a num=1*

> *:top*

> *set /a num=%num%+1*

> *echo %num%*

> *goto top*

To get the application to think mathmatically it needs to have a /a infront the variable name. Here, the script is setting the variable to 1, navigating to the top and adding one each time

### IF

> @echo off

> *set v1=Hello*

> *set v2=Goodbye*

> *echo Press 1 to say Hello*

> *echo Press 2 to say Goodbye*

> *set /p you=*

> *if %you%==1 echo %v1%*

> *if %you%==2 echo %v2%*

> *pause*

To use the 'if' statement based on user input we also add a /p to when we want the user to add a value. We the use the % again to derive the value from the variable itself. Here we are setting two variables and there associated text, we then set a user input variable. 

### Advanced

For more advanced areas of batch scripting please click [Here](https://www.instructables.com/id/Some-Cool-Batch-Applications/ "Here")

