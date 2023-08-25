from game.cell import Cell


class Board:
    def __init__(self):
        self.grid = [
            [ Cell(1, '') for _ in range(15) ]
            for _ in range(15)
        ]
