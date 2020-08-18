from scipy.integrate import ode
from scipy.misc import derivative
import matplotlib.pyplot as plt
import math


G = 6.6743e-11  # m^3 s^-2 kg^-1
M = 1.989e30  # kg
m = 5.972e24  # kg
r_earth_orbit = 150e9  # m


def u(pos):
    return - G * M * m / math.hypot(pos[0], pos[1])


def partial_derivative(func, var, pos):
    args = pos[:]

    def wraps(x):
        args[var] = x
        return func(args)
    return derivative(wraps, pos[var])


def f(t, y):
    return [y[2],
            y[3],
            -(1 / m) * partial_derivative(u, 0, [y[0], y[1]]),
            -(1 / m) * partial_derivative(u, 1, [y[0], y[1]])]


def simulate_movement(pos_init, vel_init, time, n=100):
    y0, t0 = pos_init + vel_init, 0
    r = ode(f).set_integrator('dopri5')
    r.set_initial_value(y0, t0)
    dt = time / n

    path = []
    while r.successful() and r.t < time:
        path.append([r.t + dt] + list(r.integrate(r.t+dt)))
    return path


if __name__ == '__main__':
    pos_init = [0, r_earth_orbit]
    vel_init = [30e3, 0]

    path = simulate_movement(pos_init, vel_init, 365 * 24 * 3600, n=10000)
    print(path)

    x_path = [y[1] for y in path]
    y_path = [y[2] for y in path]

    print(x_path)
    print(y_path)

    fig, ax = plt.subplots()
    ax.plot(x_path, y_path)
    plt.show()
