import matplotlib.pyplot as plt

from random_walk import Randomwalk

# Keep generating random walk as long as the program is active.

while True:
    rw = Randomwalk(5000)
    rw.fill_walk()
    # Set the size of the plotting window.
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, c ='blue', linewidth = 2)

    # Emphasize the first and last points.
    plt.plot(0,0, color= 'green', marker = 'o', markersize = 10)
    plt.plot(rw.x_values[-1], rw.y_values[-1], color= 'red', marker = 'o', markersize = 10)

    plt.title("Simulates Brownian motion of particles suspension in liquid medium.", fontsize=14)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), title='Green = start position\nRed = end position', fontsize='medium', frameon=False)
    #plt.xlabel("Pollen Grain", fontsize = 14)
    #plt.ylabel("Water Droplet", fontsize=14)

    # Remove the axes.
    plt.gca().axes.get_xaxis().set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    # make room for the legend.
    plt.tight_layout()

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break
