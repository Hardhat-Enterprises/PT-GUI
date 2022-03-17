import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from tkcalendar import DateEntry

# initialize

chars = "!,@,#,$,%%,&,*"
years = '1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020'
numfrom = 0
numto = 100
wordlistfrom = 5
wordlistto = 12
__Author__ = 'Steve Tee'
__version__ = '1.0.0'


def concats(seq, start, stop):
    for mystr in seq:
        for num in range(start, stop):
            yield mystr + str(num)


# for concatenations...
def combination(seq, start, special=""):
    for mystr in seq:
        for mystr1 in start:
            yield mystr + special + mystr1


def operation():
    data = {}

    # The lower() method converts all
    # uppercase characters in a string into lowercase characters and returns it.
    Name = e1.get()

    data["name"] = str(Name)

    data["surname"] = e2.get()
    data["nickname"] = e3.get()

    birthday = e4.get()
    data["birthday"] = str(birthday)

    data["words"] = [""]

    words = e5.get()

    data["words"] = words.split(",")

    data["spechars1"] = var1.get()

    data["randnum"] = var2.get()

    generate_wordlist(data)  # generate the wordlist


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


def AboutButton():
    messagebox.showinfo("notice", "Insert the information about your attack target to make a dictionary")


if __name__ == '__main__':
    master = tk.Tk()
    master.title('Wordlist Generator')
    master.geometry("550x350")
    frame2 = tk.Frame(master)
    tk.Label(frame2, text="Wordlist Generator", font=("Arial", 25), pady=50).grid(row=0, column=1, sticky='W')
    tk.Label(frame2, text="First Name").grid(row=1, sticky='W')
    tk.Label(frame2, text="Surname").grid(row=2, sticky='W')
    tk.Label(frame2, text="Nick Name").grid(row=3, sticky='W')
    tk.Label(frame2, text="Birthday").grid(row=4, sticky='W')
    tk.Label(frame2, text="Add key words").grid(row=5, sticky='W')

    e1 = tk.StringVar()
    e1 = ttk.Entry(frame2, textvariable=e1)
    e2 = tk.StringVar()
    e2 = ttk.Entry(frame2, textvariable=e2)
    e3 = tk.StringVar()
    e3 = ttk.Entry(frame2, textvariable=e3)
    e4 = DateEntry(frame2, date_pattern='MM/dd/yyyy', foreground="blue")
    e5 = tk.StringVar()
    e5 = ttk.Entry(frame2, textvariable=e5)
    # yes or no input get
    var1 = tk.IntVar()
    var2 = tk.IntVar()

    # Define a Checkbox
    e6 = tk.Checkbutton(frame2, text="Add special chars?", variable=var1, onvalue=1, offvalue=0)
    e7 = tk.Checkbutton(frame2, text="Add random number?", variable=var2, onvalue=1, offvalue=0)

    e1.grid(row=1, column=1, sticky='W')
    e2.grid(row=2, column=1, sticky='W')
    e3.grid(row=3, column=1, sticky='W')
    e4.grid(row=4, column=1, sticky='W')
    e5.grid(row=5, column=1, sticky='W')
    e6.grid(row=6, column=1, sticky='W')
    e7.grid(row=7, column=1, sticky='W')

    start = tk.Button(frame2,
                      text='Start', command=operation).grid(row=8, column=0,
                                                            sticky=tk.W,
                                                            pady=4)
    About = tk.Button(frame2,
                      text='About', command=AboutButton).grid(row=8, column=1,
                                                              sticky=tk.W,
                                                              pady=4)

    tk.Button(frame2,
              text='Quit', command=master.destroy).grid(row=8, column=2,
                                                        sticky=tk.W,
                                                        pady=4)
    frame2.pack()
    master.mainloop()
