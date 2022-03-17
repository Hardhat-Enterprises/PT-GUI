# Netstat Guide


---
## Overview


```
Netstat is a command line network utility tool that displays network connections for Transmission Control Protocol, routing tables and a number of network interface and network protocol statistics. It is used for finding problems in the network and to determine the amount of traffic on the network as a performance measurement.
```

---
## How To Use


```
This Netstat tool runs off of the Windows command line interface, however for the purpose of our toolkit, will be running from a batch file. The netstat.bat file can be run on any Windows operating system.
```

---
## Basic Command Usage

#### netstat
```
This will run the basic function of netstat in the Windows command line.
```

---

## Variables

#### netstat -a
```
This argument displays all active connections and the TCP and UDP ports on which the computer is listening.
```

#### netstat -e
```
This argument displays ethernet statistics, such as the number of bytes and packets sent and recieved.
```

#### netstat -i
```
This argument displays network interfaces and their statistics.
```

#### netstat -n
```
This argument displays active TCP connections, however, addresses and port numbers are expressed numerically and no attempt is made to determine names.
```

#### netstat -r
```
This argument displays the contents of the IP routing table.
```

#### netstat -s
```
This argument displays statistics by protocol. 
```
---
## Limitations and Open Issues

#### Limitations
```
This tool only runs on Windows operating systems. It also only uses the basic netstat command.
```

#### Open Issues
```
Could be updated to allow specific arguments.
```
