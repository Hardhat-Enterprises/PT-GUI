import tkinter as tk                 
from tkinter import *
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
	global background_image1
	splash_root.destroy()
	


	root = tk.Tk()
	root.title("My Work - Swapping frames")
	root.geometry("730x780+550+80") 


	main_frame = tk.Frame(root)
	enum_frame = tk.Frame(root)
	recon_frame = tk.Frame(root)
	execution_frame = tk.Frame(root)
	initialaccess_frame = tk.Frame(root)
	payload_frame = tk.Frame(root)
	resourcedev_frame = tk.Frame(root)
	help2_frame = tk.Frame(root)


	background_image1 = tk.PhotoImage(file="BkgroundImages/back2.png")
	background_label1 = tk.Label(main_frame, image=background_image1).place(relwidth=1, relheight=1)
	background_label2 = tk.Label(help2_frame, image=background_image1).place(relwidth=1, relheight=1)
	highlightFont = font.Font(family='Arial', name='appHighlightFont', size=14, weight='bold')


	def change_to_Enum():
		main_frame.forget()
		enum_frame.pack(fill='both', expand=1)

	def change_to_Recon():
		main_frame.forget()
		recon_frame.pack(fill='both', expand=1)

	def change_to_Execution():
		main_frame.forget()
		execution_frame.pack(fill='both', expand=1)

	def change_to_InitialAccess():
		main_frame.forget()
		initialaccess_frame.pack(fill='both', expand=1)

	def change_to_Payload():
		main_frame.forget()
		payload_frame.pack(fill='both', expand=1)

	def change_to_ResourceDev():
		main_frame.forget()
		resourcedev_frame.pack(fill='both', expand=1)
	def change_to_Help():
		main_frame.forget()
		help2_frame.pack(fill='both', expand=1)

	def change_to_main():
		main_frame.pack(fill='both', expand=1)
		recon_frame.forget()
		enum_frame.forget()
		initialaccess_frame.forget()
		execution_frame.forget()
		payload_frame.forget()
		resourcedev_frame.forget()
		help2_frame.forget()


	lbl_heading_main = tk.Label(main_frame, text='', bg='white').pack(pady=20)
	btn_change_to_enum = tk.Button(main_frame, text="Enum", bg="#6F0C05", fg="white", font=highlightFont, command=change_to_Enum).place( x = 200, y = 85, width=300, height=75)
	btn_change_to_recon = tk.Button(main_frame, text="Recon", bg="#191970", fg="white", font=highlightFont, command=change_to_Recon).place( x = 200, y = 85 + 90, width=300, height=75)
	btn_change_to_execution = tk.Button(main_frame, text="Execution", bg="#AE0D58", fg="white", font=highlightFont, command=change_to_Execution).place( x = 200, y = 175 + 90, width=300, height=75)
	btn_change_to_initialaccess = tk.Button(main_frame, text="Initial Access", bg="#58085E", fg="white", font=highlightFont, command=change_to_InitialAccess).place( x = 200, y = 265 + 90, width=300, height=75)
	btn_change_to_payload = tk.Button(main_frame, text="Payload", bg="#B01D06", fg="white", font=highlightFont, command=change_to_Payload).place( x = 200, y = 355 + 90, width=300, height=75)
	btn_change_to_resourcedev = tk.Button(main_frame, text="Resource Development", bg="#2F4F4F", fg="white", font=highlightFont, command=change_to_ResourceDev).place( x = 200, y = 445 + 90, width=300, height=75)
	help2btn = tk.Button(main_frame, text="Help", bg="#1D5F10", fg="white", font=highlightFont, command=change_to_Help).place( x = 200, y = 625, width=300, height=75)

	lbl_heading_Enum = tk.Label(enum_frame, text='').pack(pady=20)
	enum_nmapbtn = tk.Button(enum_frame, text='Nmap', bg="#6F0C05", fg="white", font=highlightFont, command=change_to_main).place(x = 200, y = 200, width=300, height=75)
	btn_change_to_main = tk.Button(enum_frame, text='Back to Main Menu', bg="#6F0C05", fg="white", font=highlightFont, command=change_to_main).place( x = 250, y = 535 + 90, width=200, height=60)


	lbl_heading_Recon = tk.Label(recon_frame, text='').pack(pady=20)
	paswdcrackerbtn = tk.Button(recon_frame, text='Password Cracker', bg="#191970", fg="white", font=highlightFont, command=change_to_main).place(x = 200, y = 200, width=300, height=75)
	pldmakerbtn = tk.Button(recon_frame, text='Payload Maker', bg="#191970", fg="white", font=highlightFont, command=change_to_main).place(x = 200, y = 200 + 90, width=300, height=75)
	btn_change_to_main = tk.Button(recon_frame, text='Back to Main Menu', bg="#191970", fg="white", font=highlightFont, command=change_to_main).place( x = 250, y = 535 + 90, width=200, height=60)

	lbl_heading_Execution = tk.Label(execution_frame, text='').pack(pady=20)
	ddt_notepadbtn = tk.Button(execution_frame, text='DDT Notepad', bg="#AE0D58", fg="white", font=highlightFont, command=change_to_main).place(x = 200, y = 200, width=300, height=75)
	btn_change_to_main = tk.Button(execution_frame, text='Back to Main Menu', bg="#AE0D58", fg="white", font=highlightFont, command=change_to_main).place( x = 250, y = 535 + 90, width=200, height=60)

	lbl_heading_InitialAccess = tk.Label(initialaccess_frame, text='').pack(pady=20)
	smbenumbtn = tk.Button(initialaccess_frame, text='SMB ENUM', bg="#58085E", fg="white", font=highlightFont, command=change_to_main).place(x = 200, y = 200, width=300, height=75)
	btn_change_to_main = tk.Button(initialaccess_frame, text='Back to Main Menu', bg="#58085E", fg="white", font=highlightFont, command=change_to_main).place( x = 250, y = 535 + 90, width=200, height=60)

	lbl_heading_Payload = tk.Label(payload_frame, text='This is the Payload window').pack(pady=20)
	btn_change_to_main = tk.Button(payload_frame, text='Back to Main Menu', bg="#B01D06", fg="white", font=highlightFont, command=change_to_main).place( x = 250, y = 535 + 90, width=200, height=60)

	lbl_heading_ResourceDev = tk.Label(resourcedev_frame, text='This is the Resource Development window').pack(pady=20)
	btn_change_to_main = tk.Button(resourcedev_frame, text='Back to Main Menu', bg="#2F4F4F", fg="white", font=highlightFont, command=change_to_main).place( x = 200, y = 535 + 90, width=300, height=75)

	lbl_heading_help2 = tk.Label(help2_frame, text='WHAT IS DDT?', bg="#1D5F10", fg="white", font=('Ariel', 32)).pack(pady=20)
	lbl_heading_help22 = tk.Label(help2_frame, text="\n\n In it's simplest definition, Deakin Detonator Toolkit (DDT) is a penetration testing toolkit.\n\nThe toolkit allows you to make use of a variety of tools, without needing\n the \"know-how\" of each command.\n\n\n\n We have simplified the penetration testing experience for both newcomers who\n are still learning, and those who have been hacking for years. \n\nTo get started, choose a categoery of Tools from the SubMenus\n Then chose a specific tool from the Category.\n\n\n\nHappy hacking!\n\n",
				bg="#1D5F10", fg="white", font=('Ariel', 12)).pack(pady=60)
	btn_change_to_main = tk.Button(help2_frame, text='Back to Main Menu', bg="#1D5F10", fg="white", font=highlightFont, command=change_to_main).place( x = 200, y = 535 + 90, width=300, height=75)

	main_frame.pack(fill='both', expand=1)


#splash screen timer (change timer later)!!!
splash_root.after(7000, main_window)
     
mainloop()