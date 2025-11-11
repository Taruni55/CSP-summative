import turtle as trtl
import math
import time
import random as rand
screen = trtl.Screen()

#game functions
def get_name():
    global user_name
    user_name = trtl.textinput("Name", "What is your name?")
    
def generate_message():
    global user_name
    messages = ["Dear "+ user_name+", I hope you are doing well! Here is some math practice for you to work on when you are back at school.", "Hi "+ user_name+", Hope everything is going great. I have some math practice for when you return to school!", "Dear "+ user_name+",Wishing you all the best! Here is a bit of math practice to help you get ready for when you are back in class!"]
    trtl.write(rand.choice(messages))
    
def envelope_clicked(x,y):
    global start
    envelope.hideturtle()
    get_name()
    generate_message()
    start = trtl.Turtle(shape="square")


#click envelope to open letter
envelope_image = "1.3.1 - Artistic Expression/envelope.gif"
screen.addshape(envelope_image)
envelope = trtl.Turtle(shape=envelope_image)

envelope.onclick(envelope_clicked)
#get users name

#generate random message

#draw out shape for coloring sheet

#generate math questions when clicked

#choose fill color when correct

#when done, just display image at end

#maybe add option to play again
screen.mainloop()