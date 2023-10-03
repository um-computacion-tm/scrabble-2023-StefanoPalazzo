import unittest
from game.scrabble import ScrabbleGame
from game.models import Tile


class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(
            len(scrabble_game.players),
            3,
        )
        self.assertIsNotNone(scrabble_game.bag_tiles)
    
    def test_turns_2players(self):
        Game = ScrabbleGame(2)
        self.assertEqual(Game.turn, 0)
        Game.next_turn()
        self.assertEqual(Game.turn, 1)
        Game.next_turn()
        self.assertEqual(Game.turn, 0)
    
    def test_turns_4players(self):
        Game = ScrabbleGame(4)
        self.assertEqual(Game.turn, 0)
        Game.next_turn()
        self.assertEqual(Game.turn, 1)
        Game.next_turn()
        self.assertEqual(Game.turn, 2)
        Game.next_turn()
        self.assertEqual(Game.turn, 3)
        Game.next_turn()
        self.assertEqual(Game.turn, 0)

    def test_validate_and_put_word_error_doesnt_fit(self):
        game = ScrabbleGame(1)
        game.players[0].tiles.append(Tile('M',1))
        game.players[0].tiles.append(Tile('A',1))
        game.players[0].tiles.append(Tile('R',1))
        result = game.validate_and_put_word('MAR',[15,15],'H')
        self.assertEqual(result, "Error! The word doesn't fit on the board. Please choose a valid location.")

    def test_validate_and_put_word_error_doesnt_have_enough_tiles(self):
        game = ScrabbleGame(1)
        result = game.validate_and_put_word('MAREA',[8,8],'H')
        self.assertEqual(result, 'Error! User does not have required tiles')

    def test_validate_and_put_word_doesnt_pass_by_the_center(self):
        game = ScrabbleGame(1)
        game.players[0].tiles.append(Tile('M',1))
        game.players[0].tiles.append(Tile('A',1))
        game.players[0].tiles.append(Tile('R',1))
        result = game.validate_and_put_word('MAR',[10,10],'H')
        self.assertEqual(result, 'Error! Word does not passes by the center. Try with [8][8]')

    def test_validate_and_put_word_is_not_connected(self):
        game = ScrabbleGame(1)
        game.board.put_words([Tile('T',1),Tile('E',1)], [8,8], 'H') # This puts 'TE' in the center
        game.players[0].tiles.append(Tile('S',1))
        game.players[0].tiles.append(Tile('O',1))
        game.players[0].tiles.append(Tile('L',1))
        result = game.validate_and_put_word('SOL',[2,2],'H')
        self.assertEqual(result, 'Error! Word is not connected to others')

    def test_validate_and_put_word_conflicts_with_another_word(self):
        game = ScrabbleGame(1)
        game.board.put_words([Tile('T',1),Tile('E',1)], [8,8], 'H')
        game.players[0].tiles.append(Tile('M',1))
        game.players[0].tiles.append(Tile('A',1))
        game.players[0].tiles.append(Tile('R',1))
        result = game.validate_and_put_word('MAR',[7,9],'V') # User Location starts at 1, instead of 0
        self.assertEqual(result, 'Error! Word enters in conflict with other words.')

    def test_validate_and_put_word_is_not_in_RAE(self):
        game = ScrabbleGame(1)
        game.players[0].tiles.append(Tile('R',1))
        game.players[0].tiles.append(Tile('E',1))
        game.players[0].tiles.append(Tile('L',1))
        result = game.validate_and_put_word('REL',[8,8],'V') # User Location starts at 1, instead of 0
        self.assertEqual(result, 'Error! Word was not found in RAE dictionary')

    def test_validate_and_put_word_succesful(self):
        game = ScrabbleGame(1)
        game.board.grid[7][7].letter = Tile('T',1)
        game.board.grid[7][8].letter = Tile('E',1)
        game.players[0].tiles.append(Tile('V',1))
        game.players[0].tiles.append(Tile('E',1))
        game.players[0].tiles.append(Tile('R',1))
        result = game.validate_and_put_word('VER',[7,9],'V') # User Location starts at 1, instead of 0
        self.assertEqual(result, 'Word succesfully colocated.')

    def test_validate_and_put_word_without_accent_mark_error(self):
        game = ScrabbleGame(1)
        game.players[0].tiles.append(Tile('A',1))
        game.players[0].tiles.append(Tile('V',1))
        game.players[0].tiles.append(Tile('I',1))
        game.players[0].tiles.append(Tile('O',1))
        game.players[0].tiles.append(Tile('N',1))
        result = game.validate_and_put_word('AVION',[8,8],'V') # User Location starts at 1, instead of 0
        self.assertEqual(result, 'Error! Word was not found in RAE dictionary')

    def test_validate_and_put_word_with_accent_mark_succesful(self):
        game = ScrabbleGame(1)
        game.players[0].tiles.append(Tile('A',1))
        game.players[0].tiles.append(Tile('V',1))
        game.players[0].tiles.append(Tile('I',1))
        game.players[0].tiles.append(Tile('O',1))
        game.players[0].tiles.append(Tile('N',1))
        result = game.validate_and_put_word('AVIÓN',[8,8],'V') # User Location starts at 1, instead of 0
        self.assertEqual(result, 'Word succesfully colocated.')
        
    
    

if __name__ == '__main__':
    unittest.main()
