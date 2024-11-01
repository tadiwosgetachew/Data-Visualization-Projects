from random import choice

class Randomwalk():
    """ Generates random walk."""
    def __init__ (self, num_points = 5000):
        ''' Initialize attributes of a walk.'''
        self.num_points = num_points

        # set starting points to zero.
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """ Calculate points in the random walk."""

        # Keep walking until the set value of 5000 is reached.
        while len(self.x_values) < self.num_points:
            # Decide which direction and how far to go in that direction
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            # Append the steps taken to the x, y coordinates.
            self.x_values.append(next_x)
            self.y_values.append(next_y)









