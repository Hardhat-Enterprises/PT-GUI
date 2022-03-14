# Unix DES Password Toolkit Guide

<img src="https://img.shields.io/badge/language-c-brightgreen?logo=c&style=for-the-badge"/>
<img src="https://img.shields.io/badge/language-python-brightgreen?logo=python&style=for-the-badge"/>

---
## Overview

#### Crypt

Crypt is a tool that allows you to encrypt a password using a DES encryption scheme. It can also attempt to decrypt a hash made from the same scheme using a dictionary attack to attempt to find a hash collision and the associated plain text password.

This tool implements the <a href="https://www.man7.org/linux/man-pages/man3/crypt.3.html">Crypt</a> tool found in Unix systems and is written in C code. With an overlay written in Python using the <a href="https://pypi.org/project/PySimpleGUI/PySimpleGUI"> library</a>. This allows for easy interaction with the Crypt functions.

---
## How To Use

#### To Encrypt
To encrypt a plaintext password simple add it into the top text box, add a salt to the "salt" box and click Encrypt Password. A hash will be generated.

#### To Decrypt
To decrypt a Unix DES Hash, enter the hash into the "Input hash" box, select a wordlist from the drop-down menu and click Crack Hash. If a hash collision is found the program will display it below.

---
## Basic Command Usage

### Crypt
`Crypt` is a tool found in most Unix based systems it allows its user to encrypt a given input.

This is the main line used to accomplish this:
```c
strcpy(crypt_hash, crypt(word_trimmed, salt));
```
strcpy (string copy) copies the output of the crypt function and stores it in the crypt_hash variable.
## Limitations and Open Issues

#### Limitations
In its current state the program is only able to conduct a dictionary attack on a given hash. Further development into a Brute Force attack should be added. 

It is also only capable of conducting an attack on the Unix DES Encryption Scheme, more schemes should be added to make this tool more relevant.

The program needs an import button so wordlists do not need to be dragged into the tool’s directory.

#### Open Issues

None.

```
....·▄▄▄▄..▄▄▄...▄▄▄·.▄.•▄.▪...▐.▄.....·▄▄▄▄..▄▄▄..▄▄▄▄▄.......▐.▄..▄▄▄·.▄▄▄▄▄......▄▄▄......▄▄▄▄▄............▄▄▌..▄.•▄.▪..▄▄▄▄▄....
....██▪.██.▀▄.▀·▐█.▀█.█▌▄▌▪██.•█▌▐█....██▪.██.▀▄.▀·•██..▪.....•█▌▐█▐█.▀█.•██..▪.....▀▄.█·....•██..▪.....▪.....██•..█▌▄▌▪██.•██......
....▐█·.▐█▌▐▀▀▪▄▄█▀▀█.▐▀▀▄·▐█·▐█▐▐▌....▐█·.▐█▌▐▀▀▪▄.▐█.▪.▄█▀▄.▐█▐▐▌▄█▀▀█..▐█.▪.▄█▀▄.▐▀▀▄......▐█.▪.▄█▀▄..▄█▀▄.██▪..▐▀▀▄·▐█·.▐█.▪....
....██..██.▐█▄▄▌▐█.▪▐▌▐█.█▌▐█▌██▐█▌....██..██.▐█▄▄▌.▐█▌·▐█▌.▐▌██▐█▌▐█.▪▐▌.▐█▌·▐█▌.▐▌▐█•█▌.....▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌▐▌▐█.█▌▐█▌.▐█▌·....
....▀▀▀▀▀•..▀▀▀..▀..▀.·▀..▀▀▀▀▀▀.█▪....▀▀▀▀▀•..▀▀▀..▀▀▀..▀█▄▀▪▀▀.█▪.▀..▀..▀▀▀..▀█▄▀▪.▀..▀.....▀▀▀..▀█▄▀▪.▀█▄▀▪.▀▀▀.·▀..▀▀▀▀.▀▀▀.....
```                                                                                                                                 



