import unittest
from RNG.randNum import RandNum

class MyTestCase(unittest.TestCase):

    def test_randNum(self):
        result = RandNum.randNum(0, 10)
        self.assertEqual(int, type(result))

    def test_randNumSeed(self):
        result1 = RandNum.randNumSeed(4, 0, 10)
        result2 = RandNum.randNumSeed(4, 0, 10)
        compare = result1 == result2
        self.assertEqual(True, compare)



if __name__ == '__main__':
    unittest.main()