from random import choice


def get_step(direction_variants=[1, -1], way_length=[0, 1, 2, 3, 4]):
    direction = choice(direction_variants)
    distance = choice(way_length)
    return direction*distance


class RandomWalk:

    def __init__(self, num_points=5000):
        """Initializes random walk attributes"""
        self.num_points = num_points
        # random walk starts in the point with coordinates (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculation of the walking points"""
        while len(self.x_values) < self.num_points:
            # Determining the direction and length of movement
            x_step = get_step()
            y_step = get_step()
            # Reject zero moves
            if x_step == 0 and y_step == 0:
                continue
            # Calculation of the next values x and y
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)

