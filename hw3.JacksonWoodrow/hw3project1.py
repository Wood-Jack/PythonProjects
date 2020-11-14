

#
#
# Project Name:     CostOfPizza
# Programmer:    Woodrow Jackson
#
#
# Description: a program that calculates the cost per square inch of a circular pizza,
# given its diameter and price.
#

#importing the math
import math

print("Welcome to Mik's Pizzaria where you choose the size and price of your pizza")

diameter = eval(input("please enter the diameter of your pizza: \n"))
radius = diameter/2
area = math.pi *(radius)**2
price= eval(input("So what will the price of your pizza? \n"))

costPerInch= float(area/price)

print("The cost of your pizza square inch would be :", round(costPerInch,1), "cents")


