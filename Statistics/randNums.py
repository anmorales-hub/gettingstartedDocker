import random

class RandGen:

    def randNum_seed(self, seed, lower, upper):
        random.seed(seed)
        return self.randNum(lower, upper)

    def randList_seed(self, length, seed, lower, upper):
        list =[]
        while len(list) != length:
            list.append(self.randNum_seed(seed, lower, upper))
        return list

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






