import numpy

class Quartiles:

    @staticmethod
    def quartiles(data):
        x = numpy.quantile(data,0.25)
        y = numpy.quantile(data,0.5)
        z = numpy.quantile(data,0.75)

        return [x,y,z]


