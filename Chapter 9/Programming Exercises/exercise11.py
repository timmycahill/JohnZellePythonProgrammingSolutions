# exercise11.py
#       Write a program that performs a simulation to estimate the probability of rolling five-of-a-kind in a single roll of five
#   six-sided dice.

from random import randint

def main():
    printIntroduction()
    n = getInputs()
    probability = estimateProbability(n)
    outputResults(probability)

def printIntroduction():
    print("This program uses simulations to estimate the probability of rolling five-of-a-kind with fice six-sided dice.\n")

def getInputs():
    return int(input("How many times would you like to roll: "))

def estimateProbability(n):
    hits = 0
    for i in range(n):
        fiveOfAKind = rollForFive()
        if fiveOfAKind:
            hits += 1
    probability = hits / n
    return probability

def rollForFive():
    startingRoll = rollDie()
    for i in range(4):
        die = rollDie()
        if die != startingRoll:
            return False
    return True

def rollDie():
    return randint(1, 6)

def outputResults(probability):
    print("The probability of rolling a five-of-a-kind is {0:0.2%}".format(probability))

if __name__ == "__main__":
    main()
