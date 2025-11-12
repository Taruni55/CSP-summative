import turtle as trtl
import math
import time
import random as rand

#turtle set ups
screen = trtl.Screen()
flower = trtl.Turtle()
flower.speed(0)
flower.pencolor("black")
font_setup = ("Arial",25,"normal")
start = trtl.Turtle(shape="square")
start.hideturtle()
screen.addshape("petal", ((0, 0), (20, 60), (40, 80), (60, 60), (80, 0), (60, -60), (40, -80), (20, -60)))
#game functions
def start_clicked(x,y):
    trtl.clear()
    start.hideturtle()
    trtl.teleport(-300, 200)
    trtl.write("Click on a part of the flower to draw!", font = font_setup)
    
#get users name
def get_name():
    global user_name
    user_name = trtl.textinput("Name", "What is your name?")
    
#generate random message
def generate_message():
    global user_name
    messages = ["Dear "+ user_name+",\n I hope you are doing well!\n Here is some math practice for you\n to work on when you are back at school.\nClick the square to start!", "Hi "+ user_name+",\n Hope everything is going great.\n I have some math practice for\n when you return to school!\nClick the square to start!", "Dear "+ user_name+",\n Wishing you all the best!\n Here is a bit of math practice to\n help you get ready for when you are back in class!\nClick the square to start!"]
    trtl.teleport(-300, 150)
    trtl.hideturtle()
    trtl.write(rand.choice(messages), font = font_setup)
    
def envelope_clicked(x,y):
    envelope.hideturtle()
    get_name()
    generate_message()
    start.color("blue")
    start.turtlesize(4)
    start.teleport(200,250)
    start.showturtle()
    draw_flower()

#draw out shape for coloring sheet
def draw_flower():
    center = trtl.Turtle()
    center.hideturtle()
    center.speed(0)
    center.penup()
    center.goto(0, -50)
    center.pendown()
    center.color("black", "white")
    center.begin_fill()
    center.circle(50)
    center.end_fill()
    
    petals = []
    for i in range(6):
        p = trtl.Turtle()
        p.shape("petal")
        p.color("black", "white")
        p.penup()
        p.setheading(i * 60)  
        p.forward(80)         
        petals.append(p)

#click envelope to open letter
envelope_image = "1.3.1 - Artistic Expression/envelope.gif"
screen.addshape(envelope_image)
envelope = trtl.Turtle(shape=envelope_image)
envelope.onclick(envelope_clicked)
start.onclick(start_clicked)

#generate math questions when clicked

#choose fill color when correct

#when done, just display image at end

#maybe add option to play again
screen.mainloop()