import tkinter as tk

window = tk.Tk()

label = tk.Label(
    text="Hello, Tkinter",
    width=25,
    height=5,
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)
label.pack()
window.mainloop()

#Label	A widget used to display text on the screen
#Button	A button that can contain text and can perform an action when clicked
#Entry	A text entry widget that allows only a single line of text
#Text	A text entry widget that allows multiline text entry
#Frame	A rectangular region used to group related widgets or provide padding between widgets