import itertools
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# initialize
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
lower_char= lowercase + chars
char_upper = uppercase + chars
lower_upper_char = lowercase + chars + uppercase
upper_lower_char_number = chars + lowercase + uppercase + Number
Mix = chars + lowercase + uppercase + Number + years


def get():
    MinSize = e1.get()
    if MinSize == 0:
        messagebox.showinfo("error", "Please enter an integer number")
    else:
        MaxSize = e2.get()

    filename = e4.get() + ".txt"
    name = open(filename, 'w')
    count = 0
    combination = e3.get()
    TXT = []
    size = [MinSize, MaxSize + 1]
    for i in size:
        for xs in itertools.product(combination, repeat=i):
            name.write(''.join(xs) + '\n')
            count += 1
    name.close()
    messagebox.showinfo("Finish!", "Finish! Check your file !")


def showMsg():
    messagebox.showinfo('Message', 'You clicked the Submit button!')


if __name__ == '__main__':
    master = tk.Tk()

    tk.Label(master, text="Minimum Length").grid(row=0)
    tk.Label(master, text="Maximum Length").grid(row=1)
    tk.Label(master, text="Style:").grid(row=2)
    tk.Label(master, text="File Name").grid(row=3)
    e1 = tk.IntVar()
    e1.set("0")
    MIN = tk.Entry(master, textvariable=e1, width=20)
    MIN.grid(row=0, column=1)

    e2 = tk.IntVar()
    e2.set("0")
    MAX = tk.Entry(master, textvariable=e2, width=20)
    MAX.grid(row=1, column=1)
    e3 = tk.StringVar()
    e3 = ttk.Combobox(master, textvariable=e3)
    e4 = tk.StringVar()
    e4 = tk.Entry(master, textvariable=e4)

    e3['values'] = ('lowercase',
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
                    'Mix')

    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)

    start = tk.Button(master,
                      text='Start', command=get).grid(row=7,
                                                      column=0,
                                                      sticky=tk.W,
                                                      pady=4)

    tk.Button(master,
              text='Quit', command=master.destroy).grid(row=7,
                                                        column=1,
                                                        sticky=tk.W,
                                                        pady=4)

    master.mainloop()
