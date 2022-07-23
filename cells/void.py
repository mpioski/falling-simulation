from cells.particle import Particle
from colours import BLACK


class Void(Particle):
    colour = BLACK
    movable = False

    def __init__(self, grid, position):
        self.grid = grid
        self.position = position
        super().__init__(grid=grid, position=position)

    def rule(self):
        pass
