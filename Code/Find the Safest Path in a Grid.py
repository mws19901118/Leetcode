class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        def populateDistance() -> None:                                                        #Populate distance.
            for x, y in thieves:                                                               #Set the distance to 0 for each cell that has a thief.
                distance[x][y] = 0
            count = 1                                                                          #Initialize the distance.
            q = thieves
            while q:                                                                           #BFS starting from all thieves.
                newq = []                                                                      #Initialize new queue.
                for x, y in q:                                                                 #Traverse current queue.
                    for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:              #Traverse neightbors.
                        if 0 <= u < n and 0 <= v < n and distance[u][v] > count:               #If neighbor is valid and has a higher distance, update its distance and append it to new queue.
                            newq.append((u, v))
                            distance[u][v] = count
                count += 1
                q = newq

        n = len(grid)                                                                          #Get the diemension.
        thieves = [(i, j) for i, j in product(range(n), range(n)) if grid[i][j]]               #Find coordinates for all thieves.
        distance = [[2 * n for x in range(n)] for y in range(n)]                               #Initialize minimum manhatten distance for each cell to any thief.
        populateDistance()                                                                     #Populate the distance.
        heap = [(-distance[0][0], 0, 0)]                                                       #Use a max heap to store the visited coordinates by min distance.
        grid[0][0] = -1                                                                        #Mark the top left corner as visited.
        while heap:                                                                            #Iterate while heap is not empty.
            factor, x, y = heapq.heappop(heap)                                                 #Pop heap top, which is the max safety factor so far.
            if (x, y) == (n - 1, n - 1):                                                       #If reaches bottom right corner, return factor.
                return -factor
            for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:                      #Traverse neighbors of current cell.
                if 0 <= u < n and 0 <= v < n and grid[u][v] != -1:                             #If neighbor is valid and not visited, push it to heap with new max safety factor(the smaller of its min distance and current max safety factor)
                    heapq.heappush(heap, (-min(-factor, distance[u][v]), u, v))
                    grid[u][v] = -1                                                            #Mark neighbor as visited.


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:                                                                #Alternatively, we can binary search for the result after populating distance.
        @cache                                                                                                                    #Cache result.
        def isSafe(minDistance: int) -> bool:                                                                                     #Determine if it can reach the bottom right corner from top left corner with given min distance for the entire path.
            if distance[0][0] < minDistance or distance[n - 1][n - 1] < minDistance:                                              #If either top left corner or botton right corner has distance smaller than minDistance, return false.
                return False
            q, visited = [(0, 0)], set([0, 0])
            while q:                                                                                                              #BFS starting from top left corner to find if can reach bottom right corner.
                newq = []                                                                                                         #Initialize new queue.
                for x, y in q:                                                                                                    #Traverse current queue.
                    if (x, y) == (n- 1, n - 1):                                                                                   #Return true if reaches bottom right corner.
                        return True
                    for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:                                                 #Traverse neighbors of current cell.
                        if 0 <= u < n and 0 <= v < n and (u, v) not in visited and distance[u][v] >= minDistance:                 #If neighbor is valid and not visited and has distance larger than minDistance, append it to new queue and mark it as visited.
                            newq.append((u, v))
                            visited.add((u, v))
                q = newq
            return False                                                                                                          #Return false if cannot reach.
        
        def populateDistance() -> None:
            for x, y in thieves:
                distance[x][y] = 0
            count = 1
            q = thieves
            while q:
                newq = []
                for x, y in q:
                    for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
                        if 0 <= u < n and 0 <= v < n and distance[u][v] > count:
                            newq.append((u, v))
                            distance[u][v] = count
                count += 1
                q = newq

        n = len(grid)
        thieves = [(i, j) for i, j in product(range(n), range(n)) if grid[i][j]]
        distance = [[2 * n for x in range(n)] for y in range(n)]
        populateDistance()
        start, end = 0, 2 * n - 2                                                                                                 #Binary search from 0 to 2 * n - 2, which is the max possible distance.
        while start <= end:
            mid = (start + end) // 2                                                                                              #Get mid.
            if isSafe(mid) and not isSafe(mid + 1):                                                                               #If can reach with mid as min distance but cannot with mid + 1, mid is the max safety factor.
                return mid
            elif isSafe(mid + 1):                                                                                                 #If can reach with mid + 1, set start to mid + 1.
                start = mid + 1
            else:                                                                                                                 #Otherwise, set end to mid.
                end = mid
