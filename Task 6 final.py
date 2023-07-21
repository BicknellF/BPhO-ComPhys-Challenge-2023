import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

# planet data [mass (earth masses), distance from sun (AU), radius (earth radii), rotational period (days), orbital period (years), eccentricity]
planets = {
    "Mercury": [0.055, 0.387, 0.38, 58.65, 0.24, 0.21],
    "Venus": [0.815, 0.723, 0.95, 243.02, 0.62, 0.01],
    "Earth": [1.000, 1.000, 1.00, 1.00, 1.00, 0.02],
    "Mars": [0.107, 1.523, 0.53, 1.03, 1.88, 0.09],
    "Jupiter": [317.85, 5.20, 11.21, 0.41, 11.86, 0.05],
    "Saturn": [95.16, 9.58, 9.45, 0.44, 29.63, 0.06],
    "Uranus": [14.50, 19.29, 4.01, 0.72, 84.75, 0.05],
    "Neptune": [17.20, 30.25, 3.88, 0.67, 166.34, 0.01],
    "Pluto": [0.00, 39.51, 0.19, 6.39, 248.35, 0.25] 
}

def plot_orbits():
    fig, ax = plt.subplots()
    orbits = 10
    outer = outer_planet_combobox.get()
    inner = inner_planet_combobox.get()
    
    # Check outer planet is closer to the sun than the inner planet
    if planets[outer][1] <= planets[inner][1]:
        tk.messagebox.showerror("Error", "Outer planet must be further from the sun than the inner planet.")
        return
    
    ips = []
    ops = []
    time_interval = orbits * planets[outer][4] / 1234
    
    # Calculate orbits for outer planet
    m, a, r, rp, op, e = planets[outer]
    times = np.arange(0, orbits * op, time_interval)
    angles = 2 * np.pi * times / op
    r = a * (1 - e ** 2) / (1 - e * np.cos(angles))
    x = r * np.cos(angles)
    y = r * np.sin(angles)
    ops.append(np.column_stack((x, y)))
    ax.plot(x, y, label=outer)
    
    # Calculate orbits for inner planet
    m, a, r, rp, op, e = planets[inner]
    times = np.arange(0, orbits * op, time_interval)
    angles = 2 * np.pi * times / op
    r = a * (1 - e ** 2) / (1 - e * np.cos(angles))
    x = r * np.cos(angles)
    y = r * np.sin(angles)
    ips.append(np.column_stack((x, y)))
    ax.plot(x, y, label=inner)

    # Connect nth points of orbits
    for n in range(1, len(times)):
        plt.plot([x[n - 1], x[n]], [y[n - 1], y[n]], color='black', linewidth=0.1)

    for n in range(len(times)):
        for i in range(len(ips)):
            mp_nth = ips[i]
            vp_nth = ops[i]
            plt.plot([mp_nth[n-1, 0], vp_nth[n-1, 0]], [mp_nth[n-1, 1], vp_nth[n-1, 1]], color='black', linewidth=0.1)
    
    ax.set_aspect("equal")
    ax.axis("off")
    ax.legend()
    plt.show()

# GUI window
window = tk.Tk()
window.title("Planet Orbits")
window.geometry("800x400")

# planet selection labels and comboboxes
outer_label = tk.Label(window, text="Outer Planet:")
outer_label.pack()
outer_planet_combobox = ttk.Combobox(window, values=list(planets.keys()))
outer_planet_combobox.pack()

inner_label = tk.Label(window, text="Inner Planet:")
inner_label.pack()
inner_planet_combobox = ttk.Combobox(window, values=list(planets.keys()))
inner_planet_combobox.pack()

# plot button
plot_button = tk.Button(window, text="Plot Orbits", command=plot_orbits)
plot_button.pack()

window.mainloop()