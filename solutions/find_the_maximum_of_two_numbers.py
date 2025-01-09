#!/usr/bin/env python3
# -- coding: utf-8 --
"""
A module for finding the maximum of two numbers.

Module contents:
    - find_max_number

Created on 2025-01-06
@author: Ajanduna Emmanuel
"""


def find_the_maximum_of_two_numbers(num1: int, num2: int) -> int:
    """
    This function takes two numbers and returns the greater value.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.

    Returns:
        int: The maximum number of the two numbers.

    Raises:
        AssertionError: If either input is not an int.

    Examples:
        >>> find_the_maximum_of_two_numbers(2, 4)
        4

        >>> find_the_maximum_of_two_numbers(0, -2)
        0

        >>> find_the_maximum_of_two_numbers(1, 9)
        9
    """
    assert isinstance(num1, int), "num1 must be an integer"
    assert isinstance(num2, int), "num2 must be an integer"

    return num1 if num1 > num2 else num2


if __name__ == "__main__":
    print(find_the_maximum_of_two_numbers(0, 9))
