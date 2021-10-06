# TODO: Add entry point code here
import random
from game.__init__ import Rand_num,player

def main():
    keepPlaying = True
    while player.points > 0 and keepPlaying:
        card0 = Rand_num()
        card1 = Rand_num()
        card0.card = random.randrange(1,13,1)
        print(f"The card is: {card0.card}")
        hilo = input("Higher or Lower? [h/l] ")
        card1.card = random.randrange(1,13,1)
        print(f"Next card was: {card1.card}")
        if hilo.lower() == 'h':
            if card0.card < card1.card:
                player.points += 100
            else:
                player.points -= 75
        elif hilo.lower() == 'l':
            if card0.card > card1.card:
                player.points += 100
            else:
                player.points -= 75
        print(f"Your score is: {player.points}")
        if input("Keep Playing? [y/n]") == "n":
            keepPlaying = False
        print("")
main()