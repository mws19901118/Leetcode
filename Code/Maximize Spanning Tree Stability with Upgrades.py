class UnionFind:                                                          #Union-Find class.
    def __init__(self, x: int):
        self.label = x
        self.parent = None
    
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
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        ufs = [UnionFind(i) for i in range(n)]                           #Initialize union-find for each node.
        heap = []                                                        #Use a max heap to store 
        result, remain = inf, n - 1                                      #Initialize result to be inf and also initialize remain edges of the spanning tree.
        for u, v, s, must in edges:                                      #Traverse edges.
            if not must:                                                 #If current edge is optional, push it to the max heap and continue.
                heappush(heap, (-s, u, v))
                continue
            elif not ufs[u].union(ufs[v]):                               #Otherwise, try to union u and v. If they are already unioned, there is a cycle in the spanning tree, so return -1 directly as it is prohibited.
                return -1
            remain -= 1                                                  #Decrease remain.
            result = min(result, s)                                      #Update result.
        
        while remain:                                                    #Traverse the optional edges to find best strengths. Since it is max heap, we are looking for edges with larger strength to guarantee the spanning tree has max stability.
            if not heap:                                                 #If max heap is empty, there is no more edges to complete the spanning tree, also return -1.
                return -1
            s, x, y = heappop(heap)                                      #Pop the max heap.
            if not ufs[x].union(ufs[y]):                                 #Try to union x and y. If they are already unioned, skip because both are already in the spanning tree.
                continue 
            result = min(result, -s * 2 ** (remain <= k))                #Apply upgrade on the smallest k edges in the remaning edges.
            remain -= 1
        return result                                                    #Return result.
