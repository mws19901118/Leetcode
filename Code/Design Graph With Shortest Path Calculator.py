class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.adjacentList = [[] for _ in range(n)]                            #Initialize adjacent list.
        for x, y, c in edges:                                                 #Populate adjacent list.
            self.adjacentList[x].append((c, y))

    def addEdge(self, edge: List[int]) -> None:
        self.adjacentList[edge[0]].append((edge[2], edge[1]))                 #Add new edge to adjacent list.

    def shortestPath(self, node1: int, node2: int) -> int:                    #Dijkstra algorithm.
        distances = [inf] * self.n
        distances[node1] = 0
        heap = []
        heapq.heappush(heap, (0, node1))
        while heap:
            d, curr = heapq.heappop(heap)
            for x, y in self.adjacentList[curr]:
                new_d = d + x
                if new_d < distances[y]:
                    distances[y] = new_d
                    heapq.heappush(heap, (new_d, y))
        return distances[node2] if distances[node2] < inf else -1



# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
