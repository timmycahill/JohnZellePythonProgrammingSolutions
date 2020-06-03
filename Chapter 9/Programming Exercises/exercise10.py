# exercise10.py
#       Monte Carlo techniques can be used to estimate the value of pi. Suppose you have a round dart board that just fits inside of a square
#   cabinet. If you throw darts randomly, the proportion that hit the dart board vs. those that hit the cabinet (in the corners not covered by
#   the board) will be determined by the relative area of the dart board and the cabinet. If n is the total number of darts randomly thrown (that
#   land within the confines of the cabinet), and h is the number that hit the board, it is easy to show that
#
#                   pi = 4 (h / n)
#
#       Write a program that accepts the "number of darts" as an input and then performs a simulation to estimate pi. Hint: you can use
#   2 * random() - 1 to generate the x and y cooridinates of a random point inside a 2x2 square centered at (0, 0). The point lies inside the
#   inscribed circle if x^2 + y^2 <= 1.

from random import random

def main():
    printIntroduction()
    n = getInputs()
    pi = estimatePi(n)
    outputResults(pi)

def printIntroduction():
    print("This program uses the Monte Carlo technique to estimate the value of pi.\n")

def getInputs():
    return eval(input("Enter the number of darts you would like to be thrown in the simulation: "))

def estimatePi(n):
    hits = 0
    for i in range(n):
        hit = simulateDartThrow()
        if hit:
            hits += 1
    pi = 4 * (hits / n)
    return pi

def simulateDartThrow():
    x = generateCoordinate()
    y = generateCoordinate()

    if x * x + y * y <= 1:
        return True
    else:
        return False

def generateCoordinate():
    return 2 * random() - 1

def outputResults(pi):
    print("\nThe estimation of pi is", pi)

if __name__ == "__main__":
    main()
