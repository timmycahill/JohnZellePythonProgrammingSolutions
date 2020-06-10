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
			rankName = "Ace"
		elif rank == 11:
			rankName = "Jack"
		elif rank == 12:
			rankName = "Queen"
		elif rank == 13:
			rankName = "King"
		else:
			rankName = str(rank)

		if suit == "C":
			suit = "Clubs"
		elif suit == "D":
			suit = "Diamonds"
		elif suit == "H":
			suit = "Hearts"
		else:
			suit = "Spades"

		return rankName + " of " + suit