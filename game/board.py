from game.cell import Cell
from game.models import Tile, BagTiles
from game.tools import Tools
from colorama import Fore,Style
from game.player import Player
from unidecode import unidecode


class Board:
    def __init__(self):
        emptyCell = Tile(' ', 1)
        self.grid = [
            [ Cell(emptyCell,1, None) for _ in range(15) ]
            for _ in range(15)
        ]
        for i in range(4):            # Creates the diagonal
            for i in range(7):
                  for j in range (7):
                        if i == 0:
                            self.grid[i][i] = Cell(emptyCell, 3, 'word') # Triple Word
                        elif i == 5:
                            self.grid[i][i] = Cell(emptyCell, 3, 'letter') # Triple letter
                        elif i == 6:
                            self.grid[i][i] = Cell(emptyCell, 2, 'letter')   # Double letter
                        else:
                            self.grid[i][i] = Cell(emptyCell, 2, 'word')  # Double Word
            self.grid[7][0] = Cell(emptyCell, 3, 'word')     # Triple Word
            self.grid[5][1] = Cell(emptyCell, 3, 'letter')   # Triple letter
            self.grid[1][5] = Cell(emptyCell, 3, 'letter')
            self.grid[0][3] = Cell(emptyCell, 2, 'letter')   # Double letter
            self.grid[3][0] = Cell(emptyCell, 2, 'letter')
            self.grid[6][2] = Cell(emptyCell, 2, 'letter')
            self.grid[2][6] = Cell(emptyCell, 2, 'letter')
            self.grid[7][3] = Cell(emptyCell, 2, 'letter')
            Tools.rotate(self.grid)
            self.grid[7][7] = Cell(emptyCell, 2, 'word')

    def show_board(self):
        boardRow = ''
        print ('                    ' + '  1   2   3   4   5   6   7   8   9  10  11  12  13  14  15')
        for i in range(15):
            for j in range(15):
                if self.grid[i][j].letter.letter != ' ':
                        boardRow += '[' + self.grid[i][j].letter.letter + ' ]'
                elif self.grid[i][j].multiplier_type == 'word' and self.grid[i][j].multiplier == 2: 
                    boardRow += f'[{Fore.MAGENTA}{Style.BRIGHT}2W{Style.RESET_ALL}]'
                elif self.grid[i][j].multiplier_type == 'word' and self.grid[i][j].multiplier == 3: 
                    boardRow += f'[{Fore.RED}{Style.BRIGHT}3W{Style.RESET_ALL}]'
                elif self.grid[i][j].multiplier_type == 'letter' and self.grid[i][j].multiplier == 2:
                    boardRow += f'[{Fore.CYAN}{Style.BRIGHT}2L{Style.RESET_ALL}]'
                elif self.grid[i][j].multiplier_type == 'letter' and self.grid[i][j].multiplier == 3:
                    boardRow += f'[{Fore.BLUE}{Style.BRIGHT}2L{Style.RESET_ALL}]'
                else:
                    boardRow += '[ ' + self.grid[i][j].letter.letter + ']'
            if (i+1) <= 9:
                print ('                 '  + str(i+1) + '  ' + boardRow)
            else:
                print ('                 '  + str(i+1) + ' ' + boardRow)
            boardRow = ''

    def put_words(self,word, location, orientation):
        N, M = location[0] - 1 , location[1] - 1
        for i in word:
            self.grid[N][M].letter = i
            if orientation == 'H':
                M += 1
            elif orientation == 'V':
                N += 1
    
    def validate_word_inside_board(self, word,location, orientation):
        word = unidecode(word)
        N, M = location[0] - 1, location[1] - 1 
        if orientation == 'H':
            if (M + len(word )) > 15:
                return False
            else:
                return True
        elif orientation == 'V':
            if (N + len(word)) > 15:
                return False
            else: 
                return True

    def validate_tiles_for_word(self, word, location, orientation, playerTiles):
        word1 = ''
        for i in word:
            if i == 'Ñ':
                word1 += 'Ñ'
            else:
                word1 += unidecode(i)
        word = unidecode(word)
        N, M = location[0] - 1 , location[1] - 1
        playerTilesToVerify = []
        NewWord = False
        
        for i in playerTiles:
            playerTilesToVerify.append(i.letter)    # Creates an array of the letters of the tiles
            # if i.letter == '?':                     # Checks if the user has a wildcard
            #     wildcard = True
        wildcard = self.player_has_a_wildcard(playerTilesToVerify)
        for i in word1:
            if i == self.grid[N][M].letter.letter: 
                pass
            elif i in playerTilesToVerify:
                playerTilesToVerify.remove(i)
                NewWord = True
            elif wildcard:
                self.use_wildcard_as_tile(playerTiles, i, NewWord)
            else:
                return [False, True]    # Aclaration: True does not mean it is a New Word, is just to avoid the error message
                   
            if orientation == 'H':
                M += 1
            elif orientation == 'V':
                N += 1

        return [True, NewWord]
    
    def player_has_a_wildcard(self, playertilestoverify):
        if '?' in playertilestoverify:
            return True
        
    def use_wildcard_as_tile(self, playerTiles, i, NewWord):
        for tile in range(len(playerTiles)):
                    if playerTiles[tile].letter == '?':
                        playerTiles[tile].letter = i
                        NewWord = True
    
    def validate_word_is_connected(self,word, location, orientation):
        word = unidecode(word) 
        N, M = location[0] - 1 , location[1] - 1
        for i in range(len(word)):
            if N < 0 or N >= len(self.grid) or M < 0 or M >= len(self.grid[0]):
                    continue
            
            if N == 7 and M == 7 and self.grid[7][7].letter.letter == ' ':  # Checks that the first word passes through the center
                return True
            if self.grid[N][M].letter.letter != ' ': # Checks that the word is connected by at least one letter to another word
                return True
            
            if self.check_surrounding_positions(N, M):
                return True
                
            if orientation == 'H': 
                M += 1
            elif orientation == 'V':
                N += 1
        return False
    
    def check_surrounding_positions(self, N, M ):
        # Check if any of the surrounding positions are connected to another word
            surrounding_positions = [
                            (N-1, M),
                (N, M-1),             (N, M+1),
                            (N+1, M), 
            ]
            for pos in surrounding_positions:
                J, K = pos
                if self.grid[J][K].letter.letter != ' ':
                    return True
    def validate_word_overlapping_is_possible(self, word, location, orientation):
        N, M = location[0] - 1 , location[1] - 1
        word = unidecode(word)
        for i in word:
            if self.grid[N][M].letter.letter == ' ':
                pass
            elif self.grid[N][M].letter.letter != i:
                return False
            if orientation == 'H':
                M += 1
            elif orientation == 'V':
                N += 1
        return True
    
    def validate_word_creates_valid_words_in_each_cell(self, word, location, orientation):
        if self.grid[7][7].letter.letter == ' ':
            return (True, [])
        if orientation == 'H':
            result, NewWordsAndPositionsArray = self.validate_word_creates_valid_words_in_each_cell_horizontal(word, location, orientation)[0], self.validate_word_creates_valid_words_in_each_cell_horizontal(word, location, orientation)[1]
        if orientation == 'V':
            result, NewWordsAndPositionsArray = self.validate_word_creates_valid_words_in_each_cell_vertical(word, location, orientation)[0], self.validate_word_creates_valid_words_in_each_cell_vertical(word, location, orientation)[1]
    
        return (result, NewWordsAndPositionsArray)
    
    def validate_word_creates_valid_words_in_each_cell_horizontal(self, word, location, orientation):
        N , M= location[0] - 1, location[1] - 1
        firstposition = [N,M]
        lastPosition = [N, M + len(word)-1]
    
        result = True
        NewWordsAndPositionsArray = []
        for i in word:
                if (self.grid[firstposition[0]][firstposition[1]-1].letter.letter != ' ') or (self.grid[lastPosition[0]][lastPosition[1]+1].letter.letter != ' '):  # Checks if it is a letter before or after the word, and returns false
                    result = False
                newWord = '' 
                wordOrientation = 'V'
                
                R = N
                C = M
                if self.should_continue(R, C):
                    continue
                result = result and  self.wordsAndPositions([R, C, i], newWord, wordOrientation, NewWordsAndPositionsArray)
                M += 1
        return (result, NewWordsAndPositionsArray)

    def validate_word_creates_valid_words_in_each_cell_vertical(self, word, location, orientation):
        N = location[0] - 1
        M = location[1] - 1
        firstposition = [N,M]
        lastPosition = [N + len(word)-1, M]
        result = True
        NewWordsAndPositionsArray = []
        for i in word:
                if self.grid[firstposition[0]-1][firstposition[1]].letter.letter != ' ' or self.grid[lastPosition[0]+1][lastPosition[1]].letter.letter != ' ':    # Checks if it is a letter before or after the word, and returns false
                    result = False
                newWord = ''
                wordOrientation = 'H'  
                letter_added_to_new_word = False
                R, C = N, M
                if self.should_continue:
                    continue
                result = result and  self.wordsAndPositions([R, C, i], newWord, wordOrientation, NewWordsAndPositionsArray)
                N += 1
        return (result, NewWordsAndPositionsArray)

    def wordsAndPositions(self, RCI, newWord, wordOrientation, NewWordsAndPositionsArray):
        R, C, i = RCI[0], RCI[1], RCI[2]
        newWord = self.detect_and_create_word_horizontal( R, C, newWord, i)[0]
        NewWordsAndPositionsArray.append([newWord, self.detect_and_create_word_horizontal( R, C, newWord, i)[1], wordOrientation])
        result = Tools().validate_word_in_dictionary_txt(newWord)  # If the word is in the dictionary this will remain True
        return result

    def detect_and_create_word_horizontal(self, R, C, newWord, i):
        letter_added_to_new_word = False
        while self.grid[R-1][C].letter.letter != ' ':    # Checks if the cell on top has a letter and continues until it finds an emptu cell
                R -= 1              
        startPosition = [R+1,C+1]                           # Saves the position of the first letter of the word                           
        newWord += self.grid[R][C].letter.letter       # Adds the first letter of the word
        while self.grid[R+1][C].letter.letter != ' ' or not letter_added_to_new_word:  # Checks if the cell on bottom has a letter and continues until it finds an empty cell
            if self.grid[R+1][C].letter.letter == ' ': # If it finds a blank space for the first time it makes 1 exception to add the letter of the word, this is to avoid adding the letter of the word twice
                newWord += i
                letter_added_to_new_word = True
                R += 1
            else:                                            # If it finds a letter it adds it to the new word
                newWord += self.grid[R+1][C].letter.letter
                R += 1       
        return newWord, startPosition
    
    def detect_and_create_word_vertical(self, R, C, newWord, i):
        letter_added_to_new_word = False
        while self.grid[R][C-1].letter.letter != ' ':    # Checks if the cell on top has a letter and continues until it finds an emptu cell
                C -= 1
        startPosition = [R+1,C+1]                           # Saves the position of the first letter of the word
        newWord += self.grid[R][C].letter.letter       # Adds the first letter of the word
        while self.grid[R][C+1].letter.letter != ' ' or not letter_added_to_new_word:
            if self.grid[R][C+1].letter.letter == ' ':
                newWord += i
                letter_added_to_new_word = True
                C += 1
            else:
                newWord += self.grid[R][C+1].letter.letter
                C += 1
        return newWord, startPosition
    
    def should_continue(self, R, C):
        if self.grid[R-1][C].letter.letter == ' ' and self.grid[R+1][C].letter.letter == ' ' or self.grid[R][C].letter.letter != ' ':
            return True

    def cells_of_word_in_board(self, word, location, orientation):
        N = location[0] - 1 
        M = location[1] - 1
        word_cells = []
        word = unidecode(word)
        for i in word:
            word_cells.append(self.grid[N][M])
            if orientation == 'H':
                M += 1
            elif orientation == 'V':
                N += 1
        return word_cells


