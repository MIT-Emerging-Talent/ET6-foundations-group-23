#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the specific gravity of a substance.

Module contents:
    - calculate_specific_gravity: calculates the specific gravity of a substance given its density.

Created on 06/01/2025

@author: Novel Yonas

Specific Gravity Calculator:
This module provides functionality to calculate the specific gravity
of a substance.
Specific gravity is a dimensionless quantity that compares the density of a substance
to the density of a reference substance (typically water at 4°C, which has a density
of 1000 kg/m³).

The specific gravity is calculated using the formula:
Specific Gravity = Density of substance / Density of reference substance

In this module, we use water at 4°C as the reference substance, with a density of 1000 kg/m³.

Usage:
    The main function in this module is 'calculate_specific_gravity', which takes
    the density of a substance as input and returns its specific gravity.
"""


def calculate_specific_gravity(a, w):
    """
    Calculates the specific gravity of a rock mass.

    Args:
      a: Float, weight of the rock mass measured in air.
      w: Float, weight of the rock mass measured in water.

    Returns:
      Float: The specific gravity of the rock mass.
      None: If the weight in air is less than or equal to the weight in water.

    Raises:
      ValueError: If invalid inputs are provided or the calculation cannot proceed.

    Examples:
      >>> calculate_specific_gravity(4, 2)
      2.0
      >>> calculate_specific_gravity(5, 2)
      1.6666666666666667
      >>> calculate_specific_gravity(2, 2)

    """
    if a <= w:
        return None  # Return None to indicate an error
    return a / (a - w)
