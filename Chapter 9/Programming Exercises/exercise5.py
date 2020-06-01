# exercise5.py
#       Design and implement a system that compares regular volleyball games to those using rally scoring. Your
#   program should be able to investigate whether rally scoring magnifies, reduces or has no effect on the relative
#   advantage enjoyed by the better team.

from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    regWinsA, regWinsB = simNRegGames(n, probA, probB)
    rallyWinsA, rallyWinsB = simNRallyGames(n, probA, probB)
    
    printSummary(regWinsA, regWinsB, rallyWinsA, rallyWinsB)

############################################################
#
#   Intro Function
#
############################################################

def printIntro():
    print("This program simulates a game of volleyball between two")
    print('teams called "A" and "B". The abilities of each team is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the team wins the point when serving.")

############################################################
#
#   Input Function
#
############################################################

def getInputs():
    # Returns the three simulation parameters
    a = eval(input("What is the prob. team A wins a serve? "))
    b = eval(input("What is the prob. team B wins a serve? "))
    n = eval(input("How many games to simulate? "))
    return a, b, n

############################################################
#
#   Rally Functions
#
############################################################

def simNRallyGames(n, probA, probB):
    # Simulates n games of rally volleyball between teams whose
    #   abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneRallyGame(probA, probB, i + 1)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneRallyGame(probA, probB, gameNumber):
    # Simulates a single game of rally volleyball between teams whose
    #   abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    if gameNumber % 2 == 1:
        serving = "A"
    else:
        serving = "B"
        
    scoreA = 0
    scoreB = 0
    while not gameOverRally(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                scoreB = scoreB + 1
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                scoreA = scoreA + 1
                serving = "A"
    return scoreA, scoreB

def gameOverRally(a, b):
    # a and b represent scores for a rally volleyball game
    # Returns True if the game is over. False otherwise.
    return (a >= 25 and a - b > 1) or (b >= 25 and b - a > 1)

############################################################
#
#   Regular Functions
#
############################################################

def simNRegGames(n, probA, probB):
    # Simulates n games of regular volleyball between teams whose
    #   abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneRegGame(probA, probB, i + 1)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneRegGame(probA, probB, gameNumber):
    # Simulates a single game of regular volleyball between teams whose
    #   abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    if gameNumber % 2 == 1:
        serving = "A"
    else:
        serving = "B"
        
    scoreA = 0
    scoreB = 0
    while not gameOverReg(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOverReg(a, b):
    # a and b represent scores for a regular volleyball game
    # Returns True if the game is over. False otherwise.
    return (a >= 15 and a - b > 1) or (b >= 15 and b - a > 1)

############################################################
#
#   Output Function
#
############################################################

def printSummary(regWinsA, regWinsB, rallyWinsA, rallyWinsB):
    # Prints a summary of wins for each player.
    n = regWinsA + regWinsB
    print("\nGames simulated:", n)
    print("\nRegular Games:")
    print("Wins for A: {0} ({1:0.1%})".format(regWinsA, regWinsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(regWinsB, regWinsB/n))
    
    print("\nRally Wins:")
    print("Wins for A: {0} ({1:0.1%})".format(rallyWinsA, rallyWinsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(rallyWinsB, rallyWinsB/n))
    

if __name__ == '__main__': main()
