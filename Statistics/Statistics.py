from Calculator.Calculator import Calculator
from DescriptiveStats.Mean import Mean

class Statistics(Calculator):

    def mean(self, data):
        self.result = Mean.mean(data)
        return self.result

    