# TODO: Add entry point code here
import random
from game.__init__ import Rand_num,player

#CheckRes will check results of the game, and then change points and return the new point value to the main game.
def checkRes(card0, card1, points):
    if hilo.lower() == 'h':
            if card0.card < card1.card:
                return points += 100
            else:
                return points -= 75
        elif hilo.lower() == 'l':
            if card0.card > card1.card:
                return points += 100
            else:
                return points -= 75

def main():
    keepPlaying = True
    while player.points > 0 and keepPlaying:
        #Generates 2 new cards, and prepares them for their numbers
        card0 = Rand_num()
        card1 = Rand_num()
        #Changes Card0 Number
        card0.card = random.randrange(1,13,1)
        print(f"The card is: {card0.card}")
        hilo = input("Higher or Lower? [h/l] ")
        #Changes Card1 Number
        card1.card = random.randrange(1,13,1)
        print(f"Next card was: {card1.card}")
        #calls checkres with current variables
        points = checkRes(card0, card1, points)
        print(f"Your score is: {player.points}")
        #asks user if they want to keep playing
        if input("Keep Playing? [y/n]") == "n":
            keepPlaying = False
        print("")
main()