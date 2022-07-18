import os
import shodan
import sys
import tkinter as tk
from nav_bar import *
from tkinter import font as tkfont


class ShodanCVE(tk.Frame):
    def __init__(self, parent, controller):
        #drawing frame, etc
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        #creates title
        tkfont.Font(family='OpenSans', size=13)
        framefont = tkfont.Font(family='Arial Rounded MT Bold', size=28, weight='bold')
        title_label = tk.Label(self, text="Shodan Reconnaissance: CVE discovery by IP", bg='white', fg='#92CEFF',
                               anchor="c", font=framefont)
        title_label.place(rely=0.06, relheight=0.12, relwidth=1)

        #creates blue bar as canvas below nav bar
        title_canvas = tk.Canvas(self, bg='#c8e6ff', highlightthickness=0)
        title_canvas.place(rely=0.08, relheight=0.004, relwidth=1)
        display_nav_bar(self, controller)

        #creates blue bar as canvas below title
        title_canvas = tk.Canvas(self, bg='#c8e6ff', highlightthickness=0)
        title_canvas.place(rely=0.155, relheight=0.004, relwidth=1)

        #buttons to other shodan related places
        to_api_keys = ttk.Button(self, text="API Key Manager", command = lambda: controller.show_frame("API_Keys"), style = "Accent.TButton")
        to_api_keys.place(rely=0.16, relx=0.08, relheight=0.05, relwidth=0.16)

        to_shodan_main = ttk.Button(self, text="Search by IP", command = lambda: controller.show_frame("ShodanScript"), style = "Accent.TButton")
        to_shodan_main.place(rely=0.16, relx=0.32, relheight=0.05, relwidth=0.18)

        to_CVE_discovery = ttk.Button(self, text="CVE discovery by IP", command = lambda: controller.show_frame("ShodanCVE"), style = "Rocket.TButton")
        to_CVE_discovery.place(rely=0.16, relx=0.50, relheight=0.05, relwidth=0.18)

        to_IP_discovery = ttk.Button(self, text="IP discovery by domain", command = lambda: controller.show_frame("ShodanDomain"), style = "Accent.TButton")
        to_IP_discovery.place(rely=0.16, relx=0.68, relheight=0.05, relwidth=0.18)

        #entry bar
        ttk.Label(self, text="Enter Target IP:", style='Dropdown.TButton').place(rely=0.38, relx=0.08, relheight=0.05, relwidth=0.24)
        self.entry = Entry(self)
        self.entry.place(rely=0.38, relx=0.32, relheight=0.05, relwidth=0.3)
        self.pageNumber = 1

        #default labels for the grid
        a=b=c=d=e=f=g=h=i=j=k=l=m=n=o=p=q=r = ttk.Label(self)
        self.LabelsList = [a,b,c,d,e,f,g,h,i,j,k,k,l,m,n,o,p,q,r]

        self.waitingLabel = ttk.Label(self, text="Shodan API is loading...", relief=FLAT, font=tkfont.Font(family="Ariel",size=9,slant="italic"))

        #class buttons declared
        self.nextButton = ttk.Button(self, text="Next", style="Accent.TButton")
        self.prevButton = ttk.Button(self, text="Previous", style='Accent.TButton')
        ttk.Button(self, text="Start", command=self.ShodanMain, style = "Accent.TButton").place(rely=0.38, relx=0.66, relheight=0.05, relwidth=0.05)

    def ShodanMain(self):
        #this can take a short time to load. sometimes the API gives up. this is possibly due to too many queries in too short a time. if this produces issues, check the terminal.
        self.waitingLabel.configure(text="Shodan API is loading... Please be patient\nCheck the terminal if the program *is* responsive\nShodan API may be unstable")
        self.waitingLabel.place(rely=0.30, relx=0.32, relheight=0.06, relwidth=0.3)

        #API Key needs to be added to the Environment Variable prior to use.
        api_key = os.environ['SHODAN_API_KEY'] #use API tool to make sure this is findable
        api = shodan.Shodan(api_key)

        #Takes the (IP Address) from entry
        ip_address = self.entry.get()

        host = api.host(ip_address)

        ttk.Label(self, text=("Organisation: " + str(host['org'])), relief=RAISED, style = "Accent.TButton").place(rely=0.50, relx=0.08, relheight=0.04, relwidth=0.22)
        ttk.Label(self, text=("IP Address: " + str(host['ip_str'])), relief=RAISED, style = "Accent.TButton").place(rely=0.55, relx=0.08, relheight=0.04, relwidth=0.22)
        ttk.Label(self, text=("Country Name: " + str(host['country_name'])), relief=RAISED, style = "Accent.TButton").place(rely=0.60, relx=0.08, relheight=0.04, relwidth=0.22)
        self.ShodanShowpage(host, api)

    #increases/decreases page and re-draws some elements
    def ShodanIncpage(self, host, api):
        self.pageNumber = self.pageNumber + 1
        self.ShodanShowpage(host, api)

    def ShodanDecpage(self, host, api):
        self.pageNumber = self.pageNumber - 1
        self.ShodanShowpage(host, api)

    def ShodanShowpage(self, host, api):
        #cleaning up all the old labels
        for label in self.LabelsList: 
            label.place_forget()
        self.nextButton.place_forget()
        self.prevButton.place_forget()

        #these values change as we iterate through items, placing each label in a grid.
        flexy = 0.50
        idx = 0             #this is the index of the label in the grid, 0-5 (for 6 positions)
        count = 0           #this is used to count the total number of items gotten from host
        self.update()

        #font and 0.5-relwidth for wrapping 
        halfscreenwidth = (int)((self.winfo_width()/2)-2)
        thisfont = tkfont.Font(family="Ariel",size=9,slant="italic")

        for item in host['vulns']:
            if ((count >= (self.pageNumber - 1)*6) and idx < 6):
                CVE=item.replace('!','')
                exploits = api.exploits.search(CVE)
                self.LabelsList[idx] = ttk.Label(self, text=(str(item)), relief = RAISED)
                self.LabelsList[idx].place(rely=flexy, relx=0.32, relheight=0.10, relwidth=0.12)
                idx=idx+1
                count=count+1

                for item in exploits['matches']:
                    if item.get('cve')[0] == CVE:
                        self.LabelsList[idx] = ttk.Label(self, text=(item.get('description')), font=thisfont, relief = FLAT, wraplength=halfscreenwidth)
                        self.LabelsList[idx].place(rely=flexy, relx=0.44, relheight=0.1, relwidth=0.5)
                #do the desc
            count = count+1
        self.waitingLabel.place_forget()

        #str(int(-(-(len(host ['data'])/18)//1))) is the string of labels/labels per page rounded up 1 integer
        #displays the page #/#
        ttk.Label(self, text=("Page " + str(self.pageNumber) + " of " + str(int(-(-(len(host['data'])/6)//1))) )).place(rely=0.82, relx=0.32, relheight=0.03, relwidth=0.1)
        
        #if labels go far enough down, AND there are the max number of labels per page
        #shows the next button and lets it traverse page
        if ((flexy >= 0.7) and (len(host ['data']) > (self.pageNumber * 6))):
            #go to next page
            self.nextButton.configure(text = "Next", command=lambda : self.ShodanIncpage(host))
            self.nextButton.place(rely=0.81, relx=0.52, relheight=0.04, relwidth=0.1)

        #if we're on the first page, we don't want to be able to "previous"
        #shows the prev button and lets it traverse page
        if (self.pageNumber > 1):
            self.prevButton.configure(text = "Previous", command=lambda : self.ShodanDecpage(host))
            self.prevButton.place(rely=0.81, relx=0.42, relheight=0.04, relwidth=0.1)
        ttk.Label(self, text=("Last Shodan Scan: " + str(host['last_update']))).place(rely=0.88, relx=0.08, relheight=0.05, relwidth=0.54)