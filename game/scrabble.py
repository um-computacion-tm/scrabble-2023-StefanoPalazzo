from game.board import Board
from game.player import Player
from game.models import BagTiles



class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        for _ in range(players_count):
            self.players.append(Player(self))
        self.turn = 0
    
    def playing(self):
        return True
    
    def next_turn(self):
        self.turn += 1
        if self.turn >= len(self.players):
            self.turn = 0


