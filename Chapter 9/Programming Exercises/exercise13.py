# exercise13.py
#       Suppose you are doing a random walk (see previous problem) on the blocks of a city street. At each "step" you choose to walk one block
#   (at random) either forward, backward, left or right. In n steps, how far do you expect to be from your starting point? Write a program that
#   helps answer this question.

from random import randint
from math import sqrt

def main():
    printIntroduction()
    steps, numSims = getInputs()
    averageSteps = simulateAverageSteps(steps, numSims)
    outputResults(averageSteps, steps)

def printIntroduction():
    print("This program simulates the average steps away from a starting point by performing a random walk.\n")

def getInputs():
    steps = int(input("How many steps would you like to take in each simulation: "))
    numSims = int(input("How many simulations would you like to perform: "))
    return steps, numSims

def simulateAverageSteps(steps, numSims):
    distance = 0
    for i in range(numSims):
        stepX, stepY = randomWalk(steps)
        distance += stepsFromStart(stepX, stepY)
    averageSteps = distance / numSims
    return averageSteps

def randomWalk(steps):
    xPosition = 0
    yPosition = 0

    for i in range(steps):
        direction = randint(1, 4)
        if direction == 1:
            xPosition += 1
        elif direction == 2:
            xPosition -= 1
        elif direction == 3:
            yPosition += 1
        else:
            yPosition -= 1

    return xPosition, yPosition

def stepsFromStart(x, y):
    return sqrt(x*x + y*y)

def outputResults(averageSteps, steps):
    print("\nOn average, if you take {0} random steps you will be {1} steps away from your starting point.".format(steps, averageSteps))

if __name__ == "__main__":
    main()
