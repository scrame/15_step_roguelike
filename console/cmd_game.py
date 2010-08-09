#!/usr/bin/python

from dice import Dice

print("hello")

dice = Dice()

for i in range(20):
    print "3d6: " + str(dice.roll(3,6))




def test_raw_input():
    name = raw_input("enter your name: ")
    print name
