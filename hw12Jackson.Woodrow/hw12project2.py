#
#
# File Name:     hw12Project2 (Palindrome)
# Programmer:    Woodrow Jackson
#
#
# Description:
#   A palindrome is a sentence that contains the same sequence
#   of letters reading it either forwards or backwards. A classic
#   example is: "Able was I, ere I saw Elba." Write a recursive
#   function that detects whether a string is a palindrome.
#
# Overall Plan:
# 1. Print introduction
# 2. Ask user for input text
# 3. Remove all non-alphabetic characters and make lowercase
# 4. Check if input text is palindrome using recursion
#       remove the 1st and last character from string each
#       each time it is checked. Base case is when 1 or 0
#       characters are left in the string
# 5. Display if user input string is a palindrome or not


import re

# making the recursive for cleaning the string

def recursionOfString(stringCleaned):

    # the orginal and comparing it to
    if len(stringCleaned) < 2:
        return True

    elif stringCleaned[0] == stringCleaned[-1]:
        return recursionOfString(stringCleaned[1: -1])
    else:
        return False


def stringCleaned(thePalindrome):
    return re.sub("[A-Za-z] +", '', thePalindrome)

def main():

    phrase = input("Please enter phrase: ")

    if recursionOfString(stringCleaned(phrase)):
        print(" is a Palindrome".format(phrase) )
    else:
        print("Not a Palindrome ".format(phrase))



main()