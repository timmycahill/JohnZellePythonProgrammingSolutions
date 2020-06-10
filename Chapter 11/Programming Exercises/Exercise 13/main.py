# main.py

from card import Card

def main():
	printIntroduction()
	cards = getCards()
	sortCards(cards)
	outputResults(cards)

def printIntroduction():
	print("This program reads in a list of card objects and prints them out " +
		"sorted by suit and rank.\n")

def getCards():
	cardData = readCardData()
	cards = []
	for card in cardData:
		data = card.split()
		cards.append(Card(int(data[0]), data[1]))
		print(Card(int(data[0]), data[1]))
	return cards

def readCardData():
	infile = getFile()
	return infile.readlines()

def getFile():
	infileName = input("Enter the name of the file containing the cards: ")
	return open(infileName, 'r')

def sortCards(cards):
	cards.sort(key=Card.getRank)
	cards.sort(key=Card.getSuit)

def outputResults(cards):
	print("\nSorted Cards:")
	for card in cards:
		print(card)

if __name__ == "__main__":
	main()