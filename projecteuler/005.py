"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?

Reference: https://www.calculatorsoup.com/calculators/math/lcm.php
https://www.khanacademy.org/math/algebra2/rational-expressions-equations-and-functions/adding-and-subtracting-rational-expressions/v/least-common-multiple-exercise
"""
from functools import reduce


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a * b / gcd(a, b)


print reduce(lcm, range(1, 21))
