# Exercise 1: TDD for Simple Addition Function

# Objective:
    # Implement a function that adds two numbers based on the unit tests.

# Exercise:

# Write a unittest test case for an add_numbers function
# that should take two numbers as input and return their sum.
# Run the test case and observe the failure.
# Implement the add_numbers function.
# Run the test case again to ensure it passes.

import unittest
from math_operations import add_numbers  # This is the non-existent function

class TestAddition(unittest.TestCase):
    def test_add_positive_numbers(self):
        result = add_numbers(3, 4)
        self.assertEqual(result, 17)

if __name__ == '__main__':
    unittest.main()
