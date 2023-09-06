import unittest
from game.board import Board
from game.cell import Cell
from game.models import Tile


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
        self.assertEqual(board.grid[5][5], word[0].letter)
        self.assertEqual(board.grid[5][6], word[1].letter)
        self.assertEqual(board.grid[5][7], word[2].letter)
        self.assertEqual(board.grid[5][8], word[3].letter)

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
        self.assertEqual(board.grid[5][5], word[0].letter)
        self.assertEqual(board.grid[6][5], word[1].letter)
        self.assertEqual(board.grid[7][5], word[2].letter)
        self.assertEqual(board.grid[8][5], word[3].letter)

    # def test_word_inside_board(self):
    #     board = Board()
    #     word = 'facultad'
    #     location = (14, 4)
    #     orientation = 'H'
    #     word_is_valid = board.validate_word_inside_board(word,location, orientation)
    #     assert word_is_valid == True



if __name__ == '__main__':
    unittest.main()
