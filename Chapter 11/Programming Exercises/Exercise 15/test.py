# test.py

from deck import Deck

def main():
	printIntroduction()
	n = getInputs()
	deck = Deck()
	deck.shuffle()
	dealtCards = dealNCards(deck, n)
	printDealtCards(dealtCards)

def printIntroduction():
	print("This program simulates shuffling a deck and dealing out a number of " +
		"cards.\n")

def getInputs():
	return int(input("Enter number of cards to deal: "))

def dealNCards(deck, n):
	dealtCards = []
	for i in range(n):
		dealtCards.append(deck.dealCard())
	return dealtCards

def printDealtCards(dealtCards):
	print("Dealt Cards:")
	for card in dealtCards:
		print(str(card))

if __name__ == "__main__":
	main()