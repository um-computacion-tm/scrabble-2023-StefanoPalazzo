import unittest
from game.cell import Cell
from game.models import Tile
from game.board import Board
from game.tools import Tools

class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('A', 1)),
            Cell(letter=Tile('S', 2)),
            Cell(letter=Tile('A', 1)),
        ]
        value = Tools().calculate_word_value(word)
        self.assertEqual(value, 5)

    def test_with_letter_multiplier(self):
        word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='letter',
            ),
            Cell(letter=Tile('A', 1)),
        ]
        value = Tools().calculate_word_value(word)
        self.assertEqual(value, 7)

    def test_with_word_multiplier(self):
        word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tile('A', 1)),
        ]
        value = Tools().calculate_word_value(word)
        self.assertEqual(value, 10)

    def test_with_letter_word_multiplier(self):
        word = [
            Cell(
                multiplier=3,
                multiplier_type='letter',
                letter=Tile('C', 1)
            ),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tile('A', 1)),
        ]
        value = Tools().calculate_word_value(word)
        self.assertEqual(value, 14)

    def test_with_letter_word_multiplier_no_active(self):
        word = [
            Cell(
                multiplier=3,
                multiplier_type='letter',
                letter=Tile('C', 1)
            ),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tile('A', 1)),
        ]
        value0 = Tools().calculate_word_value(word)    # Calculates word value with multipliers
        value1 = Tools().calculate_word_value(word)    # Calculates word value without multipliers (multipliers deactivated)
        self.assertEqual(value1, 5)

if __name__ == '__main__':
    unittest.main()
