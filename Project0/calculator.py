def add(x, y):
    return x + y


def factorial(n):
    if n == 0:
        return n
    elif n == 1:
        return 1
    else:
        return n*factorial(n-1)


def sin(x, N):
    sum = 0
    for n in range(0, N):
        sum += ((-1)**n*x**(2*n+1))/(factorial(2*n+1))
    return sum


def divide(x, y):
    return x/y


def multiplication(x, y):
    return x*y


def subtraction(x, y):
    return x - y
