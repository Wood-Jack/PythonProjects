#
#
# Project Name:     TestPercentage
# Programmer:    Woodrow Jackson
#
#
# Description: A program that computes the percentage for a test.
# Your input will be the number of questions and the number of correctly answered questions.
# it will give you the percentage of your test.
#
print()

correctQuestions = eval(input("How many correct questions did you get on the test : \n"))

numberOfQuestions = eval(input("How many questions was on the test: \n"))

per = (correctQuestions/numberOfQuestions) *100

print("Your test score is:", per,"%")