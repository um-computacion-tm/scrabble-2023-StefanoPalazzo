import unittest
from pyrae import dle
import re
from game.cell import Cell
from game.models import Tile
from game.tools import Tools

class TestTools(unittest.TestCase):
    def test_word_in_RAE_exists(self):

        word1 = 'CASA'
        exists = Tools().validate_word_in_RAE(word1)
        self.assertTrue(exists)

    def test_word_in_RAE_not_exists(self):

        word1 = 'ABCD'
        exists = Tools().validate_word_in_RAE(word1)
        self.assertFalse(exists)


if __name__ == '__main__':
    unittest.main()
