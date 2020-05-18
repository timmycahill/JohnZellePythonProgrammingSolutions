# exercise1.py
#       Alter the program from the last discussion question in the following
#   ways:
#           (a) Make it draw squares instead of circles.
#           (b) Have each successive click draw an additional square on the
#               screen (rather than moving the existing one).
#           (c) Print a message on the window "Click again to quit" after
#               the loop, and wait for a final click before closing the window.

from graphics import *

def main():
    win = GraphWin()
    shape = Rectangle(Point(30, 30), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        newShape = shape.clone()
        newShape.move(dx,dy)
        newShape.draw(win)
    Text(Point(100,100), "Click again to quit").draw(win)
    win.getMouse()
    win.close()
main()
