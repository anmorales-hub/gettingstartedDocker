import numpy

class Quartiles:

    @staticmethod
    def quartiles(data):
        x = numpy.percentile(data,25)
        y = numpy.percentile(data,50)
        z = numpy.percentile(data,75)

        return [x,y,z]


