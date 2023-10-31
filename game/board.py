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
        N = location[0] - 1 
        M = location[1] - 1
        for i in word:
            self.grid[N][M].letter = i
            if orientation == 'H':
                M += 1
            elif orientation == 'V':
                N += 1
    
    def validate_word_inside_board(self, word,location, orientation):
        word = unidecode(word)
        N = location[0] - 1
        M = location[1] - 1
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
        N = location[0] - 1 
        M = location[1] - 1
        playerTilesToVerify = []
        NewWord = False
        wildcard = False
        for i in playerTiles:
            playerTilesToVerify.append(i.letter)    # Creates an array of the letters of the tiles
            if i.letter == '?':                     # Checks if the user has a wildcard
                wildcard = True
        for i in word1:
            if i == self.grid[N][M].letter.letter: 
                pass
            elif i in playerTilesToVerify:
                playerTilesToVerify.remove(i)
                NewWord = True
            elif wildcard:
                for tile in range(len(playerTiles)):
                    if playerTiles[tile].letter == '?':
                        playerTiles[tile].letter = i
                        NewWord = True
            else:
                return [False, True]    # Aclaration: True does not mean it is a New Word, is just to avoid the error message
                   
            if orientation == 'H':
                M += 1
            elif orientation == 'V':
                N += 1

        return [True, NewWord]
    
    def validate_word_is_connected(self,word, location, orientation):
        word = unidecode(word) 
        N = location[0] - 1 
        M = location[1] - 1
        for i in range(len(word)):
            if N < 0 or N >= len(self.grid) or M < 0 or M >= len(self.grid[0]):
                    continue
            
            if N == 7 and M == 7 and self.grid[7][7].letter.letter == ' ':  # Checks that the first word passes through the center
                return True
            if self.grid[N][M].letter.letter != ' ': # Checks that the word is connected by at least one letter to another word
                return True
            
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
                
            if orientation == 'H': 
                M += 1
            elif orientation == 'V':
                N += 1
        return False
    
    def validate_word_overlapping_is_possible(self, word, location, orientation):
        N = location[0] - 1 
        M = location[1] - 1
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
        N = location[0] - 1
        M = location[1] - 1
        firstposition = [N,M]
        if orientation == 'H':
            lastPosition = [N, M + len(word)-1]
        else: 
            lastPosition = [N + len(word)-1, M]
        result = True
        NewWordsAndPositionsArray = []
        if self.grid[7][7].letter.letter == ' ':
            return (True, [])
        for i in word:
            if orientation == 'H':
                if (self.grid[firstposition[0]][firstposition[1]-1].letter.letter != ' ') or (self.grid[lastPosition[0]][lastPosition[1]+1].letter.letter != ' '):  # Checks if it is a letter before or after the word, and returns false
                    result = False
                newWord = '' 
                wordOrientation = 'V'
                letter_added_to_new_word = False
                R = N
                C = M
                if self.grid[R-1][C].letter.letter == ' ' and self.grid[R+1][C].letter.letter == ' ':
                    continue
                if self.grid[R][C].letter.letter != ' ':
                    continue
            
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
                M += 1
                NewWordsAndPositionsArray.append([newWord, startPosition, wordOrientation])
                result = result and Tools().validate_word_in_dictionary_txt(newWord)  # If the word is in the dictionary this will remain True

            if orientation == 'V':
                if self.grid[firstposition[0]-1][firstposition[1]].letter.letter != ' ' or self.grid[lastPosition[0]+1][lastPosition[1]].letter.letter != ' ':    # Checks if it is a letter before or after the word, and returns false
                    result = False
                newWord = ''
                wordOrientation = 'H'  
                letter_added_to_new_word = False
                R = N
                C = M
                if self.grid[R][C-1].letter.letter == ' ' and self.grid[R][C+1].letter.letter == ' ':
                    continue
                if self.grid[R][C].letter.letter != ' ':
                    continue
                while self.grid[R][C-1].letter.letter != ' ':    # Checks if the cell on top has a letter and continues until it finds an emptu cell
                    C -= 1           
                startPosition = [R+1,C+1]                     
                newWord += self.grid[R][C].letter.letter       # Adds the first letter of the word
                while self.grid[R][C+1].letter.letter != ' ' or not letter_added_to_new_word:  # Checks if the cell on bottom has a letter and continues until it finds an empty cell
                    if self.grid[R][C+1].letter.letter == ' ': # If it finds a blank space for the first time it makes 1 exception to add the letter of the word, this is to avoid adding the letter of the word twice
                        newWord += i
                        letter_added_to_new_word = True
                        C += 1
                    else:                                      # If it finds a letter it adds it to the new word
                        newWord += self.grid[R][C+1].letter.letter
                        C += 1       
                N += 1
                NewWordsAndPositionsArray.append([newWord, startPosition, wordOrientation])
                result = result and Tools().validate_word_in_dictionary_txt(newWord)    # If the word is in the dictionary this will remain True

        return (result, NewWordsAndPositionsArray)
    

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



# board1 = Board()
# # Word Casa in Horizontal
# board1.grid[7][7].add_letter(Tile('C', 1))
# board1.grid[7][8].add_letter(Tile('A', 1))
# board1.grid[7][9].add_letter(Tile('S', 1))
# board1.grid[7][10].add_letter(Tile('A', 1))
# # This creates the word 'C MA' (with the previus S) in vertical, then it will create 'CAMA' in vertical with the new word
# board1.grid[9][7].add_letter(Tile('M', 1))
# board1.grid[10][7].add_letter(Tile('A', 1))
# # This creates the word 'CA' (with the previus A) in vertical, then it will create 'CAE' in vertical with the new word
# board1.grid[6][8].add_letter(Tile('C', 1))
# # This creates the word 'MES' (with the previus S) in vertical, then it will create 'MESA' in vertical with the new word
# board1.grid[5][9].add_letter(Tile('M', 1))
# board1.grid[6][9].add_letter(Tile('E', 1))
# result = (board1.validate_word_creates_valid_words_in_each_cell('AEA', [9,8], 'H'))  # We are suppossing that 'AEA' is a valid word
# print (result[1])
# board1.show_board()