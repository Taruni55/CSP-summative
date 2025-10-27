#import modules
import turtle as trtl
import random as rand

#draw screen template
draw = trtl.Turtle()

#game functions
number_values = [0,1,2,3,4,5,6,7,8,9]
chips = 5000
wins = 0
losses = 0 

def draw_numbers():
    card_1 = rand.randint(number_values)
    print(card_1)
    
draw_numbers()
#loop for main game

#bet size

#choose player or banker


#deal cards

#check if eligible to draw 3rd card

#check winner


#end game when out of chips