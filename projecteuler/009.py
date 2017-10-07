"""
Project Euler Problem 9
=======================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Reference: https://codereview.stackexchange.com/a/60683/112605
"""

found = False


def is_pythogorean(a, b, c):
    return ((a * a) + (b * b)) == (c * c)


for a in range(1, 1000):
    for b in range(a + 1, 1000 - a):
        c = 1000 - a - b
        if c < b:
            break
        if is_pythogorean(a, b, c):
            print(a * b * c)
            found = True
            break
    if found:
        break

