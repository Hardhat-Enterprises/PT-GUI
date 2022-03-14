import tkinter as tk

window = tk.Tk()
window.columnconfigure([0,1,2,3,4,5], minsize=250)
window.rowconfigure([0, 1,2,3,4,5], minsize=100)

label1 = tk.Label(text="A", bg="black", fg="white")
label1.grid(row=0, column=0, sticky="n")

label2 = tk.Label(text="B", bg="black", fg="white")
label2.grid(row=1, column=0, sticky="s")

label3 = tk.Label(text="A", bg="black", fg="white")
label3.grid(row=2, column=0, sticky="ne")

label4 = tk.Label(text="B", bg="black", fg="white")
label4.grid(row=3, column=0, sticky="sw")

label5 = tk.Label(text="A", bg="black", fg="white")
label5.grid(row=4, column=0, sticky="ew")

label6 = tk.Label(text="B", bg="black", fg="white")
label6.grid(row=5, column=0, sticky="ns")

label7 = tk.Label(text="B", bg="black", fg="white")
label7.grid(row=6, column=0, sticky="ew")

label8 = tk.Label(text="full", bg="black", fg="white")
label8.grid(row=6, column=0, sticky="nsew")

label9 = tk.Label(text="A", bg="black", fg="white")
label9.grid(row=0, column=0, sticky="n")

label10 = tk.Label(text="B", bg="black", fg="white")
label10.grid(row=0, column=0, sticky="s")

label11 = tk.Label(text="A", bg="black", fg="white")
label11.grid(row=0, column=1, sticky="ne")

label12 = tk.Label(text="B", bg="black", fg="white")
label12.grid(row=0, column=2, sticky="sw")

label13 = tk.Label(text="A", bg="black", fg="white")
label13.grid(row=0, column=3, sticky="ew")

label14 = tk.Label(text="B", bg="black", fg="white")
label14.grid(row=0, column=4, sticky="ns")

label15 = tk.Label(text="B", bg="black", fg="white")
label15.grid(row=0, column=5, sticky="ew")

label16 = tk.Label(text="full", bg="black", fg="white")
label16.grid(row=0, column=6, sticky="nsew")

window.mainloop()
#"n" or "N" to align to the top-center part of the cell
#"e" or "E" to align to the right-center side of the cell
#"s" or "S" to align to the bottom-center part of the cell
#"w" or "W" to align to the left-center side of the cell