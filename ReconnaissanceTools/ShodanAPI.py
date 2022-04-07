import os
import shodan
import sys
import tkinter as tk
from nav_bar import *


class ShodanScript(tk.Frame):
    def __init__(self, parent, controller):
        ##drawing frame, etc
        tk.Frame.__init__(self, parent)
        self.controller = controller
        display_nav_bar(self, controller)
        
        shodanframe = tk.Label(self, text="Shodan Reconnaissance", bg='#3B5262', fg='white', anchor="c")
        shodanframe.place(rely=0.08, relheight=0.12, relwidth=1)

        allscreenframe = tk.Label(self, bg='white')
        allscreenframe.place(rely=0.2, relheight=1, relwidth=1)


        Label(self, text="Enter Target IP Address:", bg='#4D6C84', fg='white', anchor='c').place(rely=0.38, relx=0.08, relheight=0.08, relwidth=0.24)
        
        ##entry bar
        self.entry = Entry(self)
        self.entry.place(rely=0.38, relx=0.32, relheight=0.08, relwidth=0.3)
        self.pageNumber = 1

        ##default labels for the grid
        a=b=c=d=e=f=g=h=i=j=k=l=m=n=o=p=q=r = Label(self, bg='#4D6C84', fg='white', anchor='c')
        self.LabelsList = [a,b,c,d,e,f,g,h,i,j,k,k,l,m,n,o,p,q,r]

        ##buttons
        Button(self, text="Start", bg='#4D6C84', fg='white', anchor='c', command=self.ShodanMain).place(rely=0.38, relx=0.66, relheight=0.08, relwidth=0.08)
        self.nextButton = Button(self, text="Next", bg='#4D6C84', fg='white', anchor='c')
        self.prevButton = Button(self, text="Previous", bg='#4D6C84', fg='white', anchor='c')



    def ShodanMain(self):

        # API Key needs to be added to the Environment Variable prior to use.
        api_key = os.environ['SHODAN_API_KEY'] #use API tool to make sure this is findable
        api = shodan.Shodan(api_key)


        # Takes the first argument (IP Address)provided when calling the script.
        #ip_address = sys.argv[1]
        ip_address = self.entry.get()

        # Implement a TRY/CATCH to catch any errors that may occur.
        try:
            host = api.host(ip_address)

            Label(self, text=("Organisation:" + str(host['org'])), bg='#4D6C84', fg='white', anchor='c').place(rely=0.50, relx=0.08, relheight=0.05, relwidth=0.22)
            Label(self, text=("IP Address:" + str(host['ip_str'])), bg='#4D6C84', fg='white', anchor='c').place(rely=0.55, relx=0.08, relheight=0.05, relwidth=0.22)
            Label(self, text=("Country Name:" + str(host['country_name'])), bg='#4D6C84', fg='white', anchor='c').place(rely=0.60, relx=0.08, relheight=0.05, relwidth=0.22)
            Label(self, text=("Domains:" + str(host['domains'])), bg='#4D6C84', fg='white', anchor='c').place(rely=0.65, relx=0.08, relheight=0.05, relwidth=0.22)
            Label(self, text=("Host Name:" + str(host['hostnames'])), bg='#4D6C84', fg='white', anchor='c').place(rely=0.70, relx=0.08, relheight=0.05, relwidth=0.22)
            Label(self, text=("Operating System:" + str(host.get('os','n/a'))), bg='#4D6C84', fg='white', anchor='c').place(rely=0.75, relx=0.08, relheight=0.05, relwidth=0.22)
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
            if ((count > (self.pageNumber - 1)*18) and (flexx <= 0.82) and idx <18):
                self.LabelsList[idx] = Label(self, text=("""* Product: {}\n* Port: {}\n* Transport: {}""".format(item.get('product'),item['port'],item['transport'])), bg='#4D6C84', fg='white', anchor='c')
                self.LabelsList[idx].place(rely=flexy, relx=flexx, relheight=0.1, relwidth=0.1)
                flexy = flexy+0.1
                if (flexy > 0.7):
                    flexx = flexx + 0.1
                    flexy = 0.5
                idx = idx+1
            count = count+1
        
        #didn't want to import math so: str(int(-(-(len(host ['data'])/18)//1))) is the string of labels/labels per page rounded up 1 integer
        #displays the page #/#
        Label(self, text=("Page " + str(self.pageNumber) + " of " + str(int(-(-(len(host ['data'])/18)//1))) ), bg='#4D6C84', fg='white', anchor='c').place(rely=0.8, relx=0.32, relheight=0.03, relwidth=0.1)
        
        #if labels go far enough right, AND the total number of labels is greater than the number of pages * labels per page
        #shows the next button and lets it traverse page
        if ((flexx >= 0.82) and (len(host ['data']) > (self.pageNumber * 18))):
            #go to next page
            self.nextButton.configure(command=lambda : self.ShodanIncpage(host))
            self.nextButton.place(rely=0.8, relx=0.52, relheight=0.03, relwidth=0.1)

        #if we're on the first page, we don't want to be able to "previous"
        #shows the prev button and lets it traverse page
        if (self.pageNumber > 1):
            self.prevButton.configure(command=lambda : self.ShodanDecpage(host))
            self.prevButton.place(rely=0.8, relx=0.42, relheight=0.03, relwidth=0.1)
        Label(self, text=("Last Shodan Scan:", host['last_update']), bg='#4D6C84', fg='white', anchor='c').place(rely=0.85, relx=0.08, relheight=0.05, relwidth=0.54)
