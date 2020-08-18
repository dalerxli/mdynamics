import phys
from particle import Particle


class MetaSurface:

    def __init__(self, masses):
        particles = []
        for mass in masses:
            particles.append(Particle(mass))
        self.particles = particles

    def u(self, positions, index):
        u_in = 0
        for i in range(len(self.particles)):
            if i == index:
                continue
            u_in += self.particles[i].potential(phys.distance(positions[i], positions[index]))
        u_in *= self.particles[index].mass
        u_out = 0
        return u_in + u_out
