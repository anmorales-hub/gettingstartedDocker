import unittest

from Calculator.Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_calculator_return_sum(self):
        result = self.calculator.Sum(1, 2)
        self.assertEqual(3, result)

    def test_calculator_return_difference(self):
        result = self.calculator.Difference(1, 2)
        self.assertEqual(-1, result)

    def test_calculator_access_difference_result(self):
        self.calculator.Difference(1, 2)
        self.assertEqual(-1, self.calculator.Result)

    def test_calculator_access_sum_result(self):
        self.calculator.Sum(1, 2)
        self.assertEqual(3, self.calculator.Result)

    def test_multiple_calculators(self):
        calculator1 = Calculator()
        calculator2 = Calculator()

        self.calculator.Sum(calculator1.Sum(1,2), calculator2.Difference(3,4))

        self.assertEqual(2, self.calculator.Result)

    def test_calculator_multiply(self):
        result = self.calculator.Multiply(2, 3)
        self.assertEqual(6, result)

    def test_calculator_divide(self):
        result = self.calculator.Divide(6, 2)
        self.assertEqual(3, result)

    def test_calculator_root(self):
        result = self.calculator.Root(169, 2)
        self.assertEqual(13, result)

    def test_calculator_power(self):
        result = self.calculator.Power(13, 2)
        self.assertEqual(169, result)


    def test_calculator_log(self):
        result = self.calculator.Logarithm(10, 1)
        self.assertEqual(0, result)

if __name__ == '__main__':
    unittest.main()