import unittest
from game.player import Player


class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(
            len(player_1.tiles),
            0,
        )


if __name__ == '__main__':
    unittest.main()
