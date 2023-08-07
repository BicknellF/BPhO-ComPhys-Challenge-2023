# plot Keplers Third Law (T/yr against (a / AU)^(3/2))
import matplotlib.pyplot as plt
import numpy as np

planets = ["Saturn", "Uranus", "Jupiter", "Neptune", "Pluto", "Mars", "Venus", "Mercury", "Earth"]
orbital_period = [29.63, 84.75, 11.86, 166.34, 248.35, 1.88, 0.62, 0.24, 1.00]
orbital_radius = [9.58, 19.29, 5.20, 30.25, 39.51, 1.523, 0.723, 0.387, 1.000]

x_axis = [(radius ** (3 / 2)) for radius in orbital_radius]


#line of best fit from linear regression
coefficients = np.polyfit(x_axis, orbital_period, 1)
lobf = np.polyval(coefficients, x_axis)

#plot graph
plt.title("Kepler's Third Law")
plt.scatter(x_axis, orbital_period)
plt.plot(x_axis, lobf, color='red')
plt.ylabel("T /Yr")
plt.xlabel("(a / AU)^(3/2)")
plt.grid(True)

#add labels
for j, name in enumerate(planets):
    plt.annotate(name, (x_axis[j], orbital_period[j]))

plt.show()