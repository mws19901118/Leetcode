class UnionFind:                                                                               #Union-Find class.
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
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        sortedEdges = sorted((w, a, b, i) for i, (a, b, w) in enumerate(edges))               #Sort edges based on weight and keep the original order.
        critical, pseudoCritical = [], []                                                     #Initialize critical edges and pseudo critical edges.

        def calculateMST(skipIndex: int, fixIndex: tuple) -> int:                             #Calculate MST using Kruskal algorithm with the index of edge to skip and index of edge to fix.
            ufs = [UnionFind(i) for i in range(n)]                                            #Initialize a union-Find for each vertex.
            mst, count = 0, 1                                                                 #Initialize mst weight sum and count of vertexes unioned.
            if fixIndex != -1:                                                                #If there is an edge to be fixed in MST, union the vertexes on edge, add edge weight to mst and increase count.
                ufs[sortedEdges[fixIndex][1]].union(ufs[sortedEdges[fixIndex][2]])
                mst += sortedEdges[fixIndex][0]
                count += 1
            for j, (w, a, b, i) in enumerate(sortedEdges):                                    #Traverse sorted edges.
                if j == skipIndex or j == fixIndex:                                           #Skip edge to skip and edg to fix(already processed).
                    continue
                if ufs[a].union(ufs[b]):                                                      #If the vertexes on edge are not unioned, union them, add edge weight to mst and increase count.
                    mst += w
                    count += 1
                if count == n:                                                                #If all vertexes are unioned, return mst.
                    return mst
            return float('inf')                                                               #Return infinity when cannot form mst.

        mst = calculateMST(-1, -1)                                                            #Calculate the weight sum of mst of all edges.
        for j, (w, a, b, i) in enumerate(sortedEdges):                                        #Traverse sorted edges.
            if calculateMST(j, -1) > mst:                                                     #If the mst weight sum of skipping current edge is greater, current edge is critical.
                critical.append(i)
            elif calculateMST(-1, j) == mst:                                                  #Otherwise if the mst weight sum of fixing current edge is same as mst, current edge is pseudo critical.
                pseudoCritical.append(i)
        return [critical, pseudoCritical]                                                     #Return critical edges and pseudo critical edges.
