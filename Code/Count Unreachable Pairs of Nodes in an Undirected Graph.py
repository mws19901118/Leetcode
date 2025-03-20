class UnionFind:                                                                     #Union-Find class.
    def __init__(self, x: int):
        self.parent = None
        self.label = x

    def find(self) -> 'UnionFind':
        if not self.parent:
            return self
        self.parent = self.parent.find()
        return self.parent

    def union(self, uf: 'UnionFind') -> None:
        if not self.find().label == uf.find().label:
            self.find().parent = uf.find()

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        ufs = [UnionFind(i) for i in range(n)]                                      #Initialize a Union-Find for each node. 
        for x, y in edges:                                                          #For each edge, union the 2 union finds of nodes on edge.
            ufs[x].union(ufs[y])

        count = Counter([x.find().label for x in ufs])                              #Count the size of each component.
        return sum(count[x] * (n - count[x]) for x in count) // 2                   #For each component, there are count[x] * (n - count[x]) ordered pairs unreachable nodes. Sum them up and divide by 2 then return.
