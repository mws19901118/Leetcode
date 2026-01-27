class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adjacentList = [defaultdict(lambda:inf) for _ in range(n)]    #Initialize adjacent list.
        for x, y, w in edges:                                         #Traverse edges.
            adjacentList[x][y] = min(adjacentList[x][y], w)           #Update the weight from x to y to the original weight if it is smaller.
            adjacentList[y][x] = min(adjacentList[y][x], 2 * w)       #Update the weight from y to x to the original weight if it is smaller.
        heap = [(0, 0)]
        visited = set()
        while heap:                                                   #Dijkstra.
            cost, node = heappop(heap)
            if node == n - 1:
                return cost
            visited.add(node)
            for x, w in adjacentList[node].items():
                if x not in visited:
                    heappush(heap, (cost + w, x))
        return -1                                                     #Return -1 if cannot reach node n - 1.
