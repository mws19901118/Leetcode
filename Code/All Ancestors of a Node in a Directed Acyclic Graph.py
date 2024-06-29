class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adjacentList = defaultdict(list)
        indegree = [0] * n
        ancestors = [set() for _ in range(n)]
        for x, y in edges:                                      #Build adjacent list and indegrees.
            adjacentList[x].append(y)
            indegree[y] += 1
        q = [i for i, x in enumerate(indegree) if not x]        #Initialize queue to be the nodes whose indegree is 0.
        while q:                                                #BFS.
            newq = []
            for x in q:                                         #Traverse queue.
                for y in adjacentList[x]:                       #Traverse all neighbors of x.
                    ancestors[y].add(x)                         #Add x to the ancestors of y.
                    ancestors[y] |= ancestors[x]                #Add all ancestors of x to ancestors of y.
                    indegree[y] -= 1                            #Update indegree of y.
                    if not indegree[y]:                         #If indegree of y is 0, it has no nore unvisited ancestors, so append it to new queue.
                        newq.append(y)
            q = newq                                            #Replace queue with new queue.
        return [sorted(list(x)) for x in ancestors]             #Sort ancestors of each node.
