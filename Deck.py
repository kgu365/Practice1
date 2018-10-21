# class deck:
# 	def __init__(self):

# 	def shuffle(self):
	
# 	def topcard(self):
SUITS = ["spades", "hearts", "clubs", "diamonds"]
class card:
	def __init__(self, value, suit):
		self._value = value
		self._suit = suit

	def getsuit(self):
		return self._suit
	def getvalue(self):
		return self._value




if __name__ == '__main__':
	Ace_Of_Spades = card(0,0)
	print (Ace_Of_Spades)						

