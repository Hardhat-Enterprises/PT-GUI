from tkinter import *
import smtplib


# Function to clear entry fields and textbox.
def clear_click():
    provider_entry.delete(0, END)
    custom_entry.delete(0, END)
    sender_email_entry.delete(0, END)
    sender_pass_entry.delete(0, END)
    receiver_entry.delete(0, END)
    name_entry.delete(0, END)
    subject_entry.delete(0, END)
    message_entry.delete(0, END)
    email_num_entry.delete(0, END)
    textbox.delete('1.0', END)

# Message sending function: Sends email if input is > 1, prints to textbox and disconnects from server.
def run_loop():
    global email_id,rec,msg,n,server,send,process
    if n > 0:
        try:
            server.sendmail(email_id, rec, msg)
            send += 1
            textbox.insert(END,f"Emails sent: {send}\n")
        except Exception as e:
            textbox.insert(END,f"{e}\n")
        n -= 1
        root.after(100, run_loop)
    else:
        s = f"\nEmails sent: {send}\n"
        textbox.insert(END,f"{s}\n")
        process = False
        try:
            server.quit()
            textbox.insert(END,"Quit server successful.\n\n")
        except:
            pass

# Stop mailing function
def stop_bomber():
    global process, n
    if process:
        process = False
        n = 0

# Messaging start function: Checks if input entry is correct, conencts to server and prints to textbox. If incorrect, displays error message.
def start_bomber():
    global server, process
    if process:
        return
    if check_entrys():
        server = smtplib.SMTP(smtp_server, 587)
        server.ehlo()
        server.starttls()
        try:
            server.login(email_id, password)
            textbox.insert(END,"Login successful.\n\n")
        except Exception as e:

            textbox.insert(END,f"{e}\n")
            return
        process = True
        run_loop()

# Function to check input entry fields, if true proceeds with attack, if false displays relevant error message.
def check_entrys():
    global provider,smtp_server,email_id,password,rec,name,subject,body,msg,n,send
    try:
        try:
            provider = int(provider_entry.get())
        except:
            raise ValueError("Provider must be 1, 2, or 3.\n\n")
        if provider > 3 or provider < 1:
            raise ValueError("Provider must be 1, 2, or 3.\n\n")
        if provider == 1:
            smtp_server = "smtp.gmail.com"
        elif provider == 2:
            smtp_server = "smtp.office365"
        else:
            smtp_server = custom_entry.get()
            if not smtp_server:
                raise ValueError("Custom Provider must not not blank.\n\n")
        email_id = sender_email_entry.get()
        if not email_id:
            raise ValueError("Sender's Email cannot be blank.\n\n")
        password = sender_pass_entry.get()
        if not password:
            raise ValueError("Sender's Password cannot be blank.\n\n")
        rec = receiver_entry.get()
        if not rec:
            raise ValueError("Reciever's Email cannot be blank.\n\n")
        name = name_entry.get()
        if not name:
            raise ValueError("Name cannot be blank.\n\n")
        subject = subject_entry.get()
        if not subject:
            raise ValueError("The subject cannot be blank.\n\n")
        body = message_entry.get()
        if not body:
            raise ValueError("The message cannot be blank.\n\n")
        msg = f"From: {name}\nTo: {rec}\nSubject: {subject}\n\n{body}"
        try:
            n = int(email_num_entry.get())
        except:
            raise ValueError("The number of emails to send must be an integer.\n\n")
        if n < 0:
            raise ValueError("The number of emails to send must be an integer.\n\n")
        send = 0
    except Exception as e:
        textbox.insert(END,f"{e}\n")
        return False
    return True

# Boolean variable that indicates whether the mailing process is running or not
process = False

# Global variables
provider = 0
smtp_server = ""
email_id = ""
password = ""
rec = ""
name = ""
subject = ""
body = ""
msg = ""

# Number of emails to be sent
n = 0

# An instance of the SMTP server for sending emails
server = None

# Sent message counter
send = 0


# Root window configuration:
root = Tk()
root.title("Email Bomber")
root.configure(background="#A41720")

# Label settings:
provider_label = Label(root, text="                                         Email Provider:\n(1:Gmail, 2:Outlook/Hotmail, 3:Custom)", bg="#A41720", fg="white")
custom_label = Label(root, text="                       Custom Provider:\n(Leave blank if above is 1 or 2)", bg="#A41720", fg="white")
sender_email_label = Label(root, text="Sender's Email:", bg="#A41720", fg="white")
sender_pass_label = Label(root, text="Sender's Password:", bg="#A41720", fg="white")
receiver_label = Label(root, text="Reciever's Email:", bg="#A41720", fg="white")
name_label = Label(root, text="Enter a name:", bg="#A41720", fg="white")
subject_label = Label(root, text="Enter the subject:", bg="#A41720", fg="white")
message_label = Label(root, text="Enter the message:", bg="#A41720", fg="white")
email_num_label = Label(root, text="Number of emails to send:", bg="#A41720", fg="white")

# User entry settings:
provider_entry = Entry(root, width=35, highlightbackground="#A41720", bg="black", fg="white")
custom_entry = Entry(root, width=35, highlightbackground="#A41720", bg="black", fg="white")
sender_email_entry = Entry(root, width=35, highlightbackground="#A41720", bg="black", fg="white")
sender_pass_entry = Entry(root, width=35, highlightbackground="#A41720", bg="black", fg="white", show='*')
receiver_entry = Entry(root, width=35, highlightbackground="#A41720", bg="black", fg="white")
name_entry = Entry(root, width=35, highlightbackground="#A41720", bg="black", fg="white")
subject_entry = Entry(root, width=35, highlightbackground="#A41720", bg="black", fg="white")
message_entry = Entry(root, width=35, highlightbackground="#A41720", bg="black", fg="white")
email_num_entry = Entry(root, width=35, highlightbackground="#A41720", bg="black", fg="white")

# Label mounting configurations:
provider_label.grid(row=0, sticky=E, column=0)
custom_label.grid(row=1, sticky=E, column=0)
sender_email_label.grid(row=2, sticky=E, column=0)
sender_pass_label.grid(row=3, sticky=E, column=0)
receiver_label.grid(row=4, sticky=E, column=0)
name_label.grid(row=5, sticky=E, column=0)
subject_label.grid(row=6, sticky=E, column=0)
message_label.grid(row=7, sticky=E, column=0)
email_num_label.grid(row=8, sticky=E, column=0)

# Entry mounting configurations:
provider_entry.grid(row=0, sticky=W, column=1)
custom_entry.grid(row=1, sticky=W, column=1)
sender_email_entry.grid(row=2, sticky=W, column=1)
sender_pass_entry.grid(row=3, sticky=W, column=1)
receiver_entry.grid(row=4, sticky=W, column=1)
name_entry.grid(row=5, sticky=W, column=1)
subject_entry.grid(row=6, sticky=W, column=1)
message_entry.grid(row=7, sticky=W, column=1)
email_num_entry.grid(row=8, sticky=W, column=1)

# Bomb Button settings and configurations (executes attack from user input):
bomb_button = Button(root, width=13, text="BOMB!", highlightbackground="#A41720", fg="green",command=start_bomber)
bomb_button.bind("<Button-1>")
bomb_button.grid(padx=80, pady=20, sticky=W, row=9, column=1)

# Textbox window (acts as Terminal emulator window and prints attack details):
textbox = Text(root, width=45, height=25, highlightbackground="black", bg="black", fg="#00FD61")
textbox.grid(padx=1, pady=10, sticky=W, column=1)

# Stop Button settings and configurations (stops attack and exits application):
stop_button = Button(root, width=5, text="Stop", highlightbackground="#A41720", fg="red", command=stop_bomber)
stop_button.grid(pady=10, sticky=W, row=11, column=1)

# Clear Button settings and configurations (clears the user input entry fields):
clear_button = Button(root, width=5, text="Clear", highlightbackground="#A41720", fg="blue", command=clear_click)
clear_button.bind("<Button-1>")
clear_button.grid(padx=90, pady=10, sticky=W, row=11, column=1)

# Quit Button settings and configurations (stops attack and exits application):
quit_button = Button(root, text="Quit", highlightbackground="#A41720", fg="red", command=root.quit)
quit_button.grid(pady=10, sticky=E, row=11, column=2)

root.mainloop()