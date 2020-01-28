import unittest

from Calculator.Calculator import Calculator



class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)


    def test_calculator_addition(self):
        calculator = Calculator()
        result = calculator.addition(1, 2)
        self.assertEqual(3, result)

    def test_calculator_subtraction(self):
        calculator = Calculator()
        result = calculator.subtraction(1, 2)
        self.assertEqual(-1, result)

    def test_calculator_multiply(self):
        calculator = Calculator()
        result = calculator.multiply(2, 3)
        self.assertEqual(6, result)

    def test_calculator_divide(self):
        calculator = Calculator()
        result = calculator.divide(6, 2)
        self.assertEqual(3, result)

    def test_calculator_square_root(self):
        calculator = Calculator()
        result = calculator.square_root(169)
        self.assertEqual(13, result)

    def test_calculator_square(self):
        calculator = Calculator()
        result = calculator.square(13)
        self.assertEqual(169, result)

if __name__ == '__main__':
    unittest.main()