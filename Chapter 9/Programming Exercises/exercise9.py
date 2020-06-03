# exercise9.py
#       A blackjack dealer always starts with one card showing. It
#   would be useful for a player to know the dealer's bust probability
#   (see previous problem) for each possible starting value. Write a
#   simulation program that runs multiple hands of blackjack for each
#   starting value (ace-10) and estimates the probability that the
#   dealer busts for each starting value.

from random import randint

def main():
    startingCards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    numHandsBusted = []
    
    printIntroduction()
    n = getInputs()

    for card in startingCards:
        numHandsBusted.append(simulateNHands(n, card))
    
    outputResults(startingCards, numHandsBusted, n)

def printIntroduction():
    print("This game simulates a number of blackjack games and calculates " +
          "the probability that the dealer will bust for each starting card.\n")

def getInputs():
    return int(input("Enter the number of hands to simulate: "))

def simulateNHands(n, card):
    handsDealerBusted = 0
    
    for i in range(n):
        dealerBusted  = simulateHand(card)

        if dealerBusted:
            handsDealerBusted += 1

    return handsDealerBusted

def simulateHand(card):
    busted = False
    total = 0
    hasAce = False
    while total < 17:
        if card == 'A':
            if total + 11 <= 21:
                total += 11
                hasAce = True
            else:
                total += 1
        elif card == 'J' or card == 'Q' or card == 'K':
            total += 10
        else:
            total += int(card)

        if total > 21 and hasAce:
            total -= 10
            hasAce = False
            
        card = drawCard()
        
    if total > 21:
        busted = True
    return busted

def drawCard():
    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    return cards[randint(0, 12)]    
    
def outputResults(startingCards, numHandsBusted, n):
    print("\nHands played per card:", n)
    for i in range(len(startingCards)):
        print(startingCards[i] + ":")
        print("\tHands busted:", numHandsBusted[i])
        print("\tProbability dealer busts: {0:0.2%}".format(numHandsBusted[i] / n))
    
if __name__ == "__main__":
    main()
