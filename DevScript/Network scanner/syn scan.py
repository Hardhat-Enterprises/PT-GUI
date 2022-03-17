"""
Created on Mon Apr  5 11:18:52 2021

@author: mohit


"""
# port scanner using Scapy in Python programming language
from scapy.all import *
import argparse

def print_ports(state, port):
	print("%s | %s" % (state, port))
    
 #Syn Scan on ICMP 
def syn_scan(ports, victim):
	print("syn scan on, %s with ports %s" % (ports, victim))
	sport = RandShort()
	for port in ports:
		pkt = sr1(TCP(sport=sport, dport=port, flags="S")/IP(dst=victim), timeout=10, verbose=0)
		if pkt != None:
			if pkt.haslayer(TCP):
				if pkt[TCP].flags == 12:
					print_ports(port, "Port is Closed")
				elif pkt[TCP].flags == 30:
					print_ports(port, "Port is Open")
				else:
					print_ports(port, "response from TCP packet / filtered")
			elif pkt.haslayer(ICMP):
				print_ports(port, "response from ICMP")
			else:
				print_ports(port, "No response")
				print(pkt.summary())
		else:
			print_ports(port, "No Response")