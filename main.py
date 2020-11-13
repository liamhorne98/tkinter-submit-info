from tkinter import *
import tkinter
from tkinter import Checkbutton
window= Tk()
window.title("choose name")
window.geometry("500x500")
window.configure(background="grey")
fields={}
#name
name_label = Label(window, text="Name")
name_field = Entry(window)
fields["name"] = name_field

name_label.grid(row=0,column=0)
name_field.grid(row=0,column=1)
#surname
surname_label = Label(window, text="Surname")
surname_field = Entry(window)

surname_label.grid(row=1,column=0)
surname_field.grid(row=1,column=1)
fields["surname"] = surname_field
#email
email_label = Label(window, text="Email")
email_field = Entry(window)

email_label.grid(row=2,column=0)
email_field.grid(row=2,column=1)
fields["email"] = email_field
#cell number
contact_label = Label(window, text="Contact number")
contact_field = Entry(window)

contact_label.grid(row=3,column=0)
contact_field.grid(row=3,column=1)
fields["contact"] = contact_field
#submit
def submit_command():
    output= "User Data:\n"
    for key in fields.keys():
        output += f"{key}:{fields[key].get()}\n"
    print(output)

submit= Button(window,text="submit", command=submit_command)
submit.grid(row=4,column=0)
window.mainloop()