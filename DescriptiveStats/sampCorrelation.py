from DescriptiveStats.Covariance import Covariance
from DescriptiveStats.StdDeviation import StdDeviation
from RNG.listPick import ListPick

class SampCorrelation:

    @staticmethod
    def sampCorrelation(seed, samp_size, data1, data2):
        dataset1 = ListPick.listPickListSeed(seed, samp_size, data1)
        dataset2 = ListPick.listPickListSeed(seed, samp_size, data2)

        return Covariance.covariance(dataset1, dataset2) / (StdDeviation.stdDeviation(dataset1) * StdDeviation.stdDeviation(dataset2))