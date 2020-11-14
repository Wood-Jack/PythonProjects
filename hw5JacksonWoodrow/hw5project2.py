#
#
# Project Name:     readFile_writeFile
# Programmer:    Woodrow Jackson
#
#
# Description: a program that reads a file and then writes into the file
#
def main():
    # creats the fileOpener and reads the input.txt file
    fileOpener = open("input.txt", "r")

    theList = []

    #for- loop look that reads the file line by line
    for line in fileOpener:

        stripped_line = line.strip()

        # takes the line that was stripped and splits them where the spaces are at.
        line_list = stripped_line.split(" ")

        theList.append(line_list)

    fileOpener.close()

    #creates the filewrite and opens it to a new .txt file to write too
    file_writer = open("output.txt", "w")

    #reads off the length of the list and sums the numbers in the list on the same line.
    for i in range(0, len(theList)):

        #adds the two numbers on the same line to get the sum
        adder = int(theList[i][0]) + int(theList[i][1])

        print(adder, file=file_writer)

main()
