import unittest
from calculator import *

class TestMul(unittest.TestCase):
    def test_multiplication_of_two_integers(self):
        self.assertEqual(mul(2,3),
                         6,
                         "multiplication of two integers should give an integer")

    def test_multiplication_of_two_float(self):
        self.assertEqual(
            mul(2.5, 4.0),
             10.0, 
             "multiplication of two floating numbers should give a float value")

class TestDivide(unittest.TestCase):
    def test_division_of_two_positive_integers(self):
        self.assertEqual(divide(3, 2),
                         1.5,
                         "should divide two positive integers")

    def test_division_of_any_number_with_zero(self):
        with self.assertRaises(ValueError):
             divide(3, 0)

class TestSub(unittest.TestCase):
    def test_subtraction_of_two_integers(self):
        self.assertEqual(sub(3, 2),
                         1,
                         "should subtract two integers")

    def test_subtraction_of_two_floating_numbers(self):
        self.assertEqual(sub(3.5, 2.5),
                         1,
                         "should subtract two floating numbers")

    def test_subtraction_of_not_a_number(self):
        with self.assertRaises(TypeError):
             sub(3, "abc")

if __name__ == "__main__":
    unittest.main()