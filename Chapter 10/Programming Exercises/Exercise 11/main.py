# main.py

from card import Card
from random import randint

def main():
	printIntroduction()
	n = getInputs()
	cards = generateCards(n)
	outputResults(cards)

def printIntroduction():
	print("This program randomly generates a number of cards and returns their blackjack value.\n")

def getInputs():
	return int(input("How many cards would you like to generate: "))

def generateCards(n):
	cards = []
	suits = ['c', 'd', 'h', 's']

	for i in range(n):
		rank = randint(1, 13)
		suit = randint(0, 3)

		cards.append(Card(rank, suits[suit]))

	return cards

def outputResults(cards):
	blackjackTotal = 0

	print()
	for card in cards:
		print(str(card) + ":", card.BJValue())
		blackjackTotal += card.BJValue()
	print("\nBlackjack Total:", blackjackTotal)

if __name__ == "__main__":
	main()