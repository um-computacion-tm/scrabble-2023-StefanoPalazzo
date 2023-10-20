from game.board import Board
from game.player import Player
from game.models import BagTiles, Tile
from game.cell import Cell
from game.tools import Tools
from unidecode import unidecode

class WordDoesntFitOnBoardException(Exception):
    pass

class UserDoesntHaveTilesException(Exception):
    pass

class wordDoesntPassesByTheCenterException(Exception):
    pass

class WordIsNotConnectedException(Exception):    
    pass

class WordEntersInConflictWithOtherWordsException(Exception):
    pass

class WordIsNotNewException(Exception):
    pass

class WordIsNotInDictionaryException(Exception):
    pass

class WordCreatesNonValidWordsWithTheExistingOnes(Exception):
    pass


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
            raise WordDoesntFitOnBoardException("Error! The word doesn't fit on the board. Please choose a valid location.")
        
        v2 = self.board.validate_tiles_for_word(word, location, orientation, playerTiles)
        if not v2[0] and v2[1]: 
            raise UserDoesntHaveTilesException ('Error! User does not have required tiles')
        elif v2[0] and not v2[1]:
            raise WordIsNotNewException ('Error! User is not creating a new word.')
            
        v3 = self.board.validate_word_is_connected(word, location, orientation)
        if not v3 and self.board.grid[7][7].letter.letter == ' ':
            raise wordDoesntPassesByTheCenterException ('Error! Word does not passes by the center. Try with [8][8]')
        elif not v3:
            raise WordIsNotConnectedException ('Error! Word is not connected to others')
        
        v4 = self.board.validate_word_overlapping_is_possible(word, location, orientation)
        if not v4:
            raise WordEntersInConflictWithOtherWordsException ('Error! Word enters in conflict with other words.')

        v5 = Tools().validate_word_in_dictionary_txt(word)
        
        if not v5:
            v6 = Tools().validate_word_in_RAE(word)
            if not v6:
                raise WordIsNotInDictionaryException ('Error! Word was not found in RAE dictionary')
        
        v6 = self.board.validate_word_creates_valid_words_in_each_cell(word, location, orientation)
        
        if not v6[0]:
            raise WordCreatesNonValidWordsWithTheExistingOnes('Error! Any of the words created by your word is not valid.')
        
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

        # Calculates the score of the word and adds it to the player's score
        word_cells = self.board.cells_of_word_in_board(word, location , orientation)
        self.players[self.turn].score += Tools().calculate_word_value(word_cells)

        # Calculate the score of the new words created from each letter of the word
        for i in v6[1]:
            NewWordCells = self.board.cells_of_word_in_board(i[0], i[1], i[2])
            self.players[self.turn].score += Tools().calculate_word_value(NewWordCells)


        return ('Word succesfully colocated.')

    





    

    

                
