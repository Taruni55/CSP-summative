#import modules
import turtle as trtl
import random as rand

#draw screen template
draw = trtl.Turtle()
screen = trtl.Screen()
screen.bgcolor("green")
#game functions
number_values = [0,1,2,3,4,5,6,7,8,9]
chips = 5000
wins = 0
losses = 0 

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