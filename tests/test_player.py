import unittest
from game.player import Player
from game.scrabble import ScrabbleGame


class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player(ScrabbleGame(1))
        self.assertEqual(
            len(player_1.tiles),
            7,
        )
    
    def test_exchange_1_tile(self):
        gameTest = ScrabbleGame(1)
        bag = gameTest.bag_tiles.tiles
        player_2 = gameTest.players[0]
        self.assertEqual(len(bag),93)
        TilesZero = bag.copy()
        player_2.exchange([0])
        self.assertNotEqual(TilesZero,player_2.tiles)
        self.assertEqual(len(TilesZero),len(bag))
        self.assertEqual(len(bag),93)

    def test_exchange_3_tiles(self):
        gameTest = ScrabbleGame(1)
        bag = gameTest.bag_tiles.tiles
        player_2 = gameTest.players[0]
        self.assertEqual(len(bag),93)
        TilesZero = bag.copy()
        player_2.exchange([0,4,6])
        self.assertNotEquals(TilesZero,player_2.tiles)
        self.assertEqual(len(TilesZero),len(bag))
        self.assertEqual(len(bag),93)

    def test_initial_score(self):
        gameTest = ScrabbleGame(2)
        bag = gameTest.bag_tiles.tiles
        player_1 = gameTest.players[0]
        player_2 = gameTest.players[1]
        self.assertEqual(player_1.score,0)
        self.assertEqual(player_2.score,0)

    def test_shuffle_tiles(self):
        game = ScrabbleGame(1)
        player_1 = game.players[0]
        original_tiles = player_1.tiles.copy()
        player_1.shuffle_tiles()
        self.assertNotEqual(original_tiles, player_1.tiles)

if __name__ == '__main__':
    unittest.main()
