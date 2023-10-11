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

    def test_word_in_dictionary_txt_exists(self):
        # Test the function with a word that exists in the dictionary.txt file
        word = 'manzana'
        exists = Tools().validate_word_in_dictionary_txt(word)
        self.assertTrue(exists)

    def test_word_in_dictionary_txt_not_exists(self):
        # Test the function with a word that does not exist in the dictionary.txt file
        word = 'xyzzyx'
        exists = Tools().validate_word_in_dictionary_txt(word)
        self.assertFalse(exists)

    def test_word_in_dictionary_txt_mixed_case(self):
        # Test the function with a word that has mixed case
        word = 'mAnZaNa'
        exists = Tools().validate_word_in_dictionary_txt(word)
        self.assertTrue(exists)

if __name__ == '__main__':
    unittest.main()
