from RNG.listPick import ListPick

class PopProportion:

    @staticmethod
    def popProportion(seeds, nums, data):
        sample = ListPick.listPickListSeed(seeds, nums, data)
        prop = len(sample) / len(data)
        return prop