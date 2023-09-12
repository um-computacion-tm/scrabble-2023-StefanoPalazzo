import unittest
from unittest.mock import patch
from io import StringIO
from game.board import Board
import re

class TestShowBoard(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_board_initial(self, mock_stdout):
        board1 = Board()
        # Llama a la función que deseas probar
        board1.show_board()

        # Obtiene la salida de la consola como una cadena
        console_output = mock_stdout.getvalue()

        # Define la salida esperada sin eliminar los caracteres de escape ANSI
        expected_output = """\
                      1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
                 1  [3W][  ][  ][2L][  ][  ][  ][3W][  ][  ][  ][2L][  ][  ][3W]
                 2  [  ][2W][  ][  ][  ][2L][  ][  ][  ][2L][  ][  ][  ][2W][  ]
                 3  [  ][  ][2W][  ][  ][  ][2L][  ][2L][  ][  ][  ][2W][  ][  ]
                 4  [2L][  ][  ][2W][  ][  ][  ][2L][  ][  ][  ][2W][  ][  ][2L]
                 5  [  ][  ][  ][  ][2W][  ][  ][  ][  ][  ][2W][  ][  ][  ][  ]
                 6  [  ][2L][  ][  ][  ][2L][  ][  ][  ][2L][  ][  ][  ][2L][  ]
                 7  [  ][  ][2L][  ][  ][  ][2L][  ][2L][  ][  ][  ][2L][  ][  ]
                 8  [3W][  ][  ][2L][  ][  ][  ][2W][  ][  ][  ][2L][  ][  ][3W]
                 9  [  ][  ][2L][  ][  ][  ][2L][  ][2L][  ][  ][  ][2L][  ][  ]
                 10 [  ][2L][  ][  ][  ][2L][  ][  ][  ][2L][  ][  ][  ][2L][  ]
                 11 [  ][  ][  ][  ][2W][  ][  ][  ][  ][  ][2W][  ][  ][  ][  ]
                 12 [2L][  ][  ][2W][  ][  ][  ][2L][  ][  ][  ][2W][  ][  ][2L]
                 13 [  ][  ][2W][  ][  ][  ][2L][  ][2L][  ][  ][  ][2W][  ][  ]
                 14 [  ][2W][  ][  ][  ][2L][  ][  ][  ][2L][  ][  ][  ][2W][  ]
                 15 [3W][  ][  ][2L][  ][  ][  ][3W][  ][  ][  ][2L][  ][  ][3W]
"""

          # Elimina los caracteres de escape ANSI utilizando una expresión regular
        console_output_cleaned = re.sub(r'\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]', '', console_output)
        expected_output_cleaned = re.sub(r'\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]', '', expected_output)

        # Compara la salida real con la salida esperada
        self.assertEqual(console_output_cleaned, expected_output_cleaned)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_board_with_letter(self, mock_stdout):
        board1 = Board()
        board1.grid[0][0].letter = 'A'
        # Llama a la función que deseas probar
        board1.show_board()

        # Obtiene la salida de la consola como una cadena
        console_output = mock_stdout.getvalue()

        # Define la salida esperada sin eliminar los caracteres de escape ANSI
        expected_output = """\
                      1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
                 1  [A ][  ][  ][2L][  ][  ][  ][3W][  ][  ][  ][2L][  ][  ][3W]
                 2  [  ][2W][  ][  ][  ][2L][  ][  ][  ][2L][  ][  ][  ][2W][  ]
                 3  [  ][  ][2W][  ][  ][  ][2L][  ][2L][  ][  ][  ][2W][  ][  ]
                 4  [2L][  ][  ][2W][  ][  ][  ][2L][  ][  ][  ][2W][  ][  ][2L]
                 5  [  ][  ][  ][  ][2W][  ][  ][  ][  ][  ][2W][  ][  ][  ][  ]
                 6  [  ][2L][  ][  ][  ][2L][  ][  ][  ][2L][  ][  ][  ][2L][  ]
                 7  [  ][  ][2L][  ][  ][  ][2L][  ][2L][  ][  ][  ][2L][  ][  ]
                 8  [3W][  ][  ][2L][  ][  ][  ][2W][  ][  ][  ][2L][  ][  ][3W]
                 9  [  ][  ][2L][  ][  ][  ][2L][  ][2L][  ][  ][  ][2L][  ][  ]
                 10 [  ][2L][  ][  ][  ][2L][  ][  ][  ][2L][  ][  ][  ][2L][  ]
                 11 [  ][  ][  ][  ][2W][  ][  ][  ][  ][  ][2W][  ][  ][  ][  ]
                 12 [2L][  ][  ][2W][  ][  ][  ][2L][  ][  ][  ][2W][  ][  ][2L]
                 13 [  ][  ][2W][  ][  ][  ][2L][  ][2L][  ][  ][  ][2W][  ][  ]
                 14 [  ][2W][  ][  ][  ][2L][  ][  ][  ][2L][  ][  ][  ][2W][  ]
                 15 [3W][  ][  ][2L][  ][  ][  ][3W][  ][  ][  ][2L][  ][  ][3W]
"""

          # Elimina los caracteres de escape ANSI utilizando una expresión regular
        console_output_cleaned = re.sub(r'\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]', '', console_output)
        expected_output_cleaned = re.sub(r'\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]', '', expected_output)

        # Compara la salida real con la salida esperada
        self.assertEqual(console_output_cleaned, expected_output_cleaned)   

if __name__ == '__main__':
    unittest.main()

