class UnionFind:                                                                                #Union find.
    def __init__(self, x: int) -> None:
        self.parent = None
        self.label = x

    def find(self) -> 'UnionFind':
        if not self.parent:
            return self
        self.parent = self.parent.find()
        return self.parent

    def union(self, uf: 'UnionFind') -> None:
        if self.find().label == uf.find().label:
            return
        uf.find().parent = self.find()

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        adjacentList = collections.defaultdict(list)                                            #Build the adjacent list.
        for x, y in edges:
            adjacentList[x].append(y)
            adjacentList[y].append(x)
        ufs = [UnionFind(i) for i in range(len(vals))]                                          #Create a union find for each node.
        nodesByValues = collections.defaultdict(list)                                           #Group nodes by their value.
        for i, x in enumerate(vals):
            nodesByValues[x].append(i)
        result = 0
        for k in sorted(nodesByValues.keys()):                                                  #Traverse the values in asending order.
            for x in nodesByValues[k]:                                                          #Traverse all nodes with current value k.
                for y in adjacentList[x]:                                                       #Traverse each neighbor of current node.
                    if vals[y] > vals[x]:                                                       #If the neighbor has a greater value, skip; cause cannot form good path with a greater value en route.
                        continue
                    ufs[x].union(ufs[y])                                                        #Union the neighbor with current node. Since, all component with smaller value are already unioned, this operation guarantees the union of nodes that can connect indirectly via nodes with smaller values. 
            count = collections.Counter([ufs[x].find() for x in nodesByValues[k]])              #Use a counter to count the size of each unioned compnent whose nodes have same value k.
            result += sum(c + c * (c - 1) // 2 for c in count.values())                         #For each component, each node itself is a good path and each 2 nodes form a good path. So add c + c * (c - 1) // 2 to result for each size c of component.
        return result
