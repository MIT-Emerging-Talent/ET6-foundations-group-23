#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the sum of proper divisors of a number.

Module contents:
    - sum_proper_divisors: calculates the sum of proper divisors of a given number.

Created on Jan 08 2025
@author: Ibrahim Elmisbah
"""


def sum_proper_divisors(n: int) -> int:
    """Calculate the sum of proper divisors of a number.

    A proper divisor of a number is a divisor that is less than the number itself.

    Parameters:
        n: int, the input number (must be positive)

    Returns -> int: the sum of proper divisors of the number

    Raises:
        AssertionError: if the argument is not a positive integer

    >>> sum_proper_divisors(6)
    6
    >>> sum_proper_divisors(10)
    8
    >>> sum_proper_divisors(1)
    0
    """
    assert isinstance(n, int), "Input must be an integer"
    assert n > 0, "Input must be a positive integer"

    # Initialize the sum of divisors
    total = 0

    # Check all possible divisors from 1 to n // 2
    for i in range(1, n // 2 + 1):
        # If 'i' divides 'n' without a remainder, it is a divisor
        if n % i == 0:
            total += i  # Add 'i' to the total sum of proper divisors

    return total
