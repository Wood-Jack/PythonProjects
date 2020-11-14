#! /usr/bin/python
# Exercise No.   1
# File Name:     MyFirstProgram.py
# Programmer:    Guido van Rossum
# Date:          Sept. 1, 2010
#
# Problem Statement: Ask the user to enter two numbers, calculate the sum of 
# these two numbers, and display the sum to the screen
#
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for two integers
# 3. Calculate the sum of the integers
# 4. Print the sum of the integers to the screen
#
#
# import the necessary python libraries
# for this example none are needed


def main():
    # Print a message to the screen
    print("Hello! \n")
    print("I can add two number for you \n")

    # Variables are declared dynamically no need to pre-define
    num1 = eval(input("Enter one whole numbers(Ex. 52): \n"))
    num2 = eval(input("Enter second whole numbers(Ex. 41): \n"))
    num3 = eval(input("Enter third whole numbers (Ex.22): \n"))

    percentage = (num1 / num2 ) * 100
    print("Percentage = ", percentage, "\n" )

    #Here is the processing that is needed
    sum = num1 + num2 +num3

    times = num1*num2*num3

    # Output the results
    print("The sum of the three numbers is", sum,"\n")

    print("The multiple of the three numbers is", times)

main()

