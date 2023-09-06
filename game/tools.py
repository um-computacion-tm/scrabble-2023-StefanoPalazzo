

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


