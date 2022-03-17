# RAT Tool Guide
## Overview

Hello and welcome to the Remote Access Trojan server tool user guide. This tool is under a early development stage. The tool only has one function and that is to transfer a file to the victim. Each file that is transferred has to be placed in the folder where the ratserver is before the file can transfer.
The file is then placed in the location of the ratclient.py script


## How To Use
####

To change the file go to the RAT(No GUI) folder, Create a text file, change the name of the file and go to the ratserver.py script in the filename line 30 change the name of the file from the default to the new file.

## Basic Command Usage

#### Command 1
```
To run the script in a locally type "python3 ratserver.py" and
the client is "python3 ratclient.py"
```

#### Command 2
```
type '1' to transfer the file
```

#### Command 3
```
type "test" to check for a connection
```

#### Command 4
```
type "help" for more information
```

## Function

#### Variable 1
```
host "" default is set to the local host,
if attacking a client both host addresses must be set to the attacking PCs IP address
e.g.
ratserver (attacking PC)
host = "192.168.1.101"
ratclient (victim PC)
client = "192.168.1.101"
```
#### Variable 2
```
port 80 is default can use any ports between 1-65535
```
#### Variable 3
```
filename "transferfile.txt" Only text files can be transferred for now.
To change the file you want to send to the client simply change the template in the quotes
```

## Open Issues

#### Issue 1
The test feature to check whether a connection is established is currently having issues whereby the client will crash. Avoid using the test feature for now. (Patched)
