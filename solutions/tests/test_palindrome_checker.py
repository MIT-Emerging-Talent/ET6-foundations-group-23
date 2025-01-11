"""
This module contains unit tests for the `palindrome_checker` function in `palindrome_checker.py`.

The `palindrome_checker` function determines whether a string is a palindrome, ignoring spaces,
punctuation, and capitalization.
"""

import unittest

from solutions.palindrome_checker import palindrome_checker


class TestPalindromeChecker(unittest.TestCase):
    """
    Unit tests for the `palindrome_checker` function.
    """

    # Test cases where the input string is a palindrome
    def test_palindrome_phrase(self):
        """
        Test a palindrome phrase with punctuation and spaces.
        """
        self.assertTrue(palindrome_checker("A man, a plan, a canal: Panama"))

    def test_palindrome_single_word(self):
        """
        Test a single-word palindrome.
        """
        self.assertTrue(palindrome_checker("Racecar"))

    def test_palindrome_numeric(self):
        """
        Test a numeric palindrome.
        """
        self.assertTrue(palindrome_checker("12321"))

    def test_palindrome_empty_string(self):
        """
        Test an empty string as a palindrome.
        """
        self.assertTrue(palindrome_checker(""))

    # Test cases where the input string is not a palindrome
    def test_non_palindrome_single_word(self):
        """
        Test a non-palindrome word.
        """
        self.assertFalse(palindrome_checker("Hello"))

    def test_non_palindrome_phrase(self):
        """
        Test a non-palindrome phrase.
        """
        self.assertFalse(palindrome_checker("Not a palindrome"))

    # Test edge cases
    def test_edge_case_single_letter(self):
        """
        Test a single-letter string.
        """
        self.assertTrue(palindrome_checker("a"))

    def test_edge_case_single_space(self):
        """
        Test a single space character.
        """
        self.assertTrue(palindrome_checker(" "))

    def test_edge_case_special_characters(self):
        """
        Test a string with only special characters.
        """
        self.assertTrue(palindrome_checker("!!"))

    def test_edge_case_mixed_phrase(self):
        """
        Test a complex palindrome phrase with mixed case and punctuation.
        """
        self.assertTrue(palindrome_checker("Able , was I saw eLba"))

    # Defensive assertion tests
    def test_invalid_input_type_integer(self):
        """
        Test that the function raises a TypeError for non-string input (integer).
        """
        with self.assertRaises(TypeError):
            palindrome_checker(12345)

    def test_invalid_input_type_list(self):
        """
        Test that the function raises a TypeError for non-string input (list).
        """
        with self.assertRaises(TypeError):
            palindrome_checker(["a", "b", "c"])

    def test_invalid_input_type_none(self):
        """
        Test that the function raises a TypeError for non-string input (None).
        """
        with self.assertRaises(TypeError):
            palindrome_checker(None)


if __name__ == "__main__":
    unittest.main()
