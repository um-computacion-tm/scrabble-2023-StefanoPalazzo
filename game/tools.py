from pyrae import dle
import re
from game.cell import Cell
from game.models import Tile

class Tools:
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
    
    def rotate(mat):
        N = len(mat)

        # Transpose the matrix
        for i in range(N):
            for j in range(i + 1, N):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

        # Invert rows
        for i in range(N):
            mat[i] = mat[i][::-1]

    def validate_word_in_RAE(self, word):
        wordToCheck = ''
        for i in word:
            wordToCheck += i.letter.letter
        res = dle.search_by_word(wordToCheck)
        # Text that appears when the word doesn't exists
        pattern = r'.*Versión electrónica 23.6 del «Diccionario de la lengua española», obra lexicográfica académica por excelencia.'
        # Text with definitions
        text = res._meta_description
        # Searchs for the pattern in the output
        resultado = re.search(pattern, text)
        # Check if there is coincidence
        if resultado:
            return False
        else:
            return True






