class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        length = len(grid)
        width = len(grid[0])
        area = 0
        for i in range(length):
            maxInX = 0
            maxInY = 0
            for j in range(width):
                if grid[i][j]:                      #For each cell, if there is any value, there is a unit of area projection on XY.
                    area += 1
                maxInX = max(grid[i][j], maxInX)    #For YZ, the projection area of each row is the max value.
                maxInY = max(grid[j][i], maxInY)    #Fox XZ, the projection area of each column is the max value.
            area += maxInX
            area += maxInY
        return area
