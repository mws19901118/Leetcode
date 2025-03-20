class UnionFind:                                                                               #Union-Find class.
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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = [UnionFind(x) for x in range(n)]                                                   #Create a Union-Find for each node..
        for a, b in edges:                                                                      #Union the Union-Finds of the 2 nodes of each edge.
            uf[a].union(uf[b])
        return len(set([x.find().label for x in uf]))                                           #Find size of distinct label of the parent of each Union-Find. 
