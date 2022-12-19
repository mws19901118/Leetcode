class UnionFind:                                                                                        #Union find.
    def __init__(self, x: int) -> None:
        self.label = x
        self.parent = None

    def find(self):
        if not self.parent:
            return self
        self.parent = self.parent.find()
        return self.parent

    def union(self, uf) -> None:
        if self.find() != uf.find():
            self.find().parent = uf.find()

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        ufs = [UnionFind(i) for i in range(n)]                                                          #Instentiate a union find for each vertex.
        for x, y in edges:                                                                              #Union the 2 vertexes on each edge.
            ufs[x].union(ufs[y])
        return ufs[source].find() == ufs[destination].find()                                            #Return if the parent of source and destination is same.
