import numpy as np
import matplotlib.pyplot as plt
from chaos_game import ChaosGame


class Variations():
    """Calculates of variation

    Maps x-coordinates and y-coordinates
    onto a specified coordinate system

    Attributes
    ----------
    linear
    handkerchief
    swirl
    disc
    exponential
    ex
    blob
    curl
    x: array
        Contains x-coordinates
    y: array
        Contains y-coordinates
    name: str
        Name of the variation
    theta: array
        Contains angle-values
    r: array
        Contains radius-values
    """
    def __init__(self, x, y, name):
        """Stores x-coordinates, y-coordinates and name

        Parameters
        ----------
        x: array
            Contains x-coordinates
        y: array
            Contains y-coordinates
        name: str
            Name of the variation
        """
        self.x = x
        self.y = y
        self.name = name
        self.theta = np.arctan2(y, x)
        self.r = np.sqrt(x**2 + y**2)

    @classmethod
    def from_chaos_game(self, chaos, name):
        """Maps chaos game onto a variation

        Parameters
        ----------
        chaos: class
            Instance of ChaosGame
        name: str
            Name of the variation

        Returns
        -------
        Variations(x, y, name): class
            Instance of variation
        """
        x = chaos.x_values[:, 0]
        y = -chaos.x_values[:, 1]
        return Variations(x, y, name)

    @staticmethod
    def linear(self, x, y):
        """Remaps x and y

        Parameters
        ----------
        x: array
            Contains x-coordinates
        y: array
            Contains y-coordinates

        Returns
        -------
        x: array
            Contains x-coordinates
        y: array
            Contains y-coordinates
        """
        return x, y

    @staticmethod
    def handkerchief(self, x, y):
        """Remaps x and y

        Parameters
        ----------
        x: array
            Contains x-coordinates
        y: array
            Contains y-coordinates

        Returns
        -------
        x_values: array
            Remapped x-coordinates
        y_values: array
            Remapped y-coordinates
        """
        x_values = self.r*np.sin(self.theta + self.r)
        y_values = self.r*np.cos(self.theta - self.r)
        return x_values, y_values

    @staticmethod
    def swirl(self, x, y):
        """Remaps x and y

        Parameters
        ----------
        x: array
            Contains x-coordinates
        y: array
            Contains y-coordinates

        Returns
        -------
        x_values: array
            Remapped x-coordinates
        y_values: array
            Remapped y-coordinates
        """
        x_values = x*np.sin(self.r**2) - y*np.cos(self.r**2)
        y_values = x*np.cos(self.r**2) + y*np.sin(self.r**2)
        return x_values, y_values

    @staticmethod
    def disc(self, x, y):
        """Remaps x and y

        Parameters
        ----------
        x: array
            Contains x-coordinates
        y: array
            Contains y-coordinates

        Returns
        -------
        x_values: array
            Remapped x-coordinates
        y_values: array
            Remapped y-coordinates
        """
        x_values = (self.theta/np.pi)*np.sin(np.pi*self.r)
        y_values = (self.theta/np.pi)*np.cos(np.pi*self.r)
        return x_values, y_values

    @staticmethod
    def exponential(self, x, y):
        """Remaps x and y

        Parameters
        ----------
        x: array
            Contains x-coordinates
        y: array
            Contains y-coordinates

        Returns
        -------
        x_values: array
            Remapped x-coordinates
        y_values: array
            Remapped y-coordinates
        """
        x_values = np.exp(x-1)*np.cos(np.pi*y)
        y_values = np.exp(x-1)*np.sin(np.pi*y)
        return x_values, y_values

    @staticmethod
    def ex(self, x, y):
        """Remaps x and y

        Parameters
        ----------
        x: array
            Contains x-coordinates
        y: array
            Contains y-coordinates

        Returns
        -------
        x_values: array
            Remapped x-coordinates
        y_values: array
            Remapped y-coordinates
        """
        p0 = np.sin(self.theta + self.r)
        p1 = np.cos(self.theta - self.r)

        x_values = self.r*(p0**3 + p1**3)
        y_values = self.r*(p0**3 - p1**3)
        return x_values, y_values

    @staticmethod
    def blob(self, x, y):
        """Remaps x and y

        Parameters
        ----------
        x: array
            Contains x-coordinates
        y: array
            Contains y-coordinates

        Returns
        -------
        x_values: array
            Remapped x-coordinates
        y_values: array
            Remapped y-coordinates
        """
        p1 = 3
        p2 = 1
        p3 = -5
        c = self.r*(p2 + (p1-p2)/2*(np.sin(p3*self.theta)+1))
        x_values = c*np.cos(self.theta)
        y_values = c*np.sin(self.theta)
        return x_values, y_values

    @staticmethod
    def curl(self, x, y):
        """Remaps x and y

        Parameters
        ----------
        x: array
            Contains x-coordinates
        y: array
            Contains y-coordinates

        Returns
        -------
        x_values: array
            Remapped x-coordinates
        y_values: array
            Remapped y-coordinates
        """
        p1 = 0.9
        p2 = 0.4
        t1 = 1 + p1*x + p2*(x**2 - y**2)
        t2 = p1*y + 2*p2*x*y
        x_values = 1/(t1**2 + t2**2)*(x*t1 + y*t2)
        y_values = 1/(t1**2 + t2**2)*(y*t1 - x*t2)
        return x_values, y_values

    def transform(self):
        """Returning the transformed coordinates

        Returns
        -------
        _func(self, self.y, self.y): function
            Remaps coordinates of specified variation
        """
        _func = getattr(Variations, self.name)
        return _func(self, self.x, self.y)


def linear_combination_wrap(variation1, variation2):
    """Combining two variations

    Parameters
    ----------
    variation1: class
        Variation instance
    variation2: class
        Variation instance

    Returns
    -------
    function: function
        Linear combination of variation
    """
    def function(w):
        """Calculating linear combination

        Parameters
        ----------
        w: float
            Weight between 0 and 1

        Returns
        -------
        x_values: array
            x-coordinates of linear combination
        y_values: array
            y-coordinates of linear combination
        """
        u1, v1 = variation1.transform()
        u2, v2 = variation2.transform()
        x_values = w*u1+(1-w)*u2
        y_values = w*v1+(1-w)*v2
        return x_values, y_values
    return function


if __name__ == "__main__":
    grid_values = np.linspace(-1, 1, 75)
    x, y = np.meshgrid(grid_values, grid_values)
    x_values = x.flatten()
    y_values = y.flatten()
    trans = ["linear", "handkerchief",
                       "swirl", "disc",
                       "exponential", "blob",
                       "ex", "curl"]

    variations = [Variations(x_values, y_values, version) for version in trans]
    fig, axs = plt.subplots(2, 4, figsize=(9, 9))
    for i, (ax, variation) in enumerate(zip(axs.flatten(), variations)):
        u, v = variation.transform()
        ax.plot(u, -v, markersize=1, marker=".", linestyle="", color="black")
        # ax.scatter(u, -v, s=0.2, marker=".", color="black")
        ax.set_title(variation.name)
        ax.axis("off")
    fig.savefig("figures/variations_4b.png")
    plt.show()

    c = ChaosGame(4, 1/3)
    c.iterate(10000)
    variations = [Variations.from_chaos_game(c, version) for version in trans]
    fig, axs = plt.subplots(2, 4, figsize=(9, 9))
    for i, (ax, variation) in enumerate(zip(axs.flatten(), variations)):
        u, v = variation.transform()
        ax.scatter(u, -v, s=0.2, marker=".", c=c.gradient_color)
        ax.set_title(variation.name)
        ax.axis("off")
    plt.show()

    coeffs = np.linspace(0, 1, 4)
    c = ChaosGame(3)
    c.iterate(10000)
    variation1 = Variations.from_chaos_game(c, "blob")
    variation2 = Variations.from_chaos_game(c, "linear")
    variation12 = linear_combination_wrap(variation1, variation2)
    fig, axs = plt.subplots(2, 2, figsize=(9, 9))
    for ax, w in zip(axs.flatten(), coeffs):
        u, v = variation12(w)
        ax.scatter(u, -v, s=0.2, marker=".", c=c.gradient_color)
        ax.set_title(f"weight = {w:.2f}")
        ax.axis("off")
    plt.show()
