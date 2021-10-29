class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])                                                          #Get dimensions.
        count, time = 0, 0                                                                      #Intialize fresh count and total time.
        q = []                                                                                  #Intialize queue.
        for i, j in product(range(m), range(n)):                                                #Traverse grid.
            if grid[i][j] == 1:                                                                 #If current orange is fresh, increase count.
                count += 1
            elif grid[i][j] == 2:                                                               #If current orange is rotten, add coordinate to q.
                q.append((i, j))

        while q and count:                                                                      #While q is not emptu and count is larger than 0, do BFS.
            newq = []                                                                           #Initialize new queue.
            for x, y in q:                                                                      #Traverse each coordinate in q.
                for nx, ny in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:                 #Traverse its neighbors.
                    if nx >= 0 and nx < m and ny >= 0 and ny < n and grid[nx][ny] == 1:         #If neighbor is valid and is fresh, append neighbor's coordinate to newq, decrease count and set neightbor to rotten.
                        newq.append((nx, ny))
                        count -= 1
                        grid[nx][ny] = 2
            q = newq                                                                            #Replace q with newq.
            time += 1                                                                           #Increase time.
        return time if not count else -1                                                        #If count is not 0, it's impossible to rotten all oranges so return -1; otherwise, return time.
