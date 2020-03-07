import numpy

class Covariance:

    @staticmethod
    def covariance(x, y):
        return numpy.cov(x,y)[0,1]