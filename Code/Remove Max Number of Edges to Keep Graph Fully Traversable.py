class UnionFind:                                                                                                                                                                            #Union-Find class.
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
            return False
        self.find().parent = uf.find()
        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ufs1, ufs2 = [UnionFind(i) for i in range(n)], [UnionFind(i) for i in range(n)]                                                                                                     #Create Fnion-Find objects for alice and bob separately for each node.
        type1, type2, type3 = [(e[1], e[2]) for e in edges if e[0] == 1], [(e[1], e[2]) for e in edges if e[0] == 2], [(e[1], e[2]) for e in edges if e[0] == 3]                            #Group edges by type.
        result = sum(int(int(ufs1[x - 1].union(ufs1[y - 1])) + int(ufs2[x - 1].union(ufs2[y - 1])) == 0) for x, y in type3)                                                                 #Traverse type3 edges first, try to union nodes for both alice and bob; if both alice nodes and bob nodes don't need union, increase count as current edge is not needed.
        result += sum(int(not ufs1[x - 1].union(ufs1[y - 1])) for x, y in type1) + sum(int(not ufs2[x - 1].union(ufs2[y - 1])) for x, y in type2)                                           #Traverse type1 edges and type2 edges do the same process for alice nodes and bob nodes respectively and update result.
        return -1 if (len(set([x.find().label for x in ufs1])) > 1 or len(set([x.find().label for x in ufs2])) > 1) else result                                                             #If either alice nodes or bob nodes has more than one connected component, return -1 because graph cannot be fully traversed by both; otherwise return result. 
