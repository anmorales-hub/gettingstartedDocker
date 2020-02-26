import unittest
from RNG.randNum import RandNum
from RNG.randList import RandList
from RNG.listPick import ListPick


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

    def test_listPick(self):
        test = [0,1,2,3,4]
        result = ListPick.listPick(test)
        x = None
        if result in test and type(result) == int:
            x = True
        self.assertEqual(True, x)

    def test_listPickSeed(self):
        test = [0, 1, 2, 3, 4]
        result = ListPick.listPickSeed(3, test)
        result2 = ListPick.listPickSeed(3, test)
        x = None
        if result in test and type(result) == int:
            if result == result2:
                x = True
        self.assertEqual(True, x)

    def test_listPickList(self):
        test = [0, 1, 2, 3, 4]
        temp = ListPick.listPickList(2, test)
        x = None
        if len(temp) == 2:
            for item in temp:
                if item in test and type(item) == int:
                    x = True
        self.assertEqual(True, x)


if __name__ == '__main__':
    unittest.main()