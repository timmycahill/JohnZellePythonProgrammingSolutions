# exercise1.py
#       Revise the racquetball simulation so that it computes the results for best of n game matches. First
#   service alternates, so Player A serves first in the odd games of the match, and player B serves first in the
#   even games.

from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNMatches(n, probA, probB)
    printSummary(winsA, winsB)

def printIntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The abilities of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving.")

def getInputs():
    # Returns the three simulation parameters
    a = eval(input("What is the prob. player A wins a serve? "))
    b = eval(input("What is the prob. player B wins a serve? "))
    n = eval(input("How many matches to simulate? "))
    return a, b, n

def simNMatches(n, probA, probB):
    # Simulates n matches of racquetball between players whose
    #   abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    winsA = winsB = 0
    for i in range(n):
        gamesWonA, gamesWonB = simOneMatch(probA, probB)
        if gamesWonA > gamesWonB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneMatch(probA, probB):
    # Simulates a single match of racquetball between players whose
    #   abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    numGames = 3        # According to google a standarad match has 3 games
    winsA, winsB = simNGames(numGames, probA, probB)
    return winsA, winsB

def simNGames(n, probA, probB):
    # Simulates n games of racquetball between players whose
    #   abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB, i + 1)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
##        # Return results if either player wins over half the games
##        if winsA > n / 2 or winsB > n / 2:
##            return winsA, winsB
    return winsA, winsB

def simOneGame(probA, probB, gameNumber):
    # Simulates a single game of racquetball between players whose
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
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over. False otherwise.
    return a==15 or b==15

def printSummary(winsA, winsB):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print("\nGames simulated:", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))

if __name__ == '__main__': main()

