from tkinter import *
root = Tk()

canvas  = Canvas(root, height = 500, width = 500, bg  ='white')
canvas.pack()
label  = Label(root, text='')
label.pack()
img = PhotoImage(file = "snake.png")
img = img.subsample(1)
shape = canvas.create_image(100, 100, image = img)

def pressed(event):
    global img
    img = PhotoImage(file="snake.png")
    img = img.subsample(1)
    canvas.create_image(event.x, event.y, image=img)
    label.config(text=f'X: {str(event.x)}, Y: {str(event.y)}')
root.bind('<B1-Motion>', pressed)
root.mainloop()
i = int(input())
for num in range(1,i+1):
    print(f"Case#{num}:{None}")
x = 0
l1  = [x in range(0,10)]
print(l1)

def clear_canvas():
    canvas.delete("all")
    
clear_button = Button(root, text="Clear Canvas", command=clear_canvas)
clear_button.pack()

def resize_image(event):
    global img
    img = img.subsample(int(event.width/100))
    canvas.itemconfig(shape, image=img)

root.bind('<Configure>', resize_image)




