class UnionFind:                                                                            #Union-Find class.
    def __init__(self, x: int):
        self.parent = None
        self.label = x

    def find(self) -> 'UnionFind':
        if not self.parent:
            return self
        self.parent = self.parent.find()
        return self.parent

    def union(self, uf: 'UnionFind') -> bool:
        if self.find().label == uf.find().label:
            return True
        self.find().parent = uf.find()
        return False

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ufs = [UnionFind(i) for i in range(n)]                                             #Create a Union-Find for each node.
        return len(edges) == n - 1 and not any(ufs[x].union(ufs[y]) for x, y in edges)     #The number of edges should be exactly n - 1; also there shouldn't be any edge connecting 2 nodes that are already in same component.
