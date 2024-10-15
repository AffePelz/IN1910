import math

import pytest

import calculator


def test_add_exercise_1():
    assert calculator.add(1, 2) == 3


def test_add_exercise_2():
    computed = calculator.add(0.1, 0.2)
    expected = 0.3
    assert abs(computed - expected) < 1e-9


def test_add_exercise_3():
    computed = calculator.add("Hello ", "World")
    expected = "Hello World"
    assert (computed == expected)


def test_factorial_exercise_4():
    computed = calculator.factorial(3)
    expected = math.factorial(3)
    assert abs(computed - expected) < 1e-9


def test_sin_exercise_4():
    computed = calculator.sin(40, 100)
    expected = math.sin(40)
    assert abs(computed - expected) < 1e-9


def test_divide_exercise_4():
    computed = calculator.divide(6, 3)
    expected = 2
    assert abs(computed - expected) < 1e-9


def test_multiplication_exercise_4():
    computed = calculator.multiplication(3, 4)
    expected = 12
    assert abs(computed - expected) < 1e-9


def test_subtraction_exercise_4():
    computed = calculator.subtraction(6, 5)
    expected = 1
    assert abs(computed - expected) < 1e-9


def test_add_exercise_5():
    try:
        calculator.add("Joker", 2)
    except TypeError:
        print("Cannot add string and integer together")


def test_divide_exercise_5():
    try:
        calculator.divide(4, 0)
    except ZeroDivisionError:
        print("Cannot divide with 0")


@pytest.mark.parametrize("input, expected_output", [[(-1, -1), -2], [(1, 1), 2], [(1, 0), 1]])
def test_add_exercise_1(input, expected_output):
    assert calculator.add(input[0], input[1]) == expected_output


@pytest.mark.parametrize("input, expected_output", [[(0.1, 0.2), 0.3], [(0.32, 0.11), 0.43], [(7.1, 0.11), 7.21]])
def test_add_exercise_2(input, expected_output):
    assert abs(calculator.add(input[0], input[1]) - expected_output) < 1e-9


@pytest.mark.parametrize("input, expected_output", [[("Hello ", "World"), "Hello World"], [("Yo ", "Stian"), "Yo Stian"], [("Try", " me"), "Try me"]])
def test_add_exercise_3(input, expected_output):
    assert calculator.add(input[0], input[1]) == expected_output


@pytest.mark.parametrize("factorial", [(3, math.factorial(3)), (5, math.factorial(5)), (7, math.factorial(7))])
def test_factorial_exercise_4(factorial):
    assert abs(calculator.factorial(factorial[0]) - factorial[1]) < 1e-9


@pytest.mark.parametrize("input, expected_output", [[(40, 100), math.sin(40)], [(12, 100), math.sin(12)], [(70, 100), math.sin(70)]])
def test_sin_exercise_4(input, expected_output):
    assert abs(calculator.sin(input[0], input[1]) - expected_output) < 1e-9


@pytest.mark.parametrize("input, expected_output", [[(25, 5), 5], [(21, 3), 7], [(121, 11), 11]])
def test_divide_exercise_4(input, expected_output):
    assert abs(calculator.divide(input[0], input[1]) - expected_output) < 1e-9


@pytest.mark.parametrize("input, expected_output", [[(3, 4), 12], [(11, 4), 44], [(18, 11), 198]])
def test_multiplication_exercise_4(input, expected_output):
    assert abs(calculator.multiplication(input[0], input[1]) - expected_output) < 1e-9


@pytest.mark.parametrize("input, expected_output", [[(6, 5), 1], [(12, 6), 6], [(10, 0.8), 9.2]])
def test_subtraction_exercise_4(input, expected_output):
    assert abs(calculator.subtraction(input[0], input[1]) - expected_output) < 1e-9


@pytest.mark.parametrize("input", [("Joker", 2), (2, "There"), ("Hello", 23)])
def test_add_exercise_5(input):
    with pytest.raises(TypeError):
        calculator.add(input[0], input[1])


@pytest.mark.parametrize("input", [(3, 0), (1, 0), (0, 0)])
def test_divide_exercise_5(input):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(input[0], input[1])
