import unittest
from game.player import Player


class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(
            len(player_1.tiles),
            7,
        )
    
    def test_exchange(self):
        player_1 = Player()
        TilesZero = player_1.tiles
        self.assertEqual(len(bag),100)
        player_1.exchange(0)
        self.assertNotEquals(TilesZero,player_1.tiles)
        self.assertEqual(len(TilesZero),len(player_1.tiles))
        self.assertEqual(len(bag),100)



if __name__ == '__main__':
    unittest.main()
