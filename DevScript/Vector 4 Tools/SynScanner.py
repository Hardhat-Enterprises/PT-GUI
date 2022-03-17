# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 11:18:52 2021

@author: mohit
"""
# port scanner
import argparse
from scapy.all import *

def print_ports(port, state):
	print("%s | %s" % (port, state))

# syn scan
def syn_scan(target, ports):
	print("syn scan on, %s with ports %s" % (target, ports))
	sport = RandShort()
	for port in ports:
		pkt = sr1(IP(dst=target)/TCP(sport=sport, dport=port, flags="S"), timeout=1, verbose=0)
		if pkt != None:
			if pkt.haslayer(TCP):
				if pkt[TCP].flags == 20:
					print_ports(port, "Closed")
				elif pkt[TCP].flags == 18:
					print_ports(port, "Open")
				else:
					print_ports(port, "TCP packet resp / filtered")
			elif pkt.haslayer(ICMP):
				print_ports(port, "ICMP resp / filtered")
			else:
				print_ports(port, "Unknown resp")
				print(pkt.summary())
		else:
			print_ports(port, "Unanswered")
            
            
  # argument
parser = argparse.ArgumentParser("Port scanner using Scapy")
parser.add_argument("-t", "--target", help="Specify target IP", required=True)
parser.add_argument("-p", "--ports", type=int, nargs="+", help="Specify ports (21 23 80 ...)")
parser.add_argument("-s", "--scantype", help="Scan type, syn", required=True)
args = parser.parse_args()

# arg parsing
target = args.target
scantype = args.scantype.lower()
# set ports if passed
if args.ports:
	ports = args.ports
else:
	# default port range
	ports = range(1, 1024)

# scan types
if scantype == "syn" or scantype == "s":
	syn_scan(target, ports)
else:
	print("Scan type not supported")