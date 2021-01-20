"""
See this folder's README for how to execute this file.

Example from the Just Enough Python chapter in Programming Machine Learning.

This was presented as a good way to see multiple things in Python within the
context of a small script.

Finds all prime numbers between 2 and MAX_RANGE.
"""

from math import sqrt


def is_prime(n):
    max_check_value = sqrt(n)

    for x in range(2, int(max_check_value) + 1):
        if n % x == 0:
            return False

    return True


MAX_RANGE = 100

primes = []

print("Computing the prime numbers from 2 to %d:" % MAX_RANGE)

for n in range(2, MAX_RANGE):
    if is_prime(n):
        primes.append(n)

print(primes)
