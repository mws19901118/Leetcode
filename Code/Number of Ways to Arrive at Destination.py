class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adjacentList = [[] for _ in range(n)]                          #Build adjacent list.
        for u, v, w in roads:
            adjacentList[u].append((v, w))
            adjacentList[v].append((u, w))
        heap = [(0, 0)]                                                #Initialize heap.
        time, count = [0] + [inf] * (n - 1), [1] + [0] * (n - 1)       #Initialize the shortest time and number of ways of visiting each node.
        division = 10 ** 9 + 7                                         #Initialize division.
        while heap:                                                    #Dijkstra.
            t, x = heapq.heappop(heap)
            if t > time[x]:                                            #If t is greater than time[x], skip.
                continue
            for y, w in adjacentList[x]:                               #Traverse neighbors of x.
                if t + w < time[y]:                                    #If new visit time is smaller than existing one, reset time[y] and count[y] and push (time[y], y) to heap.
                    time[y] = t + w
                    count[y] = count[x]
                    heapq.heappush(heap, (time[y], y))
                elif t + w == time[y]:                                 #Otherwise if new visit time is same as existing one, add count[x] to count[y] and take modulo.
                    count[y] = (count[y] + count[x]) % division
        return count[-1]                                               #Return count[-1].
