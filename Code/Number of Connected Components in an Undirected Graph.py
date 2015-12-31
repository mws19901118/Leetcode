class Solution(object):
    class UnionFind(object):                                  #Union-Find  Data Structure.
        def __init__(self, x):
            self.x = x
            self.parent = None
        
        def Find(self):
            if self.parent != None:
                self.parent = self.parent.Find()
                return self.parent
            else:
                return self
        
        def Union(self, t):
            a = self.Find()
            b = t.Find()
            if a is not b:
                b.parent = a
            
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        uf = []
        for i in range(n):
            uf.append(Solution.UnionFind(i))                #Initially, each node is a independent union-find.
        for e in edges:                                     #Union the 2 ende of an edge.
            uf[e[0]].Union(uf[e[1]])
        result = set()
        for i in range(n):
            a = uf[i].Find()                                #Find the parent of each node.
            if a not in result:                             #If it's not in the result set, add it to the result set.
                result.add(a)
        return len(result)                                  #Return the length of result set.
