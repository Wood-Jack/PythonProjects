#
# File Name:     LadderAgainstHouse
# Programmer:    Woodrow Jackson
#
#
# Description:   a simple picture with at least 3 graphical objects
#
#

from graphics import *
from math import sqrt

def main():

    #Creating window
    win = GraphWin("Line Segement",500,500)

    #text prompt
    text = Text(Point(150,20), "Click on two points to draw the line segment")
    text.setSize(10)
    text.draw(win)
   #draw window

    point1 = win.getMouse()
    point1.draw(win)
    point2 = win.getMouse()

    line = Line(point1,point2)
    line.setWidth(3)
    line.draw(win)

#Calculations

    middleX = (point1.getX() + point2.getX())/2
    middleY = (point1.getY() + point2.getY()) /2
    middlePoint = Circle(Point(middleX, middleY),2)

    middlePoint.setOutline("red")
    middlePoint.setFill("red")
    middlePoint.draw(win)

#factor in equations

    dx = point2.getX() - point1.getX()
    dy= point2.getY() - point1.getY()

    slope = -dy/dx
    length = sqrt(dx**2 + dy**2)

    text.setText("Slope:" + format(slope, "0.5") + '\nlength: ' + format(length, 0.5) + 'px')
    win.getMouse()




main()