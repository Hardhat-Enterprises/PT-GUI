import tkinter as tk  # python 3
from tkinter import *
# import Tkinter as tk     # python 2
# import tkFont as tkfont  # python 2
from tkinter import font as tkfont

from nav_bar import *


class IMDExtractor(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        abtframefont = tkfont.Font(family='Calibri', size=33, weight="bold")
        display_nav_bar(self, controller)
        aboutframe = tk.Label(self, text="    Image MetaData Extractor", bg='#3B5262', fg='white', anchor="c",
                              font=abtframefont)
        aboutframe.place(rely=0.08, relheight=0.12, relwidth=1)

        allscreenframe = tk.Label(self, bg='white')
        allscreenframe.place(rely=0.2, relheight=1, relwidth=1)

        # Set input box Entry
        label = Label(self, text="Please paste the image location", font=('Calibri', 13), bg='#4D6C84', fg='white',
                      anchor='c').place(rely=0.38, relx=0.16, relheight=0.08, relwidth=0.22)

        self.img = Entry(self, font=('Calibri', 13), )
        self.img.place(rely=0.38, relx=0.36, relheight=0.08, relwidth=0.3)

        # Set scan button
        Button(self, text="Extract", font=('Calibri', 13), bg='#4D6C84', fg='white', anchor='c',
               command=self.myIMDE).place(rely=0.38, relx=0.7, relheight=0.08, relwidth=0.08)

    def myIMDE(self):
        from PIL import Image
        from PIL.ExifTags import TAGS

        # path to the image or video
        # imagename = sys.argv[1]
        imagename = self.img.get()

        if not imagename:
            label = Label(self, text="No Image Path Given.", font=('Calibri', 13), anchor='c').place(rely=0.48,
                                                                                                     relx=0.36,
                                                                                                     relheight=0.08,
                                                                                                     relwidth=0.3)


        else:

            allscreen = tk.Label(self, bg='#E3E4E5')
            allscreen.place(rely=0.48, relx=0.36, relheight=0.5, relwidth=0.3)

            sbb = Scrollbar(allscreen)
            sbb.pack(side=RIGHT, fill=Y)

            # read the image data using PIL
            image = Image.open(imagename)

            # extract EXIF data
            exifdata = image.getexif()

            mylist = Listbox(allscreen, yscrollcommand=sbb.set)

            # iterating over all EXIF data fields
            for tag_id in exifdata:
                # get the tag name, instead of human unreadable tag id
                tag = TAGS.get(tag_id, tag_id)
                data = exifdata.get(tag_id)
                # decode bytes
                if isinstance(data, bytes):
                    data = data.decode()

                mylist.insert(END, (f"{tag:25}: {data}"))

            mylist.pack(fill='both', expand=True)
            sbb.config(command=mylist.yview)
