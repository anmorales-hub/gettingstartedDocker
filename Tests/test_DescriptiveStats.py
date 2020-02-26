import unittest
import random
from DescriptiveStats.Mean import Mean
from DescriptiveStats.Median import Median
from DescriptiveStats.Mode import Mode


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.test = [0, 1, 2, 2, 3, 4]
        random.seed(4)

    def test_Mean(self):
        self.assertEqual(2, Mean.mean(self.test))

    def test_Median(self):
        self.assertEqual(2, Median.median(self.test))

    def test_Mode(self):
        self.assertEqual(2, Mode.mode(self.test))

if __name__ == '__main__':
    unittest.main()