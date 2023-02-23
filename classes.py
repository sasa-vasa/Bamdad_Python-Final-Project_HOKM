from enum import Enum
import pygame
import random

class Suits(Enum):
  CLUB = 0
  SPADE = 1
  HEART = 2
  DIAMOND = 3

class Card:
  suit = None
  value = None
  image = None

  def __init__(self, suit, value):
    self.suit = suit
    self.value = value
    self.image = pygame.image.load('images/' + self.suit.name + '-' + str(self.value) + '.svg')

  def __lt__(self, other):
    if self.value < other.value:
        return True
    if self.value == other.value:
        if self.suit < other.suit:
            return True
        else:
            return False
    return False

  def __gt__(self, other):
    if self.value > other.value:
        return True
    if self.value == other.value:
        if self.suit > other.suit:
            return True
        else:
            return False
    return False

class Deck:
  cards = None

  def __init__(self):
    self.cards = []
    for suit in Suits:
      for value in range(1,14):
        self.cards.append(Card(suit, value))

  def shuffle(self):
    random.shuffle(self.cards)

  def deal(self):   
    return self.cards.pop()

  def length(self):
    return len(self.cards)

class Court:          #### each round shall show the court of 4 cards from each player
  cards = None

  def __init__(self):
    self.cards = []

  def add(self, card):       ### shall add card to the court 
    self.cards.append(card)

  def peek(self):
    if (len(self.cards) > 0):
      return self.cards[-1]  #### needs to show playesr card insted of [-1] shall reduce the card added to the court from hand of player 
    else:
      return None

  def popAll(self):    ###### shall be used on each round after the winner of round is deremined
    return self.cards

  def clear(self):
    self.cards = []

  def isWinner(self):
    if (len(self.cards) == 4):
        return (self.cards[-1].value == self.cards[-2].value) ## shal be change to comaring four card based on ""suit""" and value on the courT
    return False

class Player:
  hand = None
  flipKey = None
  snapKey = None
  name = None

  def __init__(self, name, flipKey, snapKey):
    self.hand = []
    self.flipKey = flipKey ############ shall be change
    self.snapKey = snapKey ############ shall be change
    self.name = name

  def draw(self, deck:Deck, how_many:int):
    for i in range(how_many):
      self.hand.append(deck.deal())

  def played_card(self,card):
    return self.hand.remove(card)
