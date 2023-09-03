from game.cell import Cell
from game.models import Tile, BagTiles


def rotate(mat):
    N = len(mat)
    
    # Transpose the matrix
    for i in range(N):
        for j in range(i + 1, N):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    
    # Invert rows
    for i in range(N):
        mat[i] = mat[i][::-1]


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
            rotate(self.grid)
            self.grid[7][7] = Cell(' ', 2, 'word')

def calculate_word_value(word):
        word_value = 0
        word_multiplier = 1
        for i in word:
            word_value += i.calculate_value()
            if i.multiplier_type == 'word':
                word_multiplier = i.multiplier
                i.multiplier_type = None         # Deactivates the multiplier of the cell
        word_value *= word_multiplier 
        return(word_value)


# # Shows the multiplier distribution
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
#     rotate(a)
    
# a[7][7] = ' X'

# for i in  range(15):
#      print (a[i])


