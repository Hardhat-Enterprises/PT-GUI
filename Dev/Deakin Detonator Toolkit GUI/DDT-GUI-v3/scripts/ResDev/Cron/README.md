# Cron Guide

---
## Overview

#### How does this tool work?

The Cron Jobber tool creates a GUI for a user to create a Cron Job via use of the Python CronTab module.

A Cron Job allows a user to schedule a command to run at certain intervals.

This program has a learner-friendly *Easy Mode* as well as a *Custom Mode* for custom commands, and a log to store results in. 

---
## How to Use

#### Schedule a job using *Easy Mode*

1. Pick a script from the drop-down list. 
2. Choose the minute interval you wish the script to be run at. 
3. Hit *Add job* to add it to the crontab.

You can then check if the job was added correctly by clicking *See current jobs*.

To view the results, hit *View cronlog*.

#### Schedule a job using *Custom Mode*

Enter a regular Cron Job command and then click *Run*.

You can find how to do this easily by visiting the cron_how_to.txt file, which is located in the same folder as this markdown document. Elsewise, you can hit the How To button from within the program.

Note: When scheduling a custom command, if you want to store results in the log, you must specify this in your command. You can do so by adding the following to your command (and replacing the text in capitals with the real file path):
```
    >> CRONLOG FILE PATH/cronlog.txt
```

---
## Limitations & Open Issues

As the scripts in this toolkit have been changed to functions that the main menu incorporates, they are no longer dedicated scripts. As such, they cannot be scheduled through the crontab. Custom commands still work fine.


```
....·▄▄▄▄..▄▄▄...▄▄▄·.▄.•▄.▪...▐.▄.....·▄▄▄▄..▄▄▄..▄▄▄▄▄.......▐.▄..▄▄▄·.▄▄▄▄▄......▄▄▄......▄▄▄▄▄............▄▄▌..▄.•▄.▪..▄▄▄▄▄....
....██▪.██.▀▄.▀·▐█.▀█.█▌▄▌▪██.•█▌▐█....██▪.██.▀▄.▀·•██..▪.....•█▌▐█▐█.▀█.•██..▪.....▀▄.█·....•██..▪.....▪.....██•..█▌▄▌▪██.•██......
....▐█·.▐█▌▐▀▀▪▄▄█▀▀█.▐▀▀▄·▐█·▐█▐▐▌....▐█·.▐█▌▐▀▀▪▄.▐█.▪.▄█▀▄.▐█▐▐▌▄█▀▀█..▐█.▪.▄█▀▄.▐▀▀▄......▐█.▪.▄█▀▄..▄█▀▄.██▪..▐▀▀▄·▐█·.▐█.▪....
....██..██.▐█▄▄▌▐█.▪▐▌▐█.█▌▐█▌██▐█▌....██..██.▐█▄▄▌.▐█▌·▐█▌.▐▌██▐█▌▐█.▪▐▌.▐█▌·▐█▌.▐▌▐█•█▌.....▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌▐▌▐█.█▌▐█▌.▐█▌·....
....▀▀▀▀▀•..▀▀▀..▀..▀.·▀..▀▀▀▀▀▀.█▪....▀▀▀▀▀•..▀▀▀..▀▀▀..▀█▄▀▪▀▀.█▪.▀..▀..▀▀▀..▀█▄▀▪.▀..▀.....▀▀▀..▀█▄▀▪.▀█▄▀▪.▀▀▀.·▀..▀▀▀▀.▀▀▀.....
```            

