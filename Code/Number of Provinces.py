class UnionFind:                                                        #Union-Find class.
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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)                                            #Get the number of cities.
        ufs = [UnionFind(i) for i in range(n)]                          #Initialize a Union-Find for each city.
        for i in range(n):                                              #Traverse each edge in adjacent matrix and union the two cities on the edge.
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    ufs[i].union(ufs[j])
        return len(set([x.find().label for x in ufs]))                  #Return the distinct count of label of parent.
