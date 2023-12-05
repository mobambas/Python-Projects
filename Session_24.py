from tkinter import *
from tkinter import messagebox

# Function to display student details
def reprint():
    message = "Hi my name is " + entry_1.get() + ". I live in " + entry_2.get() + "."
    label_3 = Label(root, text=message)
    label_3.grid(row=3, column=3)

root = Tk()
root.title("Student Details")
root.geometry("300x150")

default_city = StringVar()
default_city.set("Singapore")

label_1 = Label(root, text="Name")
label_1.grid(row=0, column=0, pady=5, padx=10, sticky=W)

label_2 = Label(root, text="City")
label_2.grid(row=1, column=0, pady=5, padx=10, sticky=W)

entry_1 = Entry(root)
entry_1.grid(row=0, column=1, pady=5, padx=10, sticky=W)

entry_2 = Entry(root, textvariable=default_city)
entry_2.grid(row=1, column=1, pady=5, padx=10, sticky=W)

button_1 = Button(root, text="Submit", command=reprint)
button_1.grid(row=2, column=0, pady=10, padx=10, sticky=W)

root.mainloop()
