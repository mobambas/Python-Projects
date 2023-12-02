from tkinter import *

def convert_weight():
    try:
        input_weight = float(entry_weight.get())

        # Clear previous results
        for label in result_labels:
            label.config(text="")

        # Convert to other units
        grams = input_weight * 1000
        pounds = input_weight * 2.20462
        ounces = input_weight * 35.274

        # Display results
        result_labels[0].config(text=f"{grams:.2f} grams")
        result_labels[1].config(text=f"{pounds:.2f} pounds")
        result_labels[2].config(text=f"{ounces:.2f} ounces")

    except ValueError:
        for label in result_labels:
            label.config(text="Invalid input")

root = Tk()
root.title("Weight Converter")
root.geometry("500x300")

# Font style
f1 = ("bold")

# Labels and Entry
label_instruction = Label(root, text="Please enter your weight:")
label_instruction.grid(row=0, column=0, columnspan=2, pady=10)

entry_weight = Entry(root)
entry_weight.grid(row=0, column=2, padx=10, pady=10)

convert_btn = Button(root, text="Convert", command=convert_weight)
convert_btn.grid(row=0, column=3, padx=10, pady=10)

# Results Labels
result_labels = []
units = ["Grams", "Pounds", "Ounces"]

for i, unit in enumerate(units):
    label_result = Label(root, text="", font=f1)
    label_result.grid(row=3, column=i + 1, pady=5)
    result_labels.append(label_result)

root.mainloop()
