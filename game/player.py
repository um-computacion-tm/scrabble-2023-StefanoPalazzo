from game.models import Tile,BagTiles
import random



class Player:
    def __init__(self, game):
        self.game = game
        self.tiles = game.bag_tiles.take(7)
        self.score = 0

    def exchange(self, tileArrayToExchange):
        for i in tileArrayToExchange:
            self.game.bag_tiles.put([self.tiles[i]])
            del self.tiles[i]
            self.tiles.insert(i, self.game.bag_tiles.take(1)[0])

    def shuffle_tiles(self):
        random.shuffle(self.tiles)

    def player_tiles(self):
        print ('')
        print ('Player', self.game.turn+1, 'tiles:')
        tiles = []
        for i in self.game.players[self.game.turn].tiles:
            tiles.append(i.letter)
        print ('                   ' , tiles)

