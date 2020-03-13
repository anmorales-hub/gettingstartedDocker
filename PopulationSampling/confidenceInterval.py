from scipy.stats import sem, t
from DescriptiveStats.Mean import Mean
from PopulationSampling.simpRandSamp import SimpRandSamp

class ConfInterval:

    @staticmethod
    def confInterval_pop(confidence, data):
        length = len(data)
        mean = Mean.mean(data)
        stanError = sem(data)

        r = stanError * t.ppf((1 + confidence) / 2, length - 1)
        lower = mean - r
        upper = mean + r

        return lower, upper

    @staticmethod
    def confInterval_samp(confidence, seed, nums, data):
        samp = SimpRandSamp.simpRandSamp(seed, nums, data)

        return ConfInterval.confInterval_pop(confidence, samp)

