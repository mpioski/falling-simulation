from cells.particle import Particle
from colours import SAND


class Sand(Particle):
    colour = SAND
    movable = True

    def __init__(self, grid, position):
        self.grid = grid
        self.position = position
        super().__init__(grid=grid, position=position)

    def rule(self):
        x, y = self.position
        down = self.is_empty(x, y + 1)
        left = self.is_empty(x - 1, y + 1)
        right = self.is_empty(x + 1, y + 1)
        if down is True:
            return x, y + 1
        elif left is True:
            return x - 1, y + 1
        elif right is True:
            return x + 1, y + 1
        else:
            return x, y