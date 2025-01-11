"""
This module contains unit tests for the vowel_counter module.
It includes test cases for the following function:
- vowel_counter: Test the function that counts vowels in a string.

Tests cover various cases including normal strings, empty strings, and case insensitivity.

Usage:
    Run tests using unittest framework:
    >>> python -m unittest test_vowel_counter.py
"""

import unittest

from ..vowel_counter import vowel_counter


class TestVowelCounter(unittest.TestCase):
    """
    Test suite for the vowel_counter module.
    """

    def test_vowel_counter_hello_world(self):
        """
        Test the vowel_counter function with the string 'Hello World'.
        Expect 3 vowels: 'e', 'o', 'o'.
        """
        self.assertEqual(vowel_counter("Hello World"), 3)

    def test_vowel_counter_python(self):
        """
        Test the vowel_counter function with the string 'Python'.
        Expect 1 vowel: 'o'.
        """
        self.assertEqual(vowel_counter("Python"), 1)

    def test_vowel_counter_all_vowels(self):
        """
        Test the vowel_counter function with the string 'aeiou'.
        Expect 5 vowels: all vowels are present.
        """
        self.assertEqual(vowel_counter("aeiou"), 5)

    def test_vowel_counter_no_vowels(self):
        """
        Test the vowel_counter function with the string 'XYZ'.
        Expect 0 vowels: no vowels are present.
        """
        self.assertEqual(vowel_counter("XYZ"), 0)

    def test_vowel_counter_uppercase(self):
        """
        Test the vowel_counter function with the string 'HELLO WORLD!'.
        Expect 3 vowels: 'E', 'O', 'O'.
        """
        self.assertEqual(vowel_counter("HELLO WORLD!"), 3)

    def test_vowel_counter_case_sensitive(self):
        """
        Test that the vowel_counter function is case-insensitive.
        Expect 10 vowels: 'A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u'.
        """
        self.assertEqual(
            vowel_counter("AaEeIiOoUu"), 10
        )  # All vowels, case-insensitive

    # Defensive assertion tests
    def test_invalid_input_type_integer(self):
        """Test that the function raises a TypeError for non-string input (integer)."""
        with self.assertRaises(TypeError):
            vowel_counter(12345)

    def test_invalid_input_type_list(self):
        """Test that the function raises a TypeError for non-string input (list)."""
        with self.assertRaises(TypeError):
            vowel_counter(["a", "b", "c"])

    def test_empty_string(self):
        """Test that the function raises a ValueError for an empty string."""
        with self.assertRaises(ValueError):
            vowel_counter("")


if __name__ == "__main__":
    unittest.main()
