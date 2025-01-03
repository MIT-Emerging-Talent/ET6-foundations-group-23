#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module: max_area

Description:
    This module provides a solution for the "Container With Most Water" problem.
    The function determines the maximum area of water a container can hold,
    given an array of integers representing the height of the container walls.

Contents:
    - max_area: A function to compute the maximum area of water.

Challenge:
    This problem is sourced from the LeetCode platform.

Example Usage:
    >>> from max_area import Solution
    >>> height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    >>> Solution().max_area(height)
    49

Author:
    SADAM HUSEN ALI

Created:
    [02-01-2025]

Notes:
    - The solution uses the two-pointer approach for optimal performance.
    - Time complexity: O(n).
"""

from typing import List


class Solution:
    """
    A class to solve the "Container With Most Water" problem.

    Methods:
        max_area: Calculate the maximum water area a container can hold.
    """

    def max_area(self, height: List[int]) -> int:
        """
        Calculate the maximum area of water a container can hold.

        Args:
            height (List[int]): A list of non-negative integers representing the height of walls.

        Returns:
            int: The maximum area of water that can be contained.

        Raises:
            ValueError: If the input is not a list of non-negative integers.

        Examples:
            >>> Solution().max_area([1,8,6,2,5,4,8,3,7])
            49
            >>> Solution().max_area([1,1])
            1
            >>> Solution().max_area([4,3,2,1,4])
            16
        """
        if not isinstance(height, list) or not all(
            isinstance(h, int) and h >= 0 for h in height
        ):
            raise ValueError("Input must be a list of non-negative integers.")

        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            current_area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
