class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def countNodesOnDiameter(edges: List[List[int]]) -> int:                                #Count the nodes on tree diameter using topological sort.
            n = len(edges) + 1
            indegree, adjacentList = [0] * n, [set() for _ in range(n)]
            for x, y in edges:
                indegree[x] += 1
                indegree[y] += 1
                adjacentList[x].add(y)
                adjacentList[y].add(x)
            count = 0
            q = set([i for i in range(n) if indegree[i] == 1])
            while q:
                newq = set()
                count += 2
                for x in q:
                    for y in adjacentList[x]:
                        indegree[y] -= 1
                        if indegree[y] == 1:
                            newq.add(y)
                        if indegree[y] == 0:
                            if y in newq:
                                count += 1
                                return count
                q = newq
                
            return count
        count1, count2 = countNodesOnDiameter(edges1), countNodesOnDiameter(edges2)            #Count the nodes on diameter for edges1 and edges2 respectively.
        return max(count1 - 1, count2 - 1, count1 // 2 + count2 // 2 + 1)                      #The diameter after merge is the largest of diameter of edges1, diameter of edges2 and sum of half of diameter of edges1, half of diameter of edges2 plus 1 more edge to connect the 2 trees.
