import abc
import argparse
import time
from itertools import count
from socket import ntohs, socket, PF_PACKET, SOCK_RAW
import protocols
pip3 install scapy colorama

from scapy.all import *
from scapy.layers.http import HTTPRequest # import HTTP packet
from colorama import init, Fore
# initialize colorama
init()
# define colors
GREEN = Fore.GREEN
RED   = Fore.RED
RESET = Fore.RESET

        def sniff_packets(iface=None):
    """
    Sniff 80 port packets with `iface`, if None (default), then the
    Scapy's default interface is used
    """
             if iface:
        # port 80 for http (generally)
        # `process_packet` is the callback
             sniff(filter="port 80", prn=process_packet, iface=iface, store=False)
             else:
        # sniff with default interface
            sniff(filter="port 80", prn=process_packet, store=False)



        def process_packet(packet):
    """
    This function is executed whenever a packet is sniffed
    """
    if packet.haslayer(HTTPRequest):
        # if this packet is an HTTP Request
        # get the requested URL
        url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()
        # get the requester's IP Address
        ip = packet[IP].src
        # get the request method
        method = packet[HTTPRequest].Method.decode()
        print(f"\n{GREEN}[+] {ip} Requested {url} with {method}{RESET}")
        if show_raw and packet.haslayer(Raw) and method == "POST":
            # if show_raw flag is enabled, has raw data, and the requested method is "POST"
            # then show raw
            print(f"\n{RED}[*] Some useful Raw data: {packet[Raw].load}{RESET}")

    if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="HTTP Packet Sniffer, this is useful when you're a man in the middle." \
                                                 + "It is suggested that you run arp spoof before you use this script, otherwise it'll sniff your personal packets")
    parser.add_argument("-i", "--iface", help="Interface to use, default is scapy's default interface")
    parser.add_argument("--show-raw", dest="show_raw", action="store_true", help="Whether to print POST raw data, such as passwords, search queries, etc.")
    # parse arguments
    args = parser.parse_args()
    iface = args.iface
    show_raw = args.show_raw
    sniff_packets(iface)

# class PacketSniffer(object):
#     def __init__(self, interface: str):
#         self.interface = interface
#         self.data = None
#         self.protocol_queue = ['Ethernet']
#         self.__observers = list()

#     def register(self, observer):
#         self.__observers.append(observer)

#     def __notify_all(self, *args):
#         for observer in self.__observers:
#             observer.update(*args)
#         del self.protocol_queue[1:]

#     def execute(self):
#         with socket(PF_PACKET, SOCK_RAW, ntohs(0x0003)) as sock:
#             if self.interface is not None:
#                 sock.bind((self.interface, 0))
#             for self.packet_num in count(1):
#                 raw_packet = sock.recv(9000)
#                 start: int = 0
#                 for proto in self.protocol_queue:
#                     proto_class = getattr(protocols, proto)
#                     end: int = start + proto_class.header_len
#                     protocol = proto_class(raw_packet[start:end])
#                     setattr(self, proto.lower(), protocol)
#                     if protocol.encapsulated_proto is None:
#                         break
#                     self.protocol_queue.append(protocol.encapsulated_proto)
#                     start = end
#                 self.data = raw_packet[end:]
#                 self.__notify_all(self)

# class OutputMethod(abc.ABC):
#     """Interface for the implementation of all classes responsible for
#     further processing and/or output of the information gathered by
#     the PacketSniffer class (referenced as 'subject')."""

#     def __init__(self, subject):
#         subject.register(self)

#     @abc.abstractmethod
#     def update(self, *args, **kwargs):
#         pass