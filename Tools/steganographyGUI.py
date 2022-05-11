from tkinter import *
import cv2
import numpy as np


#Function that converts strings to binary
def data2binary(data):
    if type(data) == str:
        return ''.join([format(ord(i),"08b") for i in data])
    elif type(data) == bytes or type(data) == np.ndarray:
        return [format(i,"08b") for i in data]


#Function that hides the data
def hideData(image, secret_data):
    secret_data += "#####"
    data_index = 0
    binary_data = data2binary(secret_data)
    data_length = len(binary_data)
    for i in range(len(image)):
        for j in range(len(image[i])):
            r,g,b = data2binary(image[i][j])
            if data_index < data_length:
                image[i][j][0] = int(r[:-1] + binary_data[data_index])
                data_index += 1
            if data_index < data_length:
                image[i][j][1] = int(g[:-1] + binary_data[data_index])
                data_index += 1
            if data_index < data_length:
                image[i][j][2] = int(b[:-1] + binary_data[data_index])
                data_index += 1
            if data_index >= data_length:
                return image
    return image
              

#Function to embed text to image file              
def encode_text():
    image_name = load_image_entry.get()
    data = encode_text_entry.get()
    file_name = save_image_entry.get()
    if not (data and image_name and file_name):
        textbox.insert(1.0, 'All entry fields must be filled.\n')
        return
    image = cv2.imread(image_name)
    if image is None:
        textbox.insert(1.0, f'Cannot read the file {image_name}\n')
        return
    encoded_data = hideData(image, data)
    try:
        cv2.imwrite(file_name,encoded_data)
        textbox.insert(1.0, f'Image encoded successfully. {file_name}\n')
    except:
        textbox.insert(1.0, f'Cannot save the file. {file_name}\n')


#Function that shows tha data
def show_data(image):
    binary_data = ""
    for values in image:
        for pixel in values:
            r,g,b = data2binary(pixel)
            binary_data += r[-1]
            binary_data += g[-1]
            binary_data += b[-1]
    all_bytes = [binary_data[i: i+8] for i in range (0,len(binary_data),8)]
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte,2))
        if decoded_data[-5:] == "#####":
            return decoded_data[:-5]
    return ""
    

#Function to decode embedded text from image (sneds error message if no text is embedded in image file)
def decode_text():
    image_name = decode_image_entry.get()
    if not image_name:
        textbox.insert(1.0, 'Choose file to decode.\n')
        return
    image = cv2.imread(image_name)
    if image is not None:
        textbox.insert(1.0, f'\n')
        text = show_data(image)
        if text:
            textbox.insert(1.0, f'Decoded text: {text}\n')
        else:
            textbox.insert(1.0, f'Decode error: Image does not contain embedded text.\n')

    else:
        textbox.insert(1.0, f'Cannot read file {image_name}\n')


# Function to clear entry fields and textbox.
def clear_click():
    load_image_entry.delete(0, END)
    encode_text_entry.delete(0, END)
    save_image_entry.delete(0, END)
    decode_image_entry.delete(0, END)
    textbox.delete('1.0', END)


# Root window configuration:
root = Tk()
root.title("Steganography Tool")
root.configure(background="#301934")


# Encode button settings and configurations (cmbeds text to image file):
encode_button = Button(root, width=13, text="Encode", highlightbackground="#301934", fg="green", command=encode_text)
encode_button.bind("<Button-1>")


# Decode button settings and configurations (extracts text from encoded image):
decode_button = Button(root, width=13, text="Decode", highlightbackground="#301934", fg="green",command=decode_text)
decode_button.bind("<Button-1>")


# Textbox window (acts as Terminal emulator window and prints attack details):
textbox = Text(root, width=45, height=25, highlightbackground="black", bg="black", fg="#00FD61")


# Clear Button settings and configurations (clears the user input entry fields):
clear_button = Button(root, width=5, text="Clear", highlightbackground="#301934", fg="blue", command=clear_click)
clear_button.bind("<Button-1>")


# Quit Button settings and configurations (stops attack and exits application):
quit_button = Button(root, text="Quit", highlightbackground="#301934", fg="red", command=root.quit)


# Label settings:
load_image_label = Label(root, text="Load Image to Encode:", bg="#301934", fg="white")
encode_text_label = Label(root, text="Enter Text to Encode:", bg="#301934", fg="white")
save_image_label = Label(root, text="Save Image As:", bg="#301934", fg="white")
decode_image_label = Label(root, text="Load Image to Decode:", bg="#301934", fg="white")


# User entry settings:
load_image_entry = Entry(root, width=35, highlightbackground="#301934", bg="black", fg="white")
encode_text_entry = Entry(root, width=35, highlightbackground="#301934", bg="black", fg="white")
save_image_entry = Entry(root, width=35, highlightbackground="#301934", bg="black", fg="white")
decode_image_entry = Entry(root, width=35, highlightbackground="#301934", bg="black", fg="white")


# Label mounting configurations:
load_image_label.grid(row=1, sticky=E, column=0, padx=10, pady=5)
encode_text_label.grid(row=2, sticky=E, column=0, padx=10, pady=5)
save_image_label.grid(row=3, sticky=E, column=0, padx=10, pady=5)
encode_button.grid(row=4, sticky=E, column=1, padx=10, pady=15)
decode_image_label.grid(row=5, sticky=E, column=0, padx=10, pady=5)
decode_button.grid(row=6, sticky=E, column=1, padx=10, pady=15)


# Entry mounting configurations:
load_image_entry.grid(row=1, sticky=W, column=1, padx=10, pady=5)
encode_text_entry.grid(row=2, sticky=W, column=1, padx=10, pady=5)
save_image_entry.grid(row=3, sticky=W, column=1, padx=10, pady=5)
decode_image_entry.grid(row=5, sticky=W, column=1, padx=10, pady=5)
textbox.grid(row=7, sticky=W, column=1, padx=10, pady=5)
clear_button.grid(sticky=W, row=8, column=1, padx=10, pady=5)
quit_button.grid(sticky=E, row=8, column=1, padx=10, pady=5)


root.mainloop()