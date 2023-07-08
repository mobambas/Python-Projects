from tkinter import *

root = Tk()
root.title("Listbox")
root.geometry("500x500")

def delete():
    listbox.delete(ANCHOR)
    label.config(text=" ")

label  = Label(root)
label.pack(pady = 15)

listbox = Listbox(root)
listbox.pack(pady = 15)
listbox.insert(END, "This is the first item")
listbox.insert(END, "This is the second item")

list = ["magenta", "orange", "violet", "indigo", "blue", "cyan", "red", "purple", "yellow", "green"]
for item in list:
    listbox.insert(END, item)


button_1 = Button(root, text="Select", command = None)
button_1.pack(pady = 15)
button_2 = Button(root, text="Delete", command = delete)
button_2.pack(pady = 15)
root.mainloop()


