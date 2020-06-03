# exercise15.py
#       (Advanced) Here is a puzzle problem that can be solved with either some fancy analytic geometry (calculus) or a (relatively) simple
#   simulation.
#       Suppose you are located at the exact center of a cube. If you could look all around you in every direction, each wall of the cube would
#   occupy 1/6 of your field of vision. Suppose you move toward one of the walls so that you are now halfway between it and the center of the
#   cube. What fraction of your field of vision is now taken up by the closest wall? Hint: use a Monte Carlo simulation that repeatedly "looks"
#   in a random direction and counts how many times it sees the wall.

from random import randint

def main():
    printIntroduction()
    steps, numSims = getInputs()
    averageClosestWall = performNSimulations(steps, numSims)
    outputResults(averageClosestWall, steps)

def printIntroduction():
    print("This program simulates taking random steps from inside a cube and calculates the fraction of your field of vision taken up " +
          "by the closest wall.")

def getInputs():
    steps = int(input("How many steps would you like to take? "))
    numSims = int(input("How many simulations would you like to perform? "))
    return steps, numSims

def performNSimulations(steps, numSims):
    closestWall = 0
    for i in range(numSims):
        closestWall += calculateClosestWall(steps)
    return closestWall / numSims

def calculateClosestWall(steps):
    stepsPerWall = [0, 0, 0, 0, 0, 0]
    for i in range(steps):
        stepTowardWall(stepsPerWall)
    closestWall = findClosestWall(stepsPerWall)
    closestWallVision = calculateVisionPerSteps(stepsPerWall[closestWall])
    return closestWallVision

def stepTowardWall(walls):
    wall = randint(0, len(walls) - 1)
    walls[wall] = walls[wall] + 1

def findClosestWall(walls):
    closestWall = 0
    closestWallSteps = 0
    for i in range(len(walls)):
        if walls[i] > closestWallSteps:
            closestWall = i
    return closestWall

def calculateVisionPerSteps(steps):
    vision = 1 / 6
    for i in range(steps):
        vision = vision + ((1 - vision) / 2)
    return vision

def outputResults(average, steps):
    print("The closest wall after {0} steps on average takes up {1:0.2%} of your vision.".format(steps, average))
    
if __name__ == "__main__":
    main()
