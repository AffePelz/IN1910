from math import factorial, sqrt

import matplotlib.pyplot as plt
import numpy as np

from Polynomial import Polynomial


class HOWF:
    def __init__(self, n):
        self.n = n
        self.H = self._compute_Hermite(n)

    def _compute_Hermite(self, n):
        if n == 0:
            return Polynomial({0: 1})   # 1
        elif n == 1:
            return Polynomial({1: 2})   # 2x
        else:
            return Polynomial({1: 2})*self._compute_Hermite(n-1) + Polynomial({0: -2*(n-1)})*self._compute_Hermite(n-2)

    def __call__(self, chi):
        if self.n == 0:
            return np.pi**(-1/4)*np.exp(-(chi**2)/(2))
        elif self.n == 1:
            H1 = HOWF(1).H
            return np.pi**(-1/4)*(1/(sqrt(2)))*H1(chi)*np.exp(-(chi**2)/(2))
        else:
            Hn = HOWF(self.n).H
            return np.pi**(-1/4)*(1/(sqrt(2**self.n*factorial(self.n))))*Hn(chi)*np.exp(-(chi**2)/(2))

    def energy(self):
        return 2*self.n + 1


def test_Hermite():
    H0 = lambda x: 1
    H1 = lambda x: 2*x
    H2 = lambda x: 4*x*x - 2
    H3 = lambda x: 8*x**3 - 12*x
    H4 = lambda x: 16*x**4 - 48*x**2 + 12
    H5 = lambda x: 32*x**5 - 160*x**3 + 120*x
    H_table = [H0, H1, H2, H3, H4, H5]

    tol = 1e-12
    for n in range(0, 6):
        H = HOWF(n).H
        for x in [0, 0.5, 1.0/3, 1, 3/2, 2]:
            expected = H_table[n](x)
            computed = H(x)
            msg = "The implemented Hermite Polynomial yields unexpected result for n = %d\
            \n\tH(%.2f) = %.13g != %.13g" %(n, x, expected, computed)
            assert abs(expected - computed) < tol, msg


test_Hermite()

chi = np.linspace(-8, 8, 100)
with plt.style.context('dark_background'):
    for N in range(0, 30):
        psi = HOWF(N)
        plt.grid(True, linewidth=0.5, color='#ffffff', linestyle='-')
        plt.plot(chi, psi(chi) + psi.energy())
plt.show()
