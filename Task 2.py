# x = r * cos(theta)
# y = r * sin(theta)
# assuming all orbits in same plane

import numpy as np
import matplotlib.pyplot as plt

# planet data [mass (earth masses), distance from sun (AU), radius (earth radii), rotational period (days), orbital period (years), eccentricity]
inner_planets = {
    "Mercury": [0.055, 0.387, 0.38, 58.65, 0.24, 0.21],
    "Venus": [0.815, 0.723, 0.95, 243.02, 0.62, 0.01],
    "Earth": [1.000, 1.000, 1.00, 1.00, 1.00, 0.02],
    "Mars": [0.107, 1.523, 0.53, 1.03, 1.88, 0.09]
}

outer_planets = {
    "Pluto": [0.00, 39.51, 0.19, 6.39, 248.35, 0.25],
    "Neptune": [17.20, 30.25, 3.88, 0.67, 166.34, 0.01],
    "Jupiter": [317.85, 5.20, 11.21, 0.41, 11.86, 0.05],
    "Uranus": [14.50, 19.29, 4.01, 0.72, 84.75, 0.05],
    "Saturn": [95.16, 9.58, 9.45, 0.44, 29.63, 0.06]
}

# create an array of 1000 evenly spaced angles
angles = np.linspace(0, 2 * np.pi, 1000)

fig, (ax, ax2) = plt.subplots(2, figsize=(10,10))

#calculate x and y for inner planets
for planet, elements in inner_planets.items():
    # extract planet data
    m, a, r, rp, op, e = elements

    # calc distance from left focus
    r = a * (1 - e**2) / (1 - e * np.cos(angles))

    # calc x and y using equations
    x = r * np.cos(angles)
    y = r * np.sin(angles)

    ax.plot(x, y, label=planet)

#same for outer planets
for planet, elements in outer_planets.items():
    # extract planet data
    m, a, r, rp, op, e = elements

    # calc distance from left focus
    r = a * (1 - e**2) / (1 - e * np.cos(angles))

    # calc x and y using equations
    x = r * np.cos(angles)
    y = r * np.sin(angles)

    ax2.plot(x, y, label=planet)


# add sun
ax.scatter(0, 0, color="gold", label="Sun", s=100)

ax.set_aspect("equal")
ax.set_xlabel("X /AU")
ax.set_ylabel("Y /AU")
ax.set_title("Inner Solar System")
ax.grid(True)
ax.legend(loc = "upper right")

ax2.scatter(0, 0, color="gold", label="Sun", s=100)

ax2.set_aspect("equal")
ax2.set_xlabel("X /AU")
ax2.set_ylabel("Y /AU")
ax2.set_title("Outer Solar System")
ax2.grid(True)
ax2.legend(loc = "upper right")

plt.show()