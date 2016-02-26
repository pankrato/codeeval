#!/usr/bin/python

#https://www.codeeval.com/open_challenges/235/

import sys

ranks = {'2':0, '3':1, '4':2, '5':3, '6':4, '7':5, '8':6, '9':7, '10':8,
	'J':9, 'Q':10, 'K':11, 'A':12}

trump = 128 # big magic trump number

class Card:
	def __init__(self, card, trumpsuit):
		self.rank = card[:-1]
		self.suit = card[-1]
		#card strenght is its rank + big number if it is a trump
		self.strength = ranks[self.rank] + trump * (self.suit == trumpsuit)

	def __str__(self):
		return '{}{}'.format(self.rank, self.suit)

with open(sys.argv[1], 'r') as f:

	for line in f:
		# parsing the input
		input = line.strip().split('|')
		cards = input[0].split()
		trumpsuit = input[1].strip()
		card1 = Card(cards[0], trumpsuit)
		card2 = Card(cards[1], trumpsuit)

		# logic
		if card1.strength > card2.strength:
			print card1
		if card1.strength < card2.strength:
			print card2
		if card1.strength == card2.strength:
			print card1, card2

