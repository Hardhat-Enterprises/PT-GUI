from tkinter import *
import tkinter as tk
from tkinter import font, messagebox
import random, requests, os, sys
import PySimpleGUI as sg


#this is a spalsh screen before the tool opens

splash_root = Tk()
splash_root.title ("Welcome")
splash_root.geometry("1000x750+550+80")

background_image = tk.PhotoImage(file="BkgroundImages/back2.png")
background_label = tk.Label(splash_root, image=background_image).place(relwidth=1, relheight=1)

spalsh_label = Label(splash_root, text= " welcome ", font=("Ariel", 32), bg="black", fg="white").pack(padx=50, pady=50)
spalsh_label2 = Label(splash_root, text= " Deakin Detonator Toolkit is opening... ", font=("Ariel", 18), bg="black", fg="white").pack(padx=50, pady=70)
spalsh_label3 = Label(splash_root, text= " Choose a category of tools from the catalogue, then click a tool to open it. ", font=("Ariel", 18), bg="black", fg="white").pack(padx=20, pady=5)
spalsh_label4 = Label(splash_root, text= " Choose Help for more information on how to use the toolkit. ", font=("Ariel", 18), bg="black", fg="white").pack(padx=50, pady=70)
spalsh_label5 = Label(splash_root, text= " Please Note: This toolkit is intended for educational and research purposes only. ", font=("Ariel", 11), bg="black", fg="white").pack(pady=10)
spalsh_label5 = Label(splash_root, text= " The developers, owners and business correspondants are not responsible for malicious use of the tool. ", font=("Ariel", 11), bg="black", fg="white").pack()
    

def main_window():
	global background_image
	splash_root.destroy()
	
	root = tk.Tk()
	root.title ("Deakin Detonator Toolkit")
	# width x height + x_offset + y_offset:
	root.geometry("750x800+550+80") 


	background_image = tk.PhotoImage(file="BkgroundImages/back2.png")
	background_label = tk.Label(root, image=background_image)
	background_label.place(relwidth=1, relheight=1)

	#this code generates the labels on the screen

	highlightFont = font.Font(family='Arial', name='appHighlightFont', size=14, weight='bold')


	#this code makes a welcome popup


	def clicker():
		global pop
		pop = Toplevel(root)
		pop.title("Welcome")
		pop.geometry("400x300")
		pop.config(bg="White")

	def myHelp():

		sys.path.append('.')
		#sys.path.insert(0, '/Tri1/Deakin Detonator Toolkit GUI/DDT-GUI-v3/scripts/Help/')
		from scripts.Help import About
		#import About
		About.MAKE_About()



	enumbtn = Button(root, text="Enum", bg="#6F0C05", fg="white", font=highlightFont, command=clicker).place( x = 200, y = 85, width=300, height=75)
	reconbtn = Button(root, text="Recon", bg="#191970", fg="white", font=highlightFont, command=clicker).place( x = 200, y = 85 + 90, width=300, height=75)
	exebtn = Button(root, text="Execution", bg="#AE0D58", fg="white", font=highlightFont, command=clicker).place( x = 200, y = 175 + 90, width=300, height=75)
	intaccbtn = Button(root, text="Initial Access", bg="#58085E", fg="white", font=highlightFont, command=clicker).place( x = 200, y = 265 + 90, width=300, height=75)
	pyldbtn = Button(root, text="Payload", bg="#B01D06", fg="white", font=highlightFont, command=clicker).place( x = 200, y = 355 + 90, width=300, height=75)
	resdevbtn = Button(root, text="Resource Development", bg="#2F4F4F", fg="white", font=highlightFont, command=clicker).place( x = 200, y = 445 + 90, width=300, height=75)
	helpbtn = Button(root, text="Help", bg="#1D5F10", fg="white", font=highlightFont, command=myHelp).place( x = 200, y = 535 + 90, width=300, height=75)


#splash screen timer (change timer later)!!!
splash_root.after(1000, main_window)
     
mainloop()