import tkinter.messagebox
from socket import *
from threading import Thread,Lock
import sys,re,random, requests, os

import tkinter as tk  # python 3
from tkinter import font  as tkfont  # python 3
# import Tkinter as tk     # python 2
# import tkFont as tkfont  # python 2
from tkinter import font as tkfont
from tkinter import font, messagebox
import PySimpleGUI as sg
from nav_bar import *

class TestSniff(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		abtframefont = tkfont.Font(family='Calibri', size=33, weight="bold")
		display_nav_bar(self, controller)
		aboutframe = tk.Label(self, text="    Packet Sniffing Tool", bg='#3B5262', fg='white', anchor="c", font=abtframefont)
		aboutframe.place(rely=0.08, relheight=0.12, relwidth=1)

		allscreenframe = tk.Label(self, bg='white')
		allscreenframe.place(rely=0.2, relheight=1, relwidth=1)

		# Set input box Entry
		label = Label(self,text =" Enter the interface to sniff packets:",font=('Calibri', 13), bg='#4D6C84', fg='white', anchor='c').place(rely=0.38, relx=0.16, relheight=0.08, relwidth=0.22)

		self.entry = Entry(self, font=('Calibri', 13),)
		self.entry.place(rely=0.38, relx=0.36, relheight=0.08, relwidth=0.3)

		# Start button
		Button(self,text="Start",font=('Calibri', 14), bg='#4D6C84', fg='white',anchor='c',command=self.mysniffer).place(rely=0.48, relx=0.46, relheight=0.08, relwidth=0.08)
		Button(self,text="Stop",font=('Calibri', 14), bg='#4D6C84', fg='white',anchor='c',command=self.stop).place(rely=0.58, relx=0.46, relheight=0.08, relwidth=0.08)


	def mysniffer(self):
		import scapy.all as scapy
		from scapy.layers import http
		import argparse



		def sniffer(interface):
			scapy.sniff(iface = interface, store = False, prn = process_packet)

		def get_url(packet):
			return (packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path).decode('utf-8')

		def process_packet(packet):
			if packet.haslayer(http.HTTPRequest):
				url = get_url(packet)
				print('[+] HTTP Requests/URL Requested -> {}'.format(url), '\n')
				stop1()
		def stop1():
			sys.exit()
			
		interface = self.entry.get()
		sniffer(interface)


            


	def stop(self):
		sys.exit(0)
