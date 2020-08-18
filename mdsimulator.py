from metasurface import MetaSurface
from scipy.misc import derivative
from scipy.integrate import ode
import numpy as np
import phys
import matplotlib.pyplot as plt


def partial_derivative(u, particle_index, coordinate_index, pos):
    args = pos[:]

    def wrap(x):
        args[particle_index, coordinate_index] = x
        return u(args, particle_index)
    return derivative(wrap, pos[particle_index, coordinate_index])


def f(t, y, surface):
    to_return = []
    for i in range(int(len(y) / 2), len(y)):
        to_return.append(y[i])

    pos = np.reshape(y[:int(len(y) / 2)], (len(surface.particles), -1))
    for i in range(len(pos)):
        m = surface.particles[i].mass
        for j in range(len(pos[i])):
            to_return.append(-(1 / m) * partial_derivative(surface.u, i, j, pos))
    return to_return


def simulate_movement(surface, pos_init, vel_init, time, n=1000):
    y0, t0 = np.append(np.reshape(pos_init, -1), np.reshape(vel_init, -1)), 0
    r = ode(f).set_integrator('vode')
    r.set_initial_value(y0, t0).set_f_params(surface)
    dt = time / n

    path = []
    while r.successful() and r.t < time:
        path.append([r.t + dt] + list(r.integrate(r.t + dt)))
    return path


if __name__ == '__main__':
    # surface = MetaSurface([phys.m_earth, phys.m_sun])
    # pos_init = [[0, phys.r_earth_orbit], [0, 0]]
    # vel_init = [[30e3, 0], [0, 0]]

    surface = MetaSurface([1e6, 1e6, 1e6])
    pos_init = [[0, 0], [100, 0], [0, 100]]
    vel_init = [[0, 0], [0, 0], [0, 0]]

    # surface = MetaSurface([1])
    # pos_init = [[0, 0]]
    # vel_init = [[1, 0]]

    path = simulate_movement(surface, pos_init, vel_init, 1e5)

    print(path)

    x1 = [a[1] for a in path]
    y1 = [a[2] for a in path]

    x2 = [a[3] for a in path]
    y2 = [a[4] for a in path]

    x3 = [a[5] for a in path]
    y3 = [a[6] for a in path]

    plt.plot(x1, y1, label='body 1')
    plt.plot(x2, y2, label='body 2')
    plt.plot(x3, y3, label='body 3')

    plt.legend()
    plt.show()
