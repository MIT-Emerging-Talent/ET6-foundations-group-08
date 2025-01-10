#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for find_two_sum_indices function.

Created on 2025-01-05

Author: Emmanuel
"""

import unittest

from ..find_the_maximum_of_two_numbers import find_the_maximum_of_two_numbers


class TestFindMaximum(unittest.TestCase):
    """
    Unit tests for the find_max_number function.
    """


class TestFindMaxNumber(unittest.TestCase):
    """
    Test cases for the find_max_number function.
    """

    def test_max_of_two_positive_numbers(self):
        """
        Test finding the maximum of two positive numbers.
        """
        self.assertEqual(find_the_maximum_of_two_numbers(3, 5), 5)

    def test_max_of_two_negative_numbers(self):
        """
        Test finding the maximum of two negative numbers.
        """
        self.assertEqual(find_the_maximum_of_two_numbers(-3, -5), -3)

    def test_max_of_positive_and_negative_number(self):
        """
        Test finding the maximum of a positive and a negative number.
        """
        self.assertEqual(find_the_maximum_of_two_numbers(3, -5), 3)

    def test_max_of_two_equal_numbers(self):
        """
        Test finding the maximum of two equal numbers.
        """
        self.assertEqual(find_the_maximum_of_two_numbers(7, 7), 7)

    def test_invalid_input(self):
        """
        Test handling of invalid input types.
        """
        with self.assertRaises(AssertionError):
            find_the_maximum_of_two_numbers(3, "five")

        with self.assertRaises(AssertionError):
            find_the_maximum_of_two_numbers("three", 5)


if __name__ == "__main__":
    unittest.main()
