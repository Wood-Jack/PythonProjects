#File Name:     hw10project2
# Programmer:    Woodrow Jackson
# Date:          07/26/20
#
# Problem Statement:
#
#
# Overall Plan:
# 1. Create a program window
# 2. Create  list of suits
# 3. Create the graphics window
# 4. Get suit entry display suit button
# 5. Loop until Exit button clicked
# 6. Window closed when quit button is clicked
#

from graphics import *
from button import Button


class GraphicInterface:


    # the Graphics window
    def __init__(self):

        #Background
        self.win.setBackground("blue")

        #label display
        labelDisplay = Text(Point(400,40),"Showing the Suit")
        labelDisplay.setSize(24)
        labelDisplay.setFill("green")
        labelDisplay.setStyle("bold")
        labelDisplay.draw(self.win)

        self.textbox = Entry(Point(400, 75), 10)
        self.textbox.draw(self.win)

        #Instructions
        guide = Text(Point(400, 75),10)
        guide.setStyle("bold")
        guide.draw(self.win)

        self.suit = dict(spade='Spade.ppm', diamond='Diamond.ppm', heart='Hearts.ppm')
        self.win = GraphWin("Card Display", 800, 600)

        self.imgDisplayRect = Rectangle(Point(325, 160), Point(375, 350))
        self.imgDisplayRect.draw(self.win)

        self.suitButton = Button(self.win, Point(400, 125), 100, 20, "Display Suit")
        self.suitButton.activate()

        self.exitButton = Button(self.win, Point(300, 370), 100, 20, "Quit")
        self.exitButton.activate()

        self.displaySuit()



    def displaySuit(self):

        clicker = self.win.getMouse()


        while not self.exitButton.clicked(clicker):


            if self.suitButton.clicked(clicker) \
                    and self.textbox.getText() != '':

                self.imgDisplayRect.setfill('white')
                inputText = self.textbox.getText()


                suitImage = Image(Point(400,350), self.suit[inputText])
                suitImage.draw(self.win)


            clicker = self.win.getMouse()

        self.win.close()


def main():

    GraphicInterface()


    if __name__ == '__main__':
        main()


