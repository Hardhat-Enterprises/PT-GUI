# Ping Guide


---
## Overview


```
Ping is a computer network administration software utility used to test the reachability of a host on an Internet Protocol network. It measures the round-trip time from the originating host to a destination computer that are echoed back to the source. It operates by sending Internet Control Message Protocol echo request packets to the target hose and waits for an ICMP echo reply. It reports errors, packet loss and a statistical summary of the results.
```

---
## How To Use


```
This Ping tool runs off of the Windows command line interface, however for the purpose of our toolkit, will be running from a batch file. The ping.bat file can be run on any Windows operating system.
```

---
## Basic Command Usage

#### ping example.com
```
This is the basic syntax of running the ping program.
```

#### ping 8.8.8.8
```
The domain name in the basic ping function can be exchanged for an IP address.
```
---

## Variables

#### ping 5 example.com
```
Adding an interger before the domain name will send that many packets. For this example, 5 packets will be sent.
```

#### ping -t example.com
```
The -t argument before the domain will ping the target until stopped. To stop the program use CTRL+C
```

#### ping -a example.com
```
This argument will resolve addresses to hostnames.
```

#### ping -n example.com
```
This argument will dictate how many echo requests to send.
```

#### ping -l example.com
```
This argument will send the buffer size.
```

#### ping -i example.com
```
This argument will set the time to live for the packets.
```

#### ping -S example.com
```
This argument will source addresses to use.
```

#### ping -c example.com
```
This argument will route compartment identifiers.
```
---
## Limitations and Open Issues

#### Limitations
```
This version of the ping tool will only run on Windows operating systems. It will also just run the basic ping command.
```

#### Open Issues
```
Could be adjusted for argument use or number of pings to perform.
```
