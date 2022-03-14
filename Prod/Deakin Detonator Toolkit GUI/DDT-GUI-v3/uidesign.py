import tkinter as tk                 
from tkinter import *
from tkinter import font, messagebox
import random, requests, os, sys
import PySimpleGUI as sg 


global background_image1
	
#creating display window and setting title 
root = tk.Tk()
root.title("Deakin Detonator Toolkit")
#getting the width & height of display sscreen
screenwidth= root.winfo_screenwidth() 
screenheight= root.winfo_screenheight()
#setting the size of window
root.geometry("%dx%d" % (screenwidth, screenheight))


#frames for different subscreens
main_frame = tk.Frame(root)
References_frame = tk.Frame(root)
Tools_frame = tk.Frame(root)
AttackVectors_frame = tk.Frame(root)
help2_frame = tk.Frame(root)

#background picture for main screen
background_image1 = tk.PhotoImage(file="ImagesAndIcons/bkg2.PNG")
background_label1 = tk.Label(main_frame, image=background_image1)
background_label1.place(relwidth=1, relheight=1)

#font styling used throughout the UI
highlightFont = font.Font(family='Calibri', name='appHighlightFont', size=18)


#commands for buttons on main screen
def change_to_References():
	main_frame.forget()
	References_frame.pack(fill='both', expand=1)

def change_to_Tools():
	main_frame.forget()
	Tools_frame.pack(fill='both', expand=1)

def change_to_AttackVectors():
	main_frame.forget()
	AttackVectors_frame.pack(fill='both', expand=1)

def change_to_Help():
	main_frame.forget()
	help2_frame.pack(fill='both', expand=1)

def change_to_main():
	main_frame.pack(fill='both', expand=1)
	References_frame.forget()
	Tools_frame.forget()
	AttackVectors_frame.forget()
	help2_frame.forget()

def set_rounded(label, radius):
	label.corner_radius = radius
	objc_util.ObjCInstance(label).clipsToBounds = True


#buttons on the main screen
help2btn = tk.Button(main_frame, text="About", bg="#C1C2C2", fg="black", font=highlightFont, 
	command=change_to_Help, borderwidth=6)
help2btn.place( x = 250, y = 355+90, width=300, height=75)

btn_change_to_Tools = tk.Button(main_frame, text="Tools", bg="#C1C2C2", fg="black", font=highlightFont, 
	command=change_to_Tools, borderwidth=6)
btn_change_to_Tools.place( x = 250, y = 445 + 90, width=300, height=75)

btn_change_to_AttackVectors = tk.Button(main_frame, text="Attack Vectors", bg="#C1C2C2", fg="black", font=highlightFont, 
	command=change_to_AttackVectors, borderwidth=6)
btn_change_to_AttackVectors.place( x = 250, y = 535 + 90, width=300, height=75)

btn_change_to_References = tk.Button(main_frame, text="References", bg="#C1C2C2", fg="black", font=highlightFont, 
	command=change_to_References, borderwidth=6)
btn_change_to_References.place( x = 250, y = 625 + 90, width=300, height=75)



#back to main menu button on each different frame
lbl_heading_References = tk.Label(References_frame, text='').pack(pady=20)

btn_change_to_main = tk.Button(References_frame, text='Back to Main Menu', bg="#1D5F10", fg="white", font=highlightFont, 
	command=change_to_main).place( x = 200, y = 535 + 90, width=300, height=75)

lbl_heading_Tools = tk.Label(Tools_frame, text='This is the Tools window').pack(pady=20)
btn_change_to_main = tk.Button(Tools_frame, text='Back to Main Menu', bg="#1D5F10", fg="white", font=highlightFont, 
	command=change_to_main).place( x = 200, y = 535 + 90, width=300, height=75)

lbl_heading_AttackVectors = tk.Label(AttackVectors_frame, text='This is the Attack Vectors window').pack(pady=20)
btn_change_to_main = tk.Button(AttackVectors_frame, text='Back to Main Menu', bg="#2F4F4F", fg="white", font=highlightFont, 
	command=change_to_main).place( x = 200, y = 535 + 90, width=300, height=75)

btn_change_to_main = tk.Button(help2_frame, text='Back to Main Menu', bg="#1D5F10", fg="white", font=highlightFont, 
	command=change_to_main).place( x = 200, y = 535 + 90, width=300, height=75)



main_frame.pack(fill='both', expand=1)


root.mainloop()