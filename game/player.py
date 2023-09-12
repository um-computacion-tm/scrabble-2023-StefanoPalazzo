from game.models import Tile,BagTiles




class Player:
    def __init__(self, game):
        self.game = game
        self.tiles = game.bag_tiles.take(7)
        self.score = 0

    def exchange(self, tileArrayToExchange):
        for i in tileArrayToExchange:
            self.game.bag_tiles.put([self.tiles[i]])
            del self.tiles[i]
            self.tiles.insert(i, self.game.bag_tiles.take(1))


