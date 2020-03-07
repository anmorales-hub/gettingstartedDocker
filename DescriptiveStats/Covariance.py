import numpy

class Covariance:

    @staticmethod
    def covariance(x_vals, y_vals):
        return numpy.cov(x_vals,y_vals)[0,1]