from tkinter import *
import random

class AngryBirdGame:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Angry Birds")

        self.canvas = Canvas(root, width=800, height=600, bg="lightblue")
        self.canvas.pack(pady=20)

        self.bird = PhotoImage(file="red-bird3.png")
        self.slingshot = PhotoImage(file="sling.png")

        self.sling_coordinates = (400, 400)
        self.bird_coordinates = (400, 400)

        self.sling = self.canvas.create_image(self.sling_coordinates, image=self.slingshot)
        self.bird_obj = None

        self.canvas.bind("<B1-Motion>", self.drag_bird)
        self.canvas.bind("<ButtonRelease-1>", self.launch_bird)

    def drag_bird(self, event):
        self.canvas.delete(self.bird_obj)
        self.bird_coordinates = (event.x, event.y)
        self.bird_obj = self.canvas.create_image(self.bird_coordinates, image=self.bird)

    def launch_bird(self, event):
        self.canvas.delete(self.bird_obj)
        self.animate_bird()

    def animate_bird(self):
        target_x = random.randint(50, 750)
        target_y = random.randint(50, 550)

        velocity_x = (target_x - self.bird_coordinates[0]) / 10
        velocity_y = (target_y - self.bird_coordinates[1]) / 10

        for _ in range(10):
            self.canvas.move(self.bird_obj, velocity_x, velocity_y)
            self.canvas.update()
            self.root.after(30)

        self.canvas.delete(self.bird_obj)


p1 = (216, 176)
p2 = (256, 175)

on_canvas = None
l1 = None
l2 = None
sli = None
bird_speed = 10
angle = 0

label1 = Label(root, text='')
label1.pack()

def pressed(event):
    global on_canvas, l1, l2, sli, angle
    canvas.delete(l1)
    canvas.delete(l2)
    canvas.delete(on_canvas)
    canvas.delete(sli)

    angle = calculate_angle(p1, (event.x, event.y))
    on_canvas = canvas.create_image(p1[0], p1[1], image=bird)
    sli = canvas.create_image(250, 250, image=slingshot)
    draw_line(p1, angle)

def release(event):
    global on_canvas, angle
    canvas.delete(on_canvas)
    bird_movement(angle)

def draw_line(p1, angle):
    global l1, l2
    l2 = canvas.create_line(p2[0], p2[1], p2[0] + 50 * math.cos(angle), p2[1] + 50 * math.sin(angle), fill="black", width=5)
    l1 = canvas.create_line(p1[0], p1[1], p1[0] + 50 * math.cos(angle), p1[1] + 50 * math.sin(angle), fill="black", width=5)

def calculate_angle(p1, p2):
    return math.atan2(p2[1] - p1[1], p2[0] - p1[0])

def bird_movement(angle):
    global on_canvas
    speed_x = bird_speed * math.cos(angle)
    speed_y = bird_speed * math.sin(angle)

    for _ in range(100):  # Simulate motion
        canvas.move(on_canvas, speed_x, speed_y)
        canvas.update()
        root.after(10)

root.bind("<B1-Motion>", pressed)
root.bind("<ButtonRelease-1>", release)

if __name__ == "__main__":
    root = Tk()
    game = AngryBirdGame(root)
    root.mainloop()

# Game Structure:

# Create a class for the game that manages levels, scores, and game state.
# Implement a level system with increasing difficulty.
# Keep track of the score for each level.
# Obstacles:

# Add static and dynamic obstacles (blocks, structures).
# Define different types of obstacles with varying properties.
# Game Physics:

# Integrate realistic physics for bird movement (using velocity, gravity, collision detection, etc.).
# Add physics for collisions between the bird, obstacles, and pigs.
# Pigs:

# Introduce pig characters as targets.
# Assign different scores for hitting different pigs.
# User Interface:

# Display the level, score, and remaining birds.
# Show a game over screen when the player runs out of birds.
# Multiple Levels:

# Implement multiple levels with different structures and challenges.
# Increase difficulty progressively.
# Sound Effects and Music:

# Add sound effects for bird launches, collisions, and level completion.
# Include background music during gameplay.
# Winning and Losing Conditions:

# Determine winning conditions (e.g., eliminating all pigs) for each level.
# Implement losing conditions (e.g., running out of birds).
# Reset and Next Level:

# Allow the player to reset the level or move to the next level after completing one.
# High Scores:

# Keep track of high scores and display them.
