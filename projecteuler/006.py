"""
Project Euler Problem 6
=======================

The sum of the squares of the first ten natural numbers is,
                       1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
                    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""

from functools import reduce
from operator import add

n = 100
sum_of_squares = reduce(add, map(lambda x: x*x, range(1, n + 1)))
sum_of_numbers = sum(range(1, n +1))
square_of_sum = sum_of_numbers * sum_of_numbers

print square_of_sum - sum_of_squares


