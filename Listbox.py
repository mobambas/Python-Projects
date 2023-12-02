from tkinter import *

def delete():
    selected_index = listbox.curselection()
    if selected_index:
        listbox.delete(selected_index)
        label.config(text="Item deleted")

def select():
    selected_index = listbox.curselection()
    if selected_index:
        selected_item = listbox.get(selected_index)
        label.config(text=f"Selected Item: {selected_item}")

root = Tk()
root.title("Listbox")
root.geometry("500x500")

label = Label(root)
label.pack(pady=15)

listbox = Listbox(root)
listbox.pack(pady=15)
listbox.insert(END, "This is the first item")
listbox.insert(END, "This is the second item")

colors = ["magenta", "orange", "violet", "indigo", "blue", "cyan", "red", "purple", "yellow", "green"]
for item in colors:
    listbox.insert(END, item)

button_1 = Button(root, text="Select", command=select)
button_1.pack(pady=15)

button_2 = Button(root, text="Delete", command=delete)
button_2.pack(pady=15)

root.mainloop()
