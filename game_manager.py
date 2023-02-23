from enum import Enum
import pygame
from classes import *

class GameState(Enum):
  playing = 0
  trump_determine = 1
  kot = 2
  ENDED = 3

class GameManager:
    deck = None
    player1 = None
    player2 = None
    player3 = None
    player4 = None
    trump_caller = False
    team1 = [player1, player3]
    team2 = [player2, player4]
    pile = None
    state = None
    current_player = None
    result = None
  
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        self.player3 = Player("Player 3")
        self.player4 = Player("Player 4")
        self.pile = Pile()
        self.deal()
        self.currentPlayer = self.player1
        self.state = GameState.playing