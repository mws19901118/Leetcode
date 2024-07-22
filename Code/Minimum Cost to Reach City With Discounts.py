class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        adjacentList = defaultdict(list)                                                                    #Build the adjacent list.
        for x, y, t in highways:
            adjacentList[x].append((y, t))
            adjacentList[y].append((x, t))
        heap = [(0, 0, 0)]                                                                                  #Store the current frontier node in a min heap, so top of heap will have smallest cost and then fewest discounts used.
        minCost = [[inf] * (discounts + 1) for _ in range(n)]                                               #Use a 2D array to store the min cost for any node and discount used; initially minCost[0][0] is 0.
        minCost[0][0] = 0
        while heap:                                                                                         #Iterate while heap is not empty.
            cost, discount, node = heapq.heappop(heap)                                                      #Pop top of heap.
            if minCost[node][discount] < cost:                                                              #If current node with discount used already has a smaller cost, skip.
                continue
            for neighbor, toll in adjacentList[node]:                                                       #Traverse the neighbors of current node.
                if cost + toll < minCost[neighbor][discount]:                                               #If visit neighbor using toll can lead to a smaller cost for neighbor, update the min cost of neighbor with discount used and push the new cost and discount used and node to heap.
                    minCost[neighbor][discount] = cost + toll
                    heapq.heappush(heap, (minCost[neighbor][discount], discount, neighbor))
                if discount < discounts and cost + toll // 2 < minCost[neighbor][discount + 1]:             #If there are discount remain and visit neighbor using discount can lead to a smaller cost for neighbor, update the min cost of neighbor with discount used and push the new cost and discount used and node to heap.
                    minCost[neighbor][discount + 1] = cost + toll // 2
                    heapq.heappush(heap, (minCost[neighbor][discount + 1], discount + 1, neighbor))
        return min(minCost[n - 1]) if min(minCost[n - 1]) < inf else -1                                     #Return min(minCost[n - 1]) if it is not inf; otherwise return -1.
