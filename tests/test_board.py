import unittest
from game.board import Board
from game.cell import Cell
from game.models import Tile
from game.player import Player
from game.scrabble import ScrabbleGame




class TestBoard(unittest.TestCase):

    def test_init(self):
        board = Board()
        self.assertEqual(
            len(board.grid),
            15,
        )
        self.assertEqual(
            len(board.grid[0]),
            15,
        )


    def test_board_cell_00(self):
        board = Board()
        cell = board.grid
        self.assertEqual(cell[0][0].multiplier,3 )
        self.assertEqual(cell[0][0].multiplier_type,'word' )
    
    def test_board_cell_77(self):
        board = Board()
        cell = board.grid
        self.assertEqual(cell[7][7].multiplier,2 )
        self.assertEqual(cell[7][7].multiplier_type,'word' )

    def test_put_word_horizontal(self):
        board = Board()
        position = [5,5]
        orientation = 'H'
        word = 'CASA'
        board.put_words(word, position, orientation)
        self.assertEqual(board.grid[4][4].letter, word[0])
        self.assertEqual(board.grid[4][5].letter, word[1])
        self.assertEqual(board.grid[4][6].letter, word[2])
        self.assertEqual(board.grid[4][7].letter, word[3])

    def test_put_word_vertical(self):
        board = Board()
        position = [5,5]
        orientation = 'V'
        word = [
            Tile('C',1),
            Tile('A',1),
            Tile('S',1),
            Tile('A',1),
                ]
        board.put_words(word, position, orientation)
        self.assertEqual(board.grid[4][4].letter.letter, word[0].letter)
        self.assertEqual(board.grid[5][4].letter.letter, word[1].letter)
        self.assertEqual(board.grid[6][4].letter.letter, word[2].letter)
        self.assertEqual(board.grid[7][4].letter.letter, word[3].letter)

    def test_word_inside_board_horizontal_true(self):
        board = Board()
        word = 'CASA'
        location = (14, 4)
        orientation = 'H'
        word_is_valid = board.validate_word_inside_board(word,location, orientation)
        assert word_is_valid == True

    def test_word_inside_board_horizontal_false(self):
        board = Board()
        word = 'CASA'
        location = (14, 15)
        orientation = 'H'
        word_is_valid = board.validate_word_inside_board(word,location, orientation)
        assert word_is_valid == False

    def test_word_inside_board_vertical_false(self):
        board = Board()
        word = 'CASA'
        location = [14, 4]                    # User location starts at 1 instead of 0
        orientation = 'V'
        word_is_valid = board.validate_word_inside_board(word,location, orientation)
        assert word_is_valid == False

    def test_word_inside_board_vertical_true(self):
        board = Board()
        word = 'CASA'
        location = [5, 4]                    # User location starts at 1 instead of 0
        orientation = 'V'
        word_is_valid = board.validate_word_inside_board(word,location, orientation)
        assert word_is_valid == True
    
    def test_validate_tiles_for_word_PlayerHasTiles(self):
        game = ScrabbleGame(1)
        board1 = Board()
        Player1 = game.players[0]
        location = [5,5]                    # User location starts at 1 instead of 0
        orientation = 'H'
        Player1.tiles.append(Tile('C', 1))
        Player1.tiles.append(Tile('A', 1))
        Player1.tiles.append(Tile('S', 1))
        Player1.tiles.append(Tile('A', 1))
        word = 'CASA'
        result = board1.validate_tiles_for_word(word, location, orientation, Player1.tiles)
        self.assertEqual(result, [True,True])

    def test_validate_tiles_for_word_PlayerHasSomeTiles_BoardHasTiles(self):
        board1 = Board()
        game = ScrabbleGame(1)
        board1.grid[4][4].letter = Tile('C', 1)
        board1.grid[4][6].letter = Tile('S', 1)
        Player1 = game.players[0]
        location = [5,5]                    # User location starts at 1 instead of 0
        orientation = 'H'
        Player1.tiles = []
        Player1.tiles.append(Tile('K', 1))
        Player1.tiles.append(Tile('A', 1))
        Player1.tiles.append(Tile('F', 1))
        Player1.tiles.append(Tile('A', 1))
        word = 'CASA'
        result = board1.validate_tiles_for_word(word, location, orientation, Player1.tiles)
        self.assertEqual(result, [True,True])

    def test_validate_tiles_for_word_PlayerDoesNotHaveTiles(self):
        board1 = Board()
        Player1 = Player(ScrabbleGame(1))
        Player1.tiles = []
        location = [8,8]                    # User location starts at 1 instead of 0
        orientation = 'H'
        word = 'CASA'
        result = board1.validate_tiles_for_word(word, location, orientation, Player1.tiles)
        self.assertEqual(result, [False,True])

    def test_validate_player_is_creating_a_new_word_False(self):
        board1 = Board()
        board1.grid[7][7].letter = Tile('C', 1)
        board1.grid[7][8].letter = Tile('A', 1) 
        board1.grid[7][9].letter = Tile('S', 1)    
        board1.grid[7][10].letter = Tile('A', 1)
        Player1 = Player(ScrabbleGame(1))
        location = [8,8]                    # User location starts at 1 instead of 0
        orientation = 'H'
        word = 'CASA'
        result = board1.validate_tiles_for_word(word, location, orientation, Player1.tiles)
        self.assertEqual(result, [True,False])

    def test_validate_tiles_for_word_player_has_wildcard(self):
        board1 = Board()
        Player1 = Player(ScrabbleGame(1))
        Player1.tiles = [Tile('L',1),
                         Tile('E',1),
                         Tile('Ñ',1),
                         Tile('?',1),
                         ]
        location = [5,5]                    # User location starts at 1 instead of 0
        orientation = 'V'
        word = 'LEÑA'
        result = board1.validate_tiles_for_word(word, location, orientation, Player1.tiles)
        self.assertEqual(result, [True,True])
    
    def test_first_word_passes_by_the_center(self):
        board1 = Board()
        location = [8,8]                    # User location starts at 1 instead of 0
        orientation = 'H'
        word = 'LATA'
        result = board1.validate_word_is_connected(word, location, orientation)
        self.assertTrue(result)

    def test_first_word_does_not_pass_by_the_center(self):
        board1 = Board()
        location = [10,10]                    # User location starts at 1 instead of 0
        orientation = 'H'
        word = 'LATA'
        result = board1.validate_word_is_connected(word, location, orientation)
        self.assertFalse(result)

    def test_word_is_connected(self):
        board1 = Board()
        board1.grid[7][7].letter.letter = 'C'
        board1.grid[7][8].letter.letter = 'A'
        board1.grid[7][9].letter.letter = 'S'
        board1.grid[7][10].letter.letter = 'A'
        location = [7,9]                    # User location starts at 1 instead of 0
        orientation = 'V'
        word = 'LATA'
        result = board1.validate_word_is_connected(word, location, orientation)
        self.assertTrue(result)

    def test_word_is_connected_by_sourranding_letter(self):
            board1 = Board()
            board1.grid[7][7].letter.letter = 'C' 
            board1.grid[7][8].letter.letter = 'A'
            board1.grid[7][9].letter.letter = 'S'   
            board1.grid[7][10].letter.letter = 'A'  

            location = [8,12]                    # User location starts at 1 instead of 0
            orientation = 'V'
            word = 'SOPA'
            result = board1.validate_word_is_connected(word, location, orientation)
            self.assertTrue(result)

    def test_word_is_not_connected(self):
        board1 = Board()
        board1.grid[7][7].letter = 'C'
        board1.grid[7][8].letter = 'A'
        board1.grid[7][9].letter = 'S'
        board1.grid[7][10].letter = 'A'
        location = [2,2]                    # User location starts at 1 instead of 0
        orientation = 'V'
        word = 'LATA'
        result = board1.validate_word_is_connected(word, location, orientation)
        self.assertFalse(result)

    def test_word_overlapping_is_possible_horizontal_True(self):
        board1 = Board()
        board1.grid[7][7].letter = Tile('C',1)
        board1.grid[8][7].letter = Tile('A',1)
        board1.grid[9][7].letter = Tile('S',1)
        board1.grid[10][7].letter = Tile('A',1)
        location = [9,8]                  # User location starts at 1 instead of 0
        orientation = 'H'
        word = 'ALAS'
        result = board1.validate_word_overlapping_is_possible(word, location, orientation)
        self.assertTrue(result)

    def test_word_overlapping_is_possible_Vertical_True(self):
        board1 = Board()
        board1.grid[7][7].letter = Tile('C',1)
        board1.grid[7][8].letter = Tile('A',1)
        board1.grid[7][9].letter = Tile('S',1)
        board1.grid[7][10].letter =Tile('A',1)
        location = [8,9]                  # User location starts at 1 instead of 0
        orientation = 'V'
        word = 'ALAS'
        result = board1.validate_word_overlapping_is_possible(word, location, orientation)
        self.assertTrue(result)

    def test_word_overlapping_is_possible_False(self):
        board1 = Board()
        board1.grid[7][7].letter.letter = 'N'
        board1.grid[7][8].letter.letter = 'O'
        board1.grid[7][9].letter.letter = 'T'
        board1.grid[7][10].letter.letter = 'A'
        location = [8,9]                  # User location starts at 1 instead of 0
        orientation = 'V'
        word = 'PALA'
        result = board1.validate_word_overlapping_is_possible(word, location, orientation)
        self.assertFalse(result)

    def test_get_cells_of_a_word_in_the_board(self):
        board1 = Board()
        board1.grid[7][7].letter = Tile('C', 1)
        board1.grid[7][8].letter = Tile('A', 1)
        board1.grid[7][9].letter = Tile('S', 1)
        board1.grid[7][10].letter = Tile('A', 1)
        cells = board1.cells_of_word_in_board('CASA', [8,8], 'H')
        self.assertEqual(cells, [board1.grid[7][7],board1.grid[7][8],board1.grid[7][9],board1.grid[7][10]])

    def test_validate_word_creates_valid_words_in_each_cell_Horizontal_TRUE(self):
        game = ScrabbleGame(2)
        board1 = game.board
        # Word Casa in Horizontal
        board1.grid[7][7].add_letter(Tile('C', 1))
        board1.grid[7][8].add_letter(Tile('A', 1))
        board1.grid[7][9].add_letter(Tile('S', 1))
        board1.grid[7][10].add_letter(Tile('A', 1))

        # This creates the word 'C MA' (with the previus S) in vertical, then it will create 'CAMA' in vertical with the new word
        board1.grid[9][7].add_letter(Tile('M', 1))
        board1.grid[10][7].add_letter(Tile('A', 1))

        # This creates the word 'CA' (with the previus A) in vertical, then it will create 'CAE' in vertical with the new word
        board1.grid[6][8].add_letter(Tile('C', 1))

        # This creates the word 'MES' (with the previus S) in vertical, then it will create 'MESA' in vertical with the new word
        board1.grid[5][9].add_letter(Tile('M', 1))
        board1.grid[6][9].add_letter(Tile('E', 1))
        result = (board1.validate_word_creates_valid_words_in_each_cell('AEA', [9,8], 'H'))  # We are suppossing that 'AEA' is a valid word
        self.assertTrue(result[0])

    def test_validate_word_creates_valid_words_in_each_cell_Horizontal_FALSE(self):
        board1 = Board()
        # Word Casa in Horizontal
        board1.grid[7][7].add_letter(Tile('C', 1))
        board1.grid[7][8].add_letter(Tile('A', 1))
        board1.grid[7][9].add_letter(Tile('S', 1))
        board1.grid[7][10].add_letter(Tile('A', 1))

        # This creates the word 'C MA' (with the previus S) in vertical, then it will create 'CAMA' in vertical with the new word
        board1.grid[9][7].add_letter(Tile('M', 1))
        board1.grid[10][7].add_letter(Tile('A', 1))

        # This creates the word 'CA' (with the previus A) in vertical, then it will create 'CAE' in vertical with the new word
        board1.grid[6][8].add_letter(Tile('C', 1))

        # This creates the word 'MES' (with the previus S) in vertical, then it will create 'MESA' in vertical with the new word
        board1.grid[5][9].add_letter(Tile('M', 1))
        board1.grid[6][9].add_letter(Tile('E', 1))
        result = (board1.validate_word_creates_valid_words_in_each_cell('KKK', [9,8], 'H'))  # We are suppossing that 'AEA' is a valid word
        self.assertFalse(result[0])

    def test_validate_word_creates_valid_words_in_each_cell_vertical_TRUE(self):
        board1 = Board()
        # Word Casa in Horizontal
        board1.grid[7][7].add_letter(Tile('C', 1))
        board1.grid[8][7].add_letter(Tile('A', 1))
        board1.grid[9][7].add_letter(Tile('S', 1))
        board1.grid[10][7].add_letter(Tile('A', 1))

        # This creates the word 'C MA' (with the previus S) in horizontal, then it will create 'CAMA' in horizontal with the new word
        board1.grid[7][9].add_letter(Tile('M', 1))
        board1.grid[7][10].add_letter(Tile('A', 1))

        # This creates the word 'CA' (with the previus A) in horizontal, then it will create 'CAE' in horizontal with the new word
        board1.grid[8][6].add_letter(Tile('C', 1))

        # This creates the word 'MES' (with the previus S) in horizontal, then it will create 'CASA' in hotizontal with the new word
        board1.grid[9][5].add_letter(Tile('M', 1))
        board1.grid[9][6].add_letter(Tile('E', 1))

        result = (board1.validate_word_creates_valid_words_in_each_cell('AEA', [8,9], 'V'))  # We are suppossing that 'AEA' is a valid word
        self.assertTrue(result[0])

    def test_validate_word_creates_valid_words_in_each_cell_vertical_first_word(self):
        board1 = Board()

        result = (board1.validate_word_creates_valid_words_in_each_cell('Leña', [8,9], 'V'))  # We are suppossing that 'AEA' is a valid word
        self.assertTrue(result[0])

    def test_validate_word_creates_valid_words_in_each_cell_horizontal_conflicting_letter_after(self):
        board1 = Board()
        # Word Sol in Vertical
        board1.grid[5][7].add_letter(Tile('S', 1))
        board1.grid[6][7].add_letter(Tile('O', 1))
        board1.grid[7][7].add_letter(Tile('L', 1))

        # Letter that will conlfict with the word 'LEÑA' -> 'LEÑAX'
        board1.grid[7][11].add_letter(Tile('X', 1))
        result = (board1.validate_word_creates_valid_words_in_each_cell('LEÑA', [8,8], 'H'))  # 'LEÑA' is connected to 'SOL'
        self.assertFalse(result[0])

    def test_validate_word_creates_valid_words_in_each_cell_vertical_conflicting_letter_after(self):
        board1 = Board()
        # Word Sol in Horizontal
        board1.grid[7][5].add_letter(Tile('S', 1))
        board1.grid[7][6].add_letter(Tile('O', 1))
        board1.grid[7][7].add_letter(Tile('L', 1))

        # Letter that will conlfict with the word 'LEÑA' -> 'LEÑAX'
        board1.grid[11][7].add_letter(Tile('X', 1))
        result = (board1.validate_word_creates_valid_words_in_each_cell('LEÑA', [8,8], 'V'))  # 'LEÑA' is connected to 'SOL'
        self.assertFalse(result[0])

if __name__ == '__main__':
    unittest.main()
