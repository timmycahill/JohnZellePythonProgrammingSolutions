# exercise7.py
#       Craps is a dice game played at many casinos. A player rolls a
#   pair of normal six-sided dice. If the initial roll is 2, 3 or 12,
#   the player loses. If the roll is a 7 or 11, the player wins. Any
#   other initial roll causes the player to "roll for point." That is,
#   the player keeps rolling the dice until either rolling a 7 or
#   re-rolling the value of the initial roll. If the player re-rolls
#   the initial value before rolling a 7, it's a win. Rolling a 7 first
#   is a loss.
#       Write a program to simulate multiple games of craps and estimate
#   the probability that the player wins. For example, if the player
#   wins 249 out of 500 games, then the estimated probability of
#   winning is 249/500 = 0.498

from random import randint

def main():
    printIntroduction()
    n = getInputs()
    gamesWon = simulateNGames(n)
    outputResults(gamesWon, n)

def printIntroduction():
    print("This program will simulate a series of craps games.\n")

def getInputs():
    return int(input("How many games would you like to simulate? "))

def simulateNGames(n):
    gamesWon = 0
    point = 0
    for i in range(n):
        win = False
        
        win, point = initialRoll()
        if win == True:
            gamesWon += 1
        elif point != 0:
            win = rollForPoint(point)
            if win == True:
                gamesWon += 1
            point = 0
    return gamesWon

def initialRoll():
    win = False
    point = 0
    
    roll = randint(2, 12)
    if roll == 2 or roll == 3 or roll == 12:
        return win, point
    elif roll == 7 or roll == 11:
        win = True
    else:
        point = roll

    return win, point

def rollForPoint(point):
    win = False
    roll = 0

    while roll != point and roll != 7:
        roll = randint(2, 12)

        if roll == point:
            win = True

    return win

def outputResults(gamesWon, n):
    print("\nGames Played:", n)
    print("Games Won:", gamesWon)
    print("Probability of winning:", gamesWon / n)
    
if __name__ == '__main__':
    main()
            
