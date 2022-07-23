from cells.particle import Particle
from colours import GRAY


class Stone(Particle):
    colour = GRAY
    movable = False

    def __init__(self, grid, position):
        self.grid = grid
        self.position = position
        super().__init__(grid=grid, position=position)

    def rule(self):
        pass
