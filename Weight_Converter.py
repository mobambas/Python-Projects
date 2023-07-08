from tkinter import *

root = Tk()
root.title("Weight Converter")
root.geometry("500x500")

f1 = ("bold")


def convert():
    label_5 = Label(root, text=float(entry_1.get()) * 1000, font=f1)
    label_5.grid(row=7, column=2)

    label_6 = Label(root, text=float(entry_1.get()) * 2, font=f1)
    label_6.grid(row=7, column=3)

    label_7 = Label(root, text=float(entry_1.get()) * 35, font=f1)
    label_7.grid(row=7, column=4)


label_1 = Label(root, text="Please enter your desired weight in KGS")
label_1.grid(row=1, column=2, padx=10)
entry_1 = Entry(root)
entry_1.grid(row=1, column=3, padx=10)
convert_btn = Button(root, text="Convert", command=convert)
convert_btn.grid(row=1, column=4, padx=10)
label_2 = Label(root, text="Grams")
label_2.grid(row=4, column=2)
label_3 = Label(root, text="Pounds")
label_3.grid(row=4, column=3)
label_4 = Label(root, text="Ounces")
label_4.grid(row=4, column=4)

root.mainloop()

