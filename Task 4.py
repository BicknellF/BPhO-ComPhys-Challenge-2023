import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

option = input("Inner or outer?: ")

# planet data [mass (earth masses), distance from sun (AU), radius (earth radii), rotational period (days), orbital period (years), eccentricity, inclination]
inner_planets = {
    "Mercury": [0.055, 0.387, 0.38, 58.65, 0.24, 0.21, 1.85],
    "Venus": [0.815, 0.723, 0.95, 243.02, 0.62, 0.01, 1.85],
    "Earth": [1.000, 1.000, 1.00, 1.00, 1.00, 0.02, 1.85],
    "Mars": [0.107, 1.523, 0.53, 1.03, 1.88, 0.09, 1.85],
}
outer_planets = {
    "Pluto": [0.00, 39.51, 0.19, 6.39, 248.35, 0.25, 17.5],
    "Neptune": [17.20, 30.25, 3.88, 0.67, 166.34, 0.01, 1.77],
    "Jupiter": [317.85, 5.20, 11.21, 0.41, 11.86, 0.05, 1.31],
    "Uranus": [14.50, 19.29, 4.01, 0.72, 84.75, 0.05, 0.77],
    "Saturn": [95.16, 9.58, 9.45, 0.44, 29.63, 0.06, 2.49]
}

if option == "Inner":
    planets = inner_planets
elif option == "Outer":
    planets = outer_planets

time_interval = 1/1000
#fig, ax = plt.subplots()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

scatter_points = []  # list to store scatter points for each planet
coordinates = []  # list to store x and y coordinates for each planet

# calculate x and y for each planet using provided data
for planet, elements in planets.items():
    # extract planet data
    m, a, r, rp, op, e, b = elements

    orbit_time = op * 365.25  # convert orbital period from years to days

    # array of times equally spaced
    times = np.arange(0, orbit_time, time_interval * 365.25)

    # calc angle based on current time value
    angles = 2 * np.pi * (times / orbit_time)  

    # calc distance from left focus
    r = a * (1 - e**2) / (1 - e * np.cos(angles))

    # calc x and y using equations including the transformation
    x = (r * np.cos(angles)) * np.cos(b * np.pi / 180)
    z = (r * np.cos(angles)) * np.sin(b * np.pi / 180)
    y = r * np.sin(angles)

    # append the start point to the end of the coordinate arrays (completes orbital path)
    x = np.append(x, x[0])
    y = np.append(y, y[0])
    z = np.append(z, z[0])

    ax.plot(x, y, z, label=planet)

    # add scatter point for the planet at the initial position
    point, = ax.plot([x[0]], [y[0]], [z[0]], 'o', markersize=8)
    scatter_points.append(point)

    # store x and y coordinates for each planet
    coordinates.append([x, y, z])

# gets number of coordinates given in one orbit of mars which = number of frames needed
num_frames = len(coordinates[-1][0])
print(num_frames)

#same as before but using set_data_3d()
def animate(i):
    for point, coord in zip(scatter_points, coordinates):
        x, y, z = coord
        point.set_data_3d(x[i % len(x)], y[i % len(y)], z[i % len(z)])
    return scatter_points

# define the animation
anim = FuncAnimation(fig, animate, frames=num_frames, interval=1000/189, blit=True)

# add sun
ax.scatter(0, 0, color="gold", label="Sun", s=100)

ax.set_aspect("auto")
ax.set_xlabel("X /AU")
ax.set_ylabel("Y /AU")
ax.set_zlabel("Z /AU")
ax.set_title("Inner Solar System")
ax.grid(True)
ax.legend(loc="upper right")
ax.view_init(30, 225)

plt.show()
