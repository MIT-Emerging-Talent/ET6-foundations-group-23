#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for determining whether a given number is a perfect square.

Module contents:
    - is_square: checks if a given integer is a perfect square.

Created on 26th/Dec/22024

@author: WUOR BHANG GATWECH

Challenge is from the Codewars website.

Defining the square root of a given number:
In this challenge, I will create a function that determines whether a non-negative
integer is a perfect square. The function returns `True` if the input is a
perfect square and `False` otherwise.

"""

# --- before documenting ---
# def is_square(n):
#    return False # fix me


# --- after documenting ---


def is_square(n):
    """
    Determines if the given number is a perfect square.

    Parameters:
        n (int): The number to check.

    Returns:
        bool: True if the number is a perfect square, False otherwise.

    Examples:
        >>> is_square(-1)
        False
        >>> is_square(0)
        True
        >>> is_square(3)
        False
        >>> is_square(4)
        True
        >>> is_square(25)
        True
        >>> is_square(26)
        False
    """
    if n < 0:
        return False
    sqrt_n = int(n**0.5)
    return sqrt_n * sqrt_n == n


# print(is_square(-1))  # Output: False
# print(is_square(0))   # Output: True
# print(is_square(3))   # Output: False
# print(is_square(4))   # Output: True
# print(is_square(25))  # Output: True
# print(is_square(26))  # Output: False
