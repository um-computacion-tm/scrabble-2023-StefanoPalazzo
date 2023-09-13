import random

Tile_Count_Value= {
    'A': [12, 1],
    'E': [12, 1],
    'I': [6, 1],
    'L': [4, 1],
    'N': [5, 1],
    'O': [9, 1],
    'R': [5, 1],
    'S': [6, 1],
    'T': [4, 1],
    'U': [5, 1],
    'D': [5, 2],
    'G': [2, 2],
    'B': [2, 3],
    'C': [4, 3],
    'M': [2, 3],
    'P': [2, 3],
    'F': [1, 4],
    'H': [2, 4],
    'V': [1, 4],
    'Y': [1, 4],
    'CH': [1, 5],
    'Q': [1, 5],
    'J': [1, 8],
    'LL': [1, 8],
    'Ñ': [1, 8],
    'RR': [1, 8],
    'X': [1, 8],
    'Z': [1, 10],
    '?': [2, 0]
}


class Tile:
    def __init__(self,letter,value):
        self.letter = letter
        self.value = value

class BagTiles():
    def __init__(self):
        self.tiles = []
        for i in Tile_Count_Value:    #letter of the tile
            for j in range(Tile_Count_Value[i][0]):    #Amount of tiles of that letter
                self.tiles.append(Tile(i,  Tile_Count_Value[i][1])) # Adds a tile, i for the letter and Tile_Count_Value[i][1] for the value
        random.shuffle(self.tiles)

    def take(self, amount):
        tiles = []
        for _ in range(amount):
            tiles.append(self.tiles.pop())
        return tiles

    def put(self, tiles):
        self.tiles.extend(tiles)
        random.shuffle(self.tiles)



# a = BagTiles().take(3)
# print (a[0].get_value)

# # Prints each Tile and its value
# for i in range(len(BagTiles().tiles)):         
#       print (BagTiles().tiles[i].letter,BagTiles().tiles[i].value)

