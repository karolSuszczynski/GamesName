
class SingleField:
    __slots__ = ["ground_height", "building"]

class Startegicfield:
    def __init__(self, W, H, players):
        self.W = W
        self.H = H

        self.grid = []
        for y in range(self.H):
            self.grid.append([])
            for x in range(self.W):
                self.grid[y].append(SingleField())

        self.players = players

    def __getitem__(self, idx):
        return self.grid[idx]



