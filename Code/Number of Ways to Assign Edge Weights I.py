class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        adjacentList = defaultdict(list)                  #Build the adjacent list.
        for x, y in edges:
            adjacentList[x].append(y)
            adjacentList[y].append(x)
        q = [1]
        visited = set([1])
        count = 0
        while q:                                          #BFS to find the number of nodes on the path from node 1 to max depth.
            newq = []
            for x in q:
                for y in adjacentList[x]:
                    if y not in visited:
                        visited.add(y)
                        newq.append(y)
            q = newq
            count += 1
        return (1 << (count - 2)) % (10 ** 9 + 7)         #To make the cost odd, we need to assign weight 1 to an odd number of edges.
                                                          #It is the sum of combinations of all odd numbers out of n; n is count - 1.
                                                          #So, the final result is 2 ** (count - 2) % (10 ** 9 + 7).
