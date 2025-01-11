"""
This module provides a function to count the number of vowels in a given text.
The function considers vowels as 'a', 'e', 'i', 'o', 'u' in both lowercase and uppercase.

Function:
- vowel_counter: Counts vowels in a provided string.

Example:
    >>> vowel_counter("Hello World")
    3
"""


def vowel_counter(text) -> int:
    """
    Counts the number of vowels in the provided text.

    Vowels are considered to be 'a', 'e', 'i', 'o', 'u' (both lowercase and uppercase).

    Parameters:
        text (str): The input string to count vowels in.
        The purpose of this argument is to provide the text where the vowels (a, e, i, o, u) are searched for.

    Returns:
        int: The number of vowels in the input string.

    Raises:
        TypeError: If the input `text` is not a string.
        ValueError: If the input `text` is an empty string.

    Example:
        >>> vowel_counter("Hello World")
        3
        >>> vowel_counter("Hasan")
        2
        >>> vowel_counter("Shy myths fly by.")
        0
    """
    # Defensive assertion: Ensure the input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    # Defensive assertion: Ensure the string is not empty
    if not text:
        raise ValueError("Input string cannot be empty")

    # Define vowels and count occurrences
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)
