from RNG.listPick import ListPick
from DescriptiveStats.StdDeviation import StdDeviation
from DescriptiveStats.Mean import Mean



class Z_score:

    @staticmethod
    def z_score(seed, data):
        num =ListPick.listPickSeed(seed,data)
        mean = Mean.mean(data)
        return (num-mean)/StdDeviation.stdDeviation(data)