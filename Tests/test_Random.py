import unittest
from RNG.randNum import RandNum
from RNG.randList import RandList

class MyTestCase(unittest.TestCase):

    def test_randNum(self):
        result = RandNum.randNum(0, 10)
        self.assertEqual(int, type(result))

    def test_randNumSeed(self):
        result1 = RandNum.randNumSeed(4, 0, 10)
        result2 = RandNum.randNumSeed(4, 0, 10)
        self.assertEqual(True, result1 == result2)

    def test_randNumList(self):
        result1 = RandList.randList(4, 5, 0, 10)
        result2 = RandList.randList(4, 5, 0, 10)
        self.assertEqual(True, result1 == result2)


if __name__ == '__main__':
    unittest.main()