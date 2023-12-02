from tkinter import *

root = Tk()
root.title("Canvas")
root.geometry("500x500")

# Create a frame to hold the canvas and add padding
frame = Frame(root)
frame.pack(pady=10)

# Create a canvas with a colorful border
canvas_width = 400
canvas_height = 400
canvas_border_color = "cyan"
canvas_border_width = 10

canvas = Canvas(frame, width=canvas_width, height=canvas_height, bg="white", highlightbackground=canvas_border_color, highlightthickness=canvas_border_width)
canvas.pack()

# Draw shapes on the canvas
canvas.create_oval(20, 150, 380, 250, fill="green")
canvas.create_oval(50, 170, 70, 230, fill="blue")
canvas.create_line(60, 232, 60, 242, fill="black", width=10)
canvas.create_line(157, 248, 157, 253, fill="black", width=10)
canvas.create_line(254, 248, 254, 253, fill="black", width=10)
canvas.create_line(351, 229, 351, 239, fill="black", width=10)
canvas.create_line(110, 200, 290, 200, fill="red", width=5)
canvas.create_line(155, 190, 155, 210, fill="purple", width=2.5)
canvas.create_line(200, 190, 200, 210, fill="purple", width=2.5)
canvas.create_line(245, 190, 245, 210, fill="purple", width=2.5)

root.mainloop()
