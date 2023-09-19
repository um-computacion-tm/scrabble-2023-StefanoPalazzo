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
        word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('A', 1)),
            Cell(letter=Tile('S', 2)),
            Cell(letter=Tile('A', 1)),
        ]
        board.put_words(word, position, orientation)
        self.assertEqual(board.grid[4][4], word[0].letter)
        self.assertEqual(board.grid[4][5], word[1].letter)
        self.assertEqual(board.grid[4][6], word[2].letter)
        self.assertEqual(board.grid[4][7], word[3].letter)

    def test_put_word_vertical(self):
        board = Board()
        position = [5,5]
        orientation = 'V'
        word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('A', 1)),
            Cell(letter=Tile('S', 2)),
            Cell(letter=Tile('A', 1)),
        ]
        board.put_words(word, position, orientation)
        self.assertEqual(board.grid[4][4], word[0].letter)
        self.assertEqual(board.grid[5][4], word[1].letter)
        self.assertEqual(board.grid[6][4], word[2].letter)
        self.assertEqual(board.grid[7][4], word[3].letter)

    def test_word_inside_board_horizontal_true(self):
        board = Board()
        word = [
           Cell(letter=Tile('C', 1)),
           Cell(letter=Tile('A', 1)),
           Cell(letter=Tile('S', 2)),
           Cell(letter=Tile('A', 1)),
       ]
        location = (14, 4)
        orientation = 'H'
        word_is_valid = board.validate_word_inside_board(word,location, orientation)
        assert word_is_valid == True

    def test_word_inside_board_horizontal_false(self):
        board = Board()
        word = [
           Cell(letter=Tile('C', 1)),
           Cell(letter=Tile('A', 1)),
           Cell(letter=Tile('S', 2)),
           Cell(letter=Tile('A', 1)),
       ]
        location = (14, 15)
        orientation = 'H'
        word_is_valid = board.validate_word_inside_board(word,location, orientation)
        assert word_is_valid == False


    def test_word_inside_board_vertical_false(self):
        board = Board()
        word = [
           Cell(letter=Tile('C', 1)),
           Cell(letter=Tile('A', 1)),
           Cell(letter=Tile('S', 2)),
           Cell(letter=Tile('A', 1)),
       ]
        location = [14, 4]                    # User location starts at 1 instead of 0
        orientation = 'V'
        word_is_valid = board.validate_word_inside_board(word,location, orientation)
        assert word_is_valid == False

    def test_word_inside_board_vertical_true(self):
        board = Board()
        word = [
           Cell(letter=Tile('C', 1)),
           Cell(letter=Tile('A', 1)),
           Cell(letter=Tile('S', 2)),
           Cell(letter=Tile('A', 1)),
       ]
        location = [5, 4]                    # User location starts at 1 instead of 0
        orientation = 'V'
        word_is_valid = board.validate_word_inside_board(word,location, orientation)
        assert word_is_valid == True
    
    def test_validate_tiles_for_word_PlayerHasTiles(self):
        board1 = Board()
        Player1 = Player(ScrabbleGame(1))
        location = [5,5]                    # User location starts at 1 instead of 0
        orientation = 'H'
        Player1.tiles.append(Tile('C', 1))
        Player1.tiles.append(Tile('A', 1))
        Player1.tiles.append(Tile('S', 1))
        Player1.tiles.append(Tile('A', 1))
        word = [
           Cell(letter=Tile('C', 1)),
           Cell(letter=Tile('A', 1)),
           Cell(letter=Tile('S', 2)),
           Cell(letter=Tile('A', 1)),
       ]
        result = board1.validate_tiles_for_word(word, location, orientation, Player1.tiles)
        self.assertEqual(result, True)

    def test_validate_tiles_for_word_PlayerHasSomeTiles_BoardHasTiles(self):
        board1 = Board()
        board1.grid[4][4] = Tile('C', 1)
        board1.grid[4][6] = Tile('S', 1)
        Player1 = Player(ScrabbleGame(1))
        location = [5,5]                    # User location starts at 1 instead of 0
        orientation = 'H'
        Player1.tiles = []
        Player1.tiles.append(Tile('K', 1))
        Player1.tiles.append(Tile('A', 1))
        Player1.tiles.append(Tile('F', 1))
        Player1.tiles.append(Tile('A', 1))
        word = [
           Cell(letter=Tile('C', 1)),
           Cell(letter=Tile('A', 1)),
           Cell(letter=Tile('S', 2)),
           Cell(letter=Tile('A', 1)),
       ]
        result = board1.validate_tiles_for_word(word, location, orientation, Player1.tiles)
        self.assertEqual(result, True)

    def test_validate_tiles_for_word_PlayerDoesNotHaveTiles(self):
        board1 = Board()
        Player1 = Player(ScrabbleGame(1))
        location = [5,5]                    # User location starts at 1 instead of 0
        orientation = 'V'
        word = [
           Cell(letter=Tile('C', 1)),
           Cell(letter=Tile('A', 1)),
           Cell(letter=Tile('S', 2)),
           Cell(letter=Tile('A', 1)),
       ]
        result = board1.validate_tiles_for_word(word, location, orientation, Player1.tiles)
        self.assertEqual(result, False)
    
    def test_first_word_passes_by_the_center(self):
        board1 = Board()
        location = [8,5]                    # User location starts at 1 instead of 0
        orientation = 'H'
        word = [
           Cell(letter=Tile('L', 1)),
           Cell(letter=Tile('A', 1)),
           Cell(letter=Tile('T', 2)),
           Cell(letter=Tile('A', 1)),
       ]
        result = board1.validate_word_is_connected(word, location, orientation)
        self.assertTrue(result)

    def test_first_word_does_not_pass_by_the_center(self):
        board1 = Board()
        location = [10,10]                    # User location starts at 1 instead of 0
        orientation = 'H'
        word = [
           Cell(letter=Tile('L', 1)),
           Cell(letter=Tile('A', 1)),
           Cell(letter=Tile('T', 2)),
           Cell(letter=Tile('A', 1)),
       ]
        result = board1.validate_word_is_connected(word, location, orientation)
        self.assertFalse(result)

    def test_word_is_connected(self):
        board1 = Board()
        board1.grid[7][7].letter = 'C'
        board1.grid[7][8].letter = 'A'
        board1.grid[7][9].letter = 'S'
        board1.grid[7][10].letter = 'A'
        location = [7,9]                    # User location starts at 1 instead of 0
        orientation = 'V'
        word = [
           Cell(letter=Tile('L', 1)),
           Cell(letter=Tile('A', 1)),
           Cell(letter=Tile('T', 2)),
           Cell(letter=Tile('A', 1)),
       ]
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
        word = [
           Cell(letter=Tile('L', 1)),
           Cell(letter=Tile('A', 1)),
           Cell(letter=Tile('T', 2)),
           Cell(letter=Tile('A', 1)),
       ]
        result = board1.validate_word_is_connected(word, location, orientation)
        self.assertFalse(result)

    def test_word_overlapping_is_possible_horizontal_True(self):
        board1 = Board()
        board1.grid[7][7].letter = 'C'
        board1.grid[8][7].letter = 'A'
        board1.grid[9][7].letter = 'S'
        board1.grid[10][7].letter = 'A'
        location = [8,9]                  # User location starts at 1 instead of 0
        orientation = 'H'
        word = [
           Cell(letter=Tile('A', 1)),
           Cell(letter=Tile('L', 1)),
           Cell(letter=Tile('A', 2)),
           Cell(letter=Tile('S', 1)),
               ]
        result = board1.validate_word_overlapping_is_possible(word, location, orientation)
        self.assertTrue(result)

    def test_word_overlapping_is_possible_Vertical_True(self):
        board1 = Board()
        board1.grid[7][7].letter = 'C'
        board1.grid[7][8].letter = 'A'
        board1.grid[7][9].letter = 'S'
        board1.grid[7][10].letter = 'A'
        location = [8,9]                  # User location starts at 1 instead of 0
        orientation = 'V'
        word = [
           Cell(letter=Tile('A', 1)),
           Cell(letter=Tile('L', 1)),
           Cell(letter=Tile('A', 2)),
           Cell(letter=Tile('S', 1)),
               ]
        result = board1.validate_word_overlapping_is_possible(word, location, orientation)
        self.assertTrue(result)

    def test_word_overlapping_is_possible_False(self):
        board1 = Board()
        board1.grid[7][7].letter = 'N'
        board1.grid[7][8].letter = 'O'
        board1.grid[7][9].letter = 'T'
        board1.grid[7][10].letter = 'A'
        location = [8,9]                  # User location starts at 1 instead of 0
        orientation = 'V'
        word = [
           Cell(letter=Tile('P', 1)),
           Cell(letter=Tile('A', 1)),
           Cell(letter=Tile('L', 2)),
           Cell(letter=Tile('A', 1)),
               ]
        result = board1.validate_word_overlapping_is_possible(word, location, orientation)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
