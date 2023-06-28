class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adjacentList = defaultdict(list)                                                #Build adjacen list with weight of each edge.
        for i, (u, v) in enumerate(edges):
            adjacentList[u].append((v, succProb[i]))
            adjacentList[v].append((u, succProb[i]))
        
        probability = [0] * n                                                           #Initialize the probability from start to each node, probability[start] is 1.
        probability[start] = 1

        heap = [(-1.0, start)]                                                          #Put the current probability and node in a max heap, starting from start.
        while heap:                                                                     #Dijkstra.
            currProbability, currentNode = heapq.heappop(heap)                          #Pop heap top.
            if currentNode == end:                                                      #If reaches end, return currProbability.
                return -currProbability
            for nextNode, pathProbability in adjacentList[currentNode]:                 #Traverse all neighbors.
                if probability[nextNode] < -currProbability * pathProbability:          #If the probability to reach neighbor from current node is smaller than its current probability, probability[nextNode] and push neightbor to max heap. 
                    probability[nextNode] = -currProbability * pathProbability
                    heapq.heappush(heap, (-probability[nextNode], nextNode))
        return 0.0                                                                      #Return 0.0 if cannot reach end.
