# Window Creator Guide

<img src="https://img.shields.io/badge/language-python-brightgreen?logo=python&style=for-the-badge"/>

---
## Overview

#### Window Creator

The Window Creator (temporary name) is a program made in an attempt to combine the layout of the PySimpleGUI elements used in the other tools in one single class.

This is important so that the other tools do not implement differing layouts and instead simply import the class of this program and use it.

Additionally, this program as of T2 2020 has not yet been completed and is open for extension in the upcoming trimesters. Hopefully, it can be implemented as soon as DDT-GUI v4 is developed.

---
## How To Use
Do note that at this stage the program has not yet been tested when implemented by other tools and may cause errors.

#### Import the class
To use the class, you can type in `from WindowCreator import WindowCreator` on the top of your python code.

#### Create a WindowCreator object
After importing the class, make a new WindowCreator object by typing `w1 = new WindowCreator()`.

#### Adding elements to the WindowCreator object
You can then add various PySimpleGUI elements (as defined in the program) to your WindowCreator object.

For example:

`w1.AddText("This is a text")` adds a Text element at the lowest line (end of your list of elements).

`w1.AddButton("Enter", key="-ENTER-", index=0)` adds a Button element to the right of the Text element above.

#### Create the PySimpleGUI window object
Finally, you can create the final window and export it into your main function by typing `window = w1.MakeWindow("Window Title")`.

#### Check for event loop
Afterwards, you can treat the window as a PySimpleGUI window object and create an event loop with:
```
while True:
	event, values = window.read()
	
	if event == sg.WIN_CLOSED:
		break

window.close()
```

---
## Limitations
This program has not yet been tested and is expected to be expanded by T3 2020.