"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b): 
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def logarithm(a,b):
    try:
        return math.log(a,b)
    except ValueError:
        return "Cannot find the logarithm of a and b"

def exponent(a,b):
    return a**b
