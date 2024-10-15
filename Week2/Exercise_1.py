import matplotlib.pyplot as plt
import numpy as np


class Quadratic:
    def __init__(self, a2, a1, a0):
        self.a2 = a2
        self.a1 = a1
        self.a0 = a0

    def __call__(self, x):
        func = self.a2*x**2 + self.a1*x + self.a0
        return func

    def __str__(self):
        if self.a0 < 0 and self.a1 < 0:
            return f"{self.a2}*x^2 {self.a1}x {self.a0}"

        elif self.a2 == 0:
            return f"{self.a1}x {self.a0}"

        elif self.a1 < 0:
            return f"{self.a2}*x^2 {self.a1}x + {self.a0}"

        elif self.a0 < 0:
            return f"{self.a2}*x^2 + {self.a1}x {self.a0}"

        else:
            return f"{self.a2}*x^2 + {self.a1}x + {self.a0}"

    def __add__(self, other):
        a2 = self.a2 + other.a2
        a1 = self.a1 + other.a1
        a0 = self.a0 + other.a0
        return Quadratic(a2, a1, a0)

    def __sub__(self, other):
        a2 = self.a2 - other.a2
        a1 = self.a1 - other.a1
        a0 = self.a0 - other.a0
        return Quadratic(a2, a1, a0)

    def roots(self):
        root = (self.a1)**2 - 4*self.a2*self.a0
        if root < 0:
            return ()
        else:
            x1 = (-self.a1 - np.sqrt(root))/(2*self.a2)
            x2 = (-self.a1 + np.sqrt(root))/(2*self.a2)
            return (x1, x2)

    def coeffs(self):
        return self.a2, self.a1, self.a0

    def intersect(self, other):
        h = self - other
        return h.roots()


def test_Quadratic():
    f = Quadratic(1, -2, 1)
    assert abs(f(-1) - 4) < 1e-8
    assert abs(f(0) - 1) < 1e-8
    assert abs(f(1) - 0) < 1e-8


test_Quadratic()


def test_Quadratic_add():
    f = Quadratic(1, -2, 1)
    g = Quadratic(-1, 6, -3)
    h = f + g
    a2, a1, a0 = h.coeffs()
    assert a2 == 0
    assert a1 == 4
    assert a0 == -2


test_Quadratic_add()


def test_Quadratic_root():
    f1 = Quadratic(2, -2, 2)
    f2 = Quadratic(1, -2, 1)
    f3 = Quadratic(1, -3, 2)

    assert f1.roots() == ()
    assert abs(f2.roots()[0] - 1) < 1e-8
    assert abs(f3.roots()[0] - 1) < 1e-8 and abs(f3.roots()[1] - 2) < 1e-8


test_Quadratic_root()

f = Quadratic(1, -2, 1)
x = np.linspace(-5, 5, 101)
with plt.style.context('dark_background'):
    plt.grid(True, linewidth=0.5, color='#ffffff', linestyle='-')
    plt.plot(x, f(x), "red")
plt.show()

f = Quadratic(1, -2, 1)
g = Quadratic(-1, 6, -3)

h = f + g
print(h)

x = np.linspace(-5, 5, 101)
with plt.style.context('dark_background'):
    plt.grid(True, linewidth=0.5, color='#ffffff', linestyle='-')
    plt.plot(x, h(x), "red")
plt.show()

f = Quadratic(1, -2, 1)
g = Quadratic(2, 3, -2)

print(f.intersect(g))  # x-values
