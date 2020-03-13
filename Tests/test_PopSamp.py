import unittest
from PopulationSampling.simpRandSamp import SimpRandSamp
from PopulationSampling.systematicSamp import SystematicSamp
from PopulationSampling.marginOfError import MarginOfError

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



if __name__ == '__main__':
    unittest.main()