import matplotlib.pyplot as plt

x_values = list(range(1,101))
y_values =[x**3 for x in x_values]

plt.scatter(x_values, y_values, c = y_values, cmap=plt.cm.Reds, edgecolor="none", s=40)

# Set chart title and axis labels
plt.title("Cube Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Cube Value", fontsize = 14)

# Set the size of the tick label.
plt.tick_params(axis = "both", which = "major", labelsize = 14)

# Set the range for the axes.
plt.axis([0,110, 0,1100000])

plt.show()


