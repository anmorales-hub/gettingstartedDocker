import numpy
from DescriptiveStats.Mean import Mean

class MeanDeviation:

    @staticmethod
    def meanDeviation(data):
        return Mean.mean(numpy.absolute(data - Mean.mean(data)))