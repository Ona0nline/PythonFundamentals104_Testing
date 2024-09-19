# Exercise 2: TDD for Simple Even-Odd Check Function

# Objective:
    # Implement a function that checks if a number is even based on the unit tests.

# Exercise:

# Write a unittest test case for an is_even function
    # that should take a number as input and return True 
    # if it's even and False if it's odd.
# Run the test case and observe the failure.
# Implement the is_even function.
# Run the test case again to ensure it passes.

import unittest
from number_operations import is_even  # This is the non-existent function

class TestEvenOdd(unittest.TestCase):
    def test_even_number():
        result = is_even(4)
        self.assertEqual(result, False)

    def test_odd_number():
        result = is_even(7)
        assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
