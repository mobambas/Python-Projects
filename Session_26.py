from tkinter import *

root = Tk()
root.title("First Window")
root.geometry("300x300")

def open_window_2():
    top1 = Toplevel(root)
    top1.title("Second Window")
    top1.geometry("350x350")
    
    label_2 = Label(top1, text="This is a Toplevel 1 window")
    label_2.pack()
    
    button_2 = Button(top1, text="open toplevel 2", command=open_window_3)
    button_2.pack()
    
    button_3 = Button(top1, text="Exit", command=top1.destroy)
    button_3.pack()

def open_window_3():
    top2 = Toplevel(root)
    top2.title("Third Window")
    top2.geometry("350x350")
    
    label_3 = Label(top2, text="This is a Toplevel 2 window")
    label_3.pack()
    
    button_3 = Button(top2, text="Exit", command=top2.destroy)
    button_3.pack()

label_1 = Label(root, text="This is the root window")
label_1.pack()

button_1 = Button(root, text="open toplevel 1", command=open_window_2)
button_1.pack()

button_3 = Button(root, text="Exit", command=root.destroy)
button_3.pack()

root.mainloop()
