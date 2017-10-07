"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

Reference: http://www.mathblog.dk/project-euler-problem-3/
"""
num = 600851475143
largest_factor = num
counter = 2

while counter * counter <= num:
    if num % counter == 0:
        num = num / counter
        largest_factor = counter
    else:
        counter += 1

if num > largest_factor:
    largest_factor = num

print(largest_factor)


