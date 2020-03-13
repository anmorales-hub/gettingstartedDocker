from MathOperations.exponent import Exponent
from MathOperations.division import Division
from MathOperations.subtraction import Subtraction
from DescriptiveStats.z_score import Z_score
from DescriptiveStats.StdDeviation import StdDeviation
from PopulationSampling.marginOfError import MarginOfError


class SampSizeConf:

    @staticmethod
    def unknownPopStdDev(seed, data, percent):
        z_score = Z_score.z_score(seed, data)
        marginError = MarginOfError.marginOfError(seed, data)

        x = percent
        y = Subtraction.difference(1, x)
        xy = Division.quotient(z_score, marginError)

        sample = Exponent.power(xy, 2) * x * y

        return sample


    @staticmethod
    def knownPopStdDev(seed, data):
        z_score = Z_score.z_score(seed, data)
        marginError = MarginOfError.marginOfError(seed, data)
        stdDev = StdDeviation.stdDeviation(data)

        value = (z_score * stdDev) / marginError

        return Exponent.power(value, 2)