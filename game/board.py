from game.cell import Cell
from game.models import Tile, BagTiles
from game.tools import Tools



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
        print ('   ' + '  1   2   3   4   5   6   7   8   9  10  11  12  13  14  15')
        for i in range(15):
            for j in range(15):
                if self.grid[i][j].letter != ' ':
                    boardRow += '[' + self.grid[i][j].letter + ' ]'
                elif self.grid[i][j].multiplier_type == 'word' and self.grid[i][j].multiplier == 2: 
                    boardRow += '[' + '2W' + ']'
                elif self.grid[i][j].multiplier_type == 'word' and self.grid[i][j].multiplier == 3: 
                    boardRow += '[' + '3W' + ']'
                elif self.grid[i][j].multiplier_type == 'letter' and self.grid[i][j].multiplier == 2:
                    boardRow += '[' + '2L' + ']'
                elif self.grid[i][j].multiplier_type == 'letter' and self.grid[i][j].multiplier == 3:
                    boardRow += '[' + '3L' + ']'
                else:
                    boardRow += '[ ' + self.grid[i][j].letter + ']'
            if (i+1) <= 9:
                print (str(i+1) + '  ' + boardRow)
            else:
                print (str(i+1) + ' ' + boardRow)
            boardRow = ''

    def put_words(self,word, location, orientation):
        N = location[0]
        M = location[1]
        for i in word:
            self.grid[N][M] = i.letter
            if orientation == 'H':
                M += 1
            elif orientation == 'V':
                N += 1
        
    


# # Shows the multiplier distribution
# boardEx = Board()
# boardMatrix = []
# for i in range(15):
#     for j in range(15):
#         boardMatrix.append([boardEx.grid[i][j].multiplier])
#     print (boardMatrix)
#     boardMatrix = []


# # # Shows the board scheme
# a = [
#           [ '  ' for _ in range(15) ]
#             for _ in range(15)
#         ]
# for i in range(4):            # Creates the diagonal
#     for i in range(7):
#      for j in range (7):
#         if i == 0:
#             a[i][i] = 'TP'
#         elif i == 5:
#             a[i][i] = 'TL'
#         elif i == 6:
#             a[i][i] = 'DL'
#         else:
#          a[i][i] = 'DP'
#     a[7][0] = 'TP'
#     a[5][1] = 'TL'
#     a[1][5] = 'TL'
#     a[0][3] = 'DL'
#     a[3][0] = 'DL'
#     a[6][2] = 'DL'
#     a[2][6] = 'DL'
#     a[7][3] = 'DL'
#     Tools.rotate(a)
    
# a[7][7] = ' X'

# for i in  range(15):
#      print (a[i])


