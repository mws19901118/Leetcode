class UnionFind:                                                              #UnionFind.
    def __init__(self):
        self.parent = self
    
    def find(self):                                                           #Find.
        while self.parent is not self.parent.parent:
            self.parent = self.parent.parent
        return self.parent
    
    def union(self, uf):                                                      #Union.
        uf.find().parent = self.find()

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = [UnionFind() for i in range(len(edges))]                         #Create union find list.
        for x in edges:
            if uf[x[0] - 1].find() == uf[x[1] - 1].find():                    #If the 2 nodes of an edge have same parent, the edge is redundant, return the edge.
                return x
            uf[x[0] - 1].union(uf[x[1] - 1])                                  #Union the 2 nodes of an edge.
