from tkinter import *

root = Tk()
root.title("Image Handling")
root.geometry("500x500")
canvas = Canvas(root, width=450, height=450, bg="white")
canvas.pack()

shape = canvas.create_oval(22, 22, 50, 50, fill="yellow")


def move_shape(x, y):
    canvas.move(shape, x, y)
    check_boundaries()


def check_boundaries():
    x1, y1, x2, y2 = canvas.coords(shape)
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    if x1 < 0:
        canvas.move(shape, -x1, 0)
    elif x2 > canvas_width:
        canvas.move(shape, canvas_width - x2, 0)

    if y1 < 0:
        canvas.move(shape, 0, -y1)
    elif y2 > canvas_height:
        canvas.move(shape, 0, canvas_height - y2)


def left(event):
    move_shape(-5, 0)


def right(event):
    move_shape(5, 0)


def down(event):
    move_shape(0, 5)


def up(event):
    move_shape(0, -5)


def pressed(event):
    x, y = 0, 0
    if event.char == 'w':
        y = -10
    elif event.char == 'a':
        x = -10
    elif event.char == 's':
        y = 10
    elif event.char == 'd':
        x = 10

    move_shape(x, y)


root.bind('<Left>', left)
root.bind('<Right>', right)
root.bind('<Down>', down)
root.bind('<Up>', up)
root.bind('<Key>', pressed)

root.mainloop()

from tkinter import *
root = Tk()
root.title("Canvas")
root.geometry('500x500')

canvas = Canvas(root, width=500, height=500, bg='white')
canvas.pack()

shape = canvas.create_oval(25,250,50,500, fill=None)

def pressed(event):
    x = 0
    y = 0
    if event.char == 'w':
        x = 0
        y = -10
    if event.char == 'a':
        x = 0
        y = +10
    if event.char == 's':
        x = -10
        y = 0
    if event.char == 'd':
        x = +10
        y = 0
    canvas.move(shape,x,y)
root.bind('<Key>', pressed)
root.mainloop()
