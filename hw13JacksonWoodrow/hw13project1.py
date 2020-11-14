#
#
# File Name:     hw13Project1 (StandardSort,SelSort, And merge sort times)
# Programmer:    Woodrow Jackson
#
#
# Description:   Compare the sort times of python standard sort,
# selection sort and merge sort for the list sizes of 5000, 50000, and 500000
# (if this exceeds 30 minutes just put did not finish).
#
# Overall Plan:
#
# 1. Print introduction
# 2. Create sorted lists containing 5000, 50000, and 500000
#       random integers
# 3. Implement merge sort from book algorithm pg 374
# 4. Implement selection sort from book algorithm pg 372
# 5. Get time it takes to run each sort on each list
# 6. Print time comparisons
#

from time import *
from random import *


# Using some code in hw12project1 has some similiar fundtions
def theList(numberOfItems):
    randomList = [randint(0,numberOfItems) for i in range(numberOfItems)]
    randomList.sort()
    return randomList


#implementation helper for merge sort from book
def merge(lst1, lst2, lst3):

    i1= i2 =i3 = 0
    n1, n2 = len(lst1), len(lst2)

    #loop with both pieces have data
    while i1 < n1 and i2 < n2:
        if lst1[i1] < lst2[i2]:  # copy from lst1
            lst3[i3] = lst1[i1]
            i1 = i1 + 1
        else:  # copy from list2
            lst3[i3] = lst2[i2]
            i2 = i2 + 1
        i3 = i3 + 1  # item added to lst3

        # Here either lst1 or lst2 is done, One of the following loops will
        # execute to finish up the merge.

        # Copy remaining items (if any) from lst1
    while i1 < len(lst1):
        lst3[i3] = lst1[i1]
        i1 = i1 + 1
        i3 = i3 + 1
        # Copy remaining items (if any) from lst2
    while i2 < len(lst2):
        lst3[i3] = lst2[i2]
        i2 = i2 + 1
        i3 = i3 + 1

#using merge sort from book pg 375

def mergeSort(nums):

    # Put items of nums in ascending order
    n = len(nums)
    # Do nothing is nums contains 0 or 1 items
    if n > 1:
        # split into two sublists
        m = n // 2
        lst1, lst2 = nums[:m], nums[m:]
        # recursively sort each piece
        mergeSort(lst1)
        mergeSort(lst2)
        # merge the sorted pieces
        merge(lst1, lst2, nums)


# implementation of selection found in book
def selSort(numbers):

    # sort nums into ascending order
    n = len(numbers)

    # For each position in the list (except the very last)
    for bottom in range(n - 1):
        # find the smallest item in nums[bottom]..nums[n-1]
        mp = bottom  # bottom is smallest initially
        for i in range(bottom + 1, n):  # look at each position
            if numbers[i] < numbers[mp]:  # this one is smaller
                mp = i  # remember its index
        # swap smallest item to the bottom
        numbers[bottom], numbers[mp] = numbers[mp], numbers[bottom]

def timedResults (standSort, selSort, mergeSort, objects):

    # prints standard,selsort,mergeSort times of program
    print("{3} items   \n Standard time = {0} seconds \n SelSort time = {1} seconds \n MergeSort time = {3} \n".format(standSort, selSort, mergeSort,objects))

    file = open("hw13project1.txt", 'w')
    file.write("{3} items   \n Standard time = {0} seconds \n SelSort time = {1} seconds \n MergeSort time = {3} \n"
               .format(standSort, selSort, mergeSort, objects))
    file.close()


def main():

    #using code from homework12Project1 due to the similarties
    # Creating the objects  and lists
    object1 = 5000
    object2 = 50000
    object3 = 500000

    list1 = theList(object1)
    list2 = theList(object2)
    list3 = theList(object3)

    #5000 numbers

    standSortTime = perf_counter()
    list1.sort()
    standSortTime = perf_counter() - standSortTime

    # selection sort time
    selSortTime = perf_counter()
    selSort(list1)
    selSortTime = perf_counter() - selSortTime

    # merge sort time
    mergeSortTime = perf_counter()
    mergeSort(list1)
    mergeSortTime = perf_counter() - mergeSortTime
    # display time comparisons
    timedResults(round(standSortTime, 2),
                     round(selSortTime, 2),
                     round(mergeSortTime, 2),
                     object1)

    # 50000 numbers

    # standard sort time
    standSortTime = perf_counter()
    list2.sort()
    standSortTime = perf_counter() - standSortTime

    # selection sort time
    selSortTime = perf_counter()
    selSort(list2)
    selSortTime = perf_counter() - selSortTime
    # merge sort time
    mergeSortTime = perf_counter()
    mergeSort(list2)
    mergeSortTime = perf_counter() - mergeSortTime
    # display time comparisons
    timedResults(round(standSortTime, 2),
                     round(selSortTime, 2),
                     round(mergeSortTime, 2),
                     object2)

    # 500000 numbers

    # standard sort time
    standSortTime = perf_counter()
    list3.sort()
    standSortTime = perf_counter() - standSortTime
    # selection sort time
    selSortTime = perf_counter()
    selSort(list3)
    selSortTime = perf_counter() - selSortTime
    # merge sort time
    mergeSortTime = perf_counter()
    mergeSort(list3)
    mergeSortTime = perf_counter() - mergeSortTime
    # display time comparisons
    timedResults(round(standSortTime, 2),
                     round(selSortTime, 2),
                     round(mergeSortTime, 2),
                     object3)


main()