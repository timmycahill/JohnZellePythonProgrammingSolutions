# exercise2.py
#       An archery target consists of a central circle of yellow surrounded by
#   concentric rings of red, blue, black and white. Each ring has the same
#   "width," which is the same as the radius of the yellow circle. Write a
#   program that draws such a target. Hint: Objects drawn later will appear on
#   top of objects drawn earlier.

import graphics

def main():
    width = 20
    win = graphics.GraphWin()

    # Create cirlces and set colors
    center = graphics.Point(100, 100)
    yellowCircle = graphics.Circle(center, width)
    yellowCircle.setFill("yellow")
    yellowCircle.setOutline("black")
    redCircle = graphics.Circle(center, yellowCircle.getRadius()+width)
    redCircle.setFill("red")
    redCircle.setOutline("black")
    blueCircle = graphics.Circle(center, redCircle.getRadius()+width)
    blueCircle.setFill("blue")
    blueCircle.setOutline("black")
    blackCircle = graphics.Circle(center, blueCircle.getRadius()+width)
    blackCircle.setFill("black")
    blackCircle.setOutline("black")
    whiteCircle = graphics.Circle(center, blackCircle.getRadius()+width)
    whiteCircle.setFill("white")
    whiteCircle.setOutline("black")

    # Draw circles in the window
    whiteCircle.draw(win)
    blackCircle.draw(win)
    blueCircle.draw(win)
    redCircle.draw(win)
    yellowCircle.draw(win)

main()
