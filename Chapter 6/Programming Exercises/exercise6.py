# exercise6.py
#       Write a function that computes the area of a triangle given the length
#   of its three sides as parameters (see Programming Exercise 9 from Chapter 3.)
#   Use your function to augment triangle2.py so that it also displays the area
#   of the triangle.

import math
from graphics import *

def computeTriangleArea(sideA, sideB, sideC):
    s = (sideA + sideB + sideC) / 2
    return math.sqrt(s * (s - sideA) * (s - sideB) * (s - sideC))

def square(x):
    return x * x

def distance(p1, p2):
    dist = math.sqrt(square(p2.getX() - p1.getX())
                     + square(p2.getY() - p1.getY()))
    return dist

def main():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # Use polygon object to draw the triangle
    triangle = Polygon(p1,p2,p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    # Calculate the perimeter of the triangle
    sideA = distance(p1, p2)
    sideB = distance(p2, p3)
    sideC = distance(p3, p1)
    perim = sideA + sideB + sideC
    message.setText("The perimeter is: {0:0.2f}".format(perim))
    win.getMouse()

    # Calculate the area of the triangle
    area = computeTriangleArea(sideA, sideB, sideC)
    message.setText("The area is: {0:0.2f}".format(area))

    # Wait for another click to exit
    win.getMouse()
    win.close()

main()
