import phys


class Particle:

    def __init__(self, mass):
        self.mass = mass

    def potential(self, r):
        return - phys.G * self.mass / r
