from tkinter import *
import tkinter.messagebox
from socket import *
from threading import Thread, Lock
import sys, re, random, requests, os

import tkinter as tk  # python 3
from tkinter import font as tkfont  # python 3
# import Tkinter as tk     # python 2
# import tkFont as tkfont  # python 2
from tkinter import font as tkfont
from tkinter import font, messagebox
import PySimpleGUI as sg
from nav_bar import *

Port_is_open = ""


class PortScan(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        abtframefont = tkfont.Font(family='Calibri', size=33, weight="bold")
        display_nav_bar(self, controller)
        aboutframe = tk.Label(self, text="    Port Scanner Tool", bg='#3B5262', fg='white', anchor="c",
                              font=abtframefont)
        aboutframe.place(rely=0.08, relheight=0.12, relwidth=1)

        allscreenframe = tk.Label(self, bg='white')
        allscreenframe.place(rely=0.2, relheight=1, relwidth=1)

        # Set input box Entry
        label = Label(self, text="Enter Target IP address:", font=('Calibri', 13), bg='#4D6C84', fg='white',
                      anchor='c').place(rely=0.38, relx=0.16, relheight=0.08, relwidth=0.22)

        self.IP = Entry(self, font=('Calibri', 14))
        self.IP.place(rely=0.38, relx=0.36, relheight=0.08, relwidth=0.3)

        # Set scan button
        Button(self, text="Start Scan", font=('Calibri', 14), bg='#4D6C84', fg='white', anchor='c',
               command=self.Judgment_IP).place(rely=0.38, relx=0.7, relheight=0.08, relwidth=0.08)

    def Judgment_IP(self):
        # Determine whether the input IP format is correct (regular)
        reg = '^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
        ip = re.match(reg, self.IP.get())
        if ip is not None:
            action(ip.group())
            Port_open_result = Label(self, text="Results:\n", font=('Calibri', 14))
            Port_open_result.place(rely=0.48, relx=0.36, relwidth=0.3)
            Port_open_content = Label(self, text=Port_is_open, font=('Calibri', 12))
            Port_open_content.place(rely=0.58, relx=0.36, relwidth=0.3)
        else:
            tkinter.messagebox.showerror('error', 'IP Invalid, Please Enter a Valid IP Address')


class mythread(Thread):
    def __init__(self, fun, args):
        Thread.__init__(self)
        self.fun = fun
        self.args = args

    def run(self):
        self.fun(*self.args)


def action(ip):
    def scan(h, p):
        global Port_is_open
        try:
            tcpCliSock = socket(AF_INET, SOCK_STREAM)
            tcpCliSock.connect((host, p))
            if lock.acquire():
                Port_is_open += "port " + str(p) + " is open\n"
                lock.release()
        except error:
            if lock.acquire():
                # Port_is_open +=""+ str(p) + " -> not open\n"
                lock.release()
        finally:
            tcpCliSock.close()
            del tcpCliSock

    lock = Lock()
    ports = [21, 22, 23, 25, 53, 69, 80, 135, 445, 443, 137, 139, 143, 8080, 1723, 995, 993, 5900, 68, 520, 514, 162,
             49152, 4500, 1521, 1433, 3306, 3389, ]
    host = ip
    mt = []
    for p in ports:
        t = mythread(scan, (host, p))
        mt.append(t)
    for m in mt:
        m.start()
    for m in mt:
        m.join()
#	print(Port_is_open)
