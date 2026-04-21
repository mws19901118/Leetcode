class UnionFind:                                                                                       #Union-Find class.
    def __init__(self, x):
        self.index = x
        self.parent = None

    def find(self) -> 'UnionFind':
        if not self.parent:
            return self
        self.parent = self.parent.find()
        return self.parent

    def union(self, uf: 'UnionFind') -> bool:
        if self.find().index == uf.find().index:
            return True
        self.find().parent = uf.find()
        return False

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        ufs = [UnionFind(i) for i in range(len(source))]                                              #Create a union-find for each class.
        for x, y in allowedSwaps:                                                                     #Union the union find of the indexes in each swap.
            ufs[x].union(ufs[y])
        groups = defaultdict(list)
        for uf in ufs:                                                                                #Find the groups of indexes, indexes in same group can swap freely.
            groups[uf.find().index].append(uf.index)
        result = 0
        for g in groups.values():                                                                     #Traverse each group.
            counterSource = Counter(source[x] for x in g)                                             #Count the numbers in source on current indexes.
            counterTarget = Counter(target[x] for x in g)                                             #Count the numbers in target on current indexes.
            result += len(g) - sum(min(counterSource[x], counterTarget[x]) for x in counterSource)    #Non-comon numbers will increase the hamming distance.
        return result
