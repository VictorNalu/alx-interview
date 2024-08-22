#!/usr/bin/python3
"""
This module defines a function minOperations that calculates
the minimum number of operations required to get exactly n 'H' characters.
"""


def minOperations(n):
    """Calculate the minimum number of operations
    to get exactly n 'H' characters.
    """

    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
