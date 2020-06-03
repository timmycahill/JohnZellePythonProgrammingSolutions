# exercise8.py
#       Blackjack (twenty-one) is a casino game played with cards. The
#   goal of the game is to draw cards that total as close to 21 points
#   as possible without going over. All face cards count as 10 points,
#   aces count as 1 or 11, and all other cards count their numeric value.
#       The game is played against a dealer. The player tries to get
#   closer to 21 (without going over) than the dealer. If the dealer
#   busts (goes over 21), the player automatically wins (provided the
#   player had not already busted). The dealer must always take cards
#   according to a fixed set of rules. The dealer takes cards until he
#   or she achieves a total of at least 17. If the dealer's hand contains
#   an ace, it will be counted as 11 when that results in a total
#   between 17 and 21 inclusive; otherwise, the ace is counted as 1.
#       Write a program that simulates multiple games of blackjack and
#   estimates the probability that the dealer will bust. Hints: treat
#   the deck of cards as infinite (casinos use a "shoe" containing many
#   decks). You do not need to keep track of the cards in the hand,
#   just the total so far (treating an ace as 1) and a bool variable
#   hasAce that tells whether or not the hand contains an ace. A hand
#   containing an ace should have 10 points added to the total exactly
#   when doing so would produce a stopping total (something between 17
#   and 21 inclusive).

from random import randint

def main():
    printIntroduction()
    n = getInputs()
    gamesBusted = simulateNGames(n)
    outputResults(gamesBusted, n)

def printIntroduction():
    print("This game simulates a number of blackjack games and calculates " +
          "the probability that the dealer will bust.\n")

def getInputs():
    return int(input("Enter the number of games to simulate: "))

def simulateNGames(n):
    gamesDealerBusted = 0
    for i in range(n):
        dealerBusted  = simulateGame()

        if dealerBusted:
            gamesDealerBusted += 1

    return gamesDealerBusted

def simulateGame():
    dealerBusted = False
    
    playerBusted = simulateTurn()
    if not playerBusted:
        dealerBusted = simulateTurn()
    return dealerBusted

def simulateTurn():
    busted = False
    total = 0
    hasAce = False
    while total < 17:
        card = drawCard()
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
    if total > 21:
        busted = True
    return busted

def drawCard():
    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    return cards[randint(0, 12)]    
    
def outputResults(gamesBusted, n):
    print("\nGames played:", n)
    print("Hands dealer busted:", gamesBusted)
    print("Probability dealer will bust:", gamesBusted / n)
    
if __name__ == "__main__":
    main()
