class UnionFind:                                                                                                                      #Union find.
    def __init__(self, x: int):
        self.label = x
        self.parent = []

    def find(self) -> 'UnionFind':
        if not self.parent:
            return self
        self.parent = self.parent.find()
        return self.parent

    def union(self, uf: 'UnionFind') -> None:
        if self.find().label != uf.find().label:
            self.find().parent = uf.find()

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        sortedQuries = sorted([(x, y, q, i) for i, (x, y, q) in enumerate(queries)], key = lambda x: x[2])                            #Sort queires by limit in query in ascending order and keep the original order.
        edgeList.sort(key = lambda x: x[2])                                                                                           #Sort edges by weight in asceding order.
        ufs = [UnionFind(i) for i in range(n)]                                                                                        #Create a union find for each node.
        result = [False] * len(queries)                                                                                               #Initialize result.
        index = 0                                                                                                                     #Initialize the pointer traversing edge list.
        for x, y, q, i in sortedQuries:                                                                                               #Traverse sortedQuries.
            while index < len(edgeList) and edgeList[index][2] < q:                                                                   #Traverse edge list while current edge has smaller weight than the query limit.
                ufs[edgeList[index][0]].union(ufs[edgeList[index][1]])                                                                #Union the 2 nodes of the edge.
                index += 1
            result[i] = ufs[x].find().label == ufs[y].find().label                                                                    #There is a path if parent of x and parent of y has same label, and all the edges in path are smaller than query limit.
        return result                                                                                                                 #Return result.
