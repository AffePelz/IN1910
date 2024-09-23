import numpy as np
import matplotlib.pyplot as plt

class ChaosGame():
    """Iterates a chaos game for an n-gon.

    Attributes
    ----------
    gradient_color
    n: int
        Number of corners
    r: float
        Wanted ratio between two points
    c: list
        Contains array of coordinates
    x_values: array
        Contains array of coordinates
    colors: array
        Contains integers
    """
    def __init__(self, n, r=1/2):
        """Stores n and r appropriately.

        Parameters
        ----------
        n: int
            Number of corners
        r: float
            Wanted ratio between two points

        Raises
        ------
        ValueError
            If there are less than two corners
            or the ratio is not in the interval (0,1)
        """
        if n <= 2 or (r <= 0 or r >= 1):
            raise(ValueError)
        else:
            self.n = int(n)
            self.r = float(r)
            self._generate_ngon()

    def _generate_ngon(self):
        """Generates corners of an n-gon."""
        n = self.n
        theta = 2*np.pi/n
        c = []

        for i in range(n):
            c.append(np.array([np.sin(theta*i), np.cos(theta*i)]))

        self.c = c

    def plot_ngon(self):
        """Plots corners of n-gon"""
        plt.scatter(*zip(*self.c), c="black")

    def _starting_point(self):
        """Calculates random starting point.

        Uses random weights to calculate a random
        starting point.

        Returns
        -------
        X0: array
            Random starting point
        """
        weights = np.random.random(size=self.n)
        weights = weights/sum(weights)

        X0 = np.matmul(weights, self.c)

        return X0

    def iterate(self, steps, discard=5):
        """Iterates chaos game for n-gon.

        Creates starting point. Iterates five
        times, discarding the oldest points.
        Iterates again, storing coordinates
        and corner indexes in arrays.

        Parameters
        ----------
        steps: int
            Number of iterations that are stored
        discard: int
            Discarded iterations, defaulted to 5
        """
        X0 = self._starting_point()

        for i in range(discard):
            weights = np.random.random(size=self.n)
            weights = weights/sum(weights)

            j = np.random.randint(0, self.n)
            corner = self.c[j]

            xp = self.r*X0 + (1 - self.r)*corner
            X0 = xp

        x_values = np.zeros([steps, 2])
        colors = np.zeros(steps)

        for i in range(steps):
            weights = np.random.random(size=self.n)
            weights = weights/sum(weights)

            j = np.random.randint(0, self.n)
            corner = self.c[j]
            colors[i] = j

            x_values[i] = self.r*X0 + (1 - self.r)*corner
            X0 = x_values[i]

        self.x_values = x_values
        self.colors = colors

    def plot(self, color=False, cmap="jet"):
        """Plots chaos game iterations.

        Parameters
        ----------
        color: bool
            Deciedes if plot is colored or not. Defaulted
            to no color: False
        cmap: str
            A colormap corresponding to a defined colormap
            in matplolib

        Raises
        ------
        AttributeError
            If the iterate() method has not been called beforehand

        Warnings
        --------
        Calling the iterate() method beforehand is required

        See Also
        --------
        Colormaps can be found here:
            https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
        """
        if color:
            colors = self.gradient_color
        else:
            colors = "black"

        self.plot_ngon()
        plt.scatter(*zip(*self.x_values), c=colors, cmap=cmap, s=0.1)
        plt.axis("equal")

    def show(self, color=False, cmap="jet"):
        """Presents the plot.

        Calls on the plot() method and shows
        the plot.

        Parameters
        ---------
        color: bool
            Deciedes if plot is colored or not. Defaulted
            to no color: False
        cmap: str
            A colormap corresponding to a defined colormap
            in matplolib
        """
        self.plot(color, cmap)
        plt.show()

    @property
    def gradient_color(self):
        """Adds a gradient color to plot.

        Uses list of corner indexes to
        calculate array of gradient color
        values.

        Returns
        ------
        color_array: array
            Contains gradient color values

        Raises
        ------
        AttributeError
            If the iterate() method has not been called beforehand

        Warnings
        --------
        Calling the iterate() method beforehand is required
        """
        colors = self.colors
        length = len(colors)

        color_array = np.zeros(length)
        color_array[0] = colors[0]

        for i in range(length-1):
            color_array[i+1] = (color_array[i]+colors[i+1])/2

        return color_array

    def savepng(self, outfile, color=False, cmap="jet"):
        """Saves the image as png format.

        Parameters
        ----------
        outfile: str
            Wanted name of saved image
        color: bool
            Deciedes if plot is colored or not. Defaulted
            to no color: False
        cmap: str
            A colormap corresponding to a defined colormap
            in matplolib

        Raises
        ------
        TypeError
            If outfile is given as file format other than png
        """
        filename = outfile.split(".")
        if len(filename) == 1:
            filename = filename[0] + ".png"
        elif filename[-1] != "png":
            raise(TypeError)
        elif filename[-1] == "png":
            filename = outfile
        self.plot(color, cmap)
        plt.savefig(filename, dpi=300, transparent=False)


if __name__ == "__main__":
    for i in range(3, 9):
        c = ChaosGame(i)
        c.plot_ngon()
        plt.title(f"Corners of {i}-gon")
        plt.show()

    c = ChaosGame(5)
    c.plot_ngon()
    for i in range(1000):
        X = c._starting_point()
        plt.scatter(*zip(X), color="black")
    plt.title("1000 starting points in pentagon")
    plt.show()

    c = ChaosGame(3)
    c.iterate(10000)
    c.show(color=True)
    c.show()

    r = [1/2, 1/3, 1/3, 3/8, 1/3]
    n = [3, 4, 5, 5, 6]
    for i in range(5):
        c = ChaosGame(n[i], r[i])
        c.iterate(10000)
        c.savepng(f"figures/chaos{i+1}.png", color=True)
        plt.close()
