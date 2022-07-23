import pygame
from colours import SAND, BLACK, GRAY
from cells.particles import Particles
from exceptions import OutOfBound
from timer import Timer


class Grid(Particles):

    def __init__(self, display, size):
        self.display = display
        self.size = size

    def set_particle(self, x: int, y: int):
        rect = self.get_particle_rect(x=x, y=y)
        self.draw_rect(colour=SAND, rect=rect)

    @staticmethod
    def get_particle_rect(x: int, y: int):
        return pygame.Rect((x, y), (1, 1))

    def draw_rect(self, colour: tuple, rect: pygame.Rect):
        pygame.draw.rect(self.display, colour, rect)

    def move_particle(self, x: int, y: int):
        color = self.display.get_at((x, y))[:3]
        if color not in [BLACK, GRAY]:  # TODO: Trocar por algo solido
            new_position = self.get_new_position(display=self.display, position=(x, y), colour=color)
            particle = self.get_particle_rect(x=x, y=y)
            self.display.fill(BLACK, particle)
            rect = self.get_particle_rect(*new_position)
            self.draw_rect(colour=SAND, rect=rect)

    def read_and_update_pixels(self):
        with Timer("read_and_update_pixels"):
            for x in reversed(range(300)):
                for y in reversed(range(300)):
                    try:
                        self.move_particle(x=x, y=y)
                    except OutOfBound:
                        continue
