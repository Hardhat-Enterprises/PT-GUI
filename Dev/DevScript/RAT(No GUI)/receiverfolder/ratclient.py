#Imports
import socket
import time
import random

#Variables
host = ""                     #Server IP
port = 80                     #Connection Port

#Functions
def receive(file_data):
    filename = 'recievedcopy'
    file = open(filename, 'a+')
    file.write(file_data)
    file.close()
    print("file has been received successfully")

def send(msg):
    s.send(msg.encode("UTF-8"))

def getInstructions():
    while True:
        msg = s.recv(4096)
        inst = msg.decode("UTF-8")
        print(inst)
        data = inst.split(';')

        #Instructions
        if data[0] == "test":
            try:
                send("This is a test message from the client")
                #print("[OK] we received test")
            except:
                pass
        elif data[0] == "1":
            try:
                #send["[OK] We received the data"]
                receive(data[1])
            except:
                pass
#Connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connected = False
while connected == False:
    try:
        s.connect((host, port))
        connected = True
    except:
        sleepTime = random.randint(20, 30)
        time.sleep(sleepTime)
getInstructions()
