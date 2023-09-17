from game.cell import Cell
from game.models import Tile, BagTiles
from game.tools import Tools
from colorama import Fore,Style
from game.player import Player



class Board:
    def __init__(self):
        self.grid = [
            [ Cell(' ',1, None) for _ in range(15) ]
            for _ in range(15)
        ]
        for i in range(4):            # Creates the diagonal
            for i in range(7):
                  for j in range (7):
                        if i == 0:
                            self.grid[i][i] = Cell(' ', 3, 'word') # Triple Word
                        elif i == 5:
                            self.grid[i][i] = Cell(' ', 3, 'letter') # Triple letter
                        elif i == 6:
                            self.grid[i][i] = Cell(' ', 2, 'letter')   # Double letter
                        else:
                            self.grid[i][i] = Cell(' ', 2, 'word')  # Double Word
            self.grid[7][0] = Cell(' ', 3, 'word')     # Triple Word
            self.grid[5][1] = Cell(' ', 3, 'letter')   # Triple letter
            self.grid[1][5] = Cell(' ', 3, 'letter')
            self.grid[0][3] = Cell(' ', 2, 'letter')   # Double letter
            self.grid[3][0] = Cell(' ', 2, 'letter')
            self.grid[6][2] = Cell(' ', 2, 'letter')
            self.grid[2][6] = Cell(' ', 2, 'letter')
            self.grid[7][3] = Cell(' ', 2, 'letter')
            Tools.rotate(self.grid)
            self.grid[7][7] = Cell(' ', 2, 'word')

    def show_board(self):
        boardRow = ''
        print ('                    ' + '  1   2   3   4   5   6   7   8   9  10  11  12  13  14  15')
        for i in range(15):
            for j in range(15):
                if self.grid[i][j].letter != ' ':
                    boardRow += '[' + self.grid[i][j].letter + ' ]'
                elif self.grid[i][j].multiplier_type == 'word' and self.grid[i][j].multiplier == 2: 
                    boardRow += f'[{Fore.MAGENTA}{Style.BRIGHT}2W{Style.RESET_ALL}]'
                elif self.grid[i][j].multiplier_type == 'word' and self.grid[i][j].multiplier == 3: 
                    boardRow += f'[{Fore.RED}{Style.BRIGHT}3W{Style.RESET_ALL}]'
                elif self.grid[i][j].multiplier_type == 'letter' and self.grid[i][j].multiplier == 2:
                    boardRow += f'[{Fore.CYAN}{Style.BRIGHT}2L{Style.RESET_ALL}]'
                elif self.grid[i][j].multiplier_type == 'letter' and self.grid[i][j].multiplier == 3:
                    boardRow += f'[{Fore.BLUE}{Style.BRIGHT}2L{Style.RESET_ALL}]'
                else:
                    boardRow += '[ ' + self.grid[i][j].letter + ']'
            if (i+1) <= 9:
                print ('                 '  + str(i+1) + '  ' + boardRow)
            else:
                print ('                 '  + str(i+1) + ' ' + boardRow)
            boardRow = ''

    def put_words(self,word, location, orientation):
        N = location[0] - 1 
        M = location[1] - 1
        for i in word:
            self.grid[N][M] = i.letter
            if orientation == 'H':
                M += 1
            elif orientation == 'V':
                N += 1
    
    def validate_word_inside_board(self, word,location, orientation):
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
        N = location[0] - 1 
        M = location[1] - 1
        playerTilesToVerify = []
        for i in playerTiles:
            playerTilesToVerify.append(i.letter)
        for i in word:
            if i.letter.letter == self.grid[N][M].letter:
                pass
            elif i.letter.letter in playerTilesToVerify:
                playerTilesToVerify.remove(i.letter.letter)
            else:
                return False
                   
            if orientation == 'H':
                M += 1
            elif orientation == 'V':
                N += 1
        return True
    
    def validate_word_is_connected(self,word, location, orientation):
        N = location[0] - 1 
        M = location[1] - 1
        for i in range(len(word)):
            if N == 7 and M == 7 and self.grid[7][7].letter == ' ':  # Checks that the first word passes through the center
                return True
            if self.grid[N][M].letter != ' ': # Checks that the word is connected by at least one letter to another word
                return True
            if orientation == 'H':
                M += 1
            elif orientation == 'V':
                N += 1
        return False



# word = [
#            Cell(letter=Tile('C', 1)),
#            Cell(letter=Tile('A', 1)),
#            Cell(letter=Tile('S', 2)),
#            Cell(letter=Tile('A', 1)),
#        ]

# while 1 == 1:
#     N = int(input ('N: '))
#     M = int(input ('M: '))
#     array = [N,M]
#     orientation = input ('orientation: ')
#     board1.put_words(word, array, orientation)
#     board1.show_board()