# main.py

from card import Card
from generateCards import generateCards

def main():
	printIntroduction()
	hand = generateHand()
	handName = analyzeHand(hand)
	outputResults(hand, handName)

def printIntroduction():
	print("This program generates a random poker and outputs it's name.\n")

def generateHand():
	hand = []

	while len(hand) < 5:
		hand += generateCards(5 - len(hand))

		for i in range(len(hand) - 1):
			j = i + 1
			while j < len(hand):
				if str(hand[i]) == str(hand[j]):
					del hand[j]
					j -= 1
				j += 1

	return hand
 
def sortHand(hand):
	hand.sort(key=Card.getRank)
	hand.sort(key=Card.getSuit)

def analyzeHand(hand):
	rankCounter = countRanks(hand)
	if isRoyalFlush(hand):
		return "Royal Flush"
	elif isStraightFlush(hand):
		return "Straight Flush"
	elif isFourOfAKind(rankCounter):
		return "Four of a Kind"
	elif isFullHouse(rankCounter):
		return "Full House"
	elif isFlush(hand):
		return "Flush"
	elif isStraight(hand):
		return "Straight"
	elif isThreeOfAKind(rankCounter):
		return "Three of a Kind"
	elif isTwoPair(rankCounter):
		return "Two Pair"
	elif isPair(rankCounter):
		return "Pair"
	else:
		return getHighCard(hand) + " High"

def isRoyalFlush(hand):
	if isFlush(hand) and isStraight(hand):
		hand.sort(key=Card.getRank)
		if (hand[0].getRank() == 1 and hand[1].getRank() == 10 and 
			hand[2].getRank() == 11 and hand[3].getRank() == 12 and 
			hand[4].getRank() == 13):
			return True
	return False

def isStraightFlush(hand):
	if isFlush(hand) and isStraight(hand):
		return True
	return False


def isFourOfAKind(rankCounter):
	for count in rankCounter.values():
		if count == 4: 
			return True
	return False

def isFullHouse(rankCounter):
	if isThreeOfAKind(rankCounter) and isPair(rankCounter):
		return True
	return False

def isFlush(hand):
	suit = hand[0].getSuit()

	for card in hand:
		if card.getSuit() != suit:
			return False

	return True

def isStraight(hand):
	hand.sort(key=Card.getRank)
	if hand[0].getRank() == 1 and hand[1].getRank() == 10:
		nextRank = 11
		for i in range(2, len(hand)):
			if hand[i].getRank() != nextRank:
				return False
			nextRank += 1
	else:
		for i in range(len(hand) - 1):
			if hand[i].getRank() + 1 != hand[i+1].getRank():
				return False
	return True


def isThreeOfAKind(rankCounter):
	for count in rankCounter.values():
		if count == 3: 
			return True
	return False

def isTwoPair(rankCounter):
	pairCounter = 0

	for count in rankCounter.values():
		if count == 2: 
			pairCounter += 1

	if pairCounter == 2:
		return True
	return False

def isPair(rankCounter):
	for count in rankCounter.values():
		if count == 2: 
			return True
	return False

def countRanks(hand):
	rankCounter = {}
	for card in hand:
		rank = card.getRank()
		if rank in rankCounter:
			rankCounter[rank] += 1
		else:
			rankCounter[rank] = 1

	return rankCounter

def getHighCard(hand):
	hand.sort(key=Card.getRank)

	if hand[0].getRank() == 1:
		return "Ace"
	else:
		card = str(hand[4])
		card = card.split()
		return card[0]


def outputResults(hand, handName):
	print("\n" + handName + ":")
	for card in hand:
		print("\t" + str(card))

if __name__ == "__main__":
	main()