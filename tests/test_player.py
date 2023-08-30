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
        self.assertNotEquals(TilesZero,player_2.tiles)
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



if __name__ == '__main__':
    unittest.main()
