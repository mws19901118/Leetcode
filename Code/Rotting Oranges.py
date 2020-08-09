class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, rotten = set(), set()                                                                              #Use 2 sets to store all coordinates of initial fresh and rotten oranges respectively.
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    rotten.add((i, j))
                elif grid[i][j] == 1:
                    fresh.add((i, j))
        time = 0
        while rotten:                                                                                             #While there are new rotten oranges, do BFS.
            if not fresh:                                                                                         #If no more fresh oranges, stop BFS.
                break
            q = set()                                                                                             #Store all coordinates of new rotten oranges in this time.
            for x, y in rotten:
                for i, j in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    nx, ny = x + i, y + j
                    if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[x]) and grid[nx][ny] == 1:        #Find all fresh oranges next to rotten oranges, they will become rotten.
                        grid[nx][ny] = 2                                                                          #Update status in grid.
                        q.add((nx, ny))                                                                           #Add coordinate to q.
                        fresh.remove((nx, ny))                                                                    #Remove from fresh.
            rotten = q
            time += 1                                                                                             #Increase time by 1.
        if fresh:
            time = -1
        return time                                                                                               #Return time.
