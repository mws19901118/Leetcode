class UnionFind:                                                                    #Union Find class.
    def __init__(self, x: int):                                                     #Initialize.
        self.label = x
        self.parent = None

    def find(self) -> 'UnionFind':                                                  #Find and update parent.
        if not self.parent:
            return self
        self.parent = self.parent.find()
        return self.parent

    def union(self, uf: 'UnionFind') -> bool:                                       #Union with another union find and return if they are in different compoment before union.
        if self.find().label == uf.find().label:
            return True
        self.find().parent = uf.find()
        return False
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ufs = [UnionFind(i + 1) for i in range(len(edges))]                         #Create a union find for each node.
        result = []                                                                 #Initialize result.
        for x, y in edges:                                                          #Traverse edges.
            if ufs[x - 1].union(ufs[y - 1]):                                        #If union ufs[x - 1] and ufs[y - 1] and update result to [x, y] if they already are in same component.
                result = [x, y]
        return result
