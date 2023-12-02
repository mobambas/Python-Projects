from tkinter import *
import math

def click_button(value):
    current = entry1.get()
    entry1.delete(0, END)
    entry1.insert(END, str(current) + str(value))

def clear_entry():
    entry1.delete(0, END)

def calculate():
    try:
        expression = entry1.get()
        result = eval(expression)
        entry1.delete(0, END)
        entry1.insert(END, str(result))
    except Exception as e:
        entry1.delete(0, END)
        entry1.insert(END, "Error")

def calculate_exponent():
    try:
        value = float(entry1.get())
        result = math.pow(value, 2)
        entry1.delete(0, END)
        entry1.insert(END, str(result))
    except Exception as e:
        entry1.delete(0, END)
        entry1.insert(END, "Error")

def calculate_square_root():
    try:
        value = float(entry1.get())
        result = math.sqrt(value)
        entry1.delete(0, END)
        entry1.insert(END, str(result))
    except Exception as e:
        entry1.delete(0, END)
        entry1.insert(END, "Error")

def calculate_percentage():
    try:
        value = float(entry1.get())
        result = value / 100
        entry1.delete(0, END)
        entry1.insert(END, str(result))
    except Exception as e:
        entry1.delete(0, END)
        entry1.insert(END, "Error")

window = Tk()
window.geometry("500x600")
window.title("ON SCREEN CALCULATOR")

label1 = Label(window, text="*This is an on-screen GUI-based calculator*")
label1.grid(row=5, column=40, columnspan=5)

entry1 = Entry(window, font=('Arial', 20), justify='right')
entry1.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C", "x^2", "√x", "%"
]

row_val = 1
col_val = 0

for button in buttons:
    if button == "=":
        Button(window, text=button, bg="lightgray", height=3, width=5, command=calculate).grid(row=row_val, column=col_val, padx=5, pady=5)
    elif button == "C":
        Button(window, text=button, bg="red", height=3, width=5, command=clear_entry).grid(row=row_val, column=col_val, padx=5, pady=5)
    elif button == "x^2":
        Button(window, text=button, bg="lightgray", height=3, width=5, command=calculate_exponent).grid(row=row_val, column=col_val, padx=5, pady=5)
    elif button == "√x":
        Button(window, text=button, bg="lightgray", height=3, width=5, command=calculate_square_root).grid(row=row_val, column=col_val, padx=5, pady=5)
    elif button == "%":
        Button(window, text=button, bg="lightgray", height=3, width=5, command=calculate_percentage).grid(row=row_val, column=col_val, padx=5, pady=5)
    else:
        Button(window, text=button, bg="lightgray", height=3, width=5, command=lambda value=button: click_button(value)).grid(row=row_val, column=col_val, padx=5, pady=5)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

window.mainloop()
