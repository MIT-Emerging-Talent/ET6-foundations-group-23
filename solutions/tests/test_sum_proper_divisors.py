#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the sum_proper_divisors function.

This module contains unit tests for the sum_proper_divisors function.
"""

import unittest

from ..sum_proper_divisors import sum_proper_divisors


class TestSumProperDivisors(unittest.TestCase):
    """Tests for the sum_proper_divisors function."""

    def test_small_number(self):
        """It should return the correct sum for a small number."""
        actual = sum_proper_divisors(6)
        expected = 6
        self.assertEqual(actual, expected)

    def test_prime_number(self):
        """It should return 1 for a prime number."""
        actual = sum_proper_divisors(7)
        expected = 1
        self.assertEqual(actual, expected)

    def test_one(self):
        """It should return 0 for the number 1."""
        actual = sum_proper_divisors(1)
        expected = 0
        self.assertEqual(actual, expected)

    def test_large_number(self):
        """It should return the correct sum for a large number."""
        actual = sum_proper_divisors(28)
        expected = 28
        self.assertEqual(actual, expected)

    def test_non_integer(self):
        """It should raise AssertionError for non-integer input."""
        with self.assertRaises(AssertionError):
            sum_proper_divisors(10.5)

    def test_negative_number(self):
        """It should raise AssertionError for a negative number."""
        with self.assertRaises(AssertionError):
            sum_proper_divisors(-5)

    def test_zero(self):
        """It should raise AssertionError for zero input."""
        with self.assertRaises(AssertionError):
            sum_proper_divisors(0)
