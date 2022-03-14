# DumpSec Guide


---
## Overview


```
DumpSec is a security auditing program for Windows operating systems. It dumps the permissions and audit settings for the file system, registry, printers and shares in a concise, readable format, so that holes in system security are readily apparent. DumpSec also dumps user, group and replication information.
```

---
## How To Use


```
This DumpSec tool runs off of the Windows command line interface, however for the purpose of our toolkit, will be running from a batch file. The dumpsec.bat file can be run on any Windows operating system up until Windows XP.
```

---
## Basic Command Usage

#### DumpSec.exe /rpt=userscol /saveas=csv /outfile=dumpsec.txt
```
This command will dump all registered users on a Windows machine in a text file.
```

---

## Variables

#### /rpt=
```
dir=drive:\path				Directory permissions report

allsharedirs				All non-special shared directories permissions report

printers					Printers permissions report

Policy						Policy report

rights						Rights report

services					Services report
```

---
## Limitations and Open Issues

#### Limitations
```
This tool can only run on Windows machines, however it is very version specific as it only runs on Windows NT/XP/200x.
```

#### Open Issues
```
It requires the software files to run, so if we were to send it to run on a Windows XP machine, we would need to zip the entire folder and unpack it on the target machine to work.
```
