
#
#
# File Name:     hw12Project1 (Binary and linear Search)
# Programmer:    Woodrow Jackson
#
# pg 359 linear
# pg 360 binary
# Description: Compare the search times of linear search and binary search for the list sizes of 1000, 10000, and 100000
# For binary search to work the list must be sorted. Use the built-in python method to sort the list.
#
#Overall plan
# 1. Print introduction
# 2. Create sorte lists for 1000,10000, and 100000 random integers
# 3. Get time for linear search
# 4. Get time for binary search
# 5. Print the time comparisons of each
#
#

from random import *
from time import *

# the creation of a list of random numbers
def theList(numberOfItems):
    randomList = [randint(0,numberOfItems) for i in range(numberOfItems)]
    randomList.sort()
    return randomList


def linearSearch(numbers,numberList):
    # measuring the how much time using seconds
    timeStarted = perf_counter()

    # going through the whole list
    for i in range(len(numberList)):
        if numberList[i] == numbers:
            position = i
    position = -1

    return perf_counter() - timeStarted
#an iterative binary search
def binarySearch(numbers,numberList):
    timeStarted = perf_counter()
    low = 0
    high = len(numberList) -1
    while low <= high:

        mid = (low + high)//2
        object = numberList[mid]

        if numbers == object:
            object =  mid

        elif numbers < object:
            high = mid -1

        else:
            low = mid + 1

    position = -1

    return perf_counter() - timeStarted


def timeResults (linearT, binaryT, objects):

    # prints linear search time and binary time
    print("{2} items   \n Linear time = {0} seconds \n Binary time = {1} seconds \n".format(linearT,binaryT,objects))

    file = open("hw12project1.txt", 'a+')
    file.write("{2} items\n Linear time = {0} seconds\n Binary time = {1} seconds\n\n"
               .format(linearT, binaryT, objects))
    file.close()



def main():

    print("Program will now give you the difference of linear search time"
          "and binary search time")

    #Creating the objects  and lists
    object1= 1000
    object2= 10000
    object3= 100000

    list1 =  theList(object1)
    list2 =  theList(object2)
    list3 =  theList(object3)


    timeResults(linearSearch(len(list1) + 1, list1),binarySearch(len(list1)+1, list1), object1)
    timeResults(linearSearch(len(list2) + 1, list2),binarySearch(len(list2)+1, list2), object2)
    timeResults(linearSearch(len(list3) + 1, list3),binarySearch(len(list3)+1, list3), object3)


    print("looking at these results we can say the  binary search is the fastests search")



main()