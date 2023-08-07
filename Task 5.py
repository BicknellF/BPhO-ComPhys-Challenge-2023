# Orbit angle vs time for Pluto

import matplotlib.pyplot as plt
import numpy as np

a = 39.51
r = 0.19
rp = 6.39
op = 248.35
e = 0.25
b = 17.5

N=3
dtheta = 1/1000

def calc_circ_angle(time):
    ang_speed = 2 * np.pi / op
    return ang_speed * time
  
# array of angles for orbits
theta = np.arange(0, (2*np.pi*N), dtheta)
    
# integrand of time f(x)
f = (1 - e * np.cos(theta))**(-2)
    
# Simpson rule coefficients c = [1, 4, 2, 4, 2, 4, ....1]
c = [1] + [4 if i % 2 == 1 else 2 for i in range(1, len(theta)-1)] + [1]

# array of angles for y axis
y_axis = np.arange(0, (2*np.pi*3), 1/1000)

# array of times (x axis)
x_axis = op * ((1 - e**2)**(3/2)) * (1/(2*np.pi)) * dtheta * (1/3) * np.cumsum(c * f)

# interpolate
y_interp = np.interp(x_axis, theta, y_axis)

plt.scatter(x_axis, y_axis, s=0.5, color="green")
circ_x =[0, 3*op]
circ_y = [0, calc_circ_angle(3*op)]

plt.plot(circ_x, circ_y, "-")
plt.xlabel("time /years")
plt.ylabel("orbit polar angle /rad")
plt.title("Orbit angle vs time for Pluto")
plt.grid(True)
plt.show()

