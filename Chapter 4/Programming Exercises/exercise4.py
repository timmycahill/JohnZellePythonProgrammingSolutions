# exercise4.py
#       Write a program that draws a winter scene with a Christmas tree and a
#   snowman.

import graphics

def main():
    win = graphics.GraphWin("Winter Scene")

    # Draw sky and ground
    win.setBackground("blue")
    ground = graphics.Rectangle(graphics.Point(0, 140), graphics.Point(200, 200))
    ground.setFill("white")
    ground.draw(win)

    # Draw snowman
    snowmanBase = graphics.Circle(graphics.Point(40, 140), 15)
    snowmanBase.setFill("white")
    snowmanBase.setOutline("black")
    snowmanBase.draw(win)
    snowmanTorso = graphics.Circle(graphics.Point(40, 125), 13)
    snowmanTorso.setFill("white")
    snowmanTorso.setOutline("black")
    snowmanTorso.draw(win)
    snowmanHead = graphics.Circle(graphics.Point(40, 112), 11)
    snowmanHead.setFill("white")
    snowmanHead.setOutline("black")
    snowmanHead.draw(win)

    # Draw tree
    treeBase = graphics.Rectangle(graphics.Point(120, 150),
                                  graphics.Point(130, 110))
    treeBase.setFill("brown")
    treeBase.draw(win)
    treeLowNeedles = graphics.Polygon(graphics.Point(110, 140),
                                      graphics.Point(140, 140),
                                      graphics.Point(treeBase.getCenter().getX(),
                                                     110))
    treeLowNeedles.setFill("green")
    treeLowNeedles.draw(win)
    treeMidNeedles = treeLowNeedles.clone()
    treeMidNeedles.move(0, -10)
    treeMidNeedles.draw(win)
    treeHighNeedles = treeMidNeedles.clone()
    treeHighNeedles.move(0, -10)
    treeHighNeedles.draw(win)

main()
