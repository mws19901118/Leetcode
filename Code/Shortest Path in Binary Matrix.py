class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:                                                                  #Check if the start cell is empty; if not, return -1.
            return -1
        length = 1                                                                      #Initialize length.
        q = [(0, 0)]                                                                    #Initialize queue with the coordinate of the start cell.
        grid[0][0] = 1                                                                  #Set the start cell to 1.
        while q:                                                                        #BFS.
            newq = []
            for x, y in q:
                if x == len(grid) - 1 and y == len(grid) - 1:                           #If reaches the end cell, return length.
                    return length
                for nx, ny in product([x - 1, x, x + 1], [y - 1, y, y + 1]):            #Traverse surronding cells in all 8 directions.
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:               #If its valid and empty, append it to newq and set it to 1.
                        newq.append((nx, ny))
                        grid[nx][ny] = 1
            length += 1
            q = newq
        return -1                                                                       #Return -1 if cannot reach the end cell.
