#
# File Name:     HW8project1
# Programmer:    Woodrow Jackson
# Date:          07/19/20
#
# Problem Statement: Write a program that converts a color image to grayscale.
# The user supplies the name of a file containing a GIF or PPM image, and the program loads the image
# and displays the file. At the click of the mouse, the program converts the image to grayscale.
# The user is then prompted for a filename to store the grayscale image in.
#
#
# Overall Plan:
# 1. Give an introduction
# 2. Prompt user for image file name
# 3. Display the image
# 4. Convert the image to grayscale using psuedocode
# 5. Display grayscale image
# 6. Prompt user to enter new filename for grayscale image
#


from graphics import *

def main():


    print("Program will convert a color image into grayscale.\n")

    # This will be the input of the program
    imageFileName = input("Enter filename of image: ")

    picture = Image(Point(0, 0), imageFileName)

    picture = Image(Point(picture.getWidth()/2, picture.getHeight()/2), imageFileName)

    win = GraphWin("Image", picture.getWidth(), picture.getHeight())

    picture.draw(win)

    # using psuedo code given
    print("Click  to convert to grayscale")
    win.getMouse()

    for row in range(picture.getWidth()):
        for column in range(picture.getHeight()):
            r, g, b = picture.getPixel(row, column)
            brightness = int(round(0.229 * r + 0.587 * g + 0.114 * b))
            picture.setPixel(row, column, color_rgb(brightness, brightness, brightness))
            win.update()

    # creating the save file for the user to save
    saveFileName = input("Enter new filename to save grayscale image as: ")
    picture.save(saveFileName)
    print("Click image window to exit program")

    win.getMouse()
    win.close()


main()
