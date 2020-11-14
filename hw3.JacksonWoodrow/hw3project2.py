
#
# File Name:     LadderAgainstHouse
# Programmer:    Woodrow Jackson
#
#
# Description:  a program to determine the length of a ladder required to reach a given height when leaned against a house.
# The height and angle of the ladder are given as inputs.
#
#
import math

height = eval(input("What is the height of the ladder"))

inputDegree = eval(input("What is the angle of your ladder on the house"))

length = height/ math.sin(math.radians(inputDegree))


print("Your ladder length is: " ,length)