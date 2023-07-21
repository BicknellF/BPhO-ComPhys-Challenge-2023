import numpy as np
import matplotlib.pyplot as plt

#Central planet
cp = "Earth"

# planet data [mass (earth masses), distance from sun (AU), radius (earth radii), rotational period (days), orbital period (years), eccentricity]
inner_planets = {
    "Mercury": [0.055, 0.387, 0.38, 58.65, 0.24, 0.21],
    "Venus": [0.815, 0.723, 0.95, 243.02, 0.62, 0.01],
    "Earth": [1.000, 1.000, 1.00, 1.00, 1.00, 0.02],
    "Mars": [0.107, 1.523, 0.53, 1.03, 1.88, 0.09]
}

earth = [1.000, 1.000, 1.00, 1.00, 1.00, 0.02]


# array of 1000 evenly spaced angles
angles = np.linspace(0, 20 * 2 * np.pi, 1000)

fig, ax = plt.subplots(figsize=(10,10))

for planet, elements in inner_planets.items():
    if planet != cp:
        # extract planet data
        m, a, r, rp, op, e = elements

        # calc distance from left focus
        r = a * (1 - e**2) / (1 - e * np.cos(angles))

        # calc x and y using equations, postion fo planet at time + position of earth at time
        x = r*np.cos(angles/op) + ((1 - inner_planets[cp][5]**2) / (1 - inner_planets[cp][5] * np.cos(angles)))*np.cos(angles)
        y = r*np.sin(angles/op) + ((1 - inner_planets[cp][5]**2) / (1 - inner_planets[cp][5] * np.cos(angles)))*np.sin(angles)

        ax.plot(x, y, label=planet)

# plot sun
x = ((1 - inner_planets[cp][5]**2) / (1 - inner_planets[cp][5] * np.cos(angles)))*np.cos(angles)
y = ((1 - inner_planets[cp][5]**2) / (1 - inner_planets[cp][5] * np.cos(angles)))*np.sin(angles)

ax.plot(x, y, label="Sun", color="yellow")

# add earth
ax.scatter(0, 0, color="blue", label=cp, s=100)

ax.set_aspect("equal")
ax.set_xlabel("X /AU")
ax.set_ylabel("Y /AU")
ax.set_facecolor("black")
ax.set_title("Inner Solar System Relative to Earth")
ax.grid(True)
ax.legend(loc = "upper right")

plt.show()