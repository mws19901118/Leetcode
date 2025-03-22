class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        destinations = set(marked)                              #Put destination nodes in a set.
        adjacentList = [[] for _ in range(n)]                   #Build adjacent list.
        for u, v, w in edges:
            adjacentList[u].append((v, w))
        heap, visited = [(0, s)], set()                         #Initialize heap with 0 distance and s; also visited nodes.
        while heap:                                             #Dijkstra.
            distance, x = heapq.heappop(heap)
            if x in visited:
                continue
            if x in destinations:                               #Return distance if x is marked.
                return distance
            visited.add(x)
            for y, w in adjacentList[x]:
                heapq.heappush(heap, (distance + w, y))
        return -1                                               #Return -1 if cannot reach any marked nodes.
