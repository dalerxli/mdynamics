G = 6.6743e-11  # m^3 s^-2 kg^-1

m_sun = 1.989e30  # kg
m_earth = 5.972e24  # kg

r_earth_orbit = 150e9  # m


def distance(pos1, pos2):
    d = 0
    for i in range(len(pos1)):
        d += (pos1[i] - pos2[i])**2
    return d ** 0.5
