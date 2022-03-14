# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 22:47:55 2021

@author: mohit
"""



from scapy.all import Ether, ARP, srp, sniff, conf
def get_mac(ip):
    p = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip)
    result = srp(p, timeout=3, verbose=False)[0]
    return result[0][1].hwsrc
def process(packet):
    # if the packet is an ARP packet
    if packet.haslayer(ARP):
        # if it is an ARP response (ARP reply)
        if packet[ARP].op == 2:
            try:
                real_mac = get_mac(packet[ARP].psrc)
                # get the MAC address from the packet sent to us
                response_mac = packet[ARP].hwsrc
                if real_mac != response_mac:
                    print(f"[!] You are under attack, REAL-MAC: {real_mac.upper()}, FAKE-MAC: {response_mac.upper()}")
                  
                    except IndexError:
                        # unable to find the real mac
                        # may be a fake IP or firewall is blocking packets
                        pass
                    sniff(store=False, prn=process )