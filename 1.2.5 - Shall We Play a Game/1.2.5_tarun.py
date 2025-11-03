#import modules
import turtle as trtl
import random as rand
import time

#draw screen template
draw = trtl.Turtle()
screen = trtl.Screen()
screen.bgcolor("green")

#game functions
draw.hideturtle()
draw.speed(0)
draw.pensize(3) 

number_values = [0,1,2,3,4,5,6,7,8,9]
chips = 5000
wins = 0
losses = 0 

def baccarat_value(cards):
    return sum(cards) % 10 

def draw_card(x, y, value, label):
    draw.penup()
    draw.goto(x, y)
    draw.pendown()
    draw.color("white")
    draw.begin_fill()
    for _ in range(2):
        draw.forward(60)
        draw.right(90)
        draw.forward(90)
        draw.right(90)
    draw.end_fill()
    draw.penup()
    draw.goto(x + 25, y - 50)
    draw.color("black")
    draw.write(value, align="center", font=("Arial", 24, "bold"))
    draw.goto(x + 30, y - 100)
    draw.write(label, align="center", font=("Arial", 10, "normal"))
    screen.update()
    time.sleep(1) 
    
def draw_numbers():
    card_1 = rand.choice(number_values)
    card_2 = rand.choice(number_values)
    card_3 = rand.choice(number_values)
    card_4 = rand.choice(number_values)
    card_5 = rand.choice(number_values)
    card_6 = rand.choice(number_values)

    
draw_numbers()
#loop for main game

#bet size

#choose player or banker


#deal cards

#check if eligible to draw 3rd card

#check winner


#end game when out of chips

wn=trtl.Screen()
wn.mainloop()
