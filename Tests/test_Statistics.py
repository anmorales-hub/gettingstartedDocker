import unittest

from Statistics import Mean
from Statistics.Statistics import Statistics

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_mean(self):
        self.assertEqual(5,Mean.mean([5,5,5,5,5]))

if __name__ == '__main__':
    unittest.main()