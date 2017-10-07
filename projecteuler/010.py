"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from collections import defaultdict

composites = defaultdict(list)


def genprimes():
    v = 2
    while True:
        yield v
        composites[v * v] = [v]
        v += 1
        while v in composites:
            for f in composites[v]:
                composites[v + f].append(f)
            del composites[v]
            v += 1

target = 2000000

_sum_of_primes = 0

for prime in genprimes():
    if prime >= target:
        print(_sum_of_primes)
        break
    else:
        _sum_of_primes += prime

