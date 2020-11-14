#
#
# Project Name:     Acronym
# Programmer:    Woodrow Jackson
#
#
# Description: a program that takes in a phrase and makes an acronym out of it
#


def main():
    word = input("Please enter a phrase ")

    #Splits words with spaces
    word.split(" ")
    #character index of the letter in the phrase
    for phrase in word.split(" "):
        #prints out the first letter of every word in phrase
        print( phrase[0] )


main()