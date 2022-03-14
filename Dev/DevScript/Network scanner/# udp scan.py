# udp scan
def udp_scan(target, ports):
print("udp scan on, %s with ports %s" % (target, ports))
for port in ports:
pkt = sr1(IP(dst=target)/UDP(sport=port, dport=port), timeout=2, verbose=0)
if pkt == None:
print_ports(port, "Open / filtered")
else:
if pkt.haslayer(ICMP):
print_ports(port, "Closed")
elif pkt.haslayer(UDP)
print_ports(port, "Open / filtered")
else:
print_ports(port, "Unknown")
print(pkt.summary()