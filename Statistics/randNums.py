import random

class RandGen:

    def fromList(self, list):
        return random.choice(list)

    def fromList_seed(self, seed, list):
        random.seed(seed)
        return self.fromList(list)

    def fromList2(self, n, list):
        temp = []
        while len(temp) < n:
            temp.append(self.fromList(list))
        return temp

    def fromList2_seed(self, seed, n, list):
        random.seed(seed)
        self.fromList2(n,list)






