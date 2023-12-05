from tkinter import *
from tkinter import filedialog as fd

window = Tk()
window.title("File Dialog Box")
window.geometry("350x350")

def select_file():
    file_type = (("Text", "*.txt"), ("Images", "*.png"))
    
    window.file = fd.askopenfilename(
        initialdir="/",
        title="File Dialog",
        filetypes=file_type
    )

label_1 = Label(window, text="Open File Directory")
label_1.pack()

button_1 = Button(window, text="File Explorer", command=select_file)
button_1.pack()

window.mainloop()
