from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction
from MathOperations.multiplication import Multiplication
from MathOperations.division import Division
from MathOperations.exponent import Exponent
from MathOperations.root import Root
from MathOperations.log import Log

class Calculator:
    Result = 0

    def __init__(self):
        pass

    def sum(self, a, b):
        self.Result = Addition.sum(a,b)
        return self.Result

    def difference(self, a, b):
        self.Result = Subtraction.difference(a,b)
        return self.Result

    def product(self, a, b):
        self.Result = Multiplication.product(a,b)
        return self.Result

    def divide(self, a, b):
        self.Result = Division.quotient(a, b)
        return self.Result

    def root(self, a, b):
        self.Result = Root.root(a, b)
        return self.Result

    def power(self, a, b):
        self.Result = Exponent.power(a, b)
        return self.Result

    def log(self, a, b):
        self.Result = Log.logarithm(a, b)
        return self.Result