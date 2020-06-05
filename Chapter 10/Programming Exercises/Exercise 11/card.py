# card.py

class Card:
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit.upper()

	def getRank(self):
		return self.rank

	def getSuit(self):
		return self.suit

	def BJValue(self):
		if self.rank <= 10:
			return self.rank
		else:
			return 10

	def __str__(self):
		rank = self.rank
		suit = self.suit

		if rank == 1:
			rank = "Ace"
		elif rank == 2:
			rank = "Two"
		elif rank == 3:
			rank = "Three"
		elif rank == 4:
			rank = "Four"
		elif rank == 5:
			rank = "Five"
		elif rank == 6:
			rank = "Six"
		elif rank == 7:
			rank = "Seven"
		elif rank == 8:
			rank = "Eight"
		elif rank == 9:
			rank = "Nine"
		elif rank == 10:
			rank = "Ten"
		elif rank == 11:
			rank = "Jack"
		elif rank == 12:
			rank = "Queen"
		else:
			rank = "King"

		if suit == "C":
			suit = "Clubs"
		elif suit == "D":
			suit = "Diamonds"
		elif suit == "H":
			suit = "Hearts"
		else:
			suit = "Spades"

		return rank + " of " + suit