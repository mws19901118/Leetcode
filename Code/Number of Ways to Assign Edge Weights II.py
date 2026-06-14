class LCA:                                                                                                            #The lowest common ancestor class.
    def __init__(self, adjacentList: defauldict):                                                                     #Initialize the class with the adjacent list.
        n = len(adjacentList)                                                                                         #Get n from the length of the adjacent list.
        self.log = floor(log2(n)) + 1                                                                                 #Calculate the max log of 2 from the deepest node to node 1.
        self.depth = [0] * (n + 1)                                                                                    #Initialize the depth from node 1 to each node.
        self.parent = [[0] * (n + 1) for _ in range(self.log)]                                                        #Intiialize the x step parent of each node, x is power of 2.
        self.parent[0][1] = 1                                                                                         #Node 1's parent is itself.
        visited = set([1])
        q = deque([1])
        while q:                                                                                                      #BFS.
            x = q.popleft()
            for y in adjacentList[x]:
                if y not in visited:
                    visited.add(y)
                    self.depth[y] = self.depth[x] + 1                                                                 #Populate the depth of each node.
                    self.parent[0][y] = x                                                                             #Populate the direct parent of each node.
                    q.append(y)

        for x in range(1, self.log):                                                                                  #Traverse each valid power of 2, starting from 1.
            for i in range(1, n + 1):                                                                                 #Traverse each node.
                self.parent[x][i] = self.parent[x - 1][self.parent[x - 1][i]]                                         #The 2 ** x step parent of i is the 2 ** (x - 1) step parent of i's 2 ** (x - 1) step parent. 

    def query(self, u: int, v: int) -> int:                                                                           #Query the LCA node of u and v.
        if self.depth[u] < self.depth[v]:                                                                             #Swap u and v is v has a larger depth so u is always the deeper node.
            u, v = v, u
        diff = self.depth[u] - self.depth[v]                                                                          #Calculate the depth diff between u and v.
        for x in range(self.log):                                                                                     #Traverse each valid power of 2.
            if (diff >> x) & 1:                                                                                       #If the corrsponding bit in diff is 1, move u to its 2 ** x step parent. Essentially, the operation left u to the same level of v.
                u = self.parent[x][u]
        if u == v:                                                                                                    #If u == v now, then current u is the LCA so return it.
            return u
        for x in reversed(range(self.log)):                                                                           #Traverse each valid power of 2 in the reverse order.
            if self.parent[x][u] != self.parent[x][v]:                                                                #If the 2 ** x step parent of u is not the 2 ** x step parent of v, life up both u and v to its 2 ** x step parent.
                u = self.parent[x][u]
                v = self.parent[x][v]
        return self.parent[0][u]                                                                                      #At the end, both u and v is the direct child of the LCA node, so return self.parent[0][u].

    @cache                                                                                                            #Cache the result.
    def pathLength(self, u: int, v: int) -> int:                                                                      #Calculate the path length from u to v.
        return self.depth[u] + self.depth[v] - 2 * self.depth[self.query(u, v)]                                       #The result is the depth of u plus the depth of v minus the double of the depth of the LCA node of u and v.


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        division = 10 ** 9 + 7                                                                                        #Initialize division.
        adjacentList = defaultdict(list)                                                                              #Build the adjacent list.
        for x, y in edges:
            adjacentList[x].append(y)
            adjacentList[y].append(x)

        lca = LCA(adjacentList)                                                                                      #Initialize the LCA.
        return [0 if not lca.pathLength(x, y) else (1 << lca.pathLength(x, y) - 1) % division for x, y in queries]   #For each query, get the path length between x and y. If the length is 0, append 0; otherwise, append 2 ** (length - 2) % division.
                                                                                                                     #The equation is same as Number of Ways to Assign Edge Weights I.py.
