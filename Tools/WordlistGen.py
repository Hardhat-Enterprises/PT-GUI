import itertools
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from tkcalendar import DateEntry

LARGEFONT = ("Verdana", 35)
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Number = '0123456789'
chars = "!,@,#,$,%%,&,*"
years = '1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020'
numfrom = 0
numto = 100
wordlistfrom = 5
wordlistto = 12
__Author__ = 'Steve Tee'
__version__ = '1.0.0'
lower_upper = lowercase + uppercase
lower_number = lowercase + Number
lower_years = lowercase + years
upper_years = uppercase + years
lower_char = lowercase + chars
char_upper = uppercase + chars
lower_upper_char = lowercase + chars + uppercase
upper_lower_char_number = chars + lowercase + uppercase + Number
Mix = chars + lowercase + uppercase + Number + years


class WordlistGen(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Wordlist Generator")
        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        tk.Label(self, text="Wordlist Generator", font=LARGEFONT).grid(row=0, column=2, padx=10, pady=100)

        tk.Button(self, text="User Profile mode",
                  command=lambda: controller.show_frame(Page1)).grid(row=3, column=1, padx=10, pady=10)
        tk.Button(self, text="About",
                  command=About).grid(row=3, column=2, padx=10, pady=10)

        ## button to show frame 2 with text layout2
        tk.Button(self, text="Random mode",
                  command=lambda: controller.show_frame(Page2)).grid(row=3, column=4, padx=10, pady=10)


# second window frame page1
class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # tk.title('Wordlist Generator')
        ttk.Label(self, text="Wordlist", font=LARGEFONT).grid(row=0, column=1, padx=20, pady=100)
        ttk.Label(self, text="Generator", font=LARGEFONT).grid(row=0, column=2, padx=20, pady=100)
        tk.Label(self, text="First Name").grid(row=1, column=1, sticky='W')
        tk.Label(self, text="Surname").grid(row=2, column=1, sticky='W')
        tk.Label(self, text="Nick Name").grid(row=3, column=1, sticky='W')
        tk.Label(self, text="Birthday").grid(row=4, column=1, sticky='W')
        tk.Label(self, text="Add key words").grid(row=5, column=1, sticky='W')

        self.e1 = tk.StringVar()
        self.e1 = ttk.Entry(self, textvariable=self.e1)
        self.e2 = tk.StringVar()
        self.e2 = ttk.Entry(self, textvariable=self.e2)
        self.e3 = tk.StringVar()
        self.e3 = ttk.Entry(self, textvariable=self.e3)
        self.e4 = DateEntry(self, date_pattern='MM/dd/yyyy', foreground="blue")
        self.e5 = tk.StringVar()
        self.e5 = ttk.Entry(self, textvariable=self.e5)
        # yes or no input get
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()

        # Define a Checkbox
        self.e6 = tk.Checkbutton(self, text="Add special chars?", variable=self.var1, onvalue=1, offvalue=0)
        self.e7 = tk.Checkbutton(self, text="Add random number?", variable=self.var2, onvalue=1, offvalue=0)

        self.e1.grid(row=1, column=2, sticky='W')
        self.e2.grid(row=2, column=2, sticky='W')
        self.e3.grid(row=3, column=2, sticky='W')
        self.e4.grid(row=4, column=2, sticky='W')
        self.e5.grid(row=5, column=2, sticky='W')
        self.e6.grid(row=6, column=2, sticky='W')
        self.e7.grid(row=7, column=2, sticky='W')

        tk.Button(self,
                  text=' Start ', command=self.operation).grid(row=8, column=1,

                                                               padx=10, pady=10)
        tk.Button(self,
                  text=' About ', command=AboutButton).grid(row=8, column=2, padx=10, pady=10)

        # label = ttk.Label(self, text="Page 1", font=LARGEFONT)
        # label.grid(row=9, column=0, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        tk.Button(self, text="Start Page",
                  command=lambda: controller.show_frame(StartPage)).grid(row=9, column=0, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        tk.Button(self, text="Random mode",
                  command=lambda: controller.show_frame(Page2)).grid(row=9, column=3, padx=10, pady=10)

    def operation(self):
        data = {}

        # The lower() method converts all
        # uppercase characters in a string into lowercase characters and returns it.
        Name = self.e1.get()

        data["name"] = str(Name)

        data["surname"] = self.e2.get()
        data["nickname"] = self.e3.get()

        birthday = self.e4.get()
        data["birthday"] = str(birthday)

        data["words"] = [""]

        words = self.e5.get()

        data["words"] = words.split(",")

        data["spechars1"] = self.var1.get()

        data["randnum"] = self.var2.get()

        generate_wordlist(data)  # generate the wordlist


# third window frame page2
class Page2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ttk.Label(self, text="Wordlist", font=LARGEFONT).grid(row=0, column=1, padx=20, pady=100)
        ttk.Label(self, text="Generator", font=LARGEFONT).grid(row=0, column=2, padx=20, pady=100)
        tk.Label(self, text="Minimum Length").grid(row=1, column=1, sticky=tk.W)
        tk.Label(self, text="Maximum Length").grid(row=2, column=1, sticky=tk.W)
        tk.Label(self, text="Style:").grid(row=3, column=1, sticky=tk.W)
        tk.Label(self, text="File Name").grid(row=4, column=1, sticky=tk.W)
        self.e1 = tk.IntVar()
        self.e1.set("0")
        MIN = tk.Entry(self, textvariable=self.e1, width=20)
        MIN.grid(row=1, column=2, sticky=tk.E)

        self.e2 = tk.IntVar()
        self.e2.set("0")
        MAX = tk.Entry(self, textvariable=self.e2, width=20)
        MAX.grid(row=2, column=2, sticky=tk.E)
        self.e3 = tk.StringVar()
        self.e3 = ttk.Combobox(self, textvariable=self.e3, values=['lowercase',
                                                                   'uppercase',
                                                                   'Number',
                                                                   'lower_upper',
                                                                   'lower_number',
                                                                   'upper_years',
                                                                   'lower_years',
                                                                   'char_upper',
                                                                   'upper_lower_char_number',
                                                                   'lower_char',
                                                                   'lower_upper_char',
                                                                   'Mix'])
        self.e3.current(0)  # index of values for current table
        self.e4 = tk.StringVar()
        self.e4 = tk.Entry(self, textvariable=self.e4)

        self.e3.grid(row=3, column=2, sticky=tk.E)
        self.e4.grid(row=4, column=2, sticky=tk.E)

        tk.Button(self,
                  text='Start', command=self.get).grid(row=7,
                                                       column=1, padx=10, pady=10)
        tk.Button(self,
                  text='About', command=AboutR).grid(row=7,
                                                     column=2, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        tk.Button(self, text="User Profile Mode",
                  command=lambda: controller.show_frame(Page1)).grid(row=8, column=0, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        tk.Button(self, text="Start Page",
                  command=lambda: controller.show_frame(StartPage)).grid(row=8, column=3, padx=10, pady=10)

    def get(self):
        MinSize = self.e1.get()
        if MinSize == 0:
            messagebox.showinfo("error", "Please enter an integer number")

        MaxSize = self.e2.get()
        if MaxSize < MinSize:
            messagebox.showinfo('error', 'Max Size should large than Min size')

        filename = self.e4.get() + ".txt"
        name = open(filename, 'w')
        count = 0
        style = []
        combination = self.e3.get()
        if combination == 'lowercase':
            style = lowercase
        elif combination == 'Number':
            style = Number
        elif combination == 'lower_upper':
            style = lower_upper
        elif combination == 'uppercase':
            style = uppercase
        elif combination == 'lower_number':
            style = lower_number
        elif combination == 'lower_years':
            style = lower_years
        elif combination == 'char_upper':
            style = lower_upper
        elif combination == 'upper_lower_char_number':
            style = upper_lower_char_number
        elif combination == 'lower_char':
            style = lower_char
        elif combination == 'lower_upper_char':
            style = lower_upper_char
        elif combination == 'Mix':
            style = Mix
        elif combination == '':
            messagebox.showinfo("Error!", "you have to be choose something")

        TXT = []
        size = [MinSize, MaxSize]
        for i in size:
            for xs in itertools.product(style, repeat=i):
                name.write(''.join(xs) + '\n')
                count += 1
        name.close()
        messagebox.showinfo("Finish!", "Finish! Check your file !")


def showMsg():
    messagebox.showinfo('Message', 'You clicked the Submit button!')


def About():
    messagebox.showinfo('Author', 'Wordlist Generator made by Steve')
    messagebox.showinfo('About', 'Wordlist Generator provide two mode to generate wordlist')


def AboutR():
    messagebox.showinfo('Notice', 'select the length and style you want, Dont forget to get a file name')


def AboutButton():
    messagebox.showinfo("notice", "Insert the information about your attack target to make a dictionary")


def concats(seq, start, stop):
    for mystr in seq:
        for num in range(start, stop):
            yield mystr + str(num)


# for concatenations...
def combination(seq, start, special=""):
    for mystr in seq:
        for mystr1 in start:
            yield mystr + special + mystr1


def generate_wordlist(data):
    ## generate wordlist from data

    data["spechars"] = []

    if data["spechars1"] == 1:
        for spec1 in chars:
            data["spechars"].append(spec1)
            for spec2 in chars:
                data["spechars"].append(spec1 + spec2)
                for spec3 in chars:
                    data["spechars"].append(spec1 + spec2 + spec3)

    messagebox.showinfo('notice', "[+] Now making a dictionary...")

    # Now me must do some string modifications...

    # Birthdays first

    birthday_yy = data["birthday"][-2:]
    birthday_yyy = data["birthday"][-3:]
    birthday_yyyy = data["birthday"][-4:]
    birthday_xd = data["birthday"][1:2]
    birthday_xm = data["birthday"][3:4]
    birthday_dd = data["birthday"][:2]
    birthday_mm = data["birthday"][2:4]

    # Convert first letters to uppercase...

    nameup = data["name"].title()
    surnameup = data["surname"].title()
    nicknameup = data["nickname"].title()

    wordsup = []
    wordsup = list(map(str.title, data["words"]))

    word = data["words"] + wordsup

    # reverse a name

    # 【：：-1】= 1234 to 4321
    rev_name = data["name"][::-1]
    rev_nameup = nameup[::-1]
    rev_nickname = data["nickname"][::-1]
    rev_nicknameup = nicknameup[::-1]

    reverse = [
        rev_name,
        rev_nameup,
        rev_nickname,
        rev_nicknameup,

    ]
    rev_n = [rev_name, rev_nameup, rev_nickname, rev_nicknameup]

    # Let's do some serious work! This will be a mess of code, but... who cares? :)

    # Birthdays combinations

    bds = [
        birthday_yy,
        birthday_yyy,
        birthday_yyyy,
        birthday_xd,
        birthday_xm,
        birthday_dd,
        birthday_mm,
    ]

    bdss = []

    for bds1 in bds:
        bdss.append(bds1)
        for bds2 in bds:
            if bds.index(bds1) != bds.index(bds2):
                bdss.append(bds1 + bds2)
                for bds3 in bds:
                    if (
                            bds.index(bds1) != bds.index(bds2)
                            and bds.index(bds2) != bds.index(bds3)
                            and bds.index(bds1) != bds.index(bds3)
                    ):
                        bdss.append(bds1 + bds2 + bds3)

    combinations = [
        data["name"],
        data["surname"],
        data["nickname"],
        nameup,
        surnameup,
        nicknameup,
    ]

    combinationsa = []
    for combinations1 in combinations:
        combinationsa.append(combinations1)
        for combinations2 in combinations:
            if combinations.index(combinations1) != combinations.index(combinations2) and combinations.index(
                    combinations1.title()
            ) != combinations.index(combinations2.title()):
                combinationsa.append(combinations1 + combinations2)

    combinationi = {}
    combinationi[1] = list(combination(combinationsa, bdss))
    combinationi[1] += list(combination(combinationsa, bdss, "_"))
    combinationi[2] = list(combination(combinationsa, years))
    combinationi[2] += list(combination(combinationsa, years, "_"))
    combinationi[3] = list(combination(word, bdss))
    combinationi[3] += list(combination(word, bdss, "_"))
    combinationi[4] = list(combination(word, years))
    combinationi[4] += list(combination(word, years, "_"))
    combinationi[5] = [""]
    combinationi[6] = [""]
    combinationi[7] = [""]
    combinationi[8] = [""]
    if data["randnum"] == 1:
        combinationi[5] = list(concats(word, numfrom, numto))
        combinationi[6] = list(concats(combinationsa, numfrom, numto))
        combinationi[7] = list(concats(reverse, numfrom, numto))
    combinationi[9] = list(combination(reverse, years))
    combinationi[9] += list(combination(reverse, years, "_"))
    combinationi[10] = list(combination(rev_n, bdss))
    combinationi[10] += list(combination(rev_n, bdss, "_"))
    combination001 = [""]
    combination002 = [""]
    combination003 = [""]
    if len(data["spechars"]) > 0:
        combination001 = list(combination(combinationsa, data["spechars"]))
        combination002 = list(combination(word, data["spechars"]))
        combination003 = list(combination(reverse, data["spechars"]))

    messagebox.showinfo("notice", "[+] Sorting list and removing duplicates...")

    combination_unique = {}
    for i in range(1, 11):
        combination_unique[i] = list(dict.fromkeys(combinationi[i]).keys())

    combination_unique01 = list(dict.fromkeys(combinationsa).keys())
    combination_unique02 = list(dict.fromkeys(word).keys())
    combination_unique03 = list(dict.fromkeys(combination001).keys())
    combination_unique04 = list(dict.fromkeys(combination002).keys())
    combination_unique05 = list(dict.fromkeys(combination003).keys())

    uniqlist = (
            bdss
            + reverse
            + combination_unique01
            + combination_unique02
            + combination_unique03
    )

    for i in range(1, 10):
        uniqlist += combination_unique[i]

    uniqlist += (
            combination_unique04
            + combination_unique03
            + combination_unique05

    )
    unique_lista = list(dict.fromkeys(uniqlist).keys())

    unique_list = unique_lista

    unique_list_finished = []
    unique_list_finished = [
        x
        for x in unique_list
        if len(x) < wordlistto and len(x) > wordlistfrom
    ]

    print_to_file(data["name"] + ".txt", unique_list_finished)


def print_to_file(filename, unique_list_finished):
    f = open(filename, "w")
    unique_list_finished.sort()
    f.write(os.linesep.join(unique_list_finished))
    f.close()
    f = open(filename, "r")
    lines = 0
    for line in f:
        lines += 1
    f.close()
    messagebox.showinfo("notice",
                        "[+] Saving dictionary to"
                        + filename
                        )

    messagebox.showinfo("notice",
                        "Done！Good Luck！"
                        )


# Driver Code
app = WordlistGen()
app.mainloop()
