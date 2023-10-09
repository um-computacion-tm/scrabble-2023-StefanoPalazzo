from game.board import Board
from game.player import Player
from game.models import BagTiles, Tile
from game.cell import Cell
from game.tools import Tools
from unidecode import unidecode



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
        # palabra = []
        # for i in word:
        #     palabra.append(i)
        playerTiles = self.players[self.turn].tiles
        v1 = self.board.validate_word_inside_board(word,location, orientation)
        if not v1:
            return ("Error! The word doesn't fit on the board. Please choose a valid location.")
        
        v2 = self.board.validate_tiles_for_word(word, location, orientation, playerTiles)
        if not v2[0] and v2[1]: 
            return ('Error! User does not have required tiles')
        elif v2[0] and not v2[1]:
            return ('Error! User is not creating a new word.')
            
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
            if unidecode(self.board.grid[N][M].letter.letter) != ' ':        # Checks if the cell is empty     
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
        playerTiles.extend(self.bag_tiles.take(7 - len(self.players[self.turn].tiles)))  # User takes tiles from the bag
        word_cells = self.board.cells_of_word_in_board(word, location , orientation)
        self.players[self.turn].score += Tools().calculate_word_value(word_cells)
        return ('Word succesfully colocated.')

    





    

    

                
