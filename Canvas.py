from tkinter import *

root = Tk()
root.title("Canvas")
root.geometry("500x500")

my_canvas = Canvas(root, width=400, height=400, bg="white")
my_canvas.pack(pady=45)

# my_canvas.create_line(90,60,120,140, fill="orange")
# my_canvas.create_line(45,30,60,70, fill="magenta")
# # my_canvas.create_line(5,90,50,90, fill="purple")
# my_canvas.create_rectangle(24,45,60,98, fill="black")

# my_canvas.create_line(100,100,200,100, fill="black")
# my_canvas.create_rectangle(50,50,100,75, fill="black")
# my_canvas.create_rectangle(200,50, 250, 75, fill="black")
# my_canvas.create_rectangle(75,125,225,150, fill="pink")

my_canvas.create_oval(20,150,380,250,fill="green")
my_canvas.create_oval(50,170,70,230, fill="blue")
my_canvas.create_line(60,232,60,242, fill="black", width=10)
my_canvas.create_line(157,248,157,253, fill="black", width=10)
my_canvas.create_line(254,248,254,253, fill="black", width=10)
my_canvas.create_line(351,229,351,239, fill="black", width=10)
my_canvas.create_line(110,200,290,200, fill="red", width=5)
my_canvas.create_line(155,190,155,210, fill="purple", width=2.5)
my_canvas.create_line(200,190,200,210, fill="purple", width=2.5)
my_canvas.create_line(245,190,245,210, fill="purple", width=2.5)
root.mainloop()
