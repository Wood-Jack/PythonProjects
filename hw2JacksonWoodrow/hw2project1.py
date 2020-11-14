
#
#
# File Name:     FahrenheittoCelsius

# Programmer:    Woodrow Jackson
#
#
# Description: A program that takes Fahrenheit and Converts it into Celsius
#
#

degreesF = eval(input("Enter a temperature in degrees Fahrenheit (Ex. 72 ) \n"))

degreesC = 5 *(degreesF - 32)/9

print(degreesF," Fahrenheit = ",round(degreesC,1), " Celsius ")