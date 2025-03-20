class UnionFind:                                                                                       #Union-Find class.
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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        ufs = [UnionFind(i) for i in range(n)]                                                          #Initialize a Union-Find for each node.
        for x, y in connections:                                                                        #For each connection, union the 2 nodes connected.
            ufs[x].union(ufs[y])
        component = Counter()                                                                           #Count the size of each component.
        for x in ufs:
            component[x.find().label] += 1
        edges = Counter()                                                                               #Count the edges in each component.
        for x, y in connections:
            edges[ufs[x].find().label] += 1
        count = len(component)                                                                          #Count total number of components.
        redundantEdges = sum(edges[x] - component[x] + 1 for x in component)                            #Count total number of redundant edges; for each component size x, only x - 1 edges are necessaary.
        return count - 1 if redundantEdges >= count - 1 else -1                                         #To make all nodes connected, we need minumum count - 1 edges. Return count - 1 if redundantEdges >= count - 1; otherwise, return -1.
