import unittest
from RNG.randNum import RandNum

class MyTestCase(unittest.TestCase):

    def test_randNum(self):
        result = RandNum.randNum(0, 10)
        self.assertEqual(int, type(result))



if __name__ == '__main__':
    unittest.main()