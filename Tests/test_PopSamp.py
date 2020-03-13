import unittest
from PopulationSampling.simpRandSamp import SimpRandSamp
from PopulationSampling.systematicSamp import SystematicSamp
from PopulationSampling.marginOfError import MarginOfError
from PopulationSampling.cochran import Cochran
from PopulationSampling.sampSizeConf import SampSizeConf

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.test = [1,2,3,4,5,6]

    def test_simpRandSamp(self):
        result = SimpRandSamp.simpRandSamp(3,3, self.test)
        x = None
        for i in result:
            if i in self.test:
                x = True
            else:
                x = False
        self.assertEqual(True, x)


    def test_systematicSamp(self):
        result = SystematicSamp.systematicSamp(3,3,self.test)
        self.assertEqual([2,5,5], result)

    def test_marginOfError(self):
        result = MarginOfError.marginOfError(2, self.test)
        self.assertEqual(result, -2.5)

    def test_cochran(self):
        result = Cochran.cochran(self.test, 1, 3)
        self.assertEqual(result, 0.08571428571428572)

    def test_unknownStdDev(self):
        result = SampSizeConf.unknownPopStdDev(1, self.test, .50)
        self.assertEqual(0.08571428571428573, result)

    def test_knownStdDev(self):
        result = SampSizeConf.knownPopStdDev(1, self.test)
        self.assertEqual(result, 1)



if __name__ == '__main__':
    unittest.main()