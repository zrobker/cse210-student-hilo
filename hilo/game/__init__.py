"""
The game package contains the classes for playing Hilo.
"""
import random

class Rand_num:
    card = random.randrange(1,13,1)
    def changeNum(self):
        self.card = random.randrange(1,13,1)

class player:
    points = 300
