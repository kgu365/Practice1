import random
class Deck:
	def __init__(self):
		SUITS = ["spades", "hearts", "clubs", "diamonds"]

		self.deck = []
		
		for i in range(13):
			for j in SUITS:
				self.deck.append(Card(i, j))

		
		
		

	def shuffle(self):
		r_deck = []

		r_deck2 = []
		for i in self.deck:
			r_deck.append(i)

			
		for j in range(len(self.deck)):
			
			index = random.randint(0,51 - j)
			pcard = r_deck.pop(index)
			r_deck2.append(pcard)	

		self.deck = r_deck2
		
			
				

	
	def topcard(self):

		return self.deck.pop()

SUITS = ["spades", "hearts", "clubs", "diamonds"]
class Card:
	def __init__(self, value, suit):
		self._value = value
		self._suit = suit

	def getsuit(self):
		return self._suit
	def getvalue(self):
		return self._value

	def __repr__(self):
		return "Value  is " + str(self.getvalue()) + " " + "Suit is " + str(self.getsuit())

if __name__ == '__main__':
	#making the deck
	deckofcards = Deck()
	
	
	#shuffles deck
	deckofcards.shuffle()

	#returns a random card object and pop it from the deck
	cards = []
	for _ in range(52):
		cards.append(deckofcards.topcard())

	# #should print 52 cards in random order
	for card in cards:
		print(card)
	
	

