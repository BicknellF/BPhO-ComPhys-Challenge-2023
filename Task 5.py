import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

h = 1/1000

# planet data [mass (earth masses), distance from sun (AU), radius (earth radii), rotational period (days), orbital period (years), eccentricity, inclination]
Pluto = [0.00, 39.51, 0.19, 6.39, 248.35, 0.25, 17.5]
mass = 0.00
a = 39.51
r = 0.19
rp = 6.39
op = 248.35
e = 0.25
b = 17.5

#number of orbits
N = 3

y = 0
time = np.linspace(0, op, 1000)
#time = np.linspace(0, 3*op, 1000)
x_axis = []
y_axis = []

def calc_circ_angle(time):
    ang_speed = 2 * np.pi / op
    return ang_speed * time

theta0 = 0
def anle_time(time, theta0):
    theta = np.arange(theta0, (2*np.pi*N + theta0), h)
    L = len(theta)
    c = [1] + [4 if i % 2 == 1 else 2 for i in range(1, L-1)] + [1]

for i in time:
    y = y + abs(np.sin(0.1 * i))
    y = calc_circ_angle(i)
    x_axis.append(i)
    y_axis.append(y)

circ_x =[0, 3*op]
circ_y = [0, calc_circ_angle(3*op)]

plt.plot(circ_x, circ_y, "-")
plt.scatter(x_axis, y_axis)
plt.xlabel("time /years")
plt.ylabel("orbit polar angle /rad")
plt.title("Orbit angle vs time for pluto")
plt.grid(True)
plt.legend(loc="upper left")

plt.show()