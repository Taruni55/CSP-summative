import turtle as trtl
import random

# Setup screen
screen = trtl.Screen()
screen.bgcolor("black")
screen.title("Interactive Fireworks Art")

# Create one turtle for drawing fireworks
firework = trtl.Turtle()
firework.speed(0)
firework.hideturtle()

# List of colors

colors = ["red", "blue", "green", "yellow", "purple", "orange", "white"]

# Function to draw firework
def draw_firework(x, y):
    firework.penup()
    firework.goto(x, y)
    firework.pendown()
    firework.color(random.choice(colors))
    # iteration: draw lines in a circle
    for angle in range(0, 360, 30):
        firework.setheading(angle)
        firework.forward(50)
        firework.backward(50)


# User input for greeting
trtl.addshape("sixteen", ((4,0),(8,2),(8,8),(2,8),(0,4),(-2,8),(-8,8),(-8,2),(-4,0),(-8,-2),(-8,-8),(-2,-8),(0,-4),(2,-8),(8,-8),(8,-2),(4,0)))
name = screen.textinput("Welcome!", "What is your name?")
painter = trtl.Turtle(shape = "sixteen")
bruh = trtl.Turtle(shape = "sixteen")
painter.color("white")
bruh.color("white")
painter.penup()
bruh.penup()
painter.goto(0, 250)
painter.write(f"Hi {name}! Click to make fireworks!", align="center", font=("Arial", 20, "normal"))
painter.goto(-250, 250)
bruh.goto(250, 250)
bruh.shapesize(5)
painter.shapesize(5)

# Interactivity
screen.onclick(draw_firework)

screen.mainloop()