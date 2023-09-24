# import matplotlib as mpl
import sys
# from matplotlib import cm
from random import choice

import matplotlib.pyplot as plt

# -------------------------------------------------------------------------------------------------------------------------------------------
# plot
"""
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth = 5)

# Set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels
plt.tick_params(axis='both', labelsize=14)

plt.show()
"""
# -------------------------------------------------------------------------------------------------------------------------------------------
# scatter

# plt.scatter(2, 4, s = 200)

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

x_values = list(range(1, 11))
y_values = [x**2 for x in x_values]

# plt.scatter(x_values, y_values, s=20)
# plt.scatter(x_values, y_values, edgecolor='none', s=20)
# plt.scatter(x_values, y_values, c=(11, 50, 0.8), edgecolor='none', s=20) # не работает
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.plasma, edgecolor='none', s=20)

# Set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis
# plt.axis([0, 100, 0, 1000])

plt.show()

# -------------------------------------------------------------------------------------------------------------------------------------------
# Create a class


class RandomWalk():
    # A class to generate random walks
    def __init__(self, num_points=100):
        # Initialize attributes of a walk
        self.num_points = num_points
        # All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        # Calculate all the points in the walk
        # Keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far to go in that direction
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            #
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue
            # Calculate the next x and y values
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)


# -------------------------------------------------------------------------------------------------------------------------------------------
# import a class
# from random_walk import RandomWalk

# Make a random walk, and plot the points
rw = RandomWalk()
rw.fill_walk()

# Set the size of the plotting window.
# plt.figure(figsize=(10, 6))

# plt.scatter(rw.x_values, rw.y_values, s=20)
# plt.scatter(rw.x_values, rw.y_values, c=rw.y_values, cmap=plt.cm.plasma, edgecolor='none', s=20)
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.plasma, edgecolor='none', s=20)

# Emphasize the first and last points
plt.scatter(0, 0, c='green', edgecolors='none', s=50)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)

# Remove the axes
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

# plt.savefig("matplotlib_random_walk.png")
plt.savefig("matplotlib_random_walk.png", bbox_inches='tight')  # The second argument trims extra whitespace from the plot
plt.show()
# sys.exit()
