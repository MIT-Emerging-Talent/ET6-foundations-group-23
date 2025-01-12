"""
This module contains a function to check if a string is a palindrome.

A palindrome is a string that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.
"""


def palindrome_checker(s: str) -> bool:
    """
    Check if a given string is a palindrome, ignoring spaces, punctuation, and capitalization.

    Parameters:
        s (str): The input string to check.

    Returns:
        bool: True if the input string is a palindrome, False otherwise.

    Raises:
        TypeError: If the input `s` is not a string.

    Example:
        >>> palindrome_checker("A man, a plan, a canal: Panama")
        True
        >>> palindrome_checker("Hello")
        False
        >>> palindrome_checker("12321")
        True
    """
    # Defensive assertion: Ensure the input is a string
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    # Normalize the string: remove non-alphanumeric characters and convert to lowercase
    normalized = "".join(char.lower() for char in s if char.isalnum())
    # Check if the normalized string is equal to its reverse
    return normalized == normalized[::-1]
