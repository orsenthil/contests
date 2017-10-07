"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Reference: https://stackoverflow.com/a/26834494
"""
largest_3_digit = 999
max_number = 100001 # smallest

for i in range(largest_3_digit, 100, -1):
    if max_number > (i * largest_3_digit):
        break

    for j in range(largest_3_digit, i, -1):
        prod = i * j
        if str(prod) == str(prod)[::-1]:
            max_number = prod

print(max_number)
