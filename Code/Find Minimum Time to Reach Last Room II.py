class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])                                  #Get the dimensions.
        visited = {}                                                            #Store visited time of each room.
        heap = [(0, 0, 0, 0)]                                                   #Store rooms to visit in a min heap.
        while heap:                                                             #Iterate while heap is not empty.
            t, flag, x, y = heapq.heappop(heap)                                 #Pop heap.
            if x == m - 1 and y == n - 1:                                       #If this is destination, return t.
                return t
            for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:       #Traverse the neighbors of current room.
                if 0 <= u < m and 0 <= v < n and (u, v) not in visited:         #Process if neighbor is valid and unvisited.
                    visited[(u, v)] = max(t, moveTime[u][v]) + 1 + flag         #The visit time of neighbor is max(t, moveTime[u][v]) + 1 + flag.
                    heapq.heappush(heap, (visited[(u, v)], 1 - flag, u, v))     #Push visit time of neighbor and invert value of current flag and neighbor to heap.
