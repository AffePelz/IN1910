import matplotlib.pyplot as plt
import numpy as np


class Polynomial:
    def __init__(self, dict):
        self.dict = dict

    def __call__(self, x):
        dict = self.dict
        sum = 0
        for n in dict:
            sum += dict[n]*x**(n)
        return sum

    def __str__(self):
        dict = self.dict
        for i in dict:
            return ' + '.join("{}x^{}".format(dict[i], i) for i in dict)

    def __add__(self, other):
        a = AddableDict(self.dict)
        b = AddableDict(other.dict)
        return Polynomial(a + b)

    def __mul__(self, other):
        new_dict = {}
        for m in self.dict:
            for n in other.dict:
                k = m + n
                new_dict[k] = self.dict[m]*other.dict[n]
        p = {k: v for k, v in sorted(new_dict.items(), key=lambda item: item[0])}
        return Polynomial(p)

    def derivative(self):
        new_dict = {}
        for n in self.dict:
            if n == 0:
                break
            else:
                k = n-1
                new_dict[k] = self.dict[n]*n
        return Polynomial(new_dict)

    def coeffs(self):
        return self.dict


class AddableDict(dict):
    def __add__(self, other):
        ndic = {k: v for d in (self, other) for k, v in d.items()}
        for n in self:
            for j in other:
                if n == j:
                    g = self[n] + other[j]
                    ndic[n] = g
        return ndic


def test_AddableDict():
    a = AddableDict({0: 2, 1: 3, 2: 4})
    b = AddableDict({0: -1, 1: 3, 2: 3, 3: 2})
    c = a + b
    assert c[0] == 1
    assert c[1] == 6
    assert c[2] == 7
    assert c[3] == 2


test_AddableDict()


def test_derivative():
    f = Polynomial({10: 1, 6: -3, 2: 2, 0: 1})
    f_deriv = f.derivative()
    assert f_deriv.coeffs() == {9: 10, 5: -18, 1: 4}


test_derivative()


def test_Polynomial_mul():
    f = Polynomial({2: 4, 1: 1})
    g = Polynomial({3: 3, 0: 1})
    h = f*g
    assert h.coeffs() == {5: 12, 4: 3, 2: 4, 1: 1}


test_Polynomial_mul()

coeffs = {0: 1, 5: -1, 10: 1}
f = Polynomial(coeffs)
print(f)

x = np.linspace(-1, 1, 101)
with plt.style.context('dark_background'):
    plt.grid(True, linewidth=0.5, color='#ffffff', linestyle='-')
    plt.plot(x, f(x), "red")
plt.show()

f = Polynomial({0: 1, 5: -7, 10: 1})
g = Polynomial({5: 7, 10: 1, 15: -3})

print(f+g)

a = AddableDict({0: 2, 1: 3, 2: 4})
b = AddableDict({0: -1, 1: 3, 2: 3, 3: 2})
print(a + b)
