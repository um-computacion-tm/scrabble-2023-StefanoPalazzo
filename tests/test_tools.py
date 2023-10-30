import unittest
from unittest.mock import *
from pyrae import dle
import re
from game.tools import Tools

class TestTools(unittest.TestCase):
    @patch('game.tools.dle.search_by_word')
    def test_word_in_RAE_exists(self, mocked_rae):
        mocked_rae.return_value._meta_description = '1. f. Edificio para habitar. Una casa de ocho plantas. 2. f. Edificio de una o pocas plantas destinado a vivienda unifamiliar, en oposición a piso. Quieren vender el piso y comprarse una casa.'
        word1 = 'CASA'
        exists = Tools().validate_word_in_RAE(word1)
        self.assertTrue(exists)

    @patch('game.tools.dle.search_by_word')
    def test_word_in_RAE_not_exists(self, mocked_rae):
        mocked_rae.return_value._meta_description = 'Versión electrónica 23.6 del «Diccionario de la lengua española», obra lexicográfica académica por excelencia.'
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
