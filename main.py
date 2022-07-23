import numpy as np

import pygame
from pygame.locals import *
import sys

from grid import Grid


class ParticlesSimulation:

    def __init__(self):
        self.screen_size = (800, 800)
        pygame.init()
        pygame.display.set_caption("Particles Simulation")
        self.display = pygame.display.set_mode(self.screen_size)
        self.fps_clock = pygame.time.Clock()
        self.dragging = False
        self.cooldown = 20
        self.last = pygame.time.get_ticks()
        self.grid = Grid(display=self.display, size=self.screen_size)
        self.matrix = np.empty(shape=self.screen_size, dtype=object)

    def start(self):
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    self.dragging = True
                elif event.type == MOUSEBUTTONUP:
                    self.dragging = False

            if self.dragging:
                now = pygame.time.get_ticks()
                if now - self.last >= self.cooldown:
                    self.last = now
                    mpos_x, mpos_y = pygame.mouse.get_pos()
                    self.grid.set_particle(mpos_x, mpos_y)

            self.grid.read_and_update_pixels()
            pygame.display.update()
            self.fps_clock.tick(100)


if __name__ == "__main__":
    particles_simulation = ParticlesSimulation()
    particles_simulation.start()
