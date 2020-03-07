from DescriptiveStats.Covariance import Covariance
from DescriptiveStats.StdDeviation import StdDeviation

class PopCorrelation:

    @staticmethod
    def popCorrelation(data1, data2):
        return Covariance.covariance(data1, data2) / (StdDeviation.stdDeviation(data1) * StdDeviation.stdDeviation(data2))