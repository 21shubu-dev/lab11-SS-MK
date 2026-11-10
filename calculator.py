
# https://github.com/21shubu-dev/lab11-SS-MK
# Partner 1: Shubham Shanubhogue
# Partner 2: Maxim Korotkiy

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a


def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm")
    return math.log(b, a)


def exp(a, b):
    return a ** b


# Additional functions from Partner 1

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError("Cannot calculate square root of a negative number")


def hypotenuse(a, b):
    return math.hypot(a, b)


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a


def logarithm(a, b):
    try:
        return math.log(b, a)
    except ValueError:
        raise ValueError("Invalid logarithm arguments")


def exponent(a, b):
    return a ** b