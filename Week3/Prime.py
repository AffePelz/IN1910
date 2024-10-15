def is_prime(n):
    if not isinstance(n, int):
        raise ValueError("Input is not an integer")

    elif n < 0:
        raise ValueError("Only positive integers allowed")

    elif n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True
