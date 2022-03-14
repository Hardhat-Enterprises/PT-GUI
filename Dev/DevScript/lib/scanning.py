#!/usr/bin/python
# -*- coding: utf-8 -*-

# A function to call a function based on the user's input
def scanSwitcher(i):
	if i == 1:
		print('Starting SYN scan...')
	elif i == 2:
		print('Starting XMAS scan...')
	else:
		scan_choice = input('ERROR: Invalid option chosen. Please choose another: ')
		scanSwitcher(scan_choice)
		

# A function to determine what scan the user wants to undertake
def scanning():
	print("\nScan types: \n")
	
	scan_options = ["SYN Scan", "XMAS Scan"]
	
	# Print the strings from the scan_options list to the user with a corresponding number
	for idx, val in enumerate(scan_options):
		print("{}. {}".format(idx+1, val))
		
	# Get user input as category_choice	
	scan_choice = input ("\nOption: ")
	
	# Call categorySwitcher to act upon user input
	scanSwitcher(scan_choice)
	
