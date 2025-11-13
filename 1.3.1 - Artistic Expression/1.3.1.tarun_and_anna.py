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
start = trtl.Turtle(shape="turtle")
start.hideturtle()
flower.hideturtle()
screen.addshape("petal", ((0, 0), (20, 60), (40, 80), (60, 60), (80, 0), (60, -60), (40, -80), (20, -60)))
p = trtl.Turtle()
p.shape("petal")
p.color("black", "white")
p.penup()

#game functions
def generate_question():
    operators = ["+", "-", "*", "/"]
    op = rand.choice(operators)
    a, b = rand.randint(1, 10), rand.randint(1, 10) 
    
    question = f"What is {a} {op} {b}?"
    correct_answer = round(eval(f"{a} {op} {b}"), 2)
    
    while True:
        answer = screen.textinput("Math Question", question)
        if answer is None:
            return False
        try:
            if abs(float(answer) - correct_answer) < 0.01:
                global player_color
                player_color = screen.textinput("Correct!", "Nice job! What color would you like")
                
                try:
                    p.fillcolor(player_color)
                    return
                except trtl.TurtleGraphicsError:
                    p.fillcolor("orange") 
                    print("error")
                return True
            else:
                question = f"Try again! What is {a} {op} {b}?"
        except:
            question = f"Please enter a number! What is {a} {op} {b}?"
    
def start_clicked(x,y):
    trtl.clear()
    start.hideturtle()
    trtl.teleport(-300, 200)
    trtl.write("Click on a part of the flower to draw!", font = font_setup)
    draw_flower()
    
#get users name
def get_name():
    global user_name
    user_name = trtl.textinput("Name", "What is your name?")
    
#generate random message
def generate_message():
    global user_name
    messages = ["Dear "+ user_name+", I hope you are doing well!\n Here is some math practice for you\n to work on when you are back at school.\nClick the turtle to start!", "Hi "+ user_name+", Hope everything is going great.\n I have some math practice for\n when you return to school!\nClick the turtle to start!", "Dear "+ user_name+", Wishing you all the best!\n Here is a bit of math practice to\n help you get ready for when you are back in class!\nClick the turtle to start!"]
    trtl.teleport(-300, 20)
    trtl.hideturtle()
    trtl.write(rand.choice(messages), font = font_setup)
    
def envelope_clicked(x,y):
    envelope.hideturtle()
    get_name()
    generate_message()
    start.color("lightgreen")
    start.turtlesize(4)
    start.teleport(30,-100)
    start.showturtle()

#draw out shape for coloring sheet
def draw_flower():
    center = trtl.Turtle()
    center.hideturtle()
    center.speed(0)
    center.penup()
    center.goto(0, -50)
    center.pendown()
    center.color("black", "yellow")
    center.begin_fill()
    center.circle(50)
    center.end_fill()
    
    colors = ["pink", "green", "orange", "red", "purple", "blue"]

    def make_petal(i):
        p.setheading(i * 60)
        p.forward(80)
        def fill_petal(x, y):
            if generate_question(): 
                p.fillcolor(player_color)
                p.stamp()
            
        p.onclick(fill_petal)
    
    for i in range(6):
        make_petal(i)

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