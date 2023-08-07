import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# planet data [mass (earth masses), distance from sun (AU), radius (earth radii), rotational period (days), orbital period (years), eccentricity]
planets = {
    "Pluto": [0.00, 39.51, 0.19, 6.39, 248.35, 0.25],
    "Neptune": [17.20, 30.25, 3.88, 0.67, 166.34, 0.01],
    "Jupiter": [317.85, 5.20, 11.21, 0.41, 11.86, 0.05],
    "Uranus": [14.50, 19.29, 4.01, 0.72, 84.75, 0.05],
    "Saturn": [95.16, 9.58, 9.45, 0.44, 29.63, 0.06]
}

time_interval = 1/100

fig, ax = plt.subplots()

scatter_points = []  # list to store scatter points for each planet
coordinates = []  # list to store x and y coordinates for each planet

# calculate x and y for each planet using provided data
for planet, elements in planets.items():
    # extract planet data
    m, a, r, rp, op, e = elements

    orbit_time = op * 365.25  # convert orbital period from years to days

    # array of times equally spaced
    times = np.arange(0, orbit_time, time_interval * 365.25)

    # calc angle based on current time value
    angles = 2 * np.pi * (times / orbit_time)  

    # calc distance from left focus
    r = a * (1 - e**2) / (1 - e * np.cos(angles))

    # calc x and y using equations
    x = r * np.cos(angles)
    y = r * np.sin(angles)

    # append the start point to the end of the coordinate arrays (completes orbital path)
    x = np.append(x, x[0])
    y = np.append(y, y[0])

    ax.plot(x, y, label=planet)

    # add scatter point for the planet at the initial position
    point, = ax.plot(x[0], y[0], 'o', markersize=8)
    scatter_points.append(point)

    # store x and y coordinates for each planet
    coordinates.append([x, y])

# gets number of coordinates given in one orbit of pluto which = number of frames needed
num_frames = len(coordinates[-1][0])
print(num_frames)

# animate the planets' movement along the orbit
def animate(i):
    for point, coord in zip(scatter_points, coordinates):
        x, y = coord
        point.set_data(x[i % len(x)], y[i % len(y)])  # Use modulo to ensure continuous motion
    if i >= num_frames - 1:
        anim.event_source.stop()  # Stop animation after Mars completes 1 orbit
    return scatter_points

# define the animation
anim = FuncAnimation(fig, animate, frames=num_frames, interval=(planets["Jupiter"][4]/planets["Pluto"][4]) / num_frames, blit=True)

# add sun
ax.scatter(0, 0, color="gold", label="Sun", s=100)

ax.set_aspect("equal")
ax.set_xlabel("X /AU")
ax.set_ylabel("Y /AU")
ax.set_title("Inner Solar System")
ax.grid(True)
ax.legend(loc="upper right")

plt.show()
