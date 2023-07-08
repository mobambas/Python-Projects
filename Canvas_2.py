# from tkinter import *
#
#
# root = Tk()
# root.title("Image Handling")
# root.geometry("500x500")
# canvas = Canvas(root,width=450,height=450, bg="white")
# canvas.pack()
# shape = canvas.create_oval(22,22,50,50,fill="yellow")
# def left(event):
#     x = -5
#     y = 0
#     canvas.move(shape,x,y)
# def right(event):
#     x = 5
#     y = 0
#     canvas.move(shape,x,y)
#
# def down(event):
#     x = 0
#     y = 5
#     canvas.move(shape,x,y)
#
# def up(event):
#     x = 0
#     y = -5
#     canvas.move(shape, x, y)
#
# root.bind('<Left>', left)
# root.bind('<Right>', right)
# root.bind('<Down>', down)
# root.bind('<Up>', up)
# def pressed(event):
#     x,y=0,0
#     if event.char == 'w':
#         x = 0
#         y = -10
#     if event.char == 'a':
#         x = -10
#         y = 0
#     if event.char == 's':
#         x = 0
#         y = 10
#     if event.char == 'd':
#         x = 10
#         y = 0
#     canvas.move(shape,x,y)
# root.bind('<Key>', pressed)
# root.mainloop()

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