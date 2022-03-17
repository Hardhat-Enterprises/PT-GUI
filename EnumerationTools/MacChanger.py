import tkinter.messagebox
from socket import *
from threading import Thread, Lock
import sys, re, random, uuid, requests, os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font as tkfont
from tkinter import font as tkfont
from tkinter import font, messagebox
import PySimpleGUI as sg
from nav_bar import *

# !/usr/bin/env/ python
import subprocess
import re

Interfaces = subprocess.getoutput("ls /sys/class/net/").split()
Interfaces.remove('lo')

Vendors = [
    "Acer",
    "Apple",
    "Asus",
    "Dell",
    "HP",
    "Lenovo",
    "MSI",
]


class MacChange(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        abtframefont = tkfont.Font(family='Calibri', size=33, weight="bold")
        display_nav_bar(self, controller)
        aboutframe = tk.Label(self, text="    MAC Changer Tool", bg='#3B5262', fg='white', anchor="c",
                              font=abtframefont)
        aboutframe.place(rely=0.08, relheight=0.12, relwidth=1)

        allscreenframe = tk.Label(self, bg='white')
        allscreenframe.place(rely=0.2, relheight=1, relwidth=1)
        Vendorpick = StringVar()
        # instructions label to avoid confusion
        label = Label(self, text="This tool will need to run on sudo permissions\n"
                                 + "Pick a vendor from the list to change the mac address", bg='white',
                      font=('Calibri', 13), anchor='c').place(rely=0.22, relx=0.36, relheight=0.08, relwidth=0.3)

        # Set Label for vendor
        label = Label(self, text="Choose a vendor from the list", font=('Calibri', 13), bg='white', anchor='c').place(
            rely=0.33, relx=0.359, relheight=0.08)

        # Set drop down box
        label = Label(self, text="Selet your network Interface", font=('Calibri', 13), bg='white', anchor='c').place(
            rely=0.43, relx=0.359, relheight=0.08)

        # Set drop down box for interface Entry
        self.entry = ttk.Combobox(self, font=('Calibri', 20), value=Vendors)
        self.entry.place(rely=0.38, relx=0.36, relheight=0.04, relwidth=0.2)

        self.entry2 = ttk.Combobox(self, font=('Calibri', 20), value=Interfaces)
        self.entry2.place(rely=0.48, relx=0.36, relheight=0.04, relwidth=0.2)

        # Start button
        Button(self, text="Change MAC", font=('Calibri', 13), bg='#4D6C84', fg='white', anchor='c',
               command=self.myMac).place(rely=0.35, relx=0.7, relheight=0.08, relwidth=0.12)

        # revert button
        Button(self, text="Original MAC", font=('Calibri', 13), bg='#4D6C84', fg='white', anchor='c',
               command=self.OriginalMac).place(rely=0.47, relx=0.7, relheight=0.08, relwidth=0.12)

    # This will revert to the original MAC address
    def OriginalMac(self):
        interface = self.entry2.get()
        macchanger_result = StringVar()
        macchanger_result = subprocess.getoutput("macchanger eth0 -s | grep 'Permanent' ")[15:32]
        change_mac(interface, macchanger_result)
        current_mac = get_current_mac(interface)
        if current_mac == macchanger_result:
            # Displaying result for successful mac change
            successresult = Label(self, text="MAC address was succesfuly changed to \n \n" + current_mac,
                                  font=('Calibri', 13))
            successresult.place(rely=0.56, relx=0.36, relheight=0.3, relwidth=0.3)

        else:
            # Displaying result if the new mac input by user is incorrect. Clear error message displayed on screen.
            failresult = Label(self,
                               text="MAC address couldnt be changed\nAccording to standerds MAC should start with and end in even pair",
                               font=('Calibri', 13))
            failresult.place(rely=0.68, relx=0.36, relwidth=0.3)

    # function to start the actual program for Mac Changing
    def myMac(self):

        if (self.entry.get() not in Vendors):
            listfailed = Label(self, text="Please choose a vendor from the list", font=('Calibri', 13))
            listfailed.place(rely=0.68, relx=0.36, relwidth=0.3)

        # getting entries from user and binding it to the variables used in functions.
        VendorMac = self.entry.get()
        VendorPick = VendorMacs(VendorMac)
        interface = self.entry2.get()

        # generate the last 3 bytes of a mac address, the first 3 bytes are fixed from the list
        mac3 = []
        for i in range(1, 4):
            Rand = "".join(random.sample("0123456789abcdef", 2))
            mac3.append(Rand)
        randomMac = ":".join(mac3)
        new_mac = VendorPick + ":" + randomMac

        current_mac = get_current_mac(interface)

        currentmaclabel = Label(self, text="Current Mac: " + str(current_mac), font=('Calibri', 13))
        currentmaclabel.place(rely=0.54, relx=0.36, relwidth=0.3)

        changemaclabel = Label(self, text="Changeing MAC address for " + interface + " to: " + current_mac,
                               font=('Calibri', 13))
        changemaclabel.place(rely=0.60, relx=0.36, relwidth=0.3)

        change_mac(interface, new_mac)
        current_mac = get_current_mac(interface)
        if current_mac == new_mac:
            # Displaying result for successful mac change
            successresult = Label(self, text="MAC address was succesfuly changed to \n \n" + new_mac,
                                  font=('Calibri', 13))
            successresult.place(rely=0.68, relx=0.36, relwidth=0.3)


        else:
            # Displaying result if the new mac input by user is incorrect. Clear error message displayed on screen.
            failresult = Label(self,
                               text="MAC address couldnt be changed\nAccording to standerds MAC should start with and end in even pair",
                               font=('Calibri', 13))
            failresult.place(rely=0.68, relx=0.36, relwidth=0.3)


# Funtion to use OS processes for MAC changing
def change_mac(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def VendorMacs(VendorMac):
    if (VendorMac == 'Acer'):
        return '00:60:67'

    elif (VendorMac == 'Apple'):
        return '00:1e:52'

    elif (VendorMac == 'Asus'):
        return '00:1b:fc'

    elif (VendorMac == 'Dell'):
        return '00:c0:4f'

    elif (VendorMac == 'HP'):
        return '00:01:e6'

    elif (VendorMac == 'Lenovo'):
        return '6c:5f:1c'

    elif (VendorMac == 'MSI'):
        return '00:16:17'


def clear_text():
    text.delete(0, END)


# Function to get the current MAC address of the machine
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode('utf-8')
    mac_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_search_result:
        return mac_search_result.group(0)
    else:
        print("[-] Sorry could not read MAC address.")
