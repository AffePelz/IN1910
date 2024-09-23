import numpy as np
import matplotlib.pyplot as plt

class AffineTransfomation():
    """Calculate the Affine Transformation

    Attributes
    ----------
    a: float
        Constant of the formula
    b: float
        Constant of the formula
    c: float
        Constant of the formula
    d: float
        Constant of the formula
    e: float
        Constant of the formula
    f: float
        Constant of the formula

    """
    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0):
        """Stores the constants a, b, c, d, e and f

        Parameters
        ----------
        a: float
            Constant of the formula
        b: float
            Constant of the formula
        c: float
            Constant of the formula
        d: float
            Constant of the formula
        e: float
            Constant of the formula
        f: float
            Constant of the formula

        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def __call__(self, x, y):
        """Calculate the Affine Function

        Parameters
        ----------
        x: float
            x-coordinate
        y: float
            y-coordinate

        Returns
        -------
        x_value: float
            x-coordinate after Affine Transformation
        y_value: float
            y-coordinate after Affine Transformation
        """
        x_value = self.a*x + self.b*y + self.e
        y_value = self.c*x + self.d*y + self.f
        return x_value, y_value


if __name__ == "__main__":
    f1 = AffineTransfomation(d=0.16)
    f2 = AffineTransfomation(0.85, 0.04, -0.04, 0.85, 0, 1.60)
    f3 = AffineTransfomation(0.2, -0.26, 0.23, 0.22, 0, 1.6)
    f4 = AffineTransfomation(-0.15, 0.28, 0.26, 0.24, 0, 0.44)
    functions = f1, f2, f3, f4

    p1 = 0.01
    p2 = 0.85
    p3 = 0.07
    p4 = 0.07
    p_cumulative = [0.01, 0.86, 0.93, 1]

    def random_p(p_cumulative):
        r = np.random.random()
        for j, p in enumerate(p_cumulative):
            if r < p:
                return functions[j]

    X = np.zeros([50000, 2])
    X[0] = [0, 0]

    for i in range(50000-1):
        f = random_p(p_cumulative)
        x, y = X[i]
        X[i+1] = f(x, y)

    plt.scatter(*zip(*X), s=0.05, c="forestgreen")
    plt.axis('equal')
    plt.savefig("figures/barnsley_fern.png")
    plt.show()
