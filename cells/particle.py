from abc import ABC, abstractmethod
from colours import BLACK

from exceptions import OutOfBound


class Particle(ABC):

    def __init__(self, grid, position):
        self.grid = grid
        self.position = position

    @property
    def grid(self):
        return self._grid

    @grid.setter
    def grid(self, value):
        self._grid = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    @abstractmethod
    def colour(self) -> tuple:
        return 0, 0, 0

    @property
    @abstractmethod
    def movable(self) -> bool:
        return False

    @abstractmethod
    def rule(self):
        pass

    def is_empty(self, x, y):
        if not self.is_out_of_bounds(x, y):
            return self.grid[x, y] == None or BLACK
        raise OutOfBound

    def is_out_of_bounds(self, x: int, y: int):
        """
        Verifica se a posição está no grid
        :param x:
        :param y:
        :return:
        """
        return any([(a >= b) for a, b in zip((x, y), self.grid.shape)])