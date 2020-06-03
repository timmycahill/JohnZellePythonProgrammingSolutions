# exercise12.py
#       A random walk is a particular kind of probabilistic simulation that models certain statistical systems such as the Brownian motion
#   of molecules. You can think of a one-dimensional random walk in terms of coin flipping. Suppose you are standing on a very long straight
#   sidewalk that extends both in front of and behind you. You flip a coin. If it comes up heads, you take a step forward; tails means to take
#   a step backward.
#       Suppose you take a random walk of n steps. On average, how many steps away from the starting point will you end up? Write a program
#   to help you investigate this question.

from random import randint

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
    totalSteps = 0
    for i in range(numSims):
        totalSteps += abs(randomWalk(steps))
    averageSteps = totalSteps / numSims
    return averageSteps

def randomWalk(steps):
    position = 0

    for i in range(steps):
        if randint(1, 2) % 2 == 0:
            position += 1
        else:
            position -= 1

    return position

def outputResults(averageSteps, steps):
    print("\nOn average, if you take {0} random steps you will be {1} steps away from your starting point.".format(steps, averageSteps))

if __name__ == "__main__":
    main()
