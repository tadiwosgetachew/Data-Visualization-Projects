import matplotlib.pyplot as plt

from random_walk import Randomwalk

# Keep generating random walk as long as the program is active.
while True:
    rw = Randomwalk(50000)
    rw.fill_walk()
    # Set the size of the plotting window.
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap=plt.cm.Blues, edgecolor= 'none', linewidth = 5,  s = 1)

    # Emphasize the first and last points.
    plt.scatter(0,0, color= 'green', edgecolor = 'none', s= 100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], color= 'red', edgecolor = 'none', s=100)

    # Remove the axes.
    plt.gca().axes.get_xaxis().set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break
