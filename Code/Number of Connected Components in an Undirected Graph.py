class UnionFind:                                                                                #Union find.
    def __init__(self, x: int) -> None:
        self.label = x
        self.parent = None

    def find(self):
        if not self.parent:
            return self
        self.parent = self.parent.find()
        return self.parent

    def union(self, x) -> None:
        if self.find() is not x.find():
            self.find().parent = x.find()

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = [UnionFind(x) for x in range(n)]                                                   #Insteniate a list of n UnionFind.
        for a, b in edges:                                                                      #Union the UnionFind of the 2 nodes of each edge.
            uf[a].union(uf[b])
        return len(set([x.find().label for x in uf]))                                           #Find size of distinct label of the parent of each UnionFind. 
