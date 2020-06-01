# exercise6.py
#       Design and implement a simulation of some other racquet sport (e.g., tennis or table tennis).

from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

############################################################
#
#   Intro Function
#
############################################################

def printIntro():
    print("This program simulates series of table tennis games between 2 players.")

############################################################
#
#   Input Function
#
############################################################

def getInputs():
    # Returns the three simulation parameters
    a = eval(input("What is the prob. player A wins a serve? "))
    b = eval(input("What is the prob. player B wins a serve? "))
    n = eval(input("How many games to simulate? "))
    return a, b, n

############################################################
#
#   Table Tennis Simulation Functions
#
############################################################

def simNGames(n, probA, probB):
    # Simulates n games of table tennis between players whose
    #   abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB, i + 1)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneGame(probA, probB, gameNumber):
    # Simulates a single game of table tennis between players whose
    #   abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    if gameNumber % 2 == 1:
        serving = "A"
    else:
        serving = "B"
        
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                scoreB = scoreB + 1
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                scoreA = scoreA + 1
        if scoreA + scoreB % 2 == 0:
            if serving == "A":
                serving = "B"
            else:
                serving = "A"
                
    return scoreA, scoreB

def gameOver(a, b):
    # a and b represent scores for a table tennis game
    # Returns True if the game is over. False otherwise.
    return (a >= 11 and a - b > 1) or (b >= 11 and b - a > 1)

############################################################
#
#   Output Function
#
############################################################

def printSummary(winsA, winsB):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print("\nGames simulated:", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))
    

if __name__ == '__main__': main()
