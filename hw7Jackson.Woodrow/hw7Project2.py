
# Project Name:    Speedster
# Programmer:    Woodrow Jackson
#
#
# Description: a program that accepts a speed limit and a clocked speed that prints a message indicating the speed
# was legal or prints the amount of the fine, if the speed is illegal.
#

def main():

    print("Welcome to the Poducksville speed way where you choose your speed and speeding ticket \n"
          " only one rule: If your speed is over 90 mph then you will get a ticket")

    mph = eval(input("Speed Limit:"))

    cSpeed = eval(input("Clocked Speed"))


    if cSpeed > mph:

        difference= (cSpeed - mph)*5

        difference = difference + 50
        if cSpeed > 90 and mph >90 :
            difference = difference + 200

        print("Your speed is: ", mph, "\n ")
        print("Your clocked speed : ", cSpeed, " \n")
        print("Violator!!! violator!!! Law Breaker your speeding ticket is:  ", difference, "dollars" )

    if cSpeed < mph:

        print("Your speed is: " ,mph,"\n")
        print("Your clocked Speed ", cSpeed,"\n")
        print("Thank you for abiding by the speed limits")


main()