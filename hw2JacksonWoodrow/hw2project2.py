#
#
# Project Name:     ExamScore Average

# Programmer:    Woodrow Jackson
#
#
# Description: A program that allows you to put in as many exams as you want and gives you average score
#
#


numberOfEx = (eval (input("Please input a how many exams you taken")))

sum=0

for i in range(numberOfEx):

    count = i+1
    print("Enter Exam score ", count ," :")
    input2 = (eval(input()))



    sum =  sum + input2


    average = sum/ count



    print("Exam Score Average is :", average)
    continue