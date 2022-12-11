# importing random module
import random

# Card function that return suit and num value of card
class Card:
	
	# initializing suit and value
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value
		
	def get_suit(self):
		# returning suit
		return self.suit
	
	# returning num value of the card
	def get_value(self):
		if self.value == "ace":
			return 1
		elif self.value == "jack":
			return 10
		elif self.value == "queen":
			return 10
		elif self.value == "king":
			return 10
		else:
			num = self.value
			return num

# deck class
class Deck:
	
	# initalizing empty card deck
	def __init__(self):
		self.cards = []
	
	# drawing random card from the card deck
	def draw_card(self):
		selected_card = random.choice(self.cards)
		self.cards.remove(selected_card)
		return selected_card
	
	# filling up card deck
	def init_deck(self):
		suits = ['hearts', 'diamonds', 'spades', 'clubs']
		values = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']
		
		for suit in suits:
			for value in values:
				lst = []
				lst.append(suit)
				lst.append(value)
				self.cards.append(lst)

# player class
class Player:
	
	# initializing score and name
	def __init__(self, name, deck):
		self.name = name
		self.score = 0
	
	# drawing card and storing the value of card in score
	def drawCard(self, deck):
		lst = deck.draw_card()
		card1 = Card(lst[0], lst[1])
		self.score += card1.get_value()
	
	# returning score of the player
	def get_score(self):
		print(self.name, end=' ')
		print('was dealt a hand with a value of ', self.score)
	
	# printing out busted message when player goes bust
	def get_busted(self):
		print(self.name, 'BUSTED with a total value of', self.score, end='!')
		print()
	
	# printing out win message when player wins
	def win(self):
		print('\n**', self.name, end='')
		print(', You Win **\n')
		
	# printing out lose message when player lose
	def loose(self):
		print('\n**', self.name, end='')
		print(', You lose **\n')

# dealer class
class Dealer:
	
	# initializing dealer name to dealer since its not gone change
	def __init__(self, deck):
		self.name = 'Dealer'
		self.score = 0
	
	# drawing card and adding it to dealer score
	def drawCard(self, deck):
		lst = deck.draw_card()
		card1 = Card(lst[0], lst[1])
		self.score += card1.get_value()
	
	# printing out dealer score
	def get_score(self):
		print(self.name, end=' ')
		print('was dealt a hand with a value of ', self.score)
	
	# printing out bust message when dealer bust
	def get_busted(self):
		print(self.name, 'BUSTED with a total value of', self.score, end='!')
		print()
		
# blackjack game function
class BlackjackGame:
	
	# initializing deck with Deck class and, palyer and dealer to None
	def __init__(self):
		self.deck = Deck()
		self.player = None
		self.dealer = None
	
	# function to play the game
	def play_game(self):
		
		# priming the user response so player atleast a round
		user_response = 'Y'
		
		# looping until user says y
		while user_response == 'Y' or user_response == 'y':
			
			# initializing the deck
			self.deck.init_deck()
			# asking for player name
			name = input('What\'s your name?: ')
			# assigning player and dealer class
			self.player = Player(name, self.deck)
			self.dealer = Dealer(self.deck)
			
			# drawing two cards for player and dealer
			self.player.drawCard(self.deck)
			self.player.drawCard(self.deck)
			self.dealer.drawCard(self.deck)
			self.dealer.drawCard(self.deck)
			
			# printing out user score after drawing two cards
			self.player.get_score()
			
			# asking if user would like to take another card
			user_input = input('Would you like to take another card? (Y/N): ')
			
			# looping until user keep take more cards
			while user_input == 'Y' or user_input == 'y':
				
				# drawing card for both dealer and player, and updating there total
				self.player.drawCard(self.deck)
				self.dealer.drawCard(self.deck)
				
				# if player or dealer goes bust break the inner loop
				if self.player.score > 21:
					break
				
				if self.dealer.score > 21:
					break
				
				# displaying player score after drawing a card if he hasn't gone bust
				self.player.get_score()
				
				# asking if user would like to take  another card
				user_input = input('Would you like to take another card? (Y/N): ')
				
			# outputing result according to player and dealer total card value
			if self.player.score > 21:
				self.player.get_busted()
				self.player.loose()
			elif self.dealer.score > 21:
				self.dealer.get_busted()
				self.player.win()
			elif self.player.score >= self.dealer.score:
				self.dealer.get_score()
				self.player.win()
			elif self.player.score < self.dealer.score:
				self.dealer.get_score()
				self.player.loose()
			
			# asking if user would like to play again
			user_response = input('Would you like to play again? (Y/N): ')
		
		print('Thanks for playing!')
			
game = BlackjackGame()
game.play_game()