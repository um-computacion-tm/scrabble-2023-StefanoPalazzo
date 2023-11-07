import unittest
from unittest import mock
from unittest.mock import patch, Mock
from game.models import Tile
from io import StringIO
from game.board import Board
from game.scrabblecli import *
from game.main import *
import re

class TestMain(unittest.TestCase):

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

        #   Elimina los caracteres de escape ANSI utilizando una expresión regular
        console_output_cleaned = re.sub(r'\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]', '', console_output)
        expected_output_cleaned = re.sub(r'\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]', '', expected_output)

        # Compara la salida real con la salida esperada
        self.assertEqual(console_output_cleaned, expected_output_cleaned)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_board_with_letter(self, mock_stdout):
        board1 = Board()
        board1.grid[0][0].letter = Tile('A',1)
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

    @patch('builtins.print')
    def test_separator(self, mock_print):
        Tools().separator()
        mock_print.assert_called_once_with('''______________________________________________________________________________________________________
               ''')
        
    # @patch('sys.stdout', new_callable=StringIO)
    # def test_Welcome_message(self, mock_stdout):
    #     game = ScrabbleGame(2)
    #     start_game()
    #     console_output = mock_stdout.getvalue()
    #     expected_output = '''WELCOME''' 

    #     #   Elimina los caracteres de escape ANSI utilizando una expresión regular 
    #     console_output_cleaned = re.sub(r'\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]', '', console_output)
    #     expected_output_cleaned = re.sub(r'\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]', '', expected_output)

    #     # Compara la salida real con la salida esperada
    #     print (expected_output_cleaned)
    #     self.assertTrue(expected_output_cleaned in console_output_cleaned)

# class TestMain:
#     @patch('builtins.input', side_effect=['2', 'E'])
#     def test_start_game(self, mock_input):
#         with patch('sys.stdout', new=StringIO()) as mock_output:
#             start_game()
#             assert 'The winner is player None with 0 ponints!' in mock_output.getvalue()

    @patch('builtins.print')
    def test_player_tiles(self, mock_print):
        __name__ = '__main__'
        game = ScrabbleGame(2)
        gameturn = game.turn
        game.players[0].player_tiles()
        mock_print.assert_called()

    @patch('builtins.input', side_effect=['2', 'B', 'HELLO', '1', '1', 'H', 'E', 'N', 'D', 'E'])
    def test_start_game(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as mock_output:
            ScrabbleCli()
            assert 'The winner is player None with 0 points' in mock_output.getvalue()
    
    @patch('builtins.input', side_effect=['2', 'K', 'E'])
    def test_invalid_option(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as mock_output:
            ScrabbleCli()
            assert 'Error! Please, choose a valid option:' in mock_output.getvalue()

    @patch('builtins.input', side_effect=['3', 'D', 'D', 'E'])
    def test_next_turn(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as mock_output:
            ScrabbleCli()
            assert 'Player 3 turn' in mock_output.getvalue()

    # @patch('builtins.input', side_effect=['2', 'A', 'fs', '1' 'E'])
    # def test_invalid_number_of_players(self, mock_input):
    #     with patch('sys.stdout', new=StringIO()) as mock_output:
    #         start_game()
    #         assert 'Error! Please enter valid tile positions between 1 and 7.' in mock_output.getvalue()

    # @patch('builtins.input', side_effect=['3', 'A', '1', 'E'])
    # @patch('builtins.print')
    # def test_print_message(self, mock_print, mock_input):
    #     with patch('sys.stdout', new=StringIO()) as mock_output:
    #         start_game()
    #         print(mock_print.call_args_list)
    #         mock_print.assert_any_call('Type the positions of the tiles you want to exchange: ')

    @patch('builtins.input', side_effect=['3', 'A', 'AKGADD', '1', 'E'])
    def test_foo_three(self,mock_input):
        with mock.patch('sys.stdout') as fake_stdout:
            ScrabbleCli()

        fake_stdout.assert_has_calls([
            mock.call.write('Error! Please enter valid tile positions between 1 and 7.'),

        ])

class TestMain(unittest.TestCase):

    @patch('builtins.input', side_effect=['2', 'B', 'HELLO', '1', '1', 'H', 'E', 'N', 'D', 'E'])
    def test_start_game(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as mock_output:
            ScrabbleCli()
            assert 'The winner is player None with 0 points' in mock_output.getvalue()

    @patch('builtins.input', side_effect=['2', 'K', 'E'])
    def test_invalid_option(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as mock_output:
            ScrabbleCli()
            assert 'Error! Please, choose a valid option:' in mock_output.getvalue()

    @patch('builtins.input', side_effect=['3', 'D', 'D', 'E'])
    def test_next_turn(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as mock_output:
            ScrabbleCli()
            assert 'Player 3 turn' in mock_output.getvalue()

    @patch('builtins.input', side_effect=['3', 'A', 'AKGADD', '1', 'E'])
    def test_invalid_tile_positions(self,mock_input):
        with mock.patch('sys.stdout') as fake_stdout:
            ScrabbleCli()

        fake_stdout.assert_has_calls([
            mock.call.write('Error! Please enter valid tile positions between 1 and 7.'),

        ])
    def test_no_main(self):
        fun = noFunction()
        self.assertEqual(fun, 1)
