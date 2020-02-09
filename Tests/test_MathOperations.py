import unittest

from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction
from MathOperations.multiplication import Multiplication
from MathOperations.division import Division
from MathOperations.exponent import Exponent


class MyTestCase(unittest.TestCase):

    def test_MathOperations_Addition(self):
        self.assertEqual(3, Addition.sum(1,2))

    def test_MathOperations_Subtraction(self):
        self.assertEqual(-1, Subtraction.difference(1,2))

    def test_MathOperations_sum_list(self):
        valuelist = [1,2,3]
        self.assertEqual(6, Addition.sum(valuelist))

    def test_MathOperations_Multiply(self):
        self.assertEqual(6, Multiplication.product(2,3))

    def test_calculator_divide(self):
        self.assertEqual(2, Division.quotient(6,3))

    def test_calculator_square_root(self):
        calculator = Calculator()
        result = calculator.square_root(169)
        self.assertEqual(13, result)

    def test_calculator_exponent(self):
        self.assertEqual(169, Exponent.power(13,2))

if __name__ == '__main__':
    unittest.main()