#File Name:     hw10project1
# Programmer:    Woodrow Jackson
# Date:          07/26/20
#
# Problem Statement:
#
#
# Overall Plan:
# 1. Display intro
# 2. Ask user for python file
# 3. Use list of python file words
# 4. Use a dictionary of reserved words and how often they are used
# 5. Sort the list
# 7. Program end
#
#

import re


def dictionary(wordCount, wordsInFile):
    counter = {}

    for word in wordsInFile:

        if word in wordsInFile:
            counter[word] = counter.get(word,0) + 1

    return counter

    #creating list of words from the file
def textListOfFile(nameOfFile):

    file = open(nameOfFile, 'r').read()

    code = re.sub(r'(?m)^ *#.*\n?', '',file)

    for ch in '!"#$%&()*+,-.?:;<=>?@[\\]^_`{|}~' :

        filteredCode = code.replace(ch, ' ')

            #splits at white space

        #creating a list of words cleaned
    fileWordList = filteredCode.split()

    return fileWordList

def wordFreq( freqCount ):
    return freqCount[1]

def dictionaryOrganizer(pages):

    words = list(pages.words())
    words.sort()

    words.sort(wordFreq, True)
    return pages

def results(pages,words):

    for i in range(len(pages)):
        word, count = words[i]
        print("{0:<10}{1:>5}".format(word, count))

def main():

    theFile = input("Enter Python file to count reserved words")

    fileWords = textListOfFile(theFile)

    reservedKeywords = textListOfFile("Reserved.txt")


    counter = dictionary(reservedKeywords, fileWords)

    pages = sorted(counter)

    results(counter,pages)

main()