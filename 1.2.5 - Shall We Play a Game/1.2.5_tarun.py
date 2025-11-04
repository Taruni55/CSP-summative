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

number_values = [0,0,0,0,1,2,3,4,5,6,7,8,9]
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
    for i in range(2):
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
    
def clear_table():
    draw.clear()
    draw.penup()
    draw.goto(-200, 150)
    draw.color("white")
    draw.write("Baccarat Table", align="center", font=("Arial", 28, "bold"))
    screen.update()

def play_round(): 
    global chips
    clear_table()
    draw.penup()
    draw.goto(-200, 100)
    draw.color("gold")
    draw.write(f"Chips: {chips}", align="center", font=("Arial", 18, "bold"))
    screen.update()
#bet size
    bet_str = screen.textinput("Place your bet", f"You have {chips} chips.\nEnter bet amount:")
    if bet_str is None:
        return False
    try:
        bet = int(bet_str)
    except:
        return True
    if bet <= 0 or bet > chips:
        return True
#choose player or banker
    choice = screen.textinput("Bet on", "Type 'player' or 'banker':")
    if choice is None or choice.lower() not in ["player", "banker"]:
        return True
    choice = choice.lower()
    
    player_cards = [rand.choice(number_values), rand.choice(number_values)]
    banker_cards = [rand.choice(number_values), rand.choice(number_values)]

    player_total = baccarat_value(player_cards)
    banker_total = baccarat_value(banker_cards)
#deal cards
    x_start = -150
    for i, c in enumerate(player_cards):
        draw_card(x_start + i*70, 50, c, "Player")
    for i, c in enumerate(banker_cards):
        draw_card(x_start + i*70, -100, c, "Banker")
#check if eligible to draw 3rd card
    if player_total <= 5:
        player_cards.append(rand.choice(number_values))
        player_total = baccarat_value(player_cards)
        draw_card(x_start + 2*70, 50, player_cards[-1], "Player")

    if banker_total <= 5:
        banker_cards.append(rand.choice(number_values))
        banker_total = baccarat_value(banker_cards)
        draw_card(x_start + 2*70, -100, banker_cards[-1], "Banker")
#check winner
    if player_total > banker_total:
        winner = "player"
    elif banker_total > player_total:
        winner = "banker"
    else:
        winner = "tie"
        
    draw.goto(-200, -200)
    if winner == choice:
        chips += bet
        draw.color("lightgreen")
        draw.write(f"You win! {winner.title()} wins.", align="center", font=("Arial", 18, "bold"))
    elif winner == "tie":
        draw.color("yellow")
        draw.write("It's a tie! Bet returned.", align="center", font=("Arial", 18, "bold"))
    else:
        chips -= bet
        draw.color("red")
        draw.write(f"You lose! {winner.title()} wins.", align="center", font=("Arial", 18, "bold"))

    screen.update()
    time.sleep(2) 

    screen.textinput("Continue?", "Press OK to play next round, or Cancel to quit.")
    return chips > 0

#end game when out of chips
draw.clear()
draw.goto(0, 0)
draw.color("white")
draw.write(f"Game Over!\nFinal Chips: {chips}", align="center", font=("Arial", 26, "bold"))

#loop for main game
keep_playing = True
while keep_playing and chips > 0:
    keep_playing = play_round()

screen.mainloop()
