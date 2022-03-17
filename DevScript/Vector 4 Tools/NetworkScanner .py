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
            
            # udp scan
def udp_scan(ports, victim):
	print("udp scan on, %s with ports %s" % (victim, ports))
	for port in ports:
		pkt = sr1(IP(dst=victim)/UDP(sport=port, dport=port), timeout=2, verbose=0)
		if pkt == None:
			print_ports(port, "Open / filtered")
		else:
			if pkt.haslayer(ICMP):
				print_ports(port, "Port is Closed")
			elif pkt.haslayer(UDP):
				print_ports(port, "Open / filtered")
			else:
				print_ports(port, "No Response")
				print(pkt.summary())
            # xmas scan
def xmas_scan(victim, ports):
	print("Xmas scan on, %s with ports %s" %(victim, ports))
	sport = RandShort()
	for port in ports:
		pkt = sr1(IP(dst=victim)/TCP(sport=sport, dport=port, flags="FPU"), timeout=1, verbose=0)
		if pkt != None:
			if pkt.haslayer(TCP):
				if pkt[TCP].flags == 20:
					print_ports(port, "Port is Closed")
				else:
					print_ports(port, "TCP flag %s" % pkt[TCP].flag)
			elif pkt.haslayer(ICMP):
				print_ports(port, "ICMP resp / filtered")
			else:
				print_ports(port, "No Response")
				print(pkt.summary())
		else:
			print_ports(port, "Open / filtered")
            
# arguments  in order for the program to sucessfully work
parser = argparse.ArgumentParser("Caution")
parser.add_argument("-s", "--scantype", help="Insert S,U,X ", required=True)
parser.add_argument("-v", "--victim", help="Insert victim IP address", required=True)
parser.add_argument("-p", "--ports", type=int, nargs="+", help="Specify port numbers")
args = parser.parse_args()

# arg parsing
victim = args.victim
scantype = args.scantype.lower()

if args.ports:
	ports = args.ports
else:
	# default port range
	ports = range(1, 1024)

# defining the scan type
if scantype == "syn" or scantype == "s":
	syn_scan(ports, victim)

elif scantype == "udp" or scantype == "u":
	udp_scan(victim, ports)
elif scantype == "xmas" or scantype == "x":
	xmas_scan(victim, ports)
else:
	print("INVALID Scan Type")
    
    
    
    # REFERENCES 
#1) Infosecinstitute (2021) port-scanning-using-scapy , accessed 04 April 2021
#2) Ortega, José Manuel. (2018). Mastering Python for Networking and Security, 2nd edn, Packt


    
    