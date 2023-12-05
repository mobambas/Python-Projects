from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

root = Tk()
root.configure(bg='black')
root.geometry("500x500")
root.title("Happy Halloween!")

path2 = r"C:\\Users\\Lakshni\\Downloads\\Scary-pumpkin--halloween-pn-transparent-background-PNG.ico"

root.iconbitmap(path2)

def costume():
    costume_list = ["Ghoul", "Ghost", "Demon", "Witch", "Nun", "Monster", "Poltergeist", "Angel"]
    list1 = ["Horrifying", "Ghastly", "Scary", "Nasty", "Eek", "Terrifying"]
    list2 = ["red", "orange"]
    list3 = ["black"]

    if len(e1.get()) > 0 or len(e2.get()) > 0:
        label2 = Label(labelframe, text=random.choice(list1) + " " + e1.get() + " " + e2.get() + "!" + " " +
                       "You are a" + " " + random.choice(costume_list) + "!",
                       font=('bold'), foreground=random.choice(list2), background=random.choice(list3))
        label2.pack(side=BOTTOM)
    else:
        messagebox.showerror(" ", "Please enter a name OR surname")

labelframe = LabelFrame(root, text="Halloween's the best!", background="black", foreground="white", font=('bold'))
labelframe.pack()

label = Label(labelframe, text="COSTUME GENERATOR 101", foreground="black", background="red",
              font=('Lucida Calligraphy', 18, 'bold', 'underline'))
label.pack(side=TOP)

e1 = Entry(labelframe)
e1.insert(0, 'Name')
e1.pack()

e2 = Entry(labelframe)
e2.insert(0, 'Surname')
e2.pack()

label1 = Label(labelframe,
               text="Click to find out your ultimate Halloween Costume!",
               foreground="black", background="red",
               font=('Lucida Calligraphy', 13, 'bold', 'italic'))
label1.pack()

button = Button(labelframe, text="Who resides within thy soul?!",
                command=costume, bg="orange", activeforeground="yellow",
                activebackground="magenta", font=('Lucida Calligraphy', 10, 'bold'))
button.pack()

path1 = r"C:\\Users\\Lakshni\\Downloads\\file_741959_chucky.png"
path2 = r"C:\\Users\\Lakshni\\Downloads\\Scary-pumpkin--halloween-pn-transparent-background-PNG.png"
path3 = r"C:\\Users\\Lakshni\\Downloads\\pp.png"
path4 = r"C:\\Users\\Lakshni\\Downloads\\slender.png"

image1 = ImageTk.PhotoImage(Image.open(path1))
image2 = ImageTk.PhotoImage(Image.open(path2))
image3 = ImageTk.PhotoImage(Image.open(path3))
image4 = ImageTk.PhotoImage(Image.open(path4))

image_list = [image1, image2, image3, image4]

label_image1 = Label(root, image=image1, height=400, width=400)

label_image1.pack(side=BOTTOM)

def forward(image_number):
    global label_image1
    global button_forward
    global button_back

    label_image1.pack_forget()

    if 0 < image_number <= len(image_list):
        label_image1 = Label(root, image=image_list[image_number - 1], height=400, width=400)
        label_image1.pack(side=BOTTOM)

        button_forward = Button(root, text=">>>", command=lambda: forward(image_number + 1))
        button_forward.pack(side=RIGHT)

        button_back = Button(root, text="<<<", command=lambda: back(image_number - 1))
        button_back.pack(side=LEFT)

        if image_number == len(image_list):
            button_forward = Button(root, text=">>>", state=DISABLED)

def back(image_number):
    global label_image1
    global button_forward
    global button_back

    label_image1.pack_forget()

    if 0 < image_number <= len(image_list):
        label_image1 = Label(root, image=image_list[image_number - 1], height=400, width=400)
        label_image1.pack(side=BOTTOM)

        button_forward = Button(root, text=">>>", command=lambda: forward(image_number + 1))
        button_forward.pack(side=RIGHT)

        button_back = Button(root, text="<<<", command=lambda: back(image_number - 1))
        button_back.pack(side=LEFT)

button_back = Button(root, text="<<<", command=lambda: back(0))
button_back.pack(side=LEFT)

button_forward = Button(root, text=">>>", command=lambda: forward(2))
button_forward.pack(side=RIGHT)

label_4 = Label(root, text="View our spooky Costume Gallery!", bg="magenta", activeforeground="yellow",
                activebackground="orange", font=('Heltevicta', 10, 'bold', 'italic'))
label_4.pack()

root.mainloop()
