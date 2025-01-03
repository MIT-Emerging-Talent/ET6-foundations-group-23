#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the length_of_longest_substring function.

This module contains tests that verify the functionality of
the length_of_longest_substring function with various input
strings, including edge cases, boundary cases, and invalid inputs.

Author:
    SADAM HUSEN ALI

Created:
    02-01-2025
"""

import unittest
from solutions.length_of_longest_substring import Solution


class TestLengthOfLongestSubstring(unittest.TestCase):
    """Unit tests for length_of_longest_substring function."""

    def test_basic_case_1(self):
        """Test longest substring length for 'abcabcbb'."""
        self.assertEqual(Solution().length_of_longest_substring("abcabcbb"), 3)

    def test_basic_case_2(self):
        """Test longest substring length for 'bbbbb'."""
        self.assertEqual(Solution().length_of_longest_substring("bbbbb"), 1)

    def test_basic_case_3(self):
        """Test longest substring length for 'pwwkew'."""
        self.assertEqual(Solution().length_of_longest_substring("pwwkew"), 3)

    def test_edge_case_empty(self):
        """Test longest substring length for empty string."""
        self.assertEqual(Solution().length_of_longest_substring(""), 0)

    def test_edge_case_single_char(self):
        """Test longest substring length for single character string."""
        self.assertEqual(Solution().length_of_longest_substring("a"), 1)

    def test_edge_case_repeating_chars(self):
        """Test longest substring length for repeating characters."""
        self.assertEqual(Solution().length_of_longest_substring("aa"), 1)

    def test_boundary_case_all_unique(self):
        """Test longest substring length for all unique characters."""
        self.assertEqual(Solution().length_of_longest_substring("abcdefghij"), 10)

    def test_boundary_case_all_same(self):
        """Test longest substring length for all same characters."""
        self.assertEqual(Solution().length_of_longest_substring("a" * 1000), 1)

    def test_boundary_case_repeating_pattern(self):
        """Test longest substring length for repeating pattern 'abc'."""
        self.assertEqual(Solution().length_of_longest_substring("abc" * 333), 3)

    def test_invalid_input(self):
        """Test invalid input (non-string)."""
        with self.assertRaises(ValueError):
            Solution().length_of_longest_substring(123)  # Non-string input


if __name__ == "__main__":
    unittest.main()
