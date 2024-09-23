import numpy as np
import matplotlib.pyplot as plt


def plot_corners():
    """Plots the corners of an equilateral triangle."""
    plt.scatter(*zip(corners[0]), color="red")
    plt.scatter(*zip(corners[1]), color="green")
    plt.scatter(*zip(corners[2]), color="blue")


def calculate_weights():
    """Calculated 3 random weights. Returns array of them

    Returns
    -------
    array
        Three randomly generated weights
    """
    weights = np.random.random(size=3)
    s = sum(weights)
    weights = weights/s
    return weights


def func1():
    """Plots 1000 random points inside the triangle.

    Uses randomly generated weights to plot 1000
    random points.
    """
    points = []
    for i in range(1000):
        weights = calculate_weights()

        points.append(np.matmul(weights, corners))

    plt.scatter(*zip(*points))
    plt.show()


def random_iteration():
    """Iterates a chaos game

    Calculates a random staring point, iterates five times
    and discard unnecessary values. Creates 3 arrays, two
    for color values and one for points. Iterates through
    10000 points, and stores color and position in arrays.
    Then it plots the points with colors corresponding to
    a random corner chosen in the iteration.
    """
    weights = calculate_weights()
    xpp = np.matmul(weights, corners)

    for i in range(5):
        weights = calculate_weights()

        j = np.random.randint(0, 3)
        corner = corners[j]

        xp = (xpp + corner)/2
        xpp = xp

    x_values = np.zeros([10000, 2])
    colors = np.zeros(10000)
    colors_matrix = np.zeros([10000, 3])

    r = np.eye(3)
    cp = 0

    for i in range(10000):
        weights = calculate_weights()

        j = np.random.randint(0, 3)
        corner = corners[j]
        r_vec = r[j]

        colors[i] = j
        colors_matrix[i] = j

        colors_matrix[i] = (cp + r_vec)/2
        x_values[i] = (xp + corner)/2

        xp = x_values[i]
        cp = colors_matrix[i]
    red = x_values[colors == 0]
    green = x_values[colors == 1]
    blue = x_values[colors == 2]

    plt.scatter(*zip(*red), s=0.1, marker=".", color="red")
    plt.scatter(*zip(*green), s=0.1, marker=".", color="green")
    plt.scatter(*zip(*blue), s=0.1, marker=".", color="blue")
    plot_corners()
    plt.axis("equal")
    plt.axis("off")
    plt.show()
    plt.scatter(*zip(*x_values), c=colors_matrix, s=0.2)
    plot_corners()
    plt.axis("equal")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    corners = [np.array([0, 0]),
               np.array([1, 0]),
               np.array([1/2, np.sqrt(3)/2])]
    plot_corners()
    plt.show()
    func1()
    random_iteration()
