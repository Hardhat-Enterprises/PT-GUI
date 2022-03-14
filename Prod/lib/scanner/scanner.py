import nmap
import os

#defines nmap for use through the script
nmScan = nmap.PortScanner()

#sets global active hosts lists to allow for the saving of results
activeHostList = []

#scan subnet - made by Tim
def scanNetwork(returnToMemu):
    #imports activeHostList
    global activeHostList
    #checks list length - runs initial scan if <0 (has not been run yet)
    if len(activeHostList) == 0:
        global activeHostList
        subnetToScan = raw_input("\nEnter first three IP address octets:\n  example: 192.168.0\n    Input: ")+'.0/24'
        print("Scanning "+subnetToScan+"...\n")
        #sends ping to hosts on subnet to see if they are alive
        nmScan.scan(subnetToScan, arguments="-sP --unprivileged")
        #print results and return result to the activeHostList
        for host in nmScan.all_hosts():
             print('Host: ' + host + " is " + nmScan[host].state())
             activeHostList.append(host)
        if returnToMemu == 1:
            menu()
        return(activeHostList)
    #if has been run previously and activeHostList is > 1 then it prints the results of last scan
    else:
        global activeHostList
        print("Previous scan results: ")
        print(20*"=")
        for host in activeHostList:
            print('Host: ' + host + " was up")
        if returnToMemu == 1:
            menu()
        print("To get updated IP's re-run the network scanner")
        return(activeHostList)


#Quick function for setting IP and Port ranges so we arent typing it out in every function - Made by Tim
def ipportdef():
    print("\nDefine the IP and the Port to scan")
    print(30*"=")
    IP = raw_input("Enter the IP to scan: ")
    Ports = raw_input("Enter ports to scan: ")
    print("")
    return IP, Ports

#function for scannign a single target - Made by Tim
def singleScan(flags):
    #set ip and port range
    IP, Ports = ipportdef()
    print("Scanning "+IP+" on ports "+Ports+"...\n")
    #runs scan with flag defined in the menu when called
    nmScan.scan(IP, Ports, arguments=flags)
    for host in nmScan.all_hosts():
        #prints each of the results of the scan
         for proto in nmScan[host].all_protocols():
             print("Ports open for "+IP)
             print(20*'-')
             lport = nmScan[host][proto].keys()
             lport.sort()
             for port in lport:
                 print('port : %s\tstate : %s' % (port, nmScan[host][proto][port]['state']))
             print("")
    menu()

#Function for scanning whole subnet - Made by Tim
def scanAll(flags):
    #imports active hosts
    global activeHostList
    if len(activeHostList) > 0 :
        print("Choose an option: ")
        print(20*"=")
        rescanChoice = int(input("1. Use previous scan\n2. Scan again\nInput: "))
        if rescanChoice == 1:
            IPs = scanNetwork(returnToMemu = 0)
        elif rescanChoice == 2:
            del activeHostList[:]
            IPs = scanNetwork(returnToMemu = 0)
    else:
        IPs = scanNetwork(returnToMemu = 0)
    #sets port range for each hosts
    Ports = raw_input("\nPlease enter port range: ")
    print("")
    for IP in IPs:
        #runs nmap scna for each host in list with specified flags
        nmScan.scan(IP, Ports, arguments=flags)
        for host in nmScan.all_hosts():
            #for each hosts checks for open ports
             for proto in nmScan[host].all_protocols():
                 print(IP)
                 print(10*'-')
                 lport = nmScan[host][proto].keys()
                 lport.sort()
                 for port in lport:
                     print('port : %s\tstate : %s' % (port, nmScan[host][proto][port]['state']))
                 print("")
    menu()

#Detects the os information of ports a single IP - needs to be sped up as its a bit slow atm - Made by Tim
def osdetect():
    print("\nDefine the IP to scan")
    print(30*"=")
    IP = raw_input("Enter the IP to scan: ")
    #predefined port range as most information will be gathered by that point
    Ports = '0-1025'
    nmScan.scan(IP, Ports)
    for host in nmScan[IP]['tcp']:
        thisDict = nmScan[IP]['tcp'][host]
        #prints port -> product info -> version of the product runnign on that port
        print ('Port ' + str(host) + ': ' + thisDict['product'] + ' ' + thisDict['version'])
    menu()

#needs to be faster :/ - Made by Tim
def osdetectAll():
    #imports activeHostList
    global activeHostList
    #checks for rescan
    if len(activeHostList) > 0 :
        print("Choose an option: ")
        print(20*"=")
        rescanChoice = int(input("1. Use previous scan\n2. Scan again\nInput: "))
        if rescanChoice == 1:
            IPs = scanNetwork(returnToMemu = 0)
        elif rescanChoice == 2:
            del activeHostList[:]
            IPs = scanNetwork(returnToMemu = 0)
    else:
        IPs = scanNetwork(returnToMemu = 0)
    Ports = '0-1023'
    print("")
    for IP in IPs:
        nmScan.scan(IP, Ports)
        print("\n"+IP)
        print(10*'-')
        #scans for each IP in the range of active hosts lists
        for host in nmScan[IP]['tcp']:
            thisDict = nmScan[IP]['tcp'][host]
            #prints port -> product info -> version of the product runnign on that port
            print ('Port ' + str(host) + ': ' + thisDict['product'] + ' ' + thisDict['version'])
    menu()

#Menu to make everything work nicely - Made by Tim & Claudia
def menu():
    print (50 * '-')
    print ("   M A I N - M E N U")
    print (50 * '-')
    print ("1. Scan for alive hosts on subnet")
    print ("2. Scan single target")
    print ("3. Scan multiple targets")
    print ("4. Exit scanning")
    print (50 * '-')

    choice = int(raw_input('Enter your choice [1-4]: '))

    if choice == 1:
        os.system('clear')
        global activeHostList
        if len(activeHostList) > 0 :
            print("Choose an option: ")
            print(20*"=")
            rescanChoice = int(input("1. Use previous scan\n2. Scan again\nInput: "))
            if rescanChoice == 1:
                scanNetwork(returnToMemu = 1)
            elif rescanChoice == 2:
                del activeHostList[:]
                scanNetwork(returnToMemu = 1)
        else:
            scanNetwork(returnToMemu = 1)
    elif choice == 2:
        os.system('clear')
        print (50 * '-')
        print ("   S C A N - S I N G L E - T A R G E T")
        print (50 * '-')
        print ("1. SYN Scan (root)")
        print ("2. TCP Scan (user)")
        print ("3. OS & info Scan")
        print ("4. Custom Scan")
        print ("5. Back ")
        print (50 * '-')
        choice = int(raw_input('Enter your choice [1-4]: '))
        if choice == 1:
            singleScan(flags="-sS")
        elif choice == 2:
            singleScan(flags="-sT")
        elif choice == 3:
            osdetect()
        elif choice == 4:
            singleScan(flags=raw_input("Enter custom flags: "))
        elif choice == 5:
            menu()
    elif choice == 3:
        os.system('clear')
        print (50 * '-')
        print ("   S C A N - M U L T I P L E - T A R G E T S")
        print (50 * '-')
        print ("1. SYN Scan (root)")
        print ("2. TCP Scan (user)")
        print ("3. OS & info Scan")
        print ("4. Custom Scan")
        print ("5. Back ")
        print (50 * '-')
        choice = int(raw_input('Enter your choice [1-4]: '))
        if choice == 1:
            scanAll(flags="-sS")
        elif choice == 2:
            scanAll(flags="-sT")
        elif choice == 3:
            osdetectAll()
        elif choice == 4:
            scanAll(flags=raw_input("Enter custom flags: "))
        elif choice == 5:
            menu()
    else:
        print ("Invalid number. Try again...")
os.system('clear')
menu()
