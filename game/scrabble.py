from game.board import Board
from game.player import Player
from game.models import BagTiles, Tile
from game.cell import Cell
from game.tools import Tools




class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        for _ in range(players_count):
            self.players.append(Player(self))
        self.turn = 0
    
    def next_turn(self):
        self.turn += 1
        if self.turn >= len(self.players):
            self.turn = 0
        
    def validate_and_put_word (self,word, location, orientation):
        playerTiles = self.players[self.turn].tiles
        v1 = self.board.validate_word_inside_board(word,location, orientation)
        if not v1:
            return ("Error! The word doesn't fit on the board. Please choose a valid location.")
        
        v2 = self.board.validate_tiles_for_word(word, location, orientation, playerTiles)
        if not v2: 
            return ('Error! User does not have required tiles')

        v3 = self.board.validate_word_is_connected(word, location, orientation)
        if not v3 and self.board.grid[7][7].letter.letter == ' ':
            return ('Error! Word does not passes by the center. Try with [8][8]')
        elif not v3:
            return ('Error! Word is not connected to others')
        
        v4 = self.board.validate_word_overlapping_is_possible(word, location, orientation)
        if not v4:
            return ('Error! Word enters in conflict with other words.')

        v5 = Tools().validate_word_in_RAE(word)
        if not v5:
            return ('Error! Word was not found in RAE dictionary')
        
        wordToColocate = []
        N = location[0] - 1
        M = location[1] - 1 
        for i in word:
            if self.board.grid[N][M].letter.letter != ' ':        # Checks if the cell is empty     
                    wordToColocate.append(self.board.grid[N][M].letter)  # Appends the tile in the board
            else:
                for j in playerTiles: 
                    if i == j.letter:
                        wordToColocate.append(playerTiles.pop(playerTiles.index(j))) # Appends the tile of the user
                        break
            if orientation == 'H':
                M += 1
            elif orientation == 'V':
                N += 1

            
        self.board.put_words(wordToColocate, location, orientation)
        playerTiles.extend(self.bag_tiles.take(len(word)))  # User takes tiles from the bag
        # self.players[self.turn].score += Tools().calculate_word_value(wordToColocate)
        return ('Word succesfully colocated.')

    





    

    

                
