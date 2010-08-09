#!/usr/bin/python

from dice import Dice

dice = Dice()

def test_map_commands():
    def roll():
        return dice.roll(2,6)

    commands = {
        'r' : roll
        }

    print('r' + " : " + commands['r'].__name__)
    print(commands['r']())




def test_dice():
    for i in range(20):
        print "3d6: " + str(dice.roll(3,6))


def test_raw_input():
    name = raw_input("enter your name: ")
    print name
