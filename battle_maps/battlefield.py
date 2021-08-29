
class Battlefield:
    def __init__(self, W, H, squads):
        self.W = W
        self.H = H
        self.grid = []
        for h in range(self.H):
            self.grid.append([None]*self.W)

        self.squads = squads

    def __getitem__(self, idx):
        return self.grid[idx]



