#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating spaced repetition review days.

Module contents:
    - calculate_review_days: calculates review days based on an initial study day.

Created on 07/01/2025

@author: Novel Yonas

Spaced Repetition Review Calculator:
This module provides functionality to calculate review days
for a spaced repetition
learning technique. It determines the next four review days based on an initial
study day, with each subsequent review spaced at double the interval of the previous one.

The main function in this module is 'calculate_review_days', which is defined as follows:

    Calculate spaced repetition review days based on an initial study day.

    Args:
        start_day (int): The day of the initial study session (1-31).

    Returns:
        list[int]: A list of four spaced repetition review days.
        Each subsequent review is spaced at double
        the interval of the previous one, ignoring month and year changes.

"""


def calculate_review_days(start_day):
    """
    Calculate spaced repetition review days based on an initial study day.

    Args:
        start_day (int): The day of the initial study session (1-31).

    Returns:
        list[int]: A list of four spaced repetition review days.
        Each subsequent review is spaced at double
        the interval of the previous one, ignoring month and year changes.

    Examples:
        >>> calculate_review_days(1)
        [2, 4, 8, 16]

        >>> calculate_review_days(15)
        [16, 18, 22, 30]

        >>> calculate_review_days(28)
        [29, 31, 4, 12]

        >>> calculate_review_days(30)
        [31, 2, 6, 14]

        >>> calculate_review_days(31)
        [1, 3, 7, 15]
    """
    review_days = []  # Initialize an empty list to store review days
    current_day = start_day
    interval = 1  # Start with 1 day to the first review

    for _ in range(4):  # Loop to calculate four review days
        # Calculate the next review day
        current_day += interval

        # Adjust the day if it exceeds 31
        if current_day > 31:
            current_day -= 31

        review_days.append(current_day)  # Add the calculated day to the list
        interval *= 2  # Double the interval for the next review

    return review_days  # Return the list of review days
