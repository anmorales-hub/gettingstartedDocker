import unittest
from numpy.random import seed, randint

from PopulationSampling.simpRandSamp import SimpRandSamp

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(3)
        self.test = randint(0, 50, 10)

        #pprint(self.testData)

    def test_simpRandSamp(self):
        result = SimpRandSamp.simpRandSamp(3, 5,self.test)
        x = 0
        for num in result:
            if num in self.test:
                x += 1
        self.assertEqual(5, x)

if __name__ == '__main__':
    unittest.main()