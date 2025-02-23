class UnionFind:                                                                            #Union Find class.
    def __init__(self, x: int):                                                             #Initialize.
        self.label = x
        self.parent = None

    def find(self) -> 'UnionFind':                                                          #Find and update parent.
        if not self.parent:
            return self
        self.parent = self.parent.find()
        return self.parent

    def union(self, uf: 'UnionFind') -> bool:                                               #Union with another union find and return if they are in different compoment before union.
        if self.find().label == uf.find().label:
            return True
        self.find().parent = uf.find()
        return False

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ufs = [UnionFind(i) for i in range(n)]                                             #Create a union find for each node.
        return len(edges) == n - 1 and not any(ufs[x].union(ufs[y]) for x, y in edges)     #The number of edges should be exactly n - 1; also there shouldn't be any edge connecting 2 nodes that are already in same component.
