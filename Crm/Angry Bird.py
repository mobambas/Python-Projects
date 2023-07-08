from tkinter import *
root = Tk()
root.geometry("600x600")
root.title("Angry Bird")
canvas = Canvas(root, width = 500, height = 500, bg = "white")
canvas.pack(pady=20)
bird = PhotoImage(file ="red-bird3.png")
slingshot = PhotoImage(file ="sling.png")
sli = canvas.create_image(250, 250, image = slingshot)

p1 = (216,176)
p2 = (256,175)

on_canvas = canvas.create_line(0,0,1,1)
l1 = canvas.create_line(0,0,1,1)
l2 = canvas.create_line(0,0,1,1)

label1 = Label(root, text = '')
label1.pack()
def pressed(event):
    label1.config(text = f'X: {str(event.x)} Y: {str(event.y)}')

    global on_canvas,l1,l2,sli
    canvas.delete(l1)
    canvas.delete(l2)
    canvas.delete(on_canvas)
    canvas.delete(sli)

    l2 = canvas.create_line(p2[0],p2[1],event.x, event.y, fill = "black", width = 5)
    on_canvas = canvas.create_image(event.x, event.y, image = bird)
    sli = canvas.create_image(250,250, image = slingshot)
    l1 = canvas.create_line(p1[0], p1[1], event.x, event.y, fill="black", width=5)


root.bind("<B1-Motion>", pressed)
root.mainloop()