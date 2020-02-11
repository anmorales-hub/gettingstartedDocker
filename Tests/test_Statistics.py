import unittest

from Statistics import Mean
from Statistics.Statistics import Statistics

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.testData = [1,2]
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, 1.5)

if __name__ == '__main__':
    unittest.main()