#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit test class for the `calculate_specific_gravity` function.

This class contains test cases to validate the functionality
and edge cases of the
`calculate_specific_gravity` function, ensuring it handles valid inputs, invalid inputs,
and edge conditions gracefully.

Test cases include:
- Valid inputs where the specific gravity is correctly calculated.
- Cases where the weight in air equals or is less than the weight in water.
- Inputs with negative values to check for proper error handling.
"""

import unittest

from solutions.specific_gravity_calculator import calculate_specific_gravity


class TestCalculateSpecificGravity(unittest.TestCase):
    """specific_gravity_calculator"""

    def test_valid_input(self):
        """Test with valid inputs."""
        self.assertAlmostEqual(calculate_specific_gravity(4, 2), 2.0)
        self.assertAlmostEqual(calculate_specific_gravity(5, 2), 1.6666666666666667)

    def test_equal_weights(self):
        """Test when weight in air is equal to weight in water."""
        self.assertIsNone(calculate_specific_gravity(2, 2))

    def test_weight_in_air_less_than_water(self):
        """Test when weight in air is less than weight in water."""
        self.assertIsNone(calculate_specific_gravity(1, 2))

    def test_invalid_inputs(self):
        """Test with invalid inputs like negative values."""
        self.assertIsNone(calculate_specific_gravity(-4, 2))
        self.assertIsNone(calculate_specific_gravity(-4, -2))
