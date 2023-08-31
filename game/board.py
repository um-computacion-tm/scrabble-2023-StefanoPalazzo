from game.cell import Cell
from game.models import Tile

class Board:
    def __init__(self):
        self.grid = [
            [ Cell(None,1, None) for _ in range(15) ]
            for _ in range(15)
        ]

# a = [
#           [ '  ' for _ in range(15) ]
#             for _ in range(15)
#         ]

# def rotate(mat):
#     N = len(mat)
    
#     # Transponer la matriz
#     for i in range(N):
#         for j in range(i + 1, N):
#             mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    
#     # Invertir las filas
#     for i in range(N):
#         mat[i] = mat[i][::-1]


# for i in range(4):
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
 
#     rotate(a)
# a[7][7] = ' X'

# for i in  range(15):
#      print (a[i])





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
        
        
