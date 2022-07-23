import numpy as np
import pygame
from colours import SAND, BLACK, GRAY
from cells.particles import Particles
from exceptions import OutOfBound


class Grid(Particles):

    def __init__(self, display, size):
        self.display = display
        self.size = size
        self.grid_matrix = np.empty(shape=size, dtype=object)
        self.add_floor()

    def set_particle(self, x: int, y: int):
        rect = self.get_particle_rect(x=x, y=y)
        self.grid_matrix[x, y] = SAND
        self.draw_rect(colour=SAND, rect=rect)

    # def add_floor(self):
    #     left = 0
    #     top = self.size[1] - self.size[1] * 0.1
    #     width = self.size[0]
    #     height = self.size[1] / 2
    #     rect = pygame.Rect((left, top), (width, height))
    #     self.draw_rect(colour=GRAY, rect=rect)

    def add_floor(self):
        empty = np.empty((), dtype=object)
        empty[()] = GRAY
        floor = np.full((1, self.size[1]), empty, dtype=object)
        self.grid_matrix[self.size[1] - 1] = floor

    @staticmethod
    def get_particle_rect(x: int, y: int):
        return pygame.Rect((x, y), (1, 1))

    def draw_rect(self, colour: tuple, rect: pygame.Rect):
        pygame.draw.rect(self.display, colour, rect)

    def move_particle(self, x: int, y: int):
        particle = self.get_particle_rect(x=x, y=y)

        # TODO: Trocar grid por neighbors
        # neighbors = self.get_neighbors(x=x, y=y)
        # position = zip(*np.where(neighbors == SAND))

        new_position = self.get_new_position(grid=self.grid_matrix, position=(x, y), colour=SAND)
        self.set_matrix_colour(x=x, y=y, colour=None)
        self.display.fill(BLACK, particle)
        rect = self.get_particle_rect(*new_position)
        self.draw_rect(colour=SAND, rect=rect)
        return new_position

    def set_matrix_colour(self, x: int, y: int, colour: tuple or None):
        self.grid_matrix[x, y] = colour

    def get_neighbors(self, x: int, y: int, num_neighbors: int = 1):
        left = max(0, x - num_neighbors)
        right = max(0, x + (num_neighbors + 1))
        bottom = max(0, y - num_neighbors)
        top = max(0, y + (num_neighbors + 1))
        return self.grid_matrix[left:right, bottom:top]

    def read_and_update_pixels(self):
        empty = np.empty((), dtype=object)
        empty[()] = GRAY
        sand_matrix = np.full((1, 1), empty, dtype=object)
        indexes = zip(*np.where((self.grid_matrix != None) & (self.grid_matrix != sand_matrix)))

        for x, y in indexes:
            try:
                new_position = self.move_particle(x=x, y=y)
                self.set_matrix_colour(*new_position, colour=SAND)
            except OutOfBound:
                continue
