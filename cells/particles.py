from cells.sand import Sand
from cells.void import Void
from cells.stone import Stone


class Particles:

    @staticmethod
    def __get_particles():
        return {
            Void.colour: Void,
            Sand.colour: Sand,
            Stone.colour: Stone
        }

    def get_new_position(self, grid, position, colour):
        particles = self.__get_particles()
        particle_object = particles[colour]
        return particle_object(grid=grid, position=position).rule()

