class UnionFind:                                                                                                                  #Union-Find class.
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
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        ufs = [UnionFind(i) for i in range(n)]                                                                                    #Create a Union-Find for each vertex.
        for u, v, _ in edges:                                                                                                     #Traverse edges and build the Union-Find.
            ufs[u].union(ufs[v])
        weight = defaultdict(int)                                                                                                 #Initialize the weight set for each group.
        for u, v, w in edges:                                                                                                     #Get the group label.
            label = ufs[u].find().label
            if label not in weight:                                                                                               #If label is not in the weight set, initialize current group weight to w.
                weight[label] = w
            else:                                                                                                                 #Otherwise, update current group weight by the AND operation with current edge weight.
                weight[label] &= w
        return [weight[ufs[s].find().label] if ufs[s].find().label == ufs[t].find().label else -1 for s, t in query]              #Traverse query, if s and t are in same group, append the group weight(because we can go through all edges in group to minimize the cost); otherwise, append -1.
