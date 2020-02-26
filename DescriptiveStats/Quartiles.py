import numpy

class Quartiles:

    @staticmethod
    def quartile1(data):
        return numpy.percentile(data,[25])

    @staticmethod
    def quartile2(data):
        return numpy.percentile(data, [50])

    @staticmethod
    def quartile3(data):
        return numpy.percentile(data, [75])


