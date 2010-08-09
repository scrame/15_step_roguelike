import random

class Dice:
    def roll(self,sides,count):
        return random.randrange(sides,sides*count)
