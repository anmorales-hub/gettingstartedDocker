import random

class ListPick:

    @staticmethod
    def listPick(data):
        return random.choice(data)

    @staticmethod
    def listPickSeed(seed, data):
        random.seed(seed)
        return ListPick.listPick(data)