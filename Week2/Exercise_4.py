def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


class Fibonacci:
    def __init__(self):
        self.memory = {0: 0, 1: 1}

    def __call__(self, n, recursion=0, repeats=0):
        if n in self.memory:
            return self.memory[n]

        else:
            for n in range(2, n):
                fn = self(n-1) + self(n-2)
                self.memory[n] = fn
            return fn

        pass


def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return n*factorial(n-1)


class Factorial:
    def __init__(self):
        self.memory = {0: 1, 1: 1}

    def __call__(self, n, recursion=0, repeats=0):
        if n in self.memory:
            return self.memory[n]

        else:
            for n in range(2, n):
                fn = n*self(n-1)
                self.memory[n] = fn
            return fn
    pass


def test_fibonacci():
    computed = []
    for i in range(11):
        computed.append(fibonacci(i))
    assert computed == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def test_Factorial():
    f = Factorial()
    computed = []
    for i in range(6):
        computed.append(f(i))

    assert computed == [1, 1, 2, 6, 24, 120]


m = 100000
n = 10000
fib = Fibonacci()
print(f"F({m}) = {fib(m)}")
print("")
fac = Factorial()
print(f"{n}! = {fac(n)}")
