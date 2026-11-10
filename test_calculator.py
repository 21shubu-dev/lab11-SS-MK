# https://github.com/21shubu-dev/lab11-SS-MK
# Partner 1: Shubham Shanubhogue
# Partner 2: Maxim Korotkiy

import unittest
import math
from calculator import *


class TestCalculator(unittest.TestCase):

    ######### Partner 2

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-5, 3), -2)

    def test_subtract(self):
        self.assertEqual(sub(10, 5), 5)
        self.assertEqual(sub(3, 7), -4)
        self.assertEqual(sub(-2, -3), 1)

    ######### Partner 1

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 10), 0)

    def test_divide(self):
        self.assertEqual(divide(2, 10), 5)
        self.assertEqual(divide(-2, 10), -5)
        self.assertAlmostEqual(divide(3, 10), 10 / 3)

    ######### Partner 2

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(log(2, 8), 3)
        self.assertAlmostEqual(log(10, 100), 2)
        self.assertAlmostEqual(log(3, 27), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(1, 10)

    ######### Partner 1

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(-3, 4), 5)

    def test_sqrt(self):
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(0), 0)
        self.assertAlmostEqual(square_root(2), math.sqrt(2))

        with self.assertRaises(ValueError):
            square_root(-4)


# Do not touch this
if __name__ == "__main__":
    unittest.main()