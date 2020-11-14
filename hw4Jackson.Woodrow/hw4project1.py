

#
# File Name:     DrawingObjects
# Programmer:    Woodrow Jackson
#
#
# Description:   a simple picture with at least 3 graphical objects
#
#

from graphics import *

def main():
    win = GraphWin("My Objects", 200, 200)
    c = Circle(Point(50, 50), 10)
    r =Rectangle(Point(60,70),Point(30,30))
    s =Rectangle(Point(90,90),Point(70,70))
    s.draw(win)
    c.draw(win)
    r.draw(win)

    win.getMouse()  # Pause to view result
    win.close()    # Close window when donemain(

main()