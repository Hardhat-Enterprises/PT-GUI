from tkinter import *
import tkinter as tk  # python 3
import subprocess as sp
from tkinter import font as tkfont  # python 3
from nav_bar import *

class SystemInfo(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		abtframefont = tkfont.Font(family='Calibri', size=33, weight="bold")
		display_nav_bar(self, controller)
		aboutframe = tk.Label(self, text="    System Information", bg='#64C1DA', anchor="w", font=abtframefont)
		aboutframe.place(rely=0.08, relheight=0.12, relwidth=1)

		allscreenframe = tk.Label(self, bg='white')
		allscreenframe.place(rely=0.2, relheight=1, relwidth=1)

		#Set button to run command.
		Button(self,text="Start Scan",font=('Calibri', 13),anchor='c',command=self.sysinfo).place(rely=0.38, relx=0.7, relheight=0.08, relwidth=0.08)

	def sysinfo(self):
		global terminalOutput
		cmd = "lscpu"
		terminalOutput = sp.Popen(cmd, stdout=sp.PIPE).communicate()[0]
		cmdOutput = Label(self, text=terminalOutput)
		cmdOutput.place(rely=0.48, relx=0.36, relwidth=0.3)