def factorize(n):
    list = []

    def is_prime(n):
        if n == 1:
            return False

        for i in range(2, n):
            if n % i == 0:
                return False

        return True

    i = 2
    while n > 1:
        if is_prime(i):
            if n % i == 0:
                n = n/i
                list.append(i)
            else:
                i += 1
        else:
            i += 1
    return list


def test_factorize():
    assert factorize(412415) == [5, 82483]
    assert factorize(27) == [3, 3, 3]
    assert factorize(31) == [31]


test_factorize()
