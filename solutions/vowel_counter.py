"""
This module provides a function to count the number of vowels in a given text.
The function considers vowels as 'a', 'e', 'i', 'o', 'u' in both lowercase and uppercase.

Function:
- vowel_counter: Counts vowels in a provided string.

Example:
    >>> vowel_counter("Hello World")
    3
"""


def vowel_counter(text):
    """
    Counts the number of vowels in the provided text.

    Vowels are considered to be 'a', 'e', 'i', 'o', 'u' (both lowercase and uppercase).

    Args:
        text (str): The input string to count vowels in.

    Returns:
        int: The number of vowels in the input string.

    Example:
        >>> vowel_counter("Hello World")
        3
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


if __name__ == "__main__":
    # Example usage of vowel_counter
    example_string = "Hello World"
    print(
        f"The number of vowels in '{example_string}' is: {vowel_counter(example_string)}"
    )
