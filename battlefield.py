
class Battlefield:
    def __init__(self, W, H, players):
        self.W = W
        self.H = H
        self.grid = []
        for h in range(self.H):
            self.grid.append([None]*self.W)

        self.players = players

    def __getitem__(self, idx):
        return self.grid[idx]



