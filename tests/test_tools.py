import unittest
from pyrae import dle
import re
from game.cell import Cell
from game.models import Tile
from game.tools import Tools

class TestTools(unittest.TestCase):
    def test_word_in_RAE_exists(self):

        word1 = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('A', 1)),
            Cell(letter=Tile('S', 2)),
            Cell(letter=Tile('A', 1)),
        ]
        exists = Tools().validate_word_in_RAE(word1)
        self.assertTrue(exists)

    def test_word_in_RAE_not_exists(self):

        word1 = [
            Cell(letter=Tile('A', 1)),
            Cell(letter=Tile('B', 1)),
            Cell(letter=Tile('C', 2)),
            Cell(letter=Tile('D', 1)),
        ]
        exists = Tools().validate_word_in_RAE(word1)
        self.assertFalse(exists)


if __name__ == '__main__':
    unittest.main()
