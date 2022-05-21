import os
import shodan
import sys
import tkinter as tk
from nav_bar import *
from tkinter import font as tkfont


class ShodanDomain(tk.Frame):
    def __init__(self, parent, controller):
        #drawing frame, etc
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        #creates title
        tkfont.Font(family='OpenSans', size=13)
        framefont = tkfont.Font(family='Arial Rounded MT Bold', size=28, weight='bold')
        title_label = tk.Label(self, text="Shodan Reconnaissance: IP discovery by Domain", bg='white', fg='#92CEFF',
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

        to_CVE_discovery = ttk.Button(self, text="CVE discovery by IP", command = lambda: controller.show_frame("ShodanCVE"), style = "Accent.TButton")
        to_CVE_discovery.place(rely=0.16, relx=0.50, relheight=0.05, relwidth=0.18)

        to_IP_discovery = ttk.Button(self, text="IP discovery by domain", command = lambda: controller.show_frame("ShodanDomain"), style = "Rocket.TButton")
        to_IP_discovery.place(rely=0.16, relx=0.68, relheight=0.05, relwidth=0.18)


        #entry bar
        ttk.Label(self, text="Enter Target Domain:", style='Dropdown.TButton').place(rely=0.38, relx=0.08, relheight=0.05, relwidth=0.24)
        self.entry = Entry(self)
        self.entry.place(rely=0.38, relx=0.32, relheight=0.05, relwidth=0.3)
        self.pageNumber = 1

        #default labels for the grid
        a=b=c=d=e=f=g=h=i=j = ttk.Label(self)
        self.LabelsList = [a,b,c,d,e,f,g,h,i,j]

        #class buttons declared
        self.nextButton = ttk.Button(self, text="Next", style="Accent.TButton")
        self.prevButton = ttk.Button(self, text="Previous", style='Accent.TButton')
        ttk.Button(self, text="Start", command=self.ShodanMain, style = "Accent.TButton").place(rely=0.38, relx=0.66, relheight=0.05, relwidth=0.05)

    def ShodanMain(self):
        #API Key needs to be added to the Environment Variable prior to use.
        api_key = os.environ['SHODAN_API_KEY'] #use API tool to make sure this is findable
        api = shodan.Shodan(api_key)


        #the domain in entry is searched with shodan
        domain = self.entry.get()
        domainsearch=api.search(domain)

        self.ShodanShowpage(domainsearch, api)


    #increases/decreases page and re-draws some elements
    def ShodanIncpage(self, domainsearch, api):
        self.pageNumber = self.pageNumber + 1
        self.ShodanShowpage(domainsearch, api)

    def ShodanDecpage(self, domainsearch, api):
        self.pageNumber = self.pageNumber - 1
        self.ShodanShowpage(domainsearch, api)

    def ShodanShowpage(self, domainsearch, api):
        #cleaning up all the old labels
        for label in self.LabelsList: 
            label.place_forget()
        self.nextButton.place_forget()
        self.prevButton.place_forget()

        self.LabelsList[9] = ttk.Label(self, text =(str(len(domainsearch['matches'])) + " results found."), relief=FLAT)
        self.LabelsList[9].place(rely=0.45, relx=0.35, relheight=0.05, relwidth=0.3)

        #these values change as we iterate through items, placing each label in a grid.
        flexy = 0.50
        flexx = 0.05        
        idx = 0             #this is the index of the label in the grid, 0-8 (for 9 positions)
        count = 0           #this is used to count the total number of items gotten from domain
        self.update()


        for item in domainsearch['matches']:
            if ((count >= (self.pageNumber - 1)*9) and (flexx <= 0.95) and idx < 9):
                self.LabelsList[idx] = ttk.Label(self, text=('IP Address: {}' .format(item['ip_str'] + "\nLast Scan: " + (domainsearch['matches'][count]['timestamp']))), relief = FLAT)
                self.LabelsList[idx].place(rely=flexy, relx=flexx, relheight=0.10, relwidth=0.30)
                idx=idx+1
                #if a column has reached its capacity, move to the next column
                flexy = flexy+0.1
                if (flexy > 0.7):
                    flexx = flexx + 0.3
                    flexy = 0.5
            count=count+1
        
        #str(int(-(-(len(domain ['data'])/9)//1))) is the string of labels/labels per page rounded up 1 integer...
        #displays the page #/#
        ttk.Label(self, text=("Page " + str(self.pageNumber) + " of " + str(int(-(-(len(domainsearch['matches'])/9)//1))) )).place(rely=0.82, relx=0.32, relheight=0.03, relwidth=0.1)
        
        #if labels go far enough right, AND the max number of labels per page is met
        #shows the next button and lets it traverse page
        if ((flexx >= 0.95) and (len(domainsearch['matches']) > (self.pageNumber * 9))):
            #go to next page
            self.nextButton.configure(text = "Next", command=lambda : self.ShodanIncpage(domainsearch, api))
            self.nextButton.place(rely=0.81, relx=0.52, relheight=0.04, relwidth=0.1)

        #if we're on the first page, we don't want to be able to "previous", otherwise...
        #shows the prev button and lets it traverse page
        if (self.pageNumber > 1):
            self.prevButton.configure(text = "Previous", command=lambda : self.ShodanDecpage(domainsearch, api))
            self.prevButton.place(rely=0.81, relx=0.42, relheight=0.04, relwidth=0.1)