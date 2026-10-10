import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    return a ** b


def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(a)


def factorial(a):
    if a < 0 or not a.is_integer():
        raise ValueError("Factorial requires a non-negative integer")
    return math.factorial(int(a))


def sine(a):
    return math.sin(math.radians(a))


def cosine(a):
    return math.cos(math.radians(a))


def tangent(a):
    if math.isclose(
        math.cos(math.radians(a)), 0.0, abs_tol=1e-12
    ):
        raise ValueError("Tangent is undefined at this angle")
    return math.tan(math.radians(a))


def natural_log(a):
    if a <= 0:
        raise ValueError("Logarithm requires a positive number")
    return math.log(a)


def log_base_10(a):
    if a <= 0:
        raise ValueError("Logarithm requires a positive number")
    return math.log10(a)


def exponential(a):
    return math.exp(a)


def reciprocal(a):
    if a == 0:
        raise ValueError("Cannot divide by zero")
    return 1 / a


def absolute(a):
    return abs(a)


def percentage(a, b):
    return (a / 100) * b
