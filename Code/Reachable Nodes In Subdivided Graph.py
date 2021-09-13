class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        edgeNodesTaken = defaultdict(int)                                                                                                           #Store the reachable nodes count for each directed edge
        adjacentList = defaultdict(list)                                                                                                            #Store the neighbors of each main node with divided node count.
        remainMoves = [-1] * n                                                                                                                      #Store the remaining moves when reaching each main node.
        for s, e, c in edges:                                                                                                                       #Traverse edges to build adjacent list.
            adjacentList[s].append((e, c))
            adjacentList[e].append((s, c))
        remainMoves[0] = maxMoves                                                                                                                   #Starting at 0 so remaining moves at 0 is maxMoves.
        heap = []                                                                                                                                   #Initialize max heap, storing remaining moves and main node to visit.
        heapq.heappush(heap, (-maxMoves, 0))
        while heap:                                                                                                                                 #Iterate while heap is not empty.
            moves, node = heapq.heappop(heap)                                                                                                       #Pop the main node to visit with max remaining moves.
            moves = -moves
            if remainMoves[node] > moves:                                                                                                           #If node is visited with a larger remaining moves, skip.
                continue
            for x, c in adjacentList[node]:                                                                                                         #Traverse the neighbors of node.
                edgeNodesTaken[(node, x)] = max(edgeNodesTaken[(node, x)], min(moves, c))                                                           #Update the nodes taken for edge from node to x to be the larger of current value and min(moves, c).
                if moves - c - 1 > remainMoves[x]:                                                                                                  #If the remaining moves when reaching x from node is larger than current remainMoves[x].
                    remainMoves[x] = moves - c - 1                                                                                                  #Update remainMoves[x].
                    heapq.heappush(heap, (-remainMoves[x], x))                                                                                      #Push (remainMoves[x], x) to heap to visit it later.
        return sum(min(edgeNodesTaken[(s, e)] + edgeNodesTaken[(e, s)], c) for s, e, c in edges) + sum(1 for x in remainMoves if x != -1)           #Sum up the reachable nodes for each node(both direction but cannot exceed the divided node count) and plus all visited main node(remainMoves not equals -1), then return.
