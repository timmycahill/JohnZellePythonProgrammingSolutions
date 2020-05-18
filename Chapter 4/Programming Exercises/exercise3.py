# exercise3.py
#       Write a program that draws some sort of face.

import graphics

def main():
    win = graphics.GraphWin()
    
    # Draw face skin
    skin = graphics.Polygon(graphics.Point(60, 0), graphics.Point(140, 0),
                            graphics.Point(170, 40), graphics.Point(170, 140),
                            graphics.Point(130, 200), graphics.Point(70, 200),
                            graphics.Point(30, 140), graphics.Point(30, 40))
    skin.setFill("tan")
    skin.draw(win)

    # Draw eyes
    leftEye = graphics.Oval(graphics.Point(50, 90), graphics.Point(90, 70))
    leftEye.setFill("white")
    leftEye.draw(win)
    rightEye = leftEye.clone()
    rightEye.move(60, 0)
    rightEye.draw(win)
    leftIris = graphics.Circle(leftEye.getCenter(), (leftEye.getP2().getY()
                               - leftEye.getP1().getY()) / 2)
    leftIris.setFill("skyblue")
    leftIris.draw(win)
    rightIris = leftIris.clone()
    rightIris.move(60, 0)
    rightIris.draw(win)
    leftPupil = graphics.Circle(leftIris.getCenter(), leftIris.getRadius() / 2)
    leftPupil.setFill("black")
    leftPupil.draw(win)
    rightPupil = leftPupil.clone()
    rightPupil.move(60, 0)
    rightPupil.draw(win)

    # Draw Nose
    noseVertical = graphics.Line(graphics.Point(100,100), graphics.Point(110, 140))
    noseVertical.draw(win)
    noseHorizontal = graphics.Line(graphics.Point(90,140), graphics.Point(110, 140))
    noseHorizontal.draw(win)

    # Draw Mouth
    mouth = graphics.Polygon(graphics.Point(70, 160), graphics.Point(130, 160),
                             graphics.Point(110, 180), graphics.Point(90, 180))
    mouth.setFill("black")
    mouth.draw(win)

    
main()
