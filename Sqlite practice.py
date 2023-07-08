from tkinter import *


window = Tk()
window.geometry("500x500")
window.title("ON SCREEN CALCULATOR")

label1 = Label(window, text = "*This is an on-screen GUI-based calculator*")
label1.grid(row = 5, column = 40)


entry1 = Entry(window)
entry1.grid(row = 0, column = 20)

b1 = Button(window,text="1" ,bg="yellow", height = 5, width = 5)
b1.grid(row = 0, column = 5)

b2 = Button(window,text="2" ,bg="blue", height = 5, width = 5)
b2.grid(row = 0, column = 6)

b3 = Button(window,text="3" ,bg="green", height = 5, width = 5)
b3.grid(row = 0, column = 7)

b4 = Button(window,text="4" ,bg="orange", height = 5, width = 5)
b4.grid(row = 1, column = 5)

b5 = Button(window,text="5" ,bg="red", height = 5, width = 5)
b5.grid(row = 1, column = 6)

b6 = Button(window,text="6" ,bg="purple", height = 5, width = 5)
b6.grid(row = 1, column = 7)

b7 = Button(window,text="7" ,bg="pink", height = 5, width = 5)
b7.grid(row = 2, column = 5)

b8 = Button(window,text="8" ,bg="cyan", height = 5, width = 5)
b8.grid(row = 2, column = 6)

b9 = Button(window,text="9" ,bg="magenta", height = 5, width = 5)
b9.grid(row = 2, column = 7)

divide = Button(window,text="÷" ,bg="indigo", height = 5, width = 5)
divide.grid(row = 3, column = 5)

multiply = Button(window,text="x" ,bg="violet", height = 5, width = 5)
multiply.grid(row = 3, column = 6)

subtract = Button(window,text="-" ,bg="yellow", height = 5, width = 5)
subtract.grid(row = 3, column = 7)

add = Button(window,text="+" ,bg="yellow", height = 5, width = 5)
add.grid(row = 4, column = 6)
window.mainloop()