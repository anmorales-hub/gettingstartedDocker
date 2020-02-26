import random

class RandNum:

    @staticmethod
    def randNum(lower, upper):
        return random.randint(lower, upper)

    @staticmethod
    def randNumSeed(seed,lower,upper):
        random.seed(seed)
        return RandNum.randNum(lower,upper)

