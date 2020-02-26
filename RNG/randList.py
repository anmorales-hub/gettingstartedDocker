from RNG.randNum import RandNum

class RandList:

    @staticmethod
    def randList(length, seed, lower, upper):
        data = []
        while len(data) != length:
            data.append(RandNum.randNumSeed(seed, lower, upper))
        return data
