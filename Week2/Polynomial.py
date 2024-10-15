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
