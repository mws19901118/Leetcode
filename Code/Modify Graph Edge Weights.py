class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        def dijkstra(graph: List[List[Tuple[int, int]]], source: int, destination: int) -> int:       #Use Dijkstra to find the shortest distance from source to destination.
            min_distance = [inf] * len(graph)
            min_distance[source] = 0
            min_heap = [(0, source)]
            while min_heap:
                d, u = heapq.heappop(min_heap)
                if d > min_distance[u]:
                    continue
                for v, w in graph[u]:
                    if d + w < min_distance[v]:
                        min_distance[v] = d + w
                        heapq.heappush(min_heap, (min_distance[v], v))
            return min_distance[destination]

        graph = [[] for _ in range(n)]                                                               #Build the graph with known weights.
        for u, v, w in edges:
            if w != -1:
                graph[u].append((v, w))
                graph[v].append((u, w))

        initial_shortest_distance = dijkstra(graph, source, destination)                             #Compute the initial shortest distance.
        if initial_shortest_distance < target:                                                       #If initial shortest distance is smaller than target, we can not make increase shortest distance by assigning weight, so reutrn empty list.
            return []

        if initial_shortest_distance == target:                                                      #If initial shortest distance equals target, update edges with -1 weight to target + 1 so they don't affect the shortest distance.
            for edge in edges:
                if edge[2] == -1:
                    edge[2] = target + 1
            return edges

        for i, (u, v, w) in enumerate(edges):                                                        #Traverse edges with unknown weights.
            if w != -1:
                continue
            edges[i][2] = 1                                                                          #Set edge weight to 1 initially and update graph.
            graph[u].append((v, 1))
            graph[v].append((u, 1))
            new_distance = dijkstra(graph, source, destination)                                      #Recompute shortest distance with updated edge weight.
            if new_distance <= target:                                                               #If new distance is not greater than target, we find a possible solution.
                edges[i][2] += target - new_distance                                                 #Add the diff between new distance and target to gap.
                for j in range(len(edges)):                                                          #Update remaining edges with -1 weight to target + 1 so they don't affect the shortest distance.
                    if edges[j][2] == -1:
                        edges[j][2] = target + 1
                return edges                                                                         #Return edges.
        return []                                                                                    #Return empty list at the end as we cannot find a possible solution.
