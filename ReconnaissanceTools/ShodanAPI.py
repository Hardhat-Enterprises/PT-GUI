import os
import shodan
import sys
import tkinter as tk
from nav_bar import *
from tkinter import font as tkfont


class ShodanScript(tk.Frame):
    def __init__(self, parent, controller):
        #drawing frame, etc
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        
        #created title
        tkfont.Font(family='OpenSans', size=13)
        framefont = tkfont.Font(family='Arial Rounded MT Bold', size=28, weight='bold')
        title_label = tk.Label(self, text="Shodan Reconnaissance: Search by IP", bg='white', fg='#92CEFF',
                               anchor="c", font=framefont)
        title_label.place(rely=0.06, relheight=0.12, relwidth=1)

        #creates blue bar as canvas below nav bar
        title_canvas = tk.Canvas(self, bg='#c8e6ff', highlightthickness=0)
        title_canvas.place(rely=0.08, relheight=0.004, relwidth=1)
        display_nav_bar(self, controller)

        #creates blue bar as canvas below title
        title_canvas = tk.Canvas(self, bg='#c8e6ff', highlightthickness=0)
        title_canvas.place(rely=0.155, relheight=0.004, relwidth=1)

        to_api_keys = ttk.Button(self, text="API Key Manager", command = lambda: controller.show_frame("API_Keys"), style = "Accent.TButton")
        to_api_keys.place(rely=0.16, relx=0.08, relheight=0.05, relwidth=0.16)

        to_shodan_main = ttk.Button(self, text="Search by IP", command = lambda: controller.show_frame("ShodanScript"), style = "Rocket.TButton")
        to_shodan_main.place(rely=0.16, relx=0.32, relheight=0.05, relwidth=0.18)

        to_CVE_discovery = ttk.Button(self, text="CVE discovery by IP", command = lambda: controller.show_frame("ShodanCVE"), style = "Accent.TButton")
        to_CVE_discovery.place(rely=0.16, relx=0.50, relheight=0.05, relwidth=0.18)

        to_IP_discovery = ttk.Button(self, text="IP discovery by domain", command = lambda: controller.show_frame("ShodanDomain"), style = "Accent.TButton")
        to_IP_discovery.place(rely=0.16, relx=0.68, relheight=0.05, relwidth=0.18)

        ttk.Label(self, text="Enter Target IP:", style='Dropdown.TButton').place(rely=0.38, relx=0.08, relheight=0.05, relwidth=0.24)
        #entry bar
        self.entry = Entry(self)
        self.entry.place(rely=0.38, relx=0.32, relheight=0.05, relwidth=0.3)
        self.pageNumber = 1

        #default labels for the grid
        a=b=c=d=e=f=g=h=i=j=k=l=m=n=o=p=q=r = ttk.Label(self)
        self.LabelsList = [a,b,c,d,e,f,g,h,i,j,k,k,l,m,n,o,p,q,r]

        #buttons
        ttk.Button(self, text="Start", command=self.ShodanMain, style = "Accent.TButton").place(rely=0.38, relx=0.66, relheight=0.05, relwidth=0.05)
        self.nextButton = ttk.Button(self, text="Next", style="Accent.TButton")
        self.prevButton = ttk.Button(self, text="Previous", style='Accent.TButton')



    def ShodanMain(self):
        #API Key needs to be added to the Environment Variable prior to use.
        api_key = os.environ['SHODAN_API_KEY'] #use API tool to make sure this is findable
        api = shodan.Shodan(api_key)


        #Takes the first argument (IP Address)provided when calling the script.
        #ip_address = sys.argv[1]
        ip_address = self.entry.get()

        try:
            host = api.host(ip_address)

            ttk.Label(self, text=("Organisation: " + str(host['org'])), relief=RAISED, font=tkfont.Font(family="Ariel",size=12), style = "Accent.TButton").place(rely=0.50, relx=0.08, relheight=0.04, relwidth=0.22)
            ttk.Label(self, text=("IP Address: " + str(host['ip_str'])), relief=RAISED, font=tkfont.Font(family="Ariel",size=12), style = "Accent.TButton").place(rely=0.55, relx=0.08, relheight=0.04, relwidth=0.22)
            ttk.Label(self, text=("Country Name: " + str(host['country_name'])), relief=RAISED, font=tkfont.Font(family="Ariel",size=12), style = "Accent.TButton").place(rely=0.60, relx=0.08, relheight=0.04, relwidth=0.22)
            ttk.Label(self, text=("Domains: " + str(host['domains'])), relief=RAISED, font=tkfont.Font(family="Ariel",size=12), style = "Accent.TButton").place(rely=0.65, relx=0.08, relheight=0.04, relwidth=0.22)
            ttk.Label(self, text=("Host Name: " + str(host['hostnames'])), relief=RAISED, font=tkfont.Font(family="Ariel",size=12), style = "Accent.TButton").place(rely=0.70, relx=0.08, relheight=0.04, relwidth=0.22)
            ttk.Label(self, text=("Operating System: " + str(host.get('os','n/a'))), relief=RAISED, font=tkfont.Font(family="Ariel",size=12), style = "Accent.TButton").place(rely=0.75, relx=0.08, relheight=0.04, relwidth=0.22)
            self.ShodanShowpage(host)

        except Exception as e:
            print('Error: {}'.format(e))

    #increases/decreases page and re-draws some elements
    def ShodanIncpage(self, host):
        self.pageNumber = self.pageNumber + 1
        self.ShodanShowpage(host)

    def ShodanDecpage(self, host):
        self.pageNumber = self.pageNumber - 1
        self.ShodanShowpage(host)

    def ShodanShowpage(self, host):
        #cleaning up all the old labels
        for label in self.LabelsList: 
            label.place_forget()
        self.nextButton.place_forget()
        self.prevButton.place_forget()

        #these values change as we iterate through items, placing each label in a grid.
        flexy = 0.50        
        flexx = 0.32        
        idx = 0             #this is the index of the label in the grid, 0-17 (for 18 positions)
        count = 0           #this is used to count the total number of items gotten from host
    
        for item in host ['data']:
            #if the host items are within the range for the current page... and while not too many labels are placed for a page
            #places labels in a grid 6x3 in column order
            if ((count >= (self.pageNumber - 1)*18) and (flexx <= 0.82) and idx <18):
                self.LabelsList[idx] = ttk.Label(self, text=("""Product: {}\nPort: {}\nTransport: {}""".format(item.get('product'),item['port'],item['transport'])), font = tkfont.Font(family="Ariel",size=12), relief = GROOVE)
                self.LabelsList[idx].place(rely=flexy, relx=flexx, relheight=0.1, relwidth=0.1)
                flexy = flexy+0.1
                if (flexy > 0.7):
                    flexx = flexx + 0.1
                    flexy = 0.5
                idx = idx+1
            count = count+1
        
        #didn't want to import math so: str(int(-(-(len(host ['data'])/18)//1))) is the string of labels/labels per page rounded up 1 integer
        #displays the page #/#
        ttk.Label(self, text=("Page " + str(self.pageNumber) + " of " + str(int(-(-(len(host ['data'])/18)//1))) )).place(rely=0.82, relx=0.32, relheight=0.03, relwidth=0.1)
        
        #if labels go far enough right, AND the total number of labels is greater than the number of pages * labels per page
        #shows the next button and lets it traverse page
        if ((flexx >= 0.82) and (len(host ['data']) > (self.pageNumber * 18))):
            #go to next page
            self.nextButton.configure(text = "Next", command=lambda : self.ShodanIncpage(host))
            self.nextButton.place(rely=0.81, relx=0.52, relheight=0.04, relwidth=0.1)

        #if we're on the first page, we don't want to be able to "previous"
        #shows the prev button and lets it traverse page
        if (self.pageNumber > 1):
            self.prevButton.configure(text = "Previous", command=lambda : self.ShodanDecpage(host))
            self.prevButton.place(rely=0.81, relx=0.42, relheight=0.04, relwidth=0.1)
        ttk.Label(self, text=("Last Shodan Scan: " + str(host['last_update']))).place(rely=0.88, relx=0.08, relheight=0.05, relwidth=0.54)
