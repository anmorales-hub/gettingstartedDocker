import unittest , pprint
import random
from numpy.random import seed, randint
from DescriptiveStats.Mean import Mean
from DescriptiveStats.Median import Median
from DescriptiveStats.Mode import Mode
from DescriptiveStats.StdDeviation import StdDeviation
from DescriptiveStats.Variance import Variance
from DescriptiveStats.Quartiles import Quartiles
from DescriptiveStats.Skewness import Skewness
from DescriptiveStats.Covariance import Covariance
from DescriptiveStats.sampCorrelation import SampCorrelation

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        seed(3)
        self.test = randint(0, 20, 10)
        self.test2 = randint(0, 20, 10)
        pprint.pprint(self.test)

    def test_Mean(self):
        self.assertEqual(8.6, Mean.mean(self.test))

    def test_Median(self):
        self.assertEqual(9.5, Median.median(self.test))

    def test_Mode(self):
        self.assertEqual(10, Mode.mode(self.test))


    def test_StdDeviation(self):
        self.assertEqual(4.8207883172775805, StdDeviation.stdDeviation(self.test))

    def test_Variance(self):
        self.assertEqual(23.240000000000002, Variance.variance(self.test))

    def test_Quartile(self):
        self.assertEqual([6.5, 9.5, 10.0], Quartiles.quartiles(self.test))

    def test_Skewness(self):
        self.assertEqual(0.2834111291185108, Skewness.skewness(self.test))

    def test_Covariance(self):
        self.assertEqual(0.7333333333333328,Covariance.covariance(self.test,self.test2))

    def test_sampCorrelation(self):
        self.assertEqual(0.09571405070239616,SampCorrelation.sampCorrelation(3,4,self.test,self.test2))




if __name__ == '__main__':
    unittest.main()