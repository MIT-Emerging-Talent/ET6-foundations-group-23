#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module: longest_substring

Description:
    This module provides a solution for the problem of finding the length
    of the longest substring without repeating characters in a given string.

Contents:
    - Solution: A class with a method to compute the length of the longest
      substring without repeating characters.

Example Usage:
    >>> s = "abcabcbb"
    >>> Solution().length_of_longest_substring(s)
    3

Author:
    SADAM HUSEN ALI

Created:
    02-01-2025

Notes:
    - The solution uses the sliding window approach for optimal performance.
    - Time complexity: O(n).
"""

from collections import defaultdict


class Solution:
    """
    A class to solve the problem of finding the length of the longest substring
    without repeating characters.

    Methods:
        length_of_longest_substring: Calculate the length of the longest
        substring without repeating characters.
    """

    def length_of_longest_substring(self, s: str) -> int:
        """
        Calculate the length of the longest substring without repeating characters.

        Args:
            s (str): The input string.

        Returns:
            int: The length of the longest substring without repeating characters.

        Raises:
            ValueError: If the input is not a string.

        Examples:
            >>> Solution().length_of_longest_substring("abcabcbb")
            3
            >>> Solution().length_of_longest_substring("bbbbb")
            1
            >>> Solution().length_of_longest_substring("")
            0
            >>> Solution().length_of_longest_substring(12345)
            Traceback (most recent call last):
            ...
            ValueError: Input must be a string.
        """
        if not isinstance(s, str):
            raise ValueError("Input must be a string.")

        # Dictionary to track character counts in the current substring
        char_count = defaultdict(int)
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            # Increment the count of the current character
            char_count[char] += 1

            # If a duplicate character is found, adjust the left pointer
            while char_count[char] > 1:
                char_count[s[left]] -= 1
                left += 1

            # Update the maximum length
            max_length = max(max_length, right - left + 1)

        return max_length
