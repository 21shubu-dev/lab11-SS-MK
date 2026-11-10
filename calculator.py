
# First example
import math

def square_root(a):
    try:
      return math.sqrt(a)
    except ValueError:
        return "Cannot find the square root of a"

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

def add(a, b): 
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
   try:
     return b/a
   except ZeroDivisionError:
     return "Cannot divide by zero"

def logarithm(a,b):
    try:
      return math.log(a,b)
    except ValueError:
        return "Cannot find the logarithm of a and b"

def exponent(a,b):
    return a**b