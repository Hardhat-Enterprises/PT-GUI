#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import libraries
import os
from scanning import *
from exploiting import *

# A function to act based on the user's input
def categorySwitcher(i):
	if i == 1:
		scanning()
	elif i == 2:
		print('enumerating')
	elif i == 3:
		exploiting()
	else:
		category_choice = input('ERROR: Invalid option chosen. Please choose another: ')
		categorySwitcher(category_choice)
		

def main():
	# Clear the terminal
	os.system("clear")
	
	# Print a banner if there is enough room
	print("DDDDDDDDDDDDD      DDDDDDDDDDDDD       TTTTTTTTTTTTTTTTTTTTTTT")
	print("D::::::::::::DDD   D::::::::::::DDD    T:::::::::::::::::::::T")
	print("D:::::::::::::::DD D:::::::::::::::DD  T:::::::::::::::::::::T")
	print("DDD:::::DDDDD:::::DDDD:::::DDDDD:::::D T:::::TT:::::::TT:::::T")
	print("  D:::::D    D:::::D D:::::D    D:::::DTTTTTT  T:::::T  TTTTTT")
	print("  D:::::D     D:::::DD:::::D     D:::::D       T:::::T        ")
	print("  D:::::D     D:::::DD:::::D     D:::::D       T:::::T        ")
	print("  D:::::D     D:::::DD:::::D     D:::::D       T:::::T        ")
	print("  D:::::D     D:::::DD:::::D     D:::::D       T:::::T        ")
	print("  D:::::D     D:::::DD:::::D     D:::::D       T:::::T        ")
	print("  D:::::D     D:::::DD:::::D     D:::::D       T:::::T        ")
	print("  D:::::D    D:::::D D:::::D    D:::::D        T:::::T        ")
	print("DDD:::::DDDDD:::::DDDD:::::DDDDD:::::D       TT:::::::TT      ")
	print("D:::::::::::::::DD D:::::::::::::::DD        T:::::::::T      ")
	print("D::::::::::::DDD   D::::::::::::DDD          T:::::::::T      ")
	print("DDDDDDDDDDDDD      DDDDDDDDDDDDD             TTTTTTTTTTT      ")
	print("")
	print("[      DEAKIN DETONATOR TOOLKIT: NETWORK RECOVERY TOOLS      ]")
	print("")
	                         	
	
	# Create a list of action categories
	categories = ["Scan", "Enumerate", "Exploit"]

	print("What would you like to do?\n")
	
	# Print the strings from the categories list to the user with a corresponding number
	for idx, val in enumerate(categories):
		print("{}. {}".format(idx+1, val))
	
	# Get user input as category_choice	
	category_choice = input ("\nOption: ")
	
	# Call categorySwitcher to act upon user input
	categorySwitcher(category_choice)
	
main()
