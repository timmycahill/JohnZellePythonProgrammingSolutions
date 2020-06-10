# deck.py

from card import Card
from random import randrange

class Deck:
	def __init__(self):
		"""Creates a new deck of 52 cards in a standard order."""
		self.deck = []
		suits = ['s', 'h', 'd', 'c']
		ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(rank, suit))

	def shuffle(self):
		"""Randomizes the order of the cards."""
		for i in range(10):
			shuffledDeck = []
			while len(self.deck) != 0:
				shuffledDeck.append(self.deck.pop(randrange(0, len(self.deck))))
			self.deck = shuffledDeck


	def dealCard(self):
		"""Returns a single card from the top of the deck and removes
		the card from the deck."""
		return self.deck.pop(0)

	def cardsLeft(self):
		"""Returns the number of cards remaining in the deck."""
		return len(self.deck)