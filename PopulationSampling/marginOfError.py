from DescriptiveStats.StdDeviation import StdDeviation
from DescriptiveStats.z_score import Z_score





class MarginOfError:

    @staticmethod
    def marginOfError(seed, data):
        z_score = Z_score.z_score(seed, data)
        stddev = StdDeviation.stdDeviation(data)
        return z_score * stddev