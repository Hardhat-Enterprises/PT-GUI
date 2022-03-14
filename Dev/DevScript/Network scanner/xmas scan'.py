def xmas_scan(victim, ports):
	print("Xmas scan on, %s with ports %s" %(victim, ports))
	sport = RandShort()
	for port in ports:
		pkt = sr1(IP(dst=target)/TCP(sport=sport, dport=port, flags="FPU"), timeout=1, verbose=0)
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
parser.add_argument("-s", "--scantype", help="Insert S ", required=True)
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
else:
	print("INVALID Scan Type")
    
    
    
    # REFERENCES 
#1) Infosecinstitute (2021) port-scanning-using-scapy , accessed 04 April 2021
#2) Ortega, José Manuel. (2018). Mastering Python for Networking and Security, 2nd edn, Packt


    
    