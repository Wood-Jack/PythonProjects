

# Programmer:    Woodrow Jackson
# Date:          07/26/20
#
# Problem Statement:
#
#
# Overall Plan:
# 1. Create a screen class
# 2. Create window
# 3. add play and exit buttons
# 4. add button functionality
# 5. Use main driver
#
#






from pokerapp import *
from guipoker import *
from button import *
from graphics import *

class Screen(GraphWin):

    def __init__(self,win):
        GraphWin.__init__(self, win , "Dice Poker", 700, 500)

        self.win.setBackground("blue")

        self.label1 = Text(Point(170,80), " Welcome to Poker")
        self.label1.draw(win)
        self.label2 = Text(Point(150, 80), "Play poker using five dice.")
        self.label2.draw(win)
        self.label3 = Text(Point(175,105), " you can have up to re-rolls are allowed")
        self.label3.draw(win)

        self.button_play = Button(win,Point(95,200 - 40), 75 , 35 , "Play")
        self.button_play.activate()
        self.button_exit = Button(win,Point(305, 250-40), 75, 35, "Exit")
        self.button_exit.activate()

    def get_response(self,win):

        while True:
            i = self.win.checkMouse()
            if i and self.button_play.clicked(i):
                self.button_play.label.undraw()
                self.button_play.deactivate()
                self.button_play.rect.undraw()
                self.button_exit.label.undraw()
                self.button_exit.deactivate()
                self.button_exit.rect.undraw()
                self.label1.undraw()
                self.label2.undraw()
                self.label3.undraw()
                return True


            if i and self.button_exit.clicked(i):
                self.win.close()
                return False



