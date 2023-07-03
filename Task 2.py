# x = r * cos(theta)
# y = r * sin(theta)
# assuming all orbits in same plane

import numpy as np
import matplotlib.pyplot as plt

# planet data [mass (earth masses), distance from sun (AU), radius (earth radii), rotational period (days), orbital period (years), eccentricity]
planets = {
    "Mercury": [0.055, 0.387, 0.38, 58.65, 0.24, 0.21],
    "Venus": [0.815, 0.723, 0.95, 243.02, 0.62, 0.01],
    "Earth": [1.000, 1.000, 1.00, 1.00, 1.00, 0.02],
    "Mars": [0.107, 1.523, 0.53, 1.03, 1.88, 0.09]
}

# create an array of 1000 evenly spaced angles
angles = np.linspace(0, 2 * np.pi, 1000)

fig, ax = plt.subplots()

#calculate x and y for each planet using provided data
for planet, elements in planets.items():
    # extract planet data
    m, a, r, rp, op, e = elements

    # calc distance from left focus
    r = a * (1 - e**2) / (1 - e * np.cos(angles))

    # calc x and y using equations
    x = r * np.cos(angles)
    y = r * np.sin(angles)

    ax.plot(x, y, label=planet)

# add sun
ax.scatter(0, 0, color="gold", label="Sun", s=100)

ax.set_aspect("equal")
ax.set_xlabel("X /AU")
ax.set_ylabel("Y /AU")
ax.set_title("Inner Solar System")
ax.grid(True)
ax.legend(loc = "upper right")

plt.show()