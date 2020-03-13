from DescriptiveStats.z_score import Z_score
from PopulationSampling.marginOfError import MarginOfError
from DescriptiveStats.popProportion import PopProportion
from MathOperations.exponent import Exponent
from MathOperations.subtraction import Subtraction





class Cochran:

    @staticmethod

    def cochran(data, seeds, nums):
        z_score = Z_score.z_score(seeds,data)
        prop = PopProportion.popProportion(seeds, nums, data)
        marginError = MarginOfError.marginOfError(seeds, data)
        diff = Subtraction.difference(1, prop)

        return (Exponent.power(z_score, 2) * prop * diff) / Exponent.power(marginError, 2)