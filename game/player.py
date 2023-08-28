from models import Tile,BagTiles

bag = BagTiles()


class Player:
    def __init__(self):
        self.tiles = bag.take(7)
    
    def score(self):
        self.score = 0

    def exchange(self, tile):
        tileExchange = [self.tiles[tile]]
        bag.put(tileExchange)
        del self.tiles[tile]
        self.tiles.append(bag.take(1))
