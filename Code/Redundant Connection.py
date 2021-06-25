class UnionFind:
    def __init__(self):                                                 #Initalize union find.
        self.parent = self
        
    def find(self):                                                     #Find.
        if self.parent == self:
            return self
        root = self.parent.find()
        self.parent = root
        return root
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = [UnionFind() for i in range(len(edges))]                   #Create a union find for each node.
        result = None
        for e in edges:                                                 #Traverse edges.
            x, y = uf[e[0] - 1].find(), uf[e[1] - 1].find()             #Find the root of each corresponding union find.
            if x == y:                                                  #If they have same root, then this edge is redundant.
                result = e
            else:                                                       #Otherwise union these 2 roots.
                x.parent = y
        return result                                                   #Return redundant edge.
