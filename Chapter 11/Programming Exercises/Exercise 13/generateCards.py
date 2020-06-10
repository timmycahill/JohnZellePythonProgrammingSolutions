# generateCards.py

from card import Card
from random import randint

def main():
	printIntroduction()
	n, outfile = getInputs()
	cards = generateCards(n)
	outputResults(cards, outfile)

def printIntroduction():
	print("This program randomly generates a number of cards and saves then in a" +
		" text file.\n")

def getInputs():
	n = int(input("How many cards would you like to generate: "))
	outfileName = input("Enter the name of the file to save them in: ")
	outfile = open(outfileName, 'w')
	return n, outfile

def generateCards(n):
	cards = []
	suits = ['c', 'd', 'h', 's']

	for i in range(n):
		rank = randint(1, 13)
		suit = randint(0, 3)

		cards.append(Card(rank, suits[suit]))

	return cards

def outputResults(cards, outfile):
	for card in cards:
		print(card.getRank(), card.getSuit(), file=outfile)

if __name__ == "__main__":
	main()