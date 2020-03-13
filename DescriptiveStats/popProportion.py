from RNG.listPick import ListPick

class PopulationProportion:

    @staticmethod
    def PopProportion(seeds, nums, data):
        sample = ListPick.listPickListSeed(seeds, nums, data)
        prop = len(sample) / len(data)
        return prop